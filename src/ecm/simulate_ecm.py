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
from typing import Any, Dict, List


_logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    instance = Instance({
        Operator.F_INIT: ['ecm_in'],
        Operator.O_I: ['ecm_boundary_state_out', 'state_out'],
        Operator.S: ['cell_ecm_interactions_in'],
        Operator.O_F: ['ecm_out']})

    while instance.reuse_instance():
        # F_INIT
        par = from_settings(EvolutionParameters, instance)
        mcs = instance.get_setting('mcs', 'int')
        try:
            state_output_interval = instance.get_setting('state_output_interval', 'int')
        except KeyError:
            state_output_interval = mcs + 1

        msg = instance.receive('ecm_in')
        ecm = decode_mdstate(msg.data)
        sim = Simulation(par, ecm)

        for i in range(mcs):
            # O_I

            msg = instance.receive('cell_ecm_interactions_in', default=Message(0.0))
            if msg.data is not None:
                sim.apply_interactions(decode_cell_ecm_interactions(msg.data))

            sim.run()
                    
            boundary = encode_ecm_boundary_state(sim.get_boundary_state())
            msg = Message(msg.timestamp, data=boundary)
            instance.send('ecm_boundary_state_out', msg)

            if instance.is_connected('state_out'):
                if i % state_output_interval == 0:
                    state = sim.get_state()
                    instance.send('state_out', Message(i, data=encode_mdstate(state)))



        # O_F
        message = Message(msg.timestamp, data=encode_mdstate(sim.get_state()))
        instance.send('ecm_out', message)


if __name__ == '__main__':
    main()
