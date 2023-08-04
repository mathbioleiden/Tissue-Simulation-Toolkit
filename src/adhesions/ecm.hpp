#pragma once

#include "vec2.hpp"

#include <array>
#include <vector>


/// Typedef for particle ids, for clarity
typedef int ParId;

/// Typedef for bond type ids, for clarity
typedef int BondTypeId;

/// Typedef for bond ids, for clarity
typedef int BondId;

/// Typedef for angle constraint type ids, for clarity
typedef int AngleCstTypeId;

///// Typedef for angle constraint ids, for clarity
typedef int AngleCstId;


/** Types of particles in the ECM.
 *
 * There are different kinds of particles in the ECM simulation, as follows:
 *
 * - Free particles can move freely, subject to forces applied by bond and
 *   angle constraints applying to them.
 *
 * - Boundary particles are fixed. They anchor the ECM to the walls of the
 *   dish.
 *
 * - Adhesion particles are attached to the cell sitting in or on top of the
 *   ECM. They move with the cell, not with the ECM. Bonds between adhesion and
 *   non-adhesion particles attach the cell to the ECM.
 *
 * - Excluded particles are particles that essentially do not exist. This is
 *   used as a marker to remove particles that e.g. would be inside a cell,
 *   which shouldn't happen.
 */
enum class ParticleType {
    free = 0,
    boundary = 1,
    adhesion = 2,
    excluded = 3
};


/** Defines a particle.
 *
 * Particles have a location in a 2D space, and a type.
 */
struct Particle {
    /// Create a Particle
    Particle(ParPos pos, ParticleType type);

    /// Location
    ParPos pos;

    // Particle type
    ParticleType type;
};


/** Defines a type of bond.
 *
 * Bonds are linear compression/tension springs with given length and spring
 * constant.
 */
struct BondType {
    /// Create an uninitialised bond type
    BondType() = default;

    /// Create a bond type with given parameters
    BondType(double r0, double k);

    /// Rest length
    double r0;

    /// Spring constant (stiffness)
    double k;
};


/** Defines a bond.
 *
 * A bond connects two particles and is of a given type.
 */
struct Bond {
    Bond(ParId p1, ParId p2, BondTypeId type);

    /// Bonded particles
    ParId p1, p2;

    /// Bond type
    BondTypeId type;
};


/** Special named bond types in the ECM.
 *
 * Some bond types are treated specially by the code, and they're named here
 * for convenience. The numerical value is the bond type id (see
 * ExtraCellularMatrix::bond_types).
 */
enum class NamedBondTypes : BondTypeId {
    fiber = 0
};


/** Defines a type of angle constraint.
 *
 * Angle constraints can be considered to be torsion springs, with the axis
 * around which the torsion applies perpendicular to the 2D plane.
 * Intuitively, they try to keep a string of 3 bonded particless at a fixed
 * angle.
 */
struct AngleCstType {
    /// Create an uninitialised angle constraint type
    AngleCstType() = default;

    /// Create an angle constraint type with given parameters
    AngleCstType(double t0, double k);

    /// Rest angle
    double t0;

    /// Spring constant (stiffness)
    double k;
};


/** Defines an angle constraint.
 *
 * This constrains the two particles at the ends of a 3-particle string,
 * relative to the other two.
 */
struct AngleCst {
    /// Create an angle constraint
    AngleCst(ParId p1, ParId p2, ParId p3, AngleCstTypeId type);

    /// Involved particles
    ParId p1, p2, p3;

    /// Constraint type
    AngleCstTypeId type;
};


/** Coarse-grained MD representation of the extracellular matrix (ECM).
 *
 * The ECM can be viewed from different perspectives. From a biological
 * perspective, it is (in the simplified representation used here) a collection
 * of collagen strands held together by crosslinkers. The strands consist of
 * strings of a fixed number of beads each, with each bead a coarse-grained MD
 * particle.
 *
 * When seen as a coarse-grained MD simulation, the ECM is a collection of
 * particles, with linear springs constraining the distance between designated
 * pairs of particles and torsion springs constraining angles formed by groups
 * of three particles each.
 *
 * Finally, from a Cellular Potts perspective, the ECM is a substance covering
 * the domain between the cells which affects the work required to copy pixels.
 * Interaction between a cell and the ECM is via ECM particles that are adhered
 * to by the cell and are dragged along as we attempt to copy the pixel they
 * are in. In this implementation, updates to the ECM and the CPM are
 * alternated, so that the ECM is held fixed while the CPM updates, and vice
 * versa. As a result, only a small boundary region of the ECM is involved in
 * the interaction with the CPM. We call this the interface region.
 *
 * Since this is the CPM, the latter perspectives are most relevant, and this
 * class models the ECM as a collection of MD particles, bond constraints and
 * angle constraints, with no explicit representation of fibers.
 *
 * The representation used here is chosen mostly for flexibility. If a faster
 * representation is needed, then it can usually be generated once after each
 * MD update, and then used for many copy attempts. See Adhesions for an
 * example.
 */
struct ExtraCellularMatrix {
    /** Particles making up the ECM.
     *
     * The particle id of a particle is its index in this vector.
     *
     * particles[ParId].pos.x, .pos.y or .type
     */
    std::vector<Particle> particles;

    /** The different types of bonds available.
     *
     * The bond type id of a bond type is its index in this vector.
     */
    std::vector<BondType> bond_types;

    /** Bonds between two particles.
     *
     * The index of a bond in this vector is its bond id.
     */
    std::vector<Bond> bonds;

    /** Types of angle constraints.
     *
     * The angle constraint type id of an angle constraint type is its index
     * into this vector.
     */
    std::vector<AngleCstType> angle_cst_types;

    /** Angle constraints.
     *
     * The index of an angle constraint in this vector is its angle constraint
     * id.
     */
    std::vector<AngleCst> angle_csts;
};

