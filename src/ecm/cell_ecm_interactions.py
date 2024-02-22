from dataclasses import dataclass, field

import numpy as np
import numpy.typing as npt

from tissue_simulation_toolkit.ecm.ecm import ParticleType
from tissue_simulation_toolkit.ecm.util import empty_f64, empty_i32


@dataclass
class ChangeTypeInArea:
    """Request changing some of the particles' types

    This specifies an area as a list of pixels, and requests a random selection of
    particles in this area of a given type to be changed to a different type.

    This is used to implement the original adhesion generation algorithm, which is
    a bit funny biologically, but may be useful as a reference or something.

    Attributes:
        change_area: Area within which to change particles, as an Nx2 array with each
                row containing x, y pixel coordinates
        num_particles: Number of particles to change the type of
        from_type: Type the particles must have before changing them
        to_type: Type the particles will be assigned
    """
    change_area: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    num_particles: int = 0
    from_type: ParticleType = ParticleType.free
    to_type: ParticleType = ParticleType.free


@dataclass
class AddAdhesionParticles:
    """Add new adhesion particles

    These particles may represent various aspects of the cell, adhesions, etc.
    depending on the algorithm. Technically however, they are marked as type
    "adhesion", meaning that their position is controlled by the CPM and that the
    ECM will take them into account, but not move them.

    After the particles are added, for any particles that have a value >0.0 for
    bond_attempt_radius an attempt will be made to find a "free" type particle
    within that radius. If one is found, a new bond will be made between them.
    This represents the cell actually adhering to the ECM.

    Attributes:
        new_pos: Nx2 array with each row containing x, y coordinates for a new
                particle to be added.
        bond_attempt_radius: Nx1 array of maximum bond radii, index corresponds
                to the positions.
    """
    new_pos: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    bond_attempt_radius: npt.NDArray[np.float64] = field(default_factory=empty_f64)


@dataclass
class MoveAdhesionParticles:
    """Move existing adhesion particles

    Updates the position of existing "adhesion"-type particles. These particles
    are controlled by the Cellular Potts Model, but the ECM needs to know where
    they are so that they can correctly influence the rest of the ECM particles.

    Attributes:
        par_id: Nx1 array of particle ids of the particles to move
        new_pos: Nx2 array with each row containing x, y coordinates to move the
                particles to.
    """
    par_id: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    new_pos: npt.NDArray[np.float64] = field(default_factory=empty_f64)


@dataclass
class RemoveAdhesionParticles:
    """Remove adhesion particles

    Removes adhesion particles from the simulation. This does not affect any other
    particles, in particular no particle ids get renumbered.

    Attributes:
        par_id: Nx1 array of particle ids of the particles to remove
    """
    par_id: npt.NDArray[np.int32] = field(default_factory=empty_i32)


@dataclass
class CellECMInteractions:
    """Interaction requests from the cells to the ECM

    This data is sent from the Cellular Potts Model to the MD-based ECM model.

    Attributes:
        change_type_in_area: Requested particle type changes
        add_adhesion_particles: Add new adhesion particles
        move_adhesion_particles: Move adhesion particles
        remove_adhesion_particles: Remove adhesion particles
    """
    change_type_in_area: ChangeTypeInArea
    add_adhesion_particles: AddAdhesionParticles
    move_adhesion_particles: MoveAdhesionParticles
    remove_adhesion_particles: RemoveAdhesionParticles
