#include "cell_ecm_interactions.hpp"

ChangeTypeInArea::ChangeTypeInArea() { clear(); }

void ChangeTypeInArea::clear() {
  change_area.clear();
  num_particles = 0;
  from_type = ParticleType::free;
  to_type = ParticleType::free;
}

void AddAdhesionParticles::clear() {
  new_pos.clear();
  bond_attempt_radius.clear();
}

void MoveAdhesionParticles::clear() {
  par_id.clear();
  new_pos.clear();
}

void RemoveAdhesionParticles::clear() { par_id.clear(); }

void CellECMInteractions::clear() {
  change_type_in_area.clear();
  add_adhesion_particles.clear();
  move_adhesion_particles.clear();
  remove_adhesion_particles.clear();
}
