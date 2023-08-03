#include <catch2/catch_test_macros.hpp>

#include "ecm.hpp"

/** There's not much to test here, since this file just defines some data
 * structures. But we can play with them a bit and see if things compile at
 * least.
 */


TEST_CASE( "ECM can be created and populated", "[ecm]" ) {
    ExtraCellularMatrix ecm;

    ecm.particles = {
        {{1.0, 1.0}, ParticleType::boundary},
        {{2.0, 2.0}, ParticleType::free},
        {{3.0, 3.0}, ParticleType::adhesion}
    };

    ecm.bond_types.resize(1);
    ecm.bond_types[0].r0 = 1.0;
    ecm.bond_types[0].k = 1.0;

    ecm.bonds = {
        {0, 1, 0},
        {1, 2, 0},
        {3, 4, 1}
    };

    ecm.angle_cst_types.resize(1);
    ecm.angle_cst_types[0].t0 = 0.1;
    ecm.angle_cst_types[0].k = 2.0;

    ecm.angle_csts = {
        {0, 1, 2, 0}
    };

    REQUIRE(ecm.particles[1].type == ParticleType::free);
    REQUIRE(ecm.particles[ecm.bonds[0].p1].pos.x == 1.0);
    REQUIRE(ecm.angle_cst_types[ecm.angle_csts[0].type].k == 2.0);
}


