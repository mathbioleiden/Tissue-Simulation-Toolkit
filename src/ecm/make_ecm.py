from tissue_simulation_toolkit.ecm.muscle3 import from_settings
from tissue_simulation_toolkit.ecm.parameters import GenerationParameters
from tissue_simulation_toolkit.ecm.ecm import ParticleType

from ecmgen import random_network, single_strand, Network, single_spring, ISV_network, regular, random_directed_network, laminin, rotate_network


from libmuscle import Instance, Message
from libmuscle import KEEPS_NO_STATE_FOR_NEXT_USE  # type: ignore
import numpy as np
from ymmsl import Operator

import logging


_logger = logging.getLogger(__name__)


def generate_network(par):
    return random_network(
        sizex=par.box_size_x,
        sizey=par.box_size_y,
        number_of_beads_per_strand=par.beads,
        number_of_strands=par.strands,
        contour_length_of_strand=par.contour_length,
        crosslink_max_r=par.crosslink_max_r,
        maximal_number_of_initial_crosslinks=par.num_init_crosslinks,
        crosslink_bin_size=par.crosslink_bin_size,
        seed=par.network_seed,
        fix_boundary=par.fixed_boundary,
    )


def encode_net_as_dict(par, network: Network):
    # Decode particles
    particles_positions = np.array(network.beads_positions, dtype=np.float64)
    particles_types = []
    ParticleTypeDict = {i.name: i.value for i in ParticleType}
    print(ParticleTypeDict)
    for typ in network.beads_types:
        if not typ in ParticleTypeDict.keys():
            raise RuntimeError(f"Particle type {typ} is not known.")
        particles_types.append(ParticleTypeDict[typ])
    particles_types = np.array(particles_types, dtype=np.int32)  # type:ignore

    # Decode bonds
    bonds_groups = np.array(network.bonds_groups, dtype=np.int32)
    bonds_types = []

    bonds_possible_types = {
        "polymer": {"id": 0, "r0": par.spring_r0, "k": par.spring_k}
    }
    print("Details of bond types are " , network.details_of_bondtypes)
    id_counter = 1
    for typ in network.bonds_types:
        if typ not in bonds_possible_types.keys():
            bonds_possible_types[typ] = {
                "id": id_counter,
                "r0": network.details_of_bondtypes[typ]["r0"],
                "k": network.details_of_bondtypes[typ]["k"]*par.spring_k,
            }
            print("BONDS POSSIBLE K ", bonds_possible_types[typ])
            id_counter += 1
        bonds_types.append(bonds_possible_types[typ]["id"])
    bonds_types = np.array(bonds_types, dtype=np.int32)  # type: ignore

    bonds_r0 = []
    bonds_k = []
    for name, value in sorted(
        bonds_possible_types.items(), key=lambda keyvalue: keyvalue[1]["id"]
    ):
        print(f"Making bond {name} with type {value}")
        bonds_r0.append(value["r0"])
        bonds_k.append(value["k"])
    bonds_r0 = np.array(bonds_r0, dtype=np.float64)  # type: ignore
    bonds_k = np.array(bonds_k, dtype=np.float64)  # type: ignore

    return {
        "particles": {"positions": particles_positions, "types": particles_types},
        "bond_types": {
            "r0": bonds_r0,
            "k": bonds_k,
        },
        "bonds": {"groups": bonds_groups, "types": bonds_types},
        "angle_cst_types": {
            "t0": np.array([par.bend_t0], dtype=np.float64),
            "k": np.array([par.bend_k], dtype=np.float64),
        },
        "angle_csts": {
            "groups": np.array(network.angle_groups, dtype=np.int32),
            "types": np.array([0] * len(network.angle_groups), dtype=np.int32),
        },
    }


def main():
    logging.basicConfig(level=logging.INFO)
    instance = Instance({Operator.O_F: ["ecm_out"]}, KEEPS_NO_STATE_FOR_NEXT_USE)

    while instance.reuse_instance():
        par = from_settings(GenerationParameters, instance)
        try:
            nettype = instance.get_setting("network_type", "str")
        except KeyError:
            nettype = "random"

        if nettype == "single_strand":
            net = single_strand(
                sizex=par.box_size_x,
                sizey=par.box_size_y,
                start_x=-par.spring_r0,
                start_y=100,
                angle=np.pi,
                number_of_beads_per_strand=par.beads,
                contour_length_of_strand=par.contour_length,
                seed=None,
            )
        elif nettype == "random":
            net = generate_network(par)
        elif nettype == "single_spring":
            net = single_spring(
                sizex=par.box_size_x,
                sizey=par.box_size_y,
                number_of_strands=par.strands,
                number_of_beads_per_strand=par.beads,
                contour_length_of_strand=(par.beads - 1) * par.spring_r0,
                seed=None,
            )
        elif nettype == "ISV_network":
            net = ISV_network(
                sizex=par.box_size_x,
                sizey=par.box_size_y,
                number_of_beads_per_strand=par.beads,
                number_of_strands=par.strands,
                contour_length_of_strand=par.contour_length,
                crosslink_max_r=par.crosslink_max_r,
                maximal_number_of_initial_crosslinks=par.num_init_crosslinks,
                crosslink_bin_size=par.crosslink_bin_size,
                seed=par.network_seed,
                fix_boundary=par.fixed_boundary,
                spread_xaxis=instance.get_setting("ISV_xaxis_spread", "float"),
            )
        elif nettype == "ISV_network_laminin":
            net = ISV_network(
                sizex=par.box_size_x,
                sizey=par.box_size_y,
                number_of_beads_per_strand=par.beads,
                number_of_strands=par.strands,
                contour_length_of_strand=par.contour_length,
                crosslink_max_r=par.crosslink_max_r,
                maximal_number_of_initial_crosslinks=par.num_init_crosslinks,
                crosslink_bin_size=par.crosslink_bin_size,
                seed=par.network_seed,
                fix_boundary=par.fixed_boundary,
                spread_xaxis=instance.get_setting("ISV_xaxis_spread", "float"),
            )
            laminin(
                sizex=par.box_size_x,
                sizey=par.box_size_y,
                amount_of_laminin=instance.get_setting("ISV_laminin_amount", "int"),
                network=net,
                seed=par.network_seed
            )
        elif nettype == "regular":
            net = regular(
                sizex = par.box_size_x,
                sizey = par.box_size_y,
                number_of_fibers_per_side= par.strands // 2,
                number_of_beads_per_strand= par.beads,
                fix_boundary=par.fixed_boundary,
                single_side=instance.get_setting("regular_vertical", "bool"),
            )
        elif nettype == "vertical_different_bonds":
            horizonal = regular(
                sizex = par.box_size_x,
                sizey = par.box_size_y,
                number_of_fibers_per_side= par.strands // 2,
                number_of_beads_per_strand= par.beads,
                fix_boundary=par.fixed_boundary,
                single_side=True,
            )
             # rotate_network(horizonal, 3.1415 * 0.5) 
            rotate_network(horizonal, 3.1415 * 0.5) 

            vertical = regular(
                sizex = par.box_size_x,
                sizey = par.box_size_y,
                number_of_fibers_per_side= par.strands // 2,
                number_of_beads_per_strand= par.beads,
                fix_boundary=par.fixed_boundary,
                single_side=True,
            )
            vertical.bonds_types = [
                typ + "_vertical" for typ in vertical.bonds_types 
            ]
            vertical.details_of_bondtypes.clear()
            vertical.details_of_bondtypes["polymer_vertical"] = {
                "k": instance.get_setting("vertical_horizontal_ratio", "float"),
                'r0': par.spring_r0
            }
            print("vertical_polymer k is = ", instance.get_setting("vertical_horizontal_ratio", "float") * par.spring_k)

            # net = horizonal + vertical
            net =  horizonal + vertical

            print(net.details_of_bondtypes)
        elif nettype == "directed":
            net = random_directed_network(
                sizex=par.box_size_x,
                sizey=par.box_size_y,
                number_of_beads_per_strand=par.beads,
                number_of_strands=par.strands,
                direction_angle=instance.get_setting("direction_angle", "float"),
                direction_spread=instance.get_setting("direction_spread", "float"),
                contour_length_of_strand=par.contour_length,
                crosslink_max_r=par.crosslink_max_r,
                maximal_number_of_initial_crosslinks=par.num_init_crosslinks,
                crosslink_bin_size=par.crosslink_bin_size,
                seed=par.network_seed,
                fix_boundary=par.fixed_boundary,
            )
        else:
            raise NotImplementedError("Network type %s is not implemented." % nettype)

        instance.send("ecm_out", Message(0.0, data=encode_net_as_dict(par, net)))
        # encode_net(net)))

        _logger.info(f"Generated {len(net.beads_positions)} particles")
        _logger.info(f"Generated {len(net.bonds_groups)} bonds")
        _logger.info(f"Generated {len(net.angle_groups)} angle constraints")
        _logger.info(
            f"Generated {len([x for x in net.bonds_types if x.startswith('cross_')])} crosslinkers"
        )
