// Tell the preprocessor to replace some real files with mocks
#define _MOCK_CA_HPP_ "mock_ca.hpp"
#define _MOCK_PARAMETER_HPP_ "mock_parameter.hpp"

// Now load the real implementations, which will now use the mocks
#include "adhesion_creation.cpp"
#include "random.cpp"
#include "vec2.cpp"

// And add the mock implementations
#include "mock_ca.cpp"
#include "mock_parameter.cpp"


// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_range_equals.hpp>

#include "mock_ca.hpp"
#include "mock_parameter.hpp"

#include <vector>


extern Parameter par;

using Catch::Matchers::UnorderedRangeEquals;


TEST_CASE("Test adhesion zone basic", "[adhesion_creation]") {
    MockCellularPotts mock_ca;

    par.sizex = 5;
    par.sizey = 5;

    mock_ca.sigma_return_values = {
            {{0, 4}, 0}, {{1, 4}, 0}, {{2, 4}, 0}, {{3, 4}, 0}, {{4, 4}, 0},
            {{0, 3}, 0}, {{1, 3}, 1}, {{2, 3}, 0}, {{3, 3}, 0}, {{4, 3}, 0},
            {{0, 2}, 1}, {{1, 2}, 1}, {{2, 2}, 1}, {{3, 2}, 0}, {{4, 2}, 0},
            {{0, 1}, 0}, {{1, 1}, 1}, {{2, 1}, 0}, {{3, 1}, 0}, {{4, 1}, 0},
            {{0, 0}, 0}, {{1, 0}, 0}, {{2, 0}, 0}, {{3, 0}, 0}, {{4, 0}, 0}
    };

    SECTION("Radius 1.0") {
        par.adhesion_zone_radius = 1.0;

        std::vector<PixelPos> expected = {
            {1, 3}, {0, 2}, {2, 2}, {1, 1}};

        auto zone = adhesion_zone(mock_ca);
        CHECK_THAT(zone, UnorderedRangeEquals(expected));
    }

    SECTION("Radius 1.5") {
        par.adhesion_zone_radius = 1.5;

        std::vector<PixelPos> expected = {
            {1, 3}, {0, 2}, {1, 2}, {2, 2}, {1, 1}};

        auto zone = adhesion_zone(mock_ca);
        CHECK_THAT(zone, UnorderedRangeEquals(expected));
    }
}

TEST_CASE("Test adhesion zone with more cells", "[adhesion_creation]") {
    MockCellularPotts mock_ca;

    par.sizex = 5;
    par.sizey = 5;

    mock_ca.sigma_return_values = {
            {{0, 4}, 0}, {{1, 4}, 0}, {{2, 4}, 0}, {{3, 4}, 0}, {{4, 4}, 0},
            {{0, 3}, 0}, {{1, 3}, 1}, {{2, 3}, 2}, {{3, 3}, 2}, {{4, 3}, 0},
            {{0, 2}, 1}, {{1, 2}, 1}, {{2, 2}, 1}, {{3, 2}, 2}, {{4, 2}, 0},
            {{0, 1}, 0}, {{1, 1}, 1}, {{2, 1}, 2}, {{3, 1}, 2}, {{4, 1}, 0},
            {{0, 0}, 0}, {{1, 0}, 0}, {{2, 0}, 0}, {{3, 0}, 0}, {{4, 0}, 0}
    };

    SECTION("Radius 1.0") {
        par.adhesion_zone_radius = 1.0;

        std::vector<PixelPos> expected = {
            {1, 3}, {2, 3}, {3, 3},
            {0, 2}, {2, 2}, {3, 2},
            {1, 1}, {2, 1}, {3, 1}};

        auto zone = adhesion_zone(mock_ca);
        CHECK_THAT(zone, UnorderedRangeEquals(expected));
    }

    SECTION("Radius 1.5") {
        par.adhesion_zone_radius = 1.5;

        std::vector<PixelPos> expected = {
            {1, 3}, {2, 3}, {3, 3},
            {0, 2}, {1, 2}, {2, 2}, {3, 2},
            {1, 1}, {2, 1}, {3, 1}};

        auto zone = adhesion_zone(mock_ca);
        CHECK_THAT(zone, UnorderedRangeEquals(expected));
    }

}

TEST_CASE("Test adhesion zone at edge", "[adhesion_creation]") {
    MockCellularPotts mock_ca;

    par.sizex = 5;
    par.sizey = 5;

    mock_ca.sigma_return_values = {
            {{0, 4}, 1}, {{1, 4}, 1}, {{2, 4}, 1}, {{3, 4}, 0}, {{4, 4}, 0},
            {{0, 3}, 1}, {{1, 3}, 1}, {{2, 3}, 1}, {{3, 3}, 0}, {{4, 3}, 0},
            {{0, 2}, 1}, {{1, 2}, 1}, {{2, 2}, 1}, {{3, 2}, 2}, {{4, 2}, 2},
            {{0, 1}, 0}, {{1, 1}, 1}, {{2, 1}, 2}, {{3, 1}, 2}, {{4, 1}, 2},
            {{0, 0}, 0}, {{1, 0}, 0}, {{2, 0}, 2}, {{3, 0}, 2}, {{4, 0}, 2}
    };

    SECTION("Radius 1.0") {
        par.adhesion_zone_radius = 1.0;

        std::vector<PixelPos> expected = {
            {2, 4}, {2, 3},
            {0, 2}, {2, 2}, {3, 2}, {4, 2},
            {1, 1}, {2, 1}, {2, 0}};

        auto zone = adhesion_zone(mock_ca);
        CHECK_THAT(zone, UnorderedRangeEquals(expected));
    }

    SECTION("Radius 2.0") {
        par.adhesion_zone_radius = 2.0;

        std::vector<PixelPos> expected = {
            {1, 4}, {2, 4},
            {0, 3}, {1, 3}, {2, 3},
            {0, 2}, {1, 2}, {2, 2}, {3, 2}, {4, 2},
            {1, 1}, {2, 1}, {3, 1}, {4, 1},
            {2, 0}, {3, 0}};

        auto zone = adhesion_zone(mock_ca);
        CHECK_THAT(zone, UnorderedRangeEquals(expected));
    }
}

