#pragma once

#include "vec2.hpp"

#include <array>
#include <unordered_map>

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
enum class ParticleType { free = 0, boundary = 1, adhesion = 2, excluded = 3 };

typedef int Integrin;

/** Defines a particle.
 *
 * Particles have a location in a 2D space, and a type.
 */
struct Particle {
    /// Create an uninitialised particle
    Particle() = default;

    /// Create a Particle
    Particle(ParId par_id, ParPos pos, ParticleType type);

    // Id
    ParId par_id;

    /// Location
    ParPos pos;

    // Particle type
    ParticleType type;
    
    /// If the particle is an adhesion, it has a size
    Integrin size;
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
    /// Create an uninitialised bond
    Bond() = default;

    /// Create a bond with the given parameters
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
 * MDState::bond_types).
 */
enum class NamedBondTypes : BondTypeId { fiber = 0 };

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
    /// Create an uninitialised angle constraint
    AngleCst() = default;

    /// Create an angle constraint
    AngleCst(ParId p1, ParId p2, ParId p3, AngleCstTypeId type);

    /// Involved particles
    ParId p1, p2, p3;

    /// Constraint type
    AngleCstTypeId type;
};

/** Boundary of the MD representation of the extracellular matrix (ECM).
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
 * of three particles each. Most of these particles represent the ECM, but some
 * of them represent adhesions and/or other parts of the cells.
 *
 * Finally, from a Cellular Potts perspective, the ECM is a substance covering
 * the domain between the cells which affects the work required to copy pixels.
 * Interaction between a cell and the ECM is via ECM particles that are adhered
 * to by the cell and are dragged along as we attempt to copy the pixel they
 * are in.
 *
 * In this implementation, the ECM and the CPM interact via special particles
 * of type ParticleType::adhesion. These particles and the particles they
 * attach to via bonds and angle constraints form a subset of the MD simulation
 * state that is directly affected by both models. We call this subset the
 * *boundary* between the two models.
 *
 * This class contains the complete state of the boundary: the type and location
 * of the particles in it, and any bonds and angle constraints between them. It
 * does not contain particles that aren't attached to an adhesion particle
 * directly, and it doesn't contain any bonds or angle constraints that do not
 * include an adhesion particle.
 *
 * The representation used here is chosen mostly for flexibility. If a faster
 * representation is needed, then it can usually be generated once after each
 * MD update, and then used for many copy attempts. See AdhesionIndex for an
 * example.
 */
struct ECMBoundaryState {
    /** Particles making up the ECM - CPM boundary.
     *
     * particles[ParId].pos.x, .pos.y or .type
     */
    std::unordered_map<ParId, Particle> particles;

    /** The different types of bonds available.
     */
    std::unordered_map<BondTypeId, BondType> bond_types;

    /** Bonds between two particles.
     */
    std::unordered_map<BondId, Bond> bonds;

    /** Types of angle constraints.
     */
    std::unordered_map<AngleCstTypeId, AngleCstType> angle_cst_types;

    /** Angle constraints.
     */
    std::unordered_map<AngleCstId, AngleCst> angle_csts;
};
