from tissue_simulation_toolkit.ecm.util import empty_f64, empty_i32

import numpy as np
import numpy.typing as npt

from dataclasses import dataclass, field


@dataclass
class SparseParticles:
    """A subset of particles

    Attributes:
        par_ids: Id of each particle as an Nx1 array
        positions: Location of each particle as an Nx2 array
        types: Particle type, see ParticleType, Nx1 array
    """
    par_ids: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    positions: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    types: npt.NDArray[np.int32] = field(default_factory=empty_i32)


@dataclass
class SparseBondTypes:
    """Defines types of bonds.

    Bonds are linear compression/tension springs with given length and spring
    constant.

    Attributes:
        bond_type_ids: Id of each bond type as an Nx1 array
        r0: Nx1 array of rest lengths for the different bond types
        k: Nx1 array of spring constants (stiffness)
    """
    bond_type_ids: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    r0: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    k: npt.NDArray[np.float64] = field(default_factory=empty_f64)


@dataclass
class SparseBonds:
    """Defines a bond.

    A bond connects two particles and is of a given type. The ids in
    particle_groups must be matched to SparseParticles.par_ids, likewise
    for types and SparseBondTypes.bond_type_ids.

    Attributes:
        bond_ids: Id of each bond as an Nx1 array
        particle_groups: Nx2 array of particle ids, one row per bond
        types: Id of each bond's type
    """
    bond_ids: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    particle_groups: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    types: npt.NDArray[np.int32] = field(default_factory=empty_i32)


@dataclass
class SparseAngleCstTypes:
    """Defines types of angle constraint.

    Angle constraints can be considered to be torsion springs, with the axis
    around which the torsion applies perpendicular to the 2D plane.
    Intuitively, they try to keep a string of 3 bonded particless at a fixed
    angle.

    Attributes:
        angle_cst_type_ids: Id of each type, Nx1 array
        t0: Rest angle, Nx1 array
        k: Spring constant (stiffness), Nx1 array
    """
    angle_cst_type_ids: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    t0: npt.NDArray[np.float64] = field(default_factory=empty_f64)
    k: npt.NDArray[np.float64] = field(default_factory=empty_f64)


@dataclass
class SparseAngleCsts:
    """Defines angle constraints.

    This constrains the two particles at the ends of a 3-particle string,
    relative to the other two.

    The ids in particle_groups must be matched to SparseParticles.par_ids,
    likewise for types and SparseAngleCstTypes.angl_cst_type_ids.

    Attributes:
        angle_cst_ids: Nx1 array of angle constraint ids
        particle_groups: Nx3 array of particle ids, one row per constraint
        type: Constraint type as an Nx1 array
    """
    angle_cst_ids: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    particle_groups: npt.NDArray[np.int32] = field(default_factory=empty_i32)
    types: npt.NDArray[np.int32] = field(default_factory=empty_i32)


@dataclass
class ECMBoundaryState:
    """Coarse-grained MD representation of the ECM boundary.

    This is similar to MDState, but contains only the particles
    relevant to the Cellular Potts model. These are all particles of type
    adhesion, and any particles of any type that they share a bond or an
    angle constraint with.

    Attributes:
        particles: Particles making up the boundary.
        bond_types: The different types of bonds available.
        bonds: Bonds between particles, as described above.
        angle_cst_types: Types of angle constraints.
        angle_csts: Angle constraints.
    """
    particles: SparseParticles = field(default_factory=SparseParticles)
    bond_types: SparseBondTypes = field(default_factory=SparseBondTypes)
    bonds: SparseBonds = field(default_factory=SparseBonds)
    angle_cst_types: SparseAngleCstTypes = field(default_factory=SparseAngleCstTypes)
    angle_csts: SparseAngleCsts = field(default_factory=SparseAngleCsts)
