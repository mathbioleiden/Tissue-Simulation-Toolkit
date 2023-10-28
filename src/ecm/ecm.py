from tissue_simulation_toolkit.ecm.util import empty_f64, empty_i32

from dataclasses import dataclass, field
from enum import Enum

import numpy as np
import numpy.typing as npt


class ParticleType(Enum):
    """Types of particles in the ECM.

    These have to be numbered sequentially starting with 0, and match the
    corresponding definition in TST.

    There are different kinds of particles in the ECM simulation, as follows:

    - Free particles can move freely, subject to forces applied by bond and
      angle constraints applying to them.

    - Boundary particles are fixed. They anchor the ECM to the walls of the
      dish.

    - Adhesion particles are attached to the cell sitting in or on top of the
      ECM. They move with the cell, not with the ECM. Bonds between adhesion and
      non-adhesion particles attach the cell to the ECM.

    - Excluded particles are particles that essentially do not exist. This is
      used as a marker to remove particles that e.g. would be inside a cell,
      which shouldn't happen.
    """
    free = 0
    boundary = 1
    adhesion = 2
    excluded = 3


@dataclass
class Particles:
    """Defines particles.

    Attributes:
        positions: Location of each particle as an Nx2 array
        type_ids: Particle type, see ParticleType, Nx1 array
    """
    positions: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    type_ids: npt.NDArray[np.int32] = field(default_factory=empty_i32)


@dataclass
class BondTypes:
    """Defines types of bonds.

    Bonds are linear compression/tension springs with given length and spring
    constant.

    Attributes:
        r0: n-vector of rest lengths for the different bond types
        k: n-vector of spring constants (stiffness)
    """
    r0: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    k: npt.NDArray[np.float64] = field(default_factory=empty_f64)


@dataclass
class Bonds:
    """Defines a bond.

    A bond connects two particles and is of a given type.

    Attributes:
        particle_groups: n*2 array of particle ids, one row per bond
        typ: Bond type
    """
    # index into Particles
    particle_groups: npt.NDArray[np.int32] = field(default_factory=empty_i32)

    # index into BondTypes
    typ: npt.NDArray[np.int32] = field(default_factory=empty_i32)


class NamedBondTypes(Enum):
    """Special named bond types in the ECM.

    Some bond types are treated specially by the code, and they're named here
    for convenience. The numerical value is the bond type id (see
    MDState.bond_types).
    """
    fiber = 0


@dataclass
class AngleCstTypes:
    """Defines types of angle constraint.

    Angle constraints can be considered to be torsion springs, with the axis
    around which the torsion applies perpendicular to the 2D plane.
    Intuitively, they try to keep a string of 3 bonded particless at a fixed
    angle.

    Attributes:
        t0: Rest angle
        k: Spring constant (stiffness)
    """
    t0: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    k: npt.NDArray[np.float64] = field(default_factory=empty_f64)


@dataclass
class AngleCsts:
    """Defines angle constraints.

    This constrains the two particles at the ends of a 3-particle string,
    relative to the other two.

    Attributes:
        particle_groups: n*3 array of particle ids, one row per constraint
        type: Constraint type
    """
    # index into Particles
    particle_groups: npt.NDArray[np.int32] = field(default_factory=empty_i32)

    # index into AngleCstTypes
    typ: npt.NDArray[np.int32] = field(default_factory=empty_i32)


@dataclass
class MDState:
    """Coarse-grained MD simulation state.

    This represents the state of the course-grained molecular dynamics model.
    It comprises a collection of particles, with linear springs constraining the
    distance between designated pairs of particles and torsion springs
    constraining angles formed by groups of three particles each.

    Attributes:
        particles: Particles making up the ECM. The particle id of a particle
                is its index into the attributes of this object.
        bond_types: The different types of bonds available. The bond type id of
                a bond type is its index into the attributes of this object.
        bonds: Bonds between particles. The index of a bond in the attributes
                of this object is its bond id.
        angle_cst_types: Types of angle constraints. The angle constraint type
                id of an angle constraint type is its index into the attributes
                of this object.
        angle_csts: Angle constraints. The index of an angle constraint in the
                attributes of this object is its angle constraint id.
    """
    particles: Particles = field(default_factory=Particles)
    bond_types: BondTypes = field(default_factory=BondTypes)
    bonds: Bonds = field(default_factory=Bonds)
    angle_cst_types: AngleCstTypes = field(default_factory=AngleCstTypes)
    angle_csts: AngleCsts = field(default_factory=AngleCsts)
