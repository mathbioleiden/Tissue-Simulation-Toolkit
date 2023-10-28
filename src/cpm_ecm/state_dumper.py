"""Model state dumper
"""
import logging
import pickle

from libmuscle import Instance
import numpy as np
from ymmsl import Operator


_logger = logging.getLogger(__name__)



def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    instance = Instance({
        Operator.F_INIT: ['cpm_state_in', 'ecm_state_in']})

    while instance.reuse_instance():
        Lx = instance.get_setting('Lx', 'float')
        Ly = instance.get_setting('Ly', 'float')

        cpm_state_msg = instance.receive('cpm_state_in')
        ecm_state_msg = instance.receive('ecm_state_in')

        mcs = int(cpm_state_msg.timestamp)

        snapshot = {
                'Lx': Lx,
                'Ly': Ly,
                'mcs': mcs,
                'cpm_state': cpm_state_msg.data,
                'ecm_state': ecm_state_msg.data}

        with open(f'state_{mcs:05d}.pickle', 'wb') as f:
            pickle.dump(snapshot, f)


if __name__ == '__main__':
    main()
