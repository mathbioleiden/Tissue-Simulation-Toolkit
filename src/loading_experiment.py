from tissue_simulation_toolkit.ecm.muscle3 import (
    decode_cell_ecm_interactions,
    decode_mdstate,
    encode_mdstate,
    encode_ecm_boundary_state,
    from_settings,
)
from tissue_simulation_toolkit.ecm.muscle3_mpi_wrapper import Instance
from tissue_simulation_toolkit.ecm.parameters import EvolutionParameters
from tissue_simulation_toolkit.ecm.simulation import Simulation
from tissue_simulation_toolkit.ecm.cell_ecm_interactions import (
    CellECMInteractions,
    MoveAdhesionParticles,
    ChangeTypeInArea,
    AddAdhesionParticles,
    RemoveAdhesionParticles,
)


from tissue_simulation_toolkit.ecm.muscle3 import (
    decode_cell_ecm_interactions,
    decode_mdstate,
    encode_mdstate,
    encode_ecm_boundary_state,
    from_settings,
)
from tissue_simulation_toolkit.ecm.muscle3_mpi_wrapper import Instance
from tissue_simulation_toolkit.ecm.parameters import EvolutionParameters
from tissue_simulation_toolkit.ecm.simulation import Simulation

import hoomd
import hoomd.md
from libmuscle import Message
import numpy as np
import os
from ymmsl import Operator

import logging
from typing import Any, Dict, List


_logger = logging.getLogger(__name__)


def fake_cpm(par):
    return {
        "cpm": np.zeros((par.box_size_x, par.box_size_y)),
        "pde": np.zeros((1, par.box_size_x, par.box_size_y)),
        "act_state": dict(),
    }


def stretch_ecm(sim: Simulation, tagged_particles, dx) -> CellECMInteractions:
    snapshot = sim.get_state()

    move_adhesion_particles = MoveAdhesionParticles()
    move_adhesion_particles.par_id = np.empty(len(tagged_particles), dtype=np.int32)
    move_adhesion_particles.new_pos = np.empty(
        (len(tagged_particles), 2), dtype=np.float64
    )

    for k, p in enumerate(tagged_particles):
        move_adhesion_particles.par_id[k] = p
        move_adhesion_particles.new_pos[k] = (
            snapshot.particles.positions[p, :] + np.array([1.0, 0.0]) * dx
        )
    print(move_adhesion_particles)
    return CellECMInteractions(
        ChangeTypeInArea(),
        AddAdhesionParticles(),
        move_adhesion_particles,
        RemoveAdhesionParticles(),
    )


def tag_particles(par, sim: Simulation):
    snapshot = sim.get_state()

    (particles,) = np.where(
        np.logical_and(
            snapshot.particles.type_ids == 1,
            snapshot.particles.positions[:, 1] > 0.95 * par.box_size_y,
        )
    )
    _logger.info("Tagged particles %s " % particles)
    return particles


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    instance = Instance(
        {
            Operator.F_INIT: ["ecm_in"],
            Operator.O_I: ["ecm_boundary_state_out", "state_out"],
            Operator.S: ["cell_ecm_interactions_in"],
            Operator.O_F: ["ecm_out", "cpm_out"],
        }
    )

    while instance.reuse_instance():
        # F_INIT
        par = from_settings(EvolutionParameters, instance)
        mcs = instance.get_setting("mcs", "int")
        try:
            state_output_interval = instance.get_setting("state_output_interval", "int")
        except KeyError:
            state_output_interval = mcs + 1

        msg = instance.receive("ecm_in")
        ecm = decode_mdstate(msg.data)
        sim = Simulation(par, ecm)

        tagged_particles = tag_particles(par, sim)

        snapshot = sim._sim.state.get_snapshot()
        snapshot.particles.typeid[tagged_particles] = 1
        # snapshot.particles.positions[p, :] + np.array([0.0, 1.0]) * dx
        sim._sim.state.set_snapshot(snapshot)
        sim._its = 1  # 0000
        sim.run()
        sim._its = par.md_its

        delta_x = instance.get_setting("displacement_per_step", "float")

        for i in range(mcs):
            # O_I

            interactions = stretch_ecm(sim, tagged_particles, delta_x)
            print(interactions)
            sim.apply_interactions(interactions)
            sim.run()

            if i == 0:
                state = sim.get_state()
                instance.send("ecm_out", Message(i, data=encode_mdstate(state)))
                instance.send("cpm_out", Message(i, data=fake_cpm(par)))
            elif i % state_output_interval == 0:
                state = sim.get_state(skip_bonds=True)
                instance.send("ecm_out", Message(i, data=encode_mdstate(state)))
                instance.send("cpm_out", Message(i, data=fake_cpm(par)))

        # O_F


#        message = Message(msg.timestamp, data=encode_mdstate(sim.get_state()))
#        instance.send("ecm_out", message)
#        instance.send("cpm_out", Message(msg.timestamp, data=fake_cpm(par)))


if __name__ == "__main__":
    main()
