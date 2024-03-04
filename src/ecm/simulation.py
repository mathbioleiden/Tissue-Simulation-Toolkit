from tissue_simulation_toolkit.ecm.ecm import (
        AngleCstTypes, AngleCsts, BondTypes, Bonds, MDState, ParticleType,
        Particles)
from tissue_simulation_toolkit.ecm.cell_ecm_interactions import (
        CellECMInteractions, ChangeTypeInArea, MoveAdhesionParticles,RemoveAdhesionParticles)
from tissue_simulation_toolkit.ecm.ecm_boundary_state import (
        ECMBoundaryState, SparseParticles, SparseBondTypes, SparseBonds,
        SparseAngleCstTypes, SparseAngleCsts)
from tissue_simulation_toolkit.ecm.parameters import EvolutionParameters
from tissue_simulation_toolkit.util.mpiwrap import CommWorld

import hoomd
import hoomd.md
from hoomd import Snapshot
from hoomd.data import LocalSnapshot
import numpy as np
import numpy.typing as npt

from dataclasses import dataclass, field
import logging
from random import random
from time import monotonic_ns
from typing import cast, List, Optional, Set


# This doesn't appear to be exported by hoomd, but we need it to determine
# which particles we have on a given MPI process.
_HOOMD_NOT_LOCAL = 4294967295


_logger = logging.getLogger(__name__)


def int_set_to_array(s: Set[int]) -> npt.NDArray[np.int32]:
    """Convert a Python set of integers to a 1D numpy array."""
    return np.fromiter(s, np.int32, len(s))


def int_array_to_set(a: npt.NDArray[np.int32]) -> Set[int]:
    """Convert a numpy array of ints to a Python set.

    This flattens arrays with more than one dimension.
    """
    if not a.shape:
        return set()
    return set(map(int, a.flat))


class Boundary:
    """Lists of ids of all the objects in the ECM boundary

    This is a helper class for Simulation. It contains CPU-side lists of the
    ids of particles, bonds and angle constraints in the boundary, so that we
    can easily find those when we need to send the boundary state.

    Attributes:
        par_ids: Set of particle ids of particles in the boundary
        bond_ids: Set of bond ids of bonds in the boundary
        angle_cst_ids: Set of angle constraint ids of angle constraints
                in the boundary
    """
    def __init__(self, comm: CommWorld, snapshot: LocalSnapshot) -> None:
        """Create a Boundary from the current hoomd state

        Args:
            comm: MPI communicator to use
            snapshot: A snapshot of the current hoomd state to init from
        """
        self._comm = comm
        self.reinit(snapshot)

    def reinit(self, snapshot: LocalSnapshot) -> None:
        """Resets this index to match the given snapshot

        Args:
            snapshot: A snapshot of the current hoomd state to init from
        """
        self.par_ids: Set[int] = set()
        self.bond_ids: Set[int] = set()
        self.angle_cst_ids: Set[int] = set()
        self.add_adhesions(snapshot)


    def add_adhesions(
            self, snapshot: LocalSnapshot, par_ids: Optional[npt.ArrayLike] = None
            ) -> None:
        """Add new adhesions to the boundary

        This will add the given particle to the boundary, and look up all
        particles it shares a bond or angle constraint with and add those
        bonds, angles and particles too, if needed.

        If par_ids is not given, all current adhesion-type particles will
        be looked up in the state and added.

        Args:
            snapshot: State of the simulation
            par_ids: ids of the new adhesion particles
        """
        if par_ids is None:
            par_ids = snapshot.particles.tag[
                    snapshot.particles.typeid == ParticleType.adhesion.value]
            print("Adding adhesions with ids: ", par_ids)

        new_par_ids = int_array_to_set(np.array(par_ids))
        new_bond_ids = set()
        new_angle_cst_ids = set()

        matches = np.in1d(snapshot.bonds.group[:, 0], par_ids)
        new_bond_ids.update(snapshot.bonds.tag[matches])
        new_par_ids.update(snapshot.bonds.group[matches, 1])

        matches = np.in1d(snapshot.bonds.group[:, 1], par_ids)
        new_bond_ids.update(snapshot.bonds.tag[matches])
        new_par_ids.update(snapshot.bonds.group[matches, 0])

        matches = np.in1d(snapshot.angles.group[:, 0], par_ids)
        new_angle_cst_ids.update(snapshot.angles.tag[matches])
        new_par_ids.update(int_array_to_set(snapshot.angles.group[matches, 1:3]))

        matches = np.in1d(snapshot.angles.group[:, 1], par_ids)
        new_angle_cst_ids.update(snapshot.angles.tag[matches])
        new_par_ids.update(snapshot.angles.group[matches, 0])
        new_par_ids.update(snapshot.angles.group[matches, 2])

        matches = np.in1d(snapshot.angles.group[:, 2], par_ids)
        new_angle_cst_ids.update(snapshot.angles.tag[matches])
        new_par_ids.update(int_array_to_set(snapshot.angles.group[matches, 0:2]))

        all_new_par_ids = self._comm.allgather(new_par_ids)
        all_new_bond_ids = self._comm.allgather(new_bond_ids)
        all_new_angle_cst_ids = self._comm.allgather(new_angle_cst_ids)

        self.par_ids.update(*all_new_par_ids)
        self.bond_ids.update(*all_new_bond_ids)
        self.angle_cst_ids.update(*all_new_angle_cst_ids)

    def remove_adhesions(
            self, snapshot: LocalSnapshot, par_ids: Optional[npt.ArrayLike] = None
            ) -> None:
        """Remove adhesions from the boundary

        Not implemented yet

        Args:
            snapshot: State of the simulation
            par_ids: 1D array of ids of the particles to remove
        """
        self.reinit(snapshot)
        # note: we'll probably need to refcount non-adhesion particles to make
        # this work. See collections.Counter
        # raise NotImplementedError()


class Simulation:
    """Simulates the ECM using hoomd."""
    def __init__(
            self, par: EvolutionParameters, ecm: MDState) -> None:
        """Create an ECMSimulation.

        Args:
            par: Simulation parameters
            ecm: ECM to initialise from
        """
        if par.md_use_gpu:
            self.device = hoomd.device.GPU()
        else:
            self.device = hoomd.device.CPU()

        self._sim = hoomd.Simulation(device=self.device, seed=par.md_seed)
        self._comm = CommWorld()

        snapshot = hoomd.Snapshot()

        # Set up box
        box_offset = 4
        safety_margin = par.contour_length
        box_x = par.box_size_x + box_offset * par.contour_length + safety_margin
        box_y = par.box_size_y + box_offset * par.contour_length + safety_margin
        snapshot.configuration.box = [box_x, box_y, 0.0, 0.0, 0.0, 0.0]

        # Our standard coordinate ranges are [0, box_size_x] and [0, box_size_y]
        # Hoomd wants everything centered at the origin. Add this to get from
        # standard to hoomd coordinates, subtract it to go from hoomd to standard.
        self._pos_offset = np.array([
            -par.box_size_x / 2.0, -par.box_size_y / 2.0])

        # Set up initial types
        if self.device.communicator.rank == 0:
            snapshot.particles.types = [pt.name for pt in ParticleType]

            snapshot.bonds.types = [str(i) for i in range(len(ecm.bond_types.k))]
            snapshot.angles.types = [str(i) for i in range(len(ecm.angle_cst_types.k))]

        self._sim.create_state_from_snapshot(snapshot)

        # Set up integrator
        self._integrator = hoomd.md.Integrator(par.md_dt)
        free_only = hoomd.filter.Type(['free'])
        integration_method = hoomd.md.methods.Brownian(free_only, kT=par.md_kT)
        integration_method.gamma['free'] = par.viscosity
        self._integrator.methods.append(integration_method)
        self._sim.operations.integrator = self._integrator
       
        filter_updater = hoomd.update.FilterUpdater(
             trigger=1, # Periodic, might also work with par.md_its but that should be tested.
             filters=[free_only]
         )
        self._sim.operations.updaters.append(filter_updater) 


        self._dt = par.md_dt
        self._its = par.md_its

        # Load particles, bonds and angle constraints and init boundary
        self._set_state_from_ecm(ecm)
        with self._sim.state.cpu_local_snapshot as snapshot:
            self._boundary = Boundary(self._comm, snapshot)

    def get_state(self) -> Optional[MDState]:
        """Get the whole state of the MD system as an ECM

        When running under MPI, this returns the state only for rank 0, on
        other ranks None is returned.
        """
        ta = monotonic_ns()
        with self._sim.state.cpu_local_snapshot as snapshot:
            # Note that Gatherv may improve performance here, if it works
            # These contain lists of arrays, one array per MPI process
            l_par_tag = self._comm.gather(np.array(snapshot.particles.tag))
            l_par_pos = self._comm.gather(
                    snapshot.particles.position[:, :2] - self._pos_offset)
            l_par_typeid = self._comm.gather(np.array(snapshot.particles.typeid))

            l_bonds_group = self._comm.gather(np.array(snapshot.bonds.group))
            l_bonds_typeid = self._comm.gather(np.array(snapshot.bonds.typeid))

            l_angles_group = self._comm.gather(np.array(snapshot.angles.group))
            l_angles_typeid = self._comm.gather(np.array(snapshot.angles.typeid))

        if self.device.communicator.rank == 0:
            # These are not None on the root rank, and now mypy knows that too
            assert l_par_tag is not None
            assert l_par_pos is not None
            assert l_par_typeid is not None
            assert l_bonds_group is not None
            assert l_bonds_typeid is not None
            assert l_angles_group is not None
            assert l_angles_typeid is not None

            n_par = sum([len(x) for x in l_par_tag])
            par_pos = np.zeros((n_par, 2))
            for pars, tags in zip(l_par_pos, l_par_tag):
                np.put_along_axis(par_pos, tags.reshape((len(tags), 1)), pars, 0)

            par_typeid = np.zeros((n_par,), dtype=np.int32)
            for tids, tags in zip(l_par_typeid, l_par_tag):
                np.put_along_axis(par_typeid, tags, tids, 0)

            particles = Particles(par_pos, par_typeid)

            r0 = np.array([
                self._bond_force.params[bt]['r0']
                for bt in sorted(self._bond_force.params.keys(), key=int)],
                dtype=np.float64)
            k = np.array([
                self._bond_force.params[bt]['k']
                for bt in sorted(self._bond_force.params.keys(), key=int)],
                dtype=np.float64)
            bond_types = BondTypes(r0, k)

            bonds_group = np.concatenate(l_bonds_group)
            bonds_typeid = np.concatenate(l_bonds_typeid)
            bonds = Bonds(bonds_group, bonds_typeid)

            t0 = np.array([
                self._angle_cst_force.params[act]['t0']
                for act in sorted(self._angle_cst_force.params.keys(), key=int)],
                dtype=np.float64)
            k = np.array([
                self._angle_cst_force.params[act]['k']
                for act in sorted(self._angle_cst_force.params.keys(), key=int)],
                dtype=np.float64)
            angle_cst_types = AngleCstTypes(t0, k)

            angles_group = np.concatenate(l_angles_group)
            angles_typeid = np.concatenate(l_angles_typeid)
            angle_csts = AngleCsts(angles_group, angles_typeid)

            result = MDState(
                    particles, bond_types, bonds, angle_cst_types, angle_csts)
            tb = monotonic_ns()
            _logger.debug(f'get_state took {(tb - ta) * 1e-6} ms')
            return result

        return None

    def get_boundary_state(self) -> Optional[ECMBoundaryState]:
        """Get the state of the ECM boundary

        When running under MPI, this returns the state only for rank 0, on
        other ranks None is returned.
        """
        ta = monotonic_ns()
        bnd_par_ids = int_set_to_array(self._boundary.par_ids)
        bnd_bond_ids = int_set_to_array(self._boundary.bond_ids)
        bnd_angle_cst_ids = int_set_to_array(self._boundary.angle_cst_ids)

        with self._sim.state.cpu_local_snapshot as snapshot:
            indices = snapshot.particles.rtag[bnd_par_ids]
            local_indices = indices[indices != _HOOMD_NOT_LOCAL]
            n_local_par = snapshot.particles.tag.shape[0]
            non_ghost_indices = local_indices[local_indices < n_local_par]

            local_par_ids = snapshot.particles.tag[non_ghost_indices]
            local_par_pos = snapshot.particles.position[non_ghost_indices, :2]
            if len(local_par_pos) > 0:
                local_par_pos -= self._pos_offset
            local_type_ids = snapshot.particles.typeid[non_ghost_indices]

            par_ids_list = self._comm.gather(local_par_ids)
            par_pos_list = self._comm.gather(local_par_pos)
            par_type_list = self._comm.gather(local_type_ids)

            indices = snapshot.bonds.rtag[bnd_bond_ids]
            local_indices = indices[indices != _HOOMD_NOT_LOCAL]
            local_bond_ids = snapshot.bonds.tag[local_indices]
            local_bond_groups = snapshot.bonds.group[local_indices]
            local_bond_typeids = snapshot.bonds.typeid[local_indices]

            bond_ids_list = self._comm.gather(local_bond_ids)
            bond_groups_list = self._comm.gather(local_bond_groups)
            bond_typeid_list = self._comm.gather(local_bond_typeids)

            indices = snapshot.angles.rtag[bnd_angle_cst_ids]
            local_indices = indices[indices != _HOOMD_NOT_LOCAL]
            local_angle_cst_ids = snapshot.angles.tag[local_indices]
            local_angle_cst_groups = snapshot.angles.group[local_indices]
            local_angle_cst_types = snapshot.angles.typeid[local_indices]

            angle_cst_ids_list = self._comm.gather(local_angle_cst_ids)
            angle_cst_groups_list = self._comm.gather(local_angle_cst_groups)
            angle_cst_typeids_list = self._comm.gather(local_angle_cst_types)

        if self.device.communicator.rank == 0:
            assert par_ids_list is not None
            assert par_pos_list is not None
            assert par_type_list is not None

            assert bond_ids_list is not None
            assert bond_groups_list is not None
            assert bond_typeid_list is not None

            assert angle_cst_ids_list is not None
            assert angle_cst_groups_list is not None
            assert angle_cst_typeids_list is not None

            par_ids = np.concatenate(par_ids_list, dtype=np.int32)
            par_pos = np.concatenate(par_pos_list, dtype=np.float64)
            par_type = np.concatenate(par_type_list, dtype=np.int32)

            bonds_ids = np.concatenate(bond_ids_list, dtype=np.int32)
            bonds_groups = np.concatenate(bond_groups_list, dtype=np.int32)
            bonds_typeids = np.concatenate(bond_typeid_list, dtype=np.int32)

            bond_types_ids = np.unique(bonds_typeids)
            bond_types_r0 = np.array([
                self._bond_force_cache[i][1]
                for i in bond_types_ids], dtype=np.float64)
            bond_types_k = np.array([
                self._bond_force_cache[i][0]
                for i in bond_types_ids], dtype=np.float64)

            angle_csts_ids = np.concatenate(angle_cst_ids_list, dtype=np.int32)
            angle_csts_groups = np.concatenate(angle_cst_groups_list, dtype=np.int32)
            angle_csts_typeids = np.concatenate(angle_cst_typeids_list, dtype=np.int32)

            angle_cst_types_ids = np.unique(angle_csts_typeids)
            angle_cst_types_t0 = np.array([
                self._angle_cst_force_cache[i][1]
                for i in angle_csts_typeids], dtype=np.float64)
            angle_cst_types_k = np.array([
                self._angle_cst_force_cache[i][0]
                for i in angle_csts_typeids], dtype=np.float64)

            result = ECMBoundaryState(
                    SparseParticles(par_ids, par_pos, par_type),
                    SparseBondTypes(bond_types_ids, bond_types_r0, bond_types_k),
                    SparseBonds(bonds_ids, bonds_groups, bonds_typeids),
                    SparseAngleCstTypes(
                        angle_cst_types_ids, angle_cst_types_t0, angle_cst_types_k),
                    SparseAngleCsts(
                        angle_csts_ids, angle_csts_groups, angle_csts_typeids))

            tb = monotonic_ns()
            _logger.debug(f'get_boundary_state took {(tb - ta) * 1e-6} ms')
            return result

        return None

    def apply_interactions(self, interactions: CellECMInteractions) -> None:
        """Process interaction requests from cells

        Args:
            interactions: Description of the desired interactions
        """
        print("Recieved interactions.")
        print(f"Asked to change { interactions.change_type_in_area.num_particles } particles")
        print(f"Asked to move { interactions.move_adhesion_particles.new_pos.shape[0] } particles")
        print(f"Asked to remove { interactions.remove_adhesion_particles.par_id.shape[0] } particles")

        with self._sim.state.cpu_local_snapshot as snapshot:
            self._apply_particle_type_changes(
                    interactions.change_type_in_area, snapshot)
            # TODO: interactions.add_adhesion_particles
            self._apply_adhesion_particle_moves(
                    interactions.move_adhesion_particles, snapshot)
            self._apply_adhesion_removal(
                interactions.remove_adhesion_particles,
                snapshot
            )
    def _apply_adhesion_removal(self,
            remove_adhesion_particles: RemoveAdhesionParticles, snapshot: LocalSnapshot):
        print("Removing the following: ")
        print(remove_adhesion_particles.par_id)

        ids_to_remove = remove_adhesion_particles.par_id
        indices_to_remove = snapshot.particles.rtag[ids_to_remove]
        snapshot.particles.typeid[indices_to_remove] = ParticleType.free.value

        self._boundary.remove_adhesions(snapshot, ids_to_remove)

    def _apply_particle_type_changes(
            self, change_type_in_area: ChangeTypeInArea, snapshot: LocalSnapshot
            ) -> None:
        """Change type of n particles in a given area

        Args:
            change_type_in_area: Description of the requested change
        """
        ta = monotonic_ns()
        if len(change_type_in_area.change_area) == 0:
            return

        # Find all particles in the change area
        from_type_id = change_type_in_area.from_type.value
        change_zone = {(x[0], x[1]) for x in change_type_in_area.change_area}

        potential_changes = list()
        for i in range(snapshot.particles.typeid.shape[0]):
            if snapshot.particles.typeid[i] == from_type_id:
                par_pos = snapshot.particles.position[i, :2] - self._pos_offset
                pixel_pos = tuple(map(int, np.floor(par_pos)))
                if pixel_pos in change_zone:
                    potential_changes.append(snapshot.particles.tag[i])

        all_potential_changes = self._comm.allgather(potential_changes)
        potential_changes = [par_id for l in all_potential_changes for par_id in l]

        if len(potential_changes) < change_type_in_area.num_particles:
            _logger.warning(
                    'There are not enough particles in the adhesion zone to'
                    ' create the requested number of adhesions. Please increase'
                    ' adhesion_zone_radius, decrease num_initial_adhesions, or'
                    ' provide an ECM with higher particle density.')
        

        # Randomly select the required number of particles
        selected_changes = list()
        if self.device.communicator.rank == 0:

            available = len(potential_changes)
            needed = min(change_type_in_area.num_particles, available)
            while needed > 0:
                if random() <= needed / available:
                    selected_changes.append(potential_changes[available - 1])
                    needed -= 1
                available -= 1

        selected_changes = self._comm.bcast(selected_changes)

        # Change the selected particles' types
        to_type_id = change_type_in_area.to_type.value

        for par_id in selected_changes:
            i = snapshot.particles.rtag[par_id]
            if i != _HOOMD_NOT_LOCAL:
                # ghost particles are out of range
                if i < snapshot.particles.typeid.shape[0]:
                    snapshot.particles.typeid[i] = to_type_id

        if change_type_in_area.from_type == ParticleType.adhesion:
            self._boundary.remove_adhesions(snapshot, selected_changes)

        if change_type_in_area.to_type == ParticleType.adhesion:
            self._boundary.add_adhesions(snapshot, selected_changes)

        tb = monotonic_ns()

    def _apply_adhesion_particle_moves(
            self, move_adhesion_particles: MoveAdhesionParticles,
            snapshot: LocalSnapshot) -> None:
        """Move adhesion particles to new locations

        Args:
            move_adhesion_particles: Description of the requested move
        """
        ta = monotonic_ns()
        for j, par_id in enumerate(move_adhesion_particles.par_id):
            i = snapshot.particles.rtag[par_id]
            if i != _HOOMD_NOT_LOCAL:
                if i < snapshot.particles.position.shape[0]:
                    snapshot.particles.position[i, :2] = \
                            move_adhesion_particles.new_pos[j] + self._pos_offset
        # This doesn't change the topology, so no need to update the boundary
        tb = monotonic_ns()

    def _set_state_from_ecm(self, ecm: MDState) -> None:
        """Updates the simulation with a new ECM description.

        This overwrites the current state with the one represented by ecm.

        Args:
            ecm: The new ECM to load.
        """
        snapshot = self._sim.state.get_snapshot()

        if self.device.communicator.rank == 0:
            snapshot.particles.N = len(ecm.particles.positions)
            snapshot.particles.position[:, :2] = ecm.particles.positions + self._pos_offset
            snapshot.particles.typeid[:] = ecm.particles.type_ids

            snapshot.bonds.N = len(ecm.bonds.typ)
            snapshot.bonds.group[:] = ecm.bonds.particle_groups
            snapshot.bonds.typeid[:] = ecm.bonds.typ

            snapshot.angles.N = len(ecm.angle_csts.typ)
            snapshot.angles.group[:] = ecm.angle_csts.particle_groups
            snapshot.angles.typeid[:] = ecm.angle_csts.typ

        self._integrator.forces.clear()
        self._bond_force = hoomd.md.bond.Harmonic()
        for bt in range(len(ecm.bond_types.r0)):
            self._bond_force.params[str(bt)] = {
                    'k': ecm.bond_types.k[bt],
                    'r0': ecm.bond_types.r0[bt]}
        self._integrator.forces.append(self._bond_force)

        self._bond_force_cache = {
                bt: (ecm.bond_types.k[bt], ecm.bond_types.r0[bt])
                for bt in range(len(ecm.bond_types.r0))}

        self._angle_cst_force = hoomd.md.angle.Harmonic()
        for act in range(len(ecm.angle_cst_types.t0)):
            self._angle_cst_force.params[str(act)] = {
                    'k': ecm.angle_cst_types.k[act],
                    't0': ecm.angle_cst_types.t0[act]}
        self._integrator.forces.append(self._angle_cst_force)

        self._angle_cst_force_cache = {
                act: (ecm.angle_cst_types.k[act], ecm.angle_cst_types.t0[act])
                for act in range(len(ecm.angle_cst_types.t0))}

        self._sim.state.set_snapshot(snapshot)

    def run(self) -> None:
        """Run the MD simulation for the configured number of steps"""
        ta = monotonic_ns()
        self._sim.run(self._its)
        tb = monotonic_ns()
        _logger.debug(f'run took {(tb - ta) * 1e-6} ms')
        _logger.info(f'sim timesteps per second: {self._sim.tps}')
