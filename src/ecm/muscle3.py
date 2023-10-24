"""Helper functions for connecting to MUSCLE3

This module contains some functions for getting information from
MUSCLE3 into our custom data types, and vice versa for taking our
data and sending it to other components via MUSCLE3.
"""
from dataclasses import asdict, fields
import logging
from typing import Any, Optional, Type, TypeVar

from libmuscle import Instance
import numpy as np

from tissue_simulation_toolkit.ecm.ecm import (
        AngleCsts, AngleCstTypes, Bonds, BondTypes, ExtraCellularMatrix, Particles,
        ParticleType)
from tissue_simulation_toolkit.ecm.network.network import Network


_logger = logging.getLogger(__name__)


T = TypeVar('T')

def from_settings(ParType: Type[T], instance: Instance) -> T:
    """Create object with parameters from MUSCLE3 settings.

    Note that the first argument must be a type, specifically a
    dataclass, not an object. The result will be of this type.

    Example:
        par = from_settings(CreationParameters, instance)

    Args:
        par_type: The type of the parameter object to create
        instance: MUSCLE3 instance to get settings from.
    """
    # This uses introspection, which confuses mypy, so we tell it to ignore
    # the perceived problem.
    return ParType(**{
        field.name: instance.get_setting(
            field.name, field.type.__name__)    # type: ignore [call-overload]
        for field in fields(ParType)})          # type: ignore [arg-type]


def encode_ecm(ecm: Optional[ExtraCellularMatrix]) -> Any:
    """Encode an ECM into a MUSCLE3 message-compatible data object

    This does not copy the data, so the ECM object passed in must not
    be changed or the result will change too.

    Args:
        ecm: The ECM to encode
    """
    if ecm is None:
        return None

    return {
            'particles': {
                'positions': ecm.particles.positions,
                'types': ecm.particles.type_ids.astype(np.int32)},
            'bond_types': {
                'r0': ecm.bond_types.r0,
                'k': ecm.bond_types.k},
            'bonds': {
                'groups': ecm.bonds.particle_groups.astype(np.int32),
                'types': ecm.bonds.typ.astype(np.int32)},
            'angle_cst_types': {
                't0': ecm.angle_cst_types.t0,
                'k': ecm.angle_cst_types.k},
            'angle_csts': {
                'groups': ecm.angle_csts.particle_groups.astype(np.int32),
                'types': ecm.angle_csts.typ.astype(np.int32)}
            }


def encode_net(net: Network) -> Any:
    """Encode a Network into a MUSCLE3 message-compatible ECM object

    This does not copy the data, so the Network object passed in must not
    be changed or the result will change too.

    Args:
        net: The Network to encode
    """
    # This is a hack because the implementation of a limited set of
    # bond types in Network is a hack. That needs to be refactored,
    # meanwhile this is what we can do.
    bond_types_r0 = [net.bonds_r0[0]] + net.possible_r0
    bond_types_k = [net.bonds_k[0]] + net.possible_k
    _logger.debug(f'sending bond types r0: {bond_types_r0}')
    _logger.debug(f'sending bond types k: {bond_types_k}')
    return {
            'particles': {
                'positions': net.pos,
                'types': net.particles_typeid.astype(np.int32, casting='same_kind')},
            'bond_types': {
                'r0': np.array(bond_types_r0, dtype=np.float64),
                'k': np.array(bond_types_k, dtype=np.float64)
            },
            'bonds': {
                'groups': np.array(net.bonds_group, dtype=np.int32),
                'types': np.array(net.bonds_typeid, dtype=np.int32)},
            'angle_cst_types': {
                't0': np.array(net.angle_types_t0, dtype=np.float64),
                'k': np.array(net.angle_types_k, dtype=np.float64)},
            'angle_csts': {
                'groups': np.array(net.angles_group, dtype=np.int32),
                'types': np.array(net.angles_typeid, dtype=np.int32)}
            }


def decode_ecm(data: Any) -> ExtraCellularMatrix:
    """"Decode an ECM from a MUSCLE3 data object.

    This does not copy the data, so the data object passed in must not
    be changed or the result will change too.

    Args:
        data: The received message data to decode
    """
    particles = Particles(
            data['particles']['positions'].array.copy(),
            data['particles']['types'].array.copy())
    bond_types = BondTypes(
            data['bond_types']['r0'].array.copy(),
            data['bond_types']['k'].array.copy())
    bonds = Bonds(
            data['bonds']['groups'].array.copy(), data['bonds']['types'].array.copy())
    angle_cst_types = AngleCstTypes(
            data['angle_cst_types']['t0'].array.copy(),
            data['angle_cst_types']['k'].array.copy())
    angle_csts = AngleCsts(
            data['angle_csts']['groups'].array.copy(),
            data['angle_csts']['types'].array.copy())

    return ExtraCellularMatrix(
            particles, bond_types, bonds, angle_cst_types, angle_csts)
