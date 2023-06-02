#include "ecm.hpp"


Particle::Particle(ParPos pos, ParticleType type)
    : pos(pos)
    , type(type)
{}


BondType::BondType(double r0, double k)
    : r0(r0)
    , k(k)
{}


Bond::Bond(par_id p1, par_id p2, bond_type_id type)
    : p1(p1)
    , p2(p2)
    , type(type)
{}


AngleCstType::AngleCstType(double t0, double k)
    : t0(t0)
    , k(k)
{}

AngleCst::AngleCst(par_id p1, par_id p2, par_id p3, angle_cst_type_id type)
    : p1(p1)
    , p2(p2)
    , p3(p3)
    , type(type)
{}

