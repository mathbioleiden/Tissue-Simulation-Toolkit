// Tell the preprocessor to replace some real files with mocks
#define _MOCK_ADHESION_INDEX_HPP_ "mock_adhesion_index.hpp"
#define _MOCK_CA_HPP_ "mock_ca.hpp"
#define _MOCK_CA_FWD_HPP_ "mock_ca_fwd.hpp"
#define _MOCK_PARAMETER_HPP_ "mock_parameter.hpp"

// Now load the real implementations, which will now use the mocks
#include "adhesion_mover.cpp"
#include "adhesion_movement.cpp"
#include "cell_ecm_interactions.cpp"
#include "ecm_boundary_state.cpp"
#include "ecm_interaction_tracker.cpp"
#include "random.cpp"
#include "vec2.cpp"
#include "neighbours.cpp"

// And add the mock implementations
#include "mock_adhesion_index.cpp"
#include "mock_ca.cpp"
#include "mock_parameter.cpp"


// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_contains.hpp>

#include <iostream>
#include <tuple>

#include "mock_ca.hpp"


extern MockParameter par;

using std::make_tuple;
using Catch::Matchers::Contains;


bool operator==(AdhesionDisplacements const & lhs, AdhesionDisplacements const & rhs) {
    return (lhs.source == rhs.source) && (lhs.target == rhs.target);
}


TEST_CASE("Create an AdhesionMover", "[adhesion_mover]") {
    MockCellularPotts mock_ca;
    AdhesionMover mover(mock_ca);
    REQUIRE(true);
}


TEST_CASE("Move no adhesions", "[adhesion_mover]") {
    MockCellularPotts mock_ca;
    AdhesionMover mover(mock_ca);

    MockAdhesionIndex::get_adhesions_return_values[{0, 0}] = {};
    MockAdhesionIndex::get_adhesions_return_values[{0, 1}] = {};

    AdhesionDisplacements disps;
    double dh = mover.move_dh({0, 0}, {0, 1}, disps);

    REQUIRE(dh == 0.0);
    REQUIRE(disps.source == PixelDisplacement{0, 0});
    REQUIRE(disps.target == PixelDisplacement{0, 0});

    CellECMInteractions interactions = mover.get_cell_ecm_interactions();
    REQUIRE(interactions.move_adhesion_particles.par_id.empty());
    REQUIRE(interactions.move_adhesion_particles.new_pos.empty());
}


/* This test is a bit more integrated, and not a pure unit test. It covers
 * AdhesionMover as well as the functions in adhesion_movement.hpp.
 *
 * Note that it uses == for floating point comparison in a few places. We can do
 * that here because the numbers are all small integers and they're just being
 * added, which gives results that are exactly correct. See test_adhesion_index
 * for how to allow for roundoff errors.
 */
TEST_CASE("Move some adhesions in various ways", "[adhesion_mover]") {
    MockCellularPotts mock_ca;
    AdhesionMover mover(mock_ca);

    // Note: keep this in sync with sigma below
    MockAdhesionWithEnvironment a1(1, {4.2, 5.4});
    a1.move_dh_return_values[{-1, 1}] = -3.0;
    a1.move_dh_return_values[{-1, 0}] = 1.0;
    a1.move_dh_return_values[{-1, -1}] = 0.0;
    a1.move_dh_return_values[{0, -1}] = 2.0;
    a1.move_dh_return_values[{0, 0}] = 0.0;
    a1.move_dh_return_values[{1, 0}] = 3.0;

    MockAdhesionWithEnvironment a2(2, {4.7, 5.3});
    a2.move_dh_return_values[{-1, 1}] = -1.0;
    a2.move_dh_return_values[{-1, 0}] = -2.0;
    a2.move_dh_return_values[{-1, -1}] = -1.0;
    a2.move_dh_return_values[{0, -1}] = 3.0;
    a2.move_dh_return_values[{0, 0}] = 0.0;
    a2.move_dh_return_values[{1, 0}] = 1.0;

    MockAdhesionIndex::get_adhesions_return_values[{4, 5}] = {a1, a2};

    MockAdhesionWithEnvironment a3(3, {5.3, 5.0});
    a3.move_dh_return_values[{0, -1}] = 2.0;
    a3.move_dh_return_values[{0, 0}] = 0.0;     // TODO: remove?
    a3.move_dh_return_values[{1, 0}] = -2.0;

    MockAdhesionWithEnvironment a4(4, {5.6, 5.3});
    a4.move_dh_return_values[{0, -1}] = 3.0;
    a4.move_dh_return_values[{0, 0}] = 0.0;
    a4.move_dh_return_values[{1, 0}] = 1.0;

    MockAdhesionIndex::get_adhesions_return_values[{5, 5}] = {a3, a4};

    mock_ca.sigma_return_values = {
            {{3, 6}, 1}, {{4, 6}, 0}, {{5, 6}, 0}, {{6, 6}, 0},
            {{3, 5}, 1}, {{4, 5}, 1}, {{5, 5}, 2}, {{6, 5}, 2},
            {{3, 4}, 1}, {{4, 4}, 1}, {{5, 4}, 2}, {{6, 4}, 3}};

    SECTION("lazy extension and gradient selection") {
        par.adhesion_extension_mechanism = "lazy";
        par.adhesion_displacement_selection = "gradient";

        AdhesionDisplacements disps;
        double dh = mover.move_dh({4, 5}, {5, 5}, disps);
        CHECK(dh == -1.0);
        CHECK(disps.source == PixelDisplacement{0, 0});
        CHECK(disps.target == PixelDisplacement{1, 0});
    }

    SECTION("sticky extension and gradient selection") {
        par.adhesion_extension_mechanism = "sticky";
        par.adhesion_displacement_selection = "gradient";

        AdhesionDisplacements disps;
        double dh = mover.move_dh({4, 5}, {5, 5}, disps);
        CHECK(dh == 3.0);
        CHECK(disps.source == PixelDisplacement{1, 0});
        CHECK(disps.target == PixelDisplacement{1, 0});
    }

    SECTION("mixed extension and gradient selection") {
        par.adhesion_extension_mechanism = "mixed";
        par.adhesion_displacement_selection = "gradient";

        AdhesionDisplacements disps;
        double dh = mover.move_dh({4, 5}, {5, 5}, disps);
        CHECK(dh == -1.0);
        CHECK(disps.source == PixelDisplacement{0, 0});
        CHECK(disps.target == PixelDisplacement{1, 0});

        // make lazy more expensive, then we should get sticky
        auto & a1 = MockAdhesionIndex::get_adhesions_return_values[{4, 5}][0];
        a1.move_dh_return_values[{0, 0}] = 10.0;

        dh = mover.move_dh({4, 5}, {5, 5}, disps);
        CHECK(dh == 3.0);
        CHECK(disps.source == PixelDisplacement{1, 0});
        CHECK(disps.target == PixelDisplacement{1, 0});
    }

    SECTION("random extension and gradient selection") {
        /* "random" extension should really be called "any", as it allows
         * moving the source adhesions to any adjacent pixel in the cell.
         * One is then chosen according to the displacement selection
         * parameter, and only if that is "uniform" then it's actually random.
         */
        par.adhesion_extension_mechanism = "random";
        par.adhesion_displacement_selection = "gradient";

        AdhesionDisplacements disps;
        double dh = mover.move_dh({4, 5}, {5, 5}, disps);
        CHECK(dh == -5.0);
        CHECK(disps.source == PixelDisplacement{-1, 1});
        CHECK(disps.target == PixelDisplacement{1, 0});
    }

    SECTION("lazy extension and uniform selection") {
        par.adhesion_extension_mechanism = "lazy";
        par.adhesion_displacement_selection = "uniform";

        std::vector<std::tuple<double, AdhesionDisplacements>> expected = {
            {5.0, AdhesionDisplacements({0, 0}, {0, -1})},
            {-1.0, AdhesionDisplacements({0, 0}, {1, 0})}};

        AdhesionDisplacements disps;
        for (int i = 0; i < 20; ++i) {
            double dh = mover.move_dh({4, 5}, {5, 5}, disps);
            CHECK_THAT(expected, Contains(std::make_tuple(dh, disps)));
        }
    }

    SECTION("sticky extension and uniform selection") {
        par.adhesion_extension_mechanism = "sticky";
        par.adhesion_displacement_selection = "uniform";

        std::vector<std::tuple<double, AdhesionDisplacements>> expected = {
            {9.0, AdhesionDisplacements({1, 0}, {0, -1})},
            {3.0, AdhesionDisplacements({1, 0}, {1, 0})}};

        AdhesionDisplacements disps;
        for (int i = 0; i < 20; ++i) {
            double dh = mover.move_dh({4, 5}, {5, 5}, disps);
            CHECK_THAT(expected, Contains(make_tuple(dh, disps)));
        }
    }

    SECTION("mixed extension and uniform selection") {
        par.adhesion_extension_mechanism = "mixed";
        par.adhesion_displacement_selection = "uniform";

        std::vector<std::tuple<double, AdhesionDisplacements>> expected = {
            {5.0, AdhesionDisplacements({0, 0}, {0, -1})},
            {-1.0, AdhesionDisplacements({0, 0}, {1, 0})},
            {9.0, AdhesionDisplacements({1, 0}, {0, -1})},
            {3.0, AdhesionDisplacements({1, 0}, {1, 0})}};

        AdhesionDisplacements disps;
        for (int i = 0; i < 20; ++i) {
            double dh = mover.move_dh({4, 5}, {5, 5}, disps);
            CHECK_THAT(expected, Contains(make_tuple(dh, disps)));
        }
    }

    SECTION("random extension and uniform selection") {
        // This test is statistical, it should fail about once every 500 runs
        par.adhesion_extension_mechanism = "random";
        par.adhesion_displacement_selection = "uniform";

        std::vector<std::tuple<double, AdhesionDisplacements>> expected = {
            {1.0, AdhesionDisplacements({-1, 1}, {0, -1})},
            {-5.0, AdhesionDisplacements({-1, 1}, {1, 0})},
            {4.0, AdhesionDisplacements({-1, 0}, {0, -1})},
            {-2.0, AdhesionDisplacements({-1, 0}, {1, 0})},
            {4.0, AdhesionDisplacements({-1, -1}, {0, -1})},
            {-2.0, AdhesionDisplacements({-1, -1}, {1, 0})},
            {10.0, AdhesionDisplacements({0, -1}, {0, -1})},
            {4.0, AdhesionDisplacements({0, -1}, {1, 0})},
            {5.0, AdhesionDisplacements({0, 0}, {0, -1})},
            {-1.0, AdhesionDisplacements({0, 0}, {1, 0})},
            {9.0, AdhesionDisplacements({1, 0}, {0, -1})},
            {3.0, AdhesionDisplacements({1, 0}, {1, 0})}};

        std::vector<int> counts(expected.size(), 0);

        AdhesionDisplacements disps;
        int n = 160;
        for (int i = 0; i < n; ++i) {
            double dh = mover.move_dh({4, 5}, {5, 5}, disps);
            auto it = std::find(
                    expected.begin(), expected.end(), make_tuple(dh, disps));
            CHECK(it != expected.end());
            if (it != expected.end()) {
                std::size_t i = std::distance(expected.begin(), it);
                ++counts[i];
            }
        }

        // After 160 runs with a uniform choice, chances of any one count being
        // zero still are less than 1 in a million.
        CHECK(std::find(counts.begin(), counts.end(), 0) == counts.end());

        // Chi-Squared test with alpha = 0.002 and 11 degrees of freedom
        double test_stat = 0.0;
        double expected_count = static_cast<double>(n) / counts.size();
        for (int count : counts) {
            double sqdev = (count - expected_count) * (count - expected_count);
            test_stat += sqdev / expected_count;
        }
        // Two-sided, perfectly even numbers are probably also a bug!
        CHECK(test_stat > 1.834);
        CHECK(test_stat < 31.264);
    }
}


// TODO: commit_move() and check that the tracker is tracking


// TODO: test update()?

