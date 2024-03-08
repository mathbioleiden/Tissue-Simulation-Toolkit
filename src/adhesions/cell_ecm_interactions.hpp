#pragma once

#include "ecm_boundary_state.hpp"
#include "vec2.hpp"

#include <vector>

/** Request changing some of the particle's types
 *
 * This specifies an area as a list of pixels, and requests a random selection
 * of particles in this area of a given type to be changed to a different type.
 *
 * This is used to implement the original adhesion generation algorithm, which
 * is a bit funny biologically, but may be useful as a reference or something.
 */
struct ChangeTypeInArea {
  //! Create a ChangeTypeInArea representing no changes
  ChangeTypeInArea();

  //! Area within which to change particles, as a list of pixels
  std::vector<PixelPos> change_area;

  //! Number of particles to change the type of
  int num_particles;

  //! Type the particles must have before changing them
  ParticleType from_type;

  //! Type the particles will be assigned
  ParticleType to_type;

  //! Clear all changes
  void clear();
};

/** Add new adhesion particles
 *
 * These particles may represent various aspects of the cell, adhesions, etc.
 * depending on the algorithm. Technically however, they are marked as type
 * "adhesion", meaning that their position is controlled by the CPM and that the
 * ECM will take them into account, but not move them.
 *
 * After the particles are added, for any particles that have a value >0.0 for
 * bond_attempt_radius an attempt will be made to find a "free" type particle
 * within that radius. If one is found, a new bond will be made between them.
 * This represents the cell actually adhering to the ECM.
 */
struct AddAdhesionParticles {
  //! Positions of the new particles
  std::vector<ParPos> new_pos;

  //! Maximum bond radius, index corresponds to the positions
  std::vector<double> bond_attempt_radius;

  //! Clear all changes
  void clear();
};

/** Move existing adhesion particles
 *
 * Updates the position of existing "adhesion"-type particles. These particles
 * are controlled by the Cellular Potts Model, but the ECM needs to know where
 * they are so that they can correctly influence the rest of the ECM particles.
 */
struct MoveAdhesionParticles {
  //! Particle ids of the particles to move
  std::vector<ParId> par_id;

  //! New positions of the given particles
  std::vector<ParPos> new_pos;

  //! Clear all changes
  void clear();
};

/** Remove adhesion particles
 *
 * Removes adhesion particles from the simulation. This does not affect any
 * other particles, in particular no particle ids get renumbered.
 */
struct RemoveAdhesionParticles {
  //! Particle ids of the particles to remove
  std::vector<ParId> par_id;

  //! Clear all changes
  void clear();
};

/** Interaction requests from the cells to the ECM
 *
 * This data is sent from the Cellular Potts Model to the MD-based ECM model.
 */
struct CellECMInteractions {
  /** Requested particle type changes
   *
   * This one's a bit funny, it's here so we can implement the initial
   * adhesions algorithm.
   */
  ChangeTypeInArea change_type_in_area;

  //! Add new adhesion particles
  AddAdhesionParticles add_adhesion_particles;

  //! Move adhesion particles
  MoveAdhesionParticles move_adhesion_particles;

  //! Remove adhesion particles
  RemoveAdhesionParticles remove_adhesion_particles;

  //! Clear all changes
  void clear();
};
