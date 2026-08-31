from tissue_simulation_toolkit.ecm.muscle3 import encode_net, from_settings
from tissue_simulation_toolkit.ecm.network.network import generate_network
from tissue_simulation_toolkit.ecm.parameters import GenerationParameters

from libmuscle import Instance, Message
from libmuscle import KEEPS_NO_STATE_FOR_NEXT_USE   # type: ignore
import numpy as np
from ymmsl import Operator

import logging


_logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    instance = Instance(
            {Operator.O_F: ['ecm_out']}, KEEPS_NO_STATE_FOR_NEXT_USE)

    while instance.reuse_instance():
        impose_default_settings(instance)
        par = from_settings(GenerationParameters, instance)
        net = generate_network(par)
        instance.send('ecm_out', Message(0.0, data=encode_net(net)))

        _logger.info(f'Generated {len(net.particles_typeid)} particles')
        _logger.info(f'Generated {len(net.bonds_typeid)} bonds')
        _logger.info(f'Generated {len(net.angles_typeid)} angle constraints')
        _logger.info(f'Generated {len(net.crosslink_typeid)} crosslinkers')

def impose_default_settings(instance):
    # This is a function used for setting default settings in the instance
    # in case it was not specified in the ymmsl file.

    default_setting_dic = { "network_type":         "random",
                            "network_square_size":  -1.0, # This is used as a default value to avoid errors.
                            "network_file_path":    ""}

    for key in default_setting_dic.keys():
        if not key in instance._settings_manager.base.keys():
            instance._settings_manager.base[key] = default_setting_dic[key]
    return instance
