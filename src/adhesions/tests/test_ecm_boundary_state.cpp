#include <catch2/catch_test_macros.hpp>

#include "ecm_boundary_state.cpp"

/** There's not much to test here, since this file just defines some data
 * structures. But we can play with them a bit and see if things compile at
 * least.
 */


TEST_CASE( "ECM boundary can be created and populated", "[ecm]" ) {
    ECMBoundaryState ecm_boundary;

    ecm_boundary.particles = {
        {0, Particle(0, ParPos(1.0, 1.0), ParticleType::boundary)},
        {1, Particle(1, ParPos(2.0, 2.0), ParticleType::free)},
        {2, Particle(2, ParPos(3.0, 3.0), ParticleType::adhesion)}
    };

    ecm_boundary.bond_types[0].r0 = 1.0;
    ecm_boundary.bond_types[0].k = 1.0;

    ecm_boundary.bonds = {
        {0, {0, 1, 0}},
        {1, {1, 2, 0}},
        {2, {3, 4, 1}}
    };

    ecm_boundary.angle_cst_types[0].t0 = 0.1;
    ecm_boundary.angle_cst_types[0].k = 2.0;

    ecm_boundary.angle_csts = {
        {0, {0, 1, 2, 0}}
    };

    REQUIRE(ecm_boundary.particles[1].type == ParticleType::free);
    REQUIRE(ecm_boundary.particles[ecm_boundary.bonds[0].p1].pos.x == 1.0);
    REQUIRE(ecm_boundary.angle_cst_types[ecm_boundary.angle_csts[0].type].k == 2.0);
}

