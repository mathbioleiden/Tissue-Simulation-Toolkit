// Load the code to be tested and its dependencies
#include "adhesion_index.cpp"
#include "ecm_boundary_state.cpp"
#include "ecm_interaction_tracker.cpp"
#include "cell_ecm_interactions.cpp"
#include "vec2.cpp"


// Dependencies for the test itself
#include <random>

#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>
#include <catch2/matchers/catch_matchers_range_equals.hpp>

using Catch::Matchers::IsNaN;
using Catch::Matchers::UnorderedRangeEquals;
using Catch::Matchers::WithinRel;
using Catch::Matchers::WithinULP;


constexpr double degrees = 3.14159265358979323846 / 180.0;


// Helper function that accesses private member variable
std::unordered_map<
    PixelPos, std::vector<AdhesionWithEnvironment>
    > const &
adhesions_by_pixel(AdhesionIndex const & index) {
    return index.adhesions_by_pixel_;
}


// Helper comparison operators

bool operator==(BondType const & lhs, BondType const & rhs) {
    return (lhs.r0 == rhs.r0) && (lhs.k == rhs.k);
}

bool operator==(AttachedBond const & lhs, AttachedBond const & rhs) {
    return (lhs.neighbour == rhs.neighbour) && (lhs.bond_type == rhs.bond_type);
}


TEST_CASE("Create an AttachedBond", "[adhesion_index]") {
    AttachedBond b({2.0, 1.0}, BondType{0.5, 0.1});

    REQUIRE(b.neighbour.x == 2.0);
    REQUIRE(b.neighbour.y == 1.0);
    REQUIRE(b.bond_type.r0 == 0.5);
    REQUIRE(b.bond_type.k == 0.1);
}


TEST_CASE("Calculate Delta-H for an AttachedBond", "[adhesion_index]") {
    AttachedBond b({2.0, 1.0}, BondType{0.5, 0.1});

    // if the length does not change, no work is done
    REQUIRE_THAT(
            b.move_dh({0.0, 0.0}, {0.0, 2.0}),
            WithinULP(0.0, 4));

    // 0.5 * 0.1 * (1 - 0.5)^2 = 0.0125
    // 0.5 * 0.1 * (2 - 0.5)^2 = 0.1125
    REQUIRE_THAT(
            b.move_dh({1.0, 1.0}, {0.0, 1.0}),
            WithinULP(0.1, 4));

    // bond is linear in stiffness k
    b.bond_type.k = 0.2;
    REQUIRE_THAT(
            b.move_dh({1.0, 1.0}, {0.0, 1.0}),
            WithinULP(0.2, 4));

    // validation test with random numbers
    b.bond_type.k = 1.23;
    b.bond_type.r0 = 4.56;
    b.neighbour.x = 7.8;
    b.neighbour.y = 90.1;

    REQUIRE_THAT(
            b.move_dh({12.3, 45.6}, {7.89, 0.123}),
            WithinULP(3494.8529704043532, 4));
}


TEST_CASE("Create an AttachedAngleCst", "[adhesion_index]") {
    AttachedAngleCst c(
            {1.0, 1.0}, {2.0, 2.0}, AngleCstType{10.0 * degrees, 1.5});

    REQUIRE(c.middle.x == 1.0);
    REQUIRE(c.middle.y == 1.0);
    REQUIRE(c.far.x == 2.0);
    REQUIRE(c.far.y == 2.0);

    REQUIRE(c.angle_cst_type.t0 * 18.0 == 3.14159265358979323846);
    REQUIRE(c.angle_cst_type.k == 1.5);
}


TEST_CASE("Calculate Delta-H for an AttachedAngleCst", "[adhesion_index]") {
    AttachedAngleCst c(
            {1.0, 1.0}, {2.0, 2.0}, AngleCstType{165.0 * degrees, 1.5});

    // Precision is lousy around 180 degrees, which is unfortunate because
    // that's where our fibers are, but we'll end up rounding the result to an
    // int anyway, so it'll work.
    REQUIRE_THAT(
            c.move_dh({0.0, 0.0}, {1.0, -1.0}),
            WithinRel(0.154212568767021228, 1e-7));

    // constraint is linear in stiffness k
    c.angle_cst_type.k = 4.5;
    REQUIRE_THAT(
            c.move_dh({0.0, 0.0}, {1.0, -1.0}),
            WithinRel(0.462637706301063685, 1e-7));

    // Check that precision is better at right angles
    REQUIRE_THAT(
            c.move_dh({2.0, 0.0}, {2.0, 0.125}),
            WithinRel(0.40208932274113485, 1e-17));
}


TEST_CASE("Regression-test acos domain error", "[adhesion_index]") {
    // Just checking that this doesn't crash because of a domain error
    // For a 180 degree angle at -45 degrees, the calculation of the
    // cosine rounds off to an absolute value of just a tiny bit above 1,
    // which then causes the acos() to return NaN. So there's a clamp now,
    // and this test makes sure it works.
    AttachedAngleCst c(
            {144.836836830561367, 186.707216898972149},
            {145.055796016773854, 186.488257712759662},
            AngleCstType{180.0 * degrees, 1.5});

    auto dh = c.move_dh(
            {144.61787764434888, 186.926176085184636},
            {144.61787764434788, 186.926176084184636});

    REQUIRE_THAT(dh, !IsNaN());

    // Now repeat with some random values just in case different round-off
    // modes throw a spanner in the works and the above passes.
    std::default_random_engine generator;
    std::uniform_real_distribution<double> cdist(128.0, 256.0);
    std::uniform_real_distribution<double> ddist(0.0, 1.0);

    for (int i = 0; i < 10; ++i) {
        double cx = cdist(generator);
        double cy = cdist(generator);
        double d = ddist(generator);

        AttachedAngleCst c(
                {cx, cy}, {cx + d, cy - d}, AngleCstType{180.0 * degrees, 1.5});

        auto dh = c.move_dh({cx - d, cy + d}, {cx - d - 1e-14, cy - d + 1e-14});
        REQUIRE_THAT(dh, !IsNaN());
    }
}


TEST_CASE("Create an AdhesionWithEnvironment", "[adhesion_index]") {
    AdhesionWithEnvironment a(12, {1.3, 1.4});

    REQUIRE(a.par_id == 12);
    REQUIRE(a.position.x == 1.3);
    REQUIRE(a.position.y == 1.4);
}


TEST_CASE("Calculate Delta-H for an AdhesionWithEnvironment", "[adhesion_index]") {
    AdhesionWithEnvironment a(0, {2.0, 2.0});
    BondType bt1(1.0, 2.0);

    a.bonds.emplace_back(ParPos(3.0, 2.0), bt1);

    REQUIRE_THAT(
            a.move_dh({0, -1}),
            WithinRel(0.1715728752538097, 1e-14));

    a.bonds.emplace_back(ParPos(1.0, 2.0), bt1);

    REQUIRE_THAT(
            a.move_dh({0, -1}),
            WithinRel(0.3431457505076194, 1e-14));

    a.angle_csts.emplace_back(
            ParPos(3.0, 2.0), ParPos(4.0, 2.0), AngleCstType(170.0 * degrees, 0.5));
    REQUIRE_THAT(
            a.move_dh({0, -1}),
            WithinRel(0.42881939982263173, 1e-14));

    a.angle_csts.emplace_back(
            ParPos(1.0, 2.0), ParPos(0.1, 2.1), AngleCstType(180.0 * degrees, 0.3));
    REQUIRE_THAT(
            a.move_dh({0, -1}),
            WithinRel(0.4952739475998516, 1e-14));
}


TEST_CASE("Build Adhesionindex", "[adhesion_index]") {
    ECMBoundaryState ecm_boundary;
    AdhesionIndex index;
    auto const & abp = adhesions_by_pixel(index);

    // Check build without adhesions
    ecm_boundary.particles[0] = Particle(0, ParPos{1.2, 1.3}, ParticleType::free);
    index.rebuild(ecm_boundary);
    CHECK(adhesions_by_pixel(index).empty());

    // Check a single adhesion without bonds
    ecm_boundary.particles[1] = Particle(1, ParPos{2.3, 4.5}, ParticleType::adhesion);
    index.rebuild(ecm_boundary);

    REQUIRE(abp.size() == 1u);
    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 1u);
    auto awe = abp.at({2, 4})[0];
    CHECK(awe.par_id == 1);
    CHECK(awe.position == ParPos{2.3, 4.5});
    CHECK(awe.bonds.empty());
    CHECK(awe.angle_csts.empty());

    // Add a bond
    ecm_boundary.bond_types[0] = BondType(1.5, 5.0);
    ecm_boundary.bonds[0] = Bond(0, 1, 0);
    index.rebuild(ecm_boundary);
    REQUIRE(abp.size() == 1u);
    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 1u);

    awe = abp.at({2, 4})[0];
    CHECK(awe.par_id == 1);
    CHECK(awe.position == ParPos{2.3, 4.5});

    REQUIRE(awe.bonds.size() == 1);
    CHECK(awe.bonds.at(0).neighbour == ParPos{1.2, 1.3});
    CHECK(awe.bonds.at(0).bond_type.r0 == 1.5);
    CHECK(awe.bonds.at(0).bond_type.k == 5.0);

    // Check that bonds with other adhesion particles are ignored
    ecm_boundary.particles[0].type = ParticleType::adhesion;
    index.rebuild(ecm_boundary);

    REQUIRE(abp.size() == 2u);

    REQUIRE(abp.count({1, 1}) == 1u);
    REQUIRE(abp.at({1, 1}).size() == 1u);
    awe = abp.at({1, 1})[0];
    CHECK(awe.par_id == 0);
    CHECK(awe.position == ParPos{1.2, 1.3});
    CHECK(awe.bonds.empty());
    CHECK(awe.angle_csts.empty());

    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 1u);
    awe = abp.at({2, 4})[0];
    CHECK(awe.par_id == 1);
    CHECK(awe.position == ParPos{2.3, 4.5});
    CHECK(awe.bonds.empty());
    CHECK(awe.angle_csts.empty());

    // Check that bonds with excluded particles are ignored
    ecm_boundary.particles[0].type = ParticleType::excluded;
    index.rebuild(ecm_boundary);
    REQUIRE(abp.size() == 1u);

    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 1u);
    awe = abp.at({2, 4})[0];
    CHECK(awe.par_id == 1);
    CHECK(awe.position == ParPos{2.3, 4.5});
    CHECK(awe.bonds.empty());
    CHECK(awe.angle_csts.empty());

    // Restore first and add a second bond
    ecm_boundary.particles[0].type = ParticleType::free;
    ecm_boundary.particles[2] = Particle(2, ParPos{3.3, 1.5}, ParticleType::free);
    ecm_boundary.bond_types[1] = BondType(1.7, 3.0);
    ecm_boundary.bonds[1] = Bond(2, 1, 1);

    index.rebuild(ecm_boundary);

    REQUIRE(abp.size() == 1u);

    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 1u);
    awe = abp.at({2, 4})[0];
    CHECK(awe.par_id == 1);
    CHECK(awe.position == ParPos{2.3, 4.5});

    REQUIRE(awe.bonds.size() == 2);
    AttachedBond ref_abond_01({1.2, 1.3}, BondType(1.5, 5.0));
    AttachedBond ref_abond_21({3.3, 1.5}, BondType(1.7, 3.0));

    CHECK((
            (awe.bonds.at(0) == ref_abond_01 && awe.bonds.at(1) == ref_abond_21) ||
            (awe.bonds.at(1) == ref_abond_01 && awe.bonds.at(0) == ref_abond_21)));

    CHECK(awe.angle_csts.empty());

    // Add an angle constraint
    ecm_boundary.particles[3] = Particle(3, ParPos{4.1, 0.3}, ParticleType::free);
    ecm_boundary.angle_cst_types[0] = AngleCstType(3.141593, 6.7);
    ecm_boundary.angle_csts[0] = AngleCst(1, 2, 3, 0);

    index.rebuild(ecm_boundary);

    REQUIRE(abp.size() == 1u);
    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 1u);

    awe = abp.at({2, 4})[0];
    REQUIRE(awe.angle_csts.size() == 1);
    auto const & cst = awe.angle_csts.at(0);
    CHECK(cst.middle == ParPos{3.3, 1.5});
    CHECK(cst.far == ParPos{4.1, 0.3});
    CHECK(cst.angle_cst_type.t0 == 3.141593);
    CHECK(cst.angle_cst_type.k == 6.7);

    // Check multiple adhesions in the same pixel
    ecm_boundary.particles[4] = Particle(4, ParPos{2.7, 4.1}, ParticleType::adhesion);
    index.rebuild(ecm_boundary);

    REQUIRE(abp.size() == 1u);
    REQUIRE(abp.count({2, 4}) == 1u);
    REQUIRE(abp.at({2, 4}).size() == 2u);

    // We don't know the order, so this check is a bit tricky
    // If we had a lot of these, we could define some more operator==s and use
    // Catch2's UnorderedRangeEquals.
    int count = 0;
    for (auto const & id_awe : abp.at({2, 4})) {
        if (awe.par_id == 1) {
            CHECK(awe.position == ParPos{2.3, 4.5});
            ++count;
        }
        else if (awe.par_id == 4) {
            CHECK(awe.position == ParPos{2.7, 4.1});
            CHECK(awe.bonds.empty());
            CHECK(awe.angle_csts.empty());
            ++count;
        }
        else {
            // found an unexpected AdhesionWithEnvironment
            REQUIRE(false);
        }
    }
    CHECK(count == 2);
}


TEST_CASE("Get adhesions for a given pixel", "[adhesion_index]") {
    AdhesionIndex index;

    CHECK(index.get_adhesions({123, 76}).empty());

    ECMBoundaryState ecm_boundary;
    ecm_boundary.particles[0] = Particle(0, ParPos{2.3, 4.8}, ParticleType::adhesion);
    AdhesionIndex index2;
    index2.rebuild(ecm_boundary);

    REQUIRE(index2.get_adhesions({2, 4}).size() == 1u);
    CHECK(index2.get_adhesions({2, 4})[0].par_id == 0);
    CHECK(index2.get_adhesions({2, 4})[0].position == ParPos{2.3, 4.8});

    CHECK(index2.get_adhesions({2, 5}).size() == 0u);
}


TEST_CASE("Move adhesions from one pixel to another", "[adhesion_index]") {
    AdhesionIndex index;

    ECMBoundaryState ecm_boundary;
    ecm_boundary.particles[0] = Particle(0, ParPos{2.3, 4.8}, ParticleType::adhesion);
    ecm_boundary.particles[1] = Particle(1, ParPos{2.2, 4.3}, ParticleType::adhesion);
    ecm_boundary.particles[2] = Particle(2, ParPos{3.3, 4.0}, ParticleType::adhesion);
    ecm_boundary.particles[3] = Particle(3, ParPos{3.8, 4.2}, ParticleType::adhesion);
    index.rebuild(ecm_boundary);

    index.move_adhesions({2, 4}, {3, 4});

    CHECK(index.get_adhesions({2, 4}).empty());
    CHECK(index.get_adhesions({3, 4}).size() == 4u);
    for (auto const & adh: index.get_adhesions({3, 4})) {
        CHECK(adh.position.x >= 3.0);
        CHECK(adh.position.x < 4.0);
        CHECK(adh.position.y >= 4.0);
        CHECK(adh.position.y < 5.0);
    }

    CellECMInteractions actions = index.get_cell_ecm_interactions();
    CHECK(actions.change_type_in_area.num_particles == 0);
    CHECK(actions.add_adhesion_particles.new_pos.empty());
    CHECK(actions.move_adhesion_particles.par_id.size() == 2u);
    std::vector<ParId> ids(2u);
    if (actions.move_adhesion_particles.par_id[0] == 0)
        ids = {0, 1};
    else
        ids = {1, 0};

    CHECK(actions.move_adhesion_particles.par_id == ids);
    CHECK(actions.move_adhesion_particles.new_pos[ids[0]] == ParPos{3.3, 4.8});
    CHECK(actions.move_adhesion_particles.new_pos[ids[1]] == ParPos{3.2, 4.3});

    CHECK(actions.remove_adhesion_particles.par_id.empty());

    index.move_adhesions({4, 4}, {3, 4});
    CHECK(index.get_adhesions({4, 4}).empty());
    CHECK(index.get_adhesions({3, 4}).size() == 4u);
    for (auto const & adh: index.get_adhesions({3, 4})) {
        CHECK(adh.position.x >= 3.0);
        CHECK(adh.position.x < 4.0);
        CHECK(adh.position.y >= 4.0);
        CHECK(adh.position.y < 5.0);
    }

    actions = index.get_cell_ecm_interactions();
    CHECK(actions.change_type_in_area.num_particles == 0);
    CHECK(actions.add_adhesion_particles.new_pos.empty());
    CHECK(actions.move_adhesion_particles.par_id.size() == 2u);

    if (actions.move_adhesion_particles.par_id[0] == 0)
        ids = {0, 1};
    else
        ids = {1, 0};

    CHECK(actions.move_adhesion_particles.par_id == ids);
    CHECK(actions.move_adhesion_particles.new_pos[ids[0]] == ParPos{3.3, 4.8});
    CHECK(actions.move_adhesion_particles.new_pos[ids[1]] == ParPos{3.2, 4.3});

    CHECK(actions.remove_adhesion_particles.par_id.empty());
}


TEST_CASE("Remove adhesions from a pixel", "[adhesion_index]") {
    AdhesionIndex index;

    ECMBoundaryState ecm_boundary;
    ecm_boundary.particles[0] = Particle(0, ParPos{2.3, 4.8}, ParticleType::adhesion);
    ecm_boundary.particles[1] = Particle(1, ParPos{2.2, 4.3}, ParticleType::adhesion);
    ecm_boundary.particles[2] = Particle(2, ParPos{3.3, 4.0}, ParticleType::adhesion);
    index.rebuild(ecm_boundary);

    index.remove_adhesions({2, 4});

    CHECK(index.get_adhesions({2, 4}).empty());
    CHECK(index.get_adhesions({3, 4}).size() == 1u);
    for (auto const & adh: index.get_adhesions({3, 4})) {
        CHECK(adh.position.x >= 3.0);
        CHECK(adh.position.x < 4.0);
        CHECK(adh.position.y >= 4.0);
        CHECK(adh.position.y < 5.0);
    }

    CellECMInteractions actions = index.get_cell_ecm_interactions();
    CHECK(actions.change_type_in_area.num_particles == 0);
    CHECK(actions.add_adhesion_particles.new_pos.empty());
    CHECK(actions.move_adhesion_particles.par_id.empty());

    CHECK_THAT(
            actions.remove_adhesion_particles.par_id,
            UnorderedRangeEquals(std::vector<ParId>{0, 1}));

    index.reset_cell_ecm_interactions();

    index.remove_adhesions({1, 4});
    CHECK(index.get_adhesions({1, 4}).empty());
    CHECK(index.get_adhesions({3, 4}).size() == 1u);
    for (auto const & adh: index.get_adhesions({3, 4})) {
        CHECK(adh.position.x >= 3.0);
        CHECK(adh.position.x < 4.0);
        CHECK(adh.position.y >= 4.0);
        CHECK(adh.position.y < 5.0);
    }

    actions = index.get_cell_ecm_interactions();
    CHECK(actions.change_type_in_area.num_particles == 0);
    CHECK(actions.add_adhesion_particles.new_pos.empty());
    CHECK(actions.move_adhesion_particles.par_id.empty());
    CHECK(actions.remove_adhesion_particles.par_id.empty());
}

