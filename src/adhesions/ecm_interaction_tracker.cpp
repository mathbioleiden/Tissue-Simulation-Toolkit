#include "ecm_interaction_tracker.hpp"

void ECMInteractionTracker::record_new_particle(ParPos pos,
                                                double bond_attempt_radius) {
  update_.add_adhesion_particles.new_pos.push_back(pos);
  update_.add_adhesion_particles.bond_attempt_radius.push_back(
      bond_attempt_radius);
}

void ECMInteractionTracker::record_move_particle(ParId par_id, ParPos new_pos) {
  update_.move_adhesion_particles.par_id.push_back(par_id);
  update_.move_adhesion_particles.new_pos.push_back(new_pos);
}

void ECMInteractionTracker::record_remove_particle(ParId par_id) {
  update_.remove_adhesion_particles.par_id.push_back(par_id);
}

CellECMInteractions ECMInteractionTracker::get_changes() const {
  return update_;
}

void ECMInteractionTracker::reset() { update_.clear(); }
