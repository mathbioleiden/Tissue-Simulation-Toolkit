#pragma once

#include "cell_ecm_interactions.hpp"
#include "ecm_boundary_state.hpp"
#include "vec2.hpp"

/** Tracks changes to the adhesions that affect the ECM */
class ECMInteractionTracker {
public:
  /** Record a particle being added
   *
   * If bond_attempt_radius is given and >0.0, the ECM model will try to add
   * a bond between the new particle and an existing ECM particle, if such
   * a particle can be found within the given radius.
   *
   * @param pos Position of the new particle
   * @param bond_attempt_radius Radius for a bond attempt
   */
  void record_new_particle(ParPos pos, double bond_attempt_radius);

  /** Record a particle being moved
   *
   * @param id Id of the particle that was displaced
   * @param new_pos Its new position
   */
  void record_move_particle(ParId par_id, ParPos new_pos);

  /** Record a particle being deleted
   *
   * @param id Id of the particle that was removed
   */
  void record_remove_particle(ParId par_id);

  /** Get a copy of the accumulated changes
   *
   * @return The changes recorded so far
   */
  CellECMInteractions get_changes() const;

  /** Reset records
   *
   * This clears the accumulated updates
   */
  void reset();

private:
  CellECMInteractions update_;
};
