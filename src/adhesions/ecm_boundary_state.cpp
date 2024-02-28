#include "ecm_boundary_state.hpp"

Particle::Particle(ParId par_id, ParPos pos, ParticleType type)
    : par_id(par_id), pos(pos), type(type) {}

BondType::BondType(double r0, double k) : r0(r0), k(k) {}

Bond::Bond(ParId p1, ParId p2, BondTypeId type) : p1(p1), p2(p2), type(type) {}

AngleCstType::AngleCstType(double t0, double k) : t0(t0), k(k) {}

AngleCst::AngleCst(ParId p1, ParId p2, ParId p3, AngleCstTypeId type)
    : p1(p1), p2(p2), p3(p3), type(type) {}
