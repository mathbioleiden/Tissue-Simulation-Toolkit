from tissue_simulation_toolkit.ecm.muscle3 import (
        decode_cell_ecm_interactions, decode_mdstate, encode_mdstate,
        encode_ecm_boundary_state, from_settings)
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
from typing import Any, Dict, List, Tuple


_logger = logging.getLogger(__name__)

from dataclasses import dataclass

@dataclass
class TaggedParticle:
    index: int
    direction: Tuple[float, float]
    
def tag_boundary_cardinal__directions(sim, par) -> List[TaggedParticle]:
    ecm = sim.get_state()
    particle_pos = ecm.particles.positions
    
    output = []
    
    # Horizontal, left
    for index in np.nonzero(particle_pos[:,0] < 0)[0]:
        output.append( TaggedParticle(index, (-1, 0))) 

    # Horizontal, right
    for index in np.nonzero(particle_pos[:,0] > par.box_size_x)[0]:
        output.append( TaggedParticle(index, (1, 0))) 

    # Vertical, up
    for index in np.nonzero(particle_pos[:,1] > par.box_size_y)[0]:
        output.append( TaggedParticle(index, (0, 1))) 

    # Vertical, down
    for index in np.nonzero(particle_pos[:,1] < 0)[0]:
        output.append( TaggedParticle(index, (0, -1))) 
    
    return output 
    
from tissue_simulation_toolkit.ecm.cell_ecm_interactions import CellECMInteractions, ChangeTypeInArea, AddAdhesionParticles, MoveAdhesionParticles, RemoveAdhesionParticles
def stretch_network(sim: Simulation,par: EvolutionParameters, stretch_steps: int, tagged_particles: List[TaggedParticle]):
    for i in range(stretch_steps):
        ecm = sim.get_state()
        move_adhesion_particles = MoveAdhesionParticles()
        move_adhesion_particles.par_id = np.empty(len(tagged_particles),dtype=np.int32)
        move_adhesion_particles.new_pos = np.empty((len(tagged_particles),2),dtype=np.float64)
        for k, tp in enumerate(tagged_particles):
            move_adhesion_particles.new_pos[k,:] = ecm.particles.positions[tp.index, :] + np.array(tp.direction)
            move_adhesion_particles.par_id[k]  = tp.index
            _logger.debug("Request particle %s to move from %s to %s " % (tp.index, ecm.particles.positions[tp.index, :],move_adhesion_particles.new_pos[k, :]))

        interactions = CellECMInteractions(
            ChangeTypeInArea(),
            AddAdhesionParticles(),
            move_adhesion_particles,
            RemoveAdhesionParticles()
        )
        sim.apply_interactions(interactions)
        _logger.info("Stretching step %s" % i) 
        sim.run()


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    instance = Instance({
        Operator.F_INIT: ['ecm_in'],
        Operator.O_I: ['ecm_boundary_state_out', 'state_out'],
        Operator.S: ['cell_ecm_interactions_in'],
        Operator.O_F: ['ecm_out']})

    while instance.reuse_instance():
        # F_INIT
        evo_par = from_settings(EvolutionParameters, instance)

        mcs = instance.get_setting('mcs', 'int')
        msg = instance.receive('ecm_in')
        ecm = decode_mdstate(msg.data)
        sim = Simulation(evo_par, ecm)
        
        stretch_steps = instance.get_setting("number_of_stretch_steps", "int")

        tagged_particles = tag_boundary_cardinal__directions(sim, evo_par)
        _logger.info("Tagged %s particles for stretching." % len(tagged_particles))
        stretch_network(sim, evo_par, stretch_steps, tagged_particles)
                    
        # O_F
        message = Message(msg.timestamp, data=encode_mdstate(sim.get_state()))
        instance.send('ecm_out', message)


if __name__ == '__main__':
    main()

