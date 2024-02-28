// Tell the preprocessor to replace some real files with mocks
#define _MOCK_ADHESION_INDEX_HPP_ "mock_adhesion_index.hpp"
#define _MOCK_CA_HPP_ "mock_ca.hpp"
#define _MOCK_PARAMETER_HPP_ "mock_parameter.hpp"

// Now load the real implementations, which will now use the mocks
#include "adhesion_movement.cpp"
#include "cell_ecm_interactions.cpp"
#include "ecm_boundary_state.cpp"
#include "random.cpp"
#include "vec2.cpp"
#include "neighbours.cpp"

// And add the mock implementations
#include "mock_adhesion_index.cpp"
#include "mock_ca.cpp"
#include "mock_parameter.cpp"


// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_range_equals.hpp>

#include <algorithm>
#include <tuple>

#include "mock_ca.hpp"
#include "mock_parameter.hpp"

extern Parameter par;

using Catch::Matchers::UnorderedRangeEquals;


TEST_CASE("Test retraction_displacements", "[adhesion_movement]") {
    MockCellularPotts mock_ca;

    // check that all neighbours are considered
    mock_ca.sigma_return_values = {
            {{4, 6}, 1}, {{5, 6}, 1}, {{6, 6}, 1},
            {{4, 5}, 0}, {{5, 5}, 1}, {{6, 5}, 1},
            {{4, 4}, 1}, {{5, 4}, 1}, {{6, 4}, 1}};

    std::vector<PixelDisplacement> expected = {
            {-1, 1}, {0, 1}, {1, 1},
                             {1, 0},
            {-1,-1}, {0,-1}, {1,-1}};

    auto displacements = retraction_displacements(mock_ca, {4, 5}, {5, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    // check cell-internal copy
    mock_ca.sigma_return_values = {
            {{4, 6}, 1}, {{5, 6}, 1}, {{6, 6}, 1},
            {{4, 5}, 1}, {{5, 5}, 1}, {{6, 5}, 1},
            {{4, 4}, 1}, {{5, 4}, 1}, {{6, 4}, 1}};

    expected = {
            {-1, 1}, {0, 1}, {1, 1},
            {-1, 0}, {0, 0}, {1, 0},
            {-1,-1}, {0,-1}, {1,-1}};

    displacements = retraction_displacements(mock_ca, {4, 5}, {5, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    // check that neighbours owned by a different cell are omitted
    mock_ca.sigma_return_values = {
            {{4, 6}, 0}, {{5, 6}, 0}, {{6, 6}, 1},
            {{4, 5}, 0}, {{5, 5}, 1}, {{6, 5}, 1},
            {{4, 4}, 2}, {{5, 4}, 1}, {{6, 4}, 2}};

    expected = {
                             {1, 1},
                             {1, 0},
                     {0,-1}};

    displacements = retraction_displacements(mock_ca, {4, 5}, {5, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));
}


TEST_CASE("Test extension_displacements_all", "[adhesion_movement]") {
    MockCellularPotts mock_ca;

    // check that all neighbours are considered
    mock_ca.sigma_return_values = {
            {{4, 6}, 1}, {{5, 6}, 1}, {{6, 6}, 1},
            {{4, 5}, 1}, {{5, 5}, 1}, {{6, 5}, 0},
            {{4, 4}, 1}, {{5, 4}, 1}, {{6, 4}, 1}};

    std::vector<PixelDisplacement> expected = {
            {-1, 1}, {0, 1}, {1, 1},
            {-1, 0}, {0, 0}, {1, 0},
            {-1,-1}, {0,-1}, {1,-1}};

    auto displacements = extension_displacements_all(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    // check cell-internal copy
    mock_ca.sigma_return_values = {
            {{4, 6}, 1}, {{5, 6}, 1}, {{6, 6}, 1},
            {{4, 5}, 1}, {{5, 5}, 1}, {{6, 5}, 1},
            {{4, 4}, 1}, {{5, 4}, 1}, {{6, 4}, 1}};

    expected = {
            {-1, 1}, {0, 1}, {1, 1},
            {-1, 0}, {0, 0}, {1, 0},
            {-1,-1}, {0,-1}, {1,-1}};

    displacements = extension_displacements_all(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    // check that neighbours owned by a different cell are omitted
    mock_ca.sigma_return_values = {
            {{4, 6}, 0}, {{5, 6}, 0}, {{6, 6}, 1},
            {{4, 5}, 0}, {{5, 5}, 1}, {{6, 5}, 0},
            {{4, 4}, 2}, {{5, 4}, 1}, {{6, 4}, 2}};

    expected = {
                             {1, 1},
                     {0, 0}, {1, 0},
                     {0,-1}};

    displacements = extension_displacements_all(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));
}


TEST_CASE("Test extension_displacements", "[adhesion_movement]") {
    MockCellularPotts mock_ca;

    par.adhesion_extension_mechanism = "random";
    mock_ca.sigma_return_values = {
            {{4, 6}, 1}, {{5, 6}, 1}, {{6, 6}, 1},
            {{4, 5}, 1}, {{5, 5}, 1}, {{6, 5}, 0},
            {{4, 4}, 1}, {{5, 4}, 1}, {{6, 4}, 1}};

    std::vector<PixelDisplacement> expected = {
            {-1, 1}, {0, 1}, {1, 1},
            {-1, 0}, {0, 0}, {1, 0},
            {-1,-1}, {0,-1}, {1,-1}};

    auto displacements = extension_displacements(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    par.adhesion_extension_mechanism = "lazy";
    expected = {{0, 0}};
    displacements = extension_displacements(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    par.adhesion_extension_mechanism = "mixed";
    expected = {{0, 0}, {1, 0}};
    displacements = extension_displacements(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));

    par.adhesion_extension_mechanism = "sticky";
    expected = {{1, 0}};
    displacements = extension_displacements(mock_ca, {5, 5}, {6, 5});
    CHECK_THAT(displacements, UnorderedRangeEquals(expected));
}


TEST_CASE("Test select_displacement_gradient", "[adhesion_movement]") {
    MockAdhesionWithEnvironment a1(1, {5.2, 5.4});
    a1.move_dh_return_values[{-1, 0}] = 1.0;
    a1.move_dh_return_values[{0, 1}] = 2.0;
    a1.move_dh_return_values[{1, 0}] = -2.0;

    MockAdhesionWithEnvironment a2(2, {5.7, 5.3});
    a2.move_dh_return_values[{-1, 0}] = 2.0;
    a2.move_dh_return_values[{0, 1}] = 3.0;
    a2.move_dh_return_values[{1, 0}] = 1.0;

    std::vector<PixelDisplacement> possibilities = {{-1, 0}, {0, 1}, {1, 0}};

    auto disp_dh = select_displacement_gradient({a1, a2}, possibilities);

    CHECK(std::get<0>(disp_dh) == PixelDisplacement{1, 0});
    CHECK(std::get<1>(disp_dh) == -1.0);
}

