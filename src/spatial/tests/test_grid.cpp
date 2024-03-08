
#define _MOCK_PARAMETER_HPP_ "mock_parameter_spatial.hpp"

// Load the code to be tested
#include "mock_parameter_spatial.cpp"

#include "array2d.cpp"
#include "grid.cpp"
#include "neighbours.cpp"

// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>

extern Parameter par;

TEST_CASE("Creating grid", "[grid]")
{
    SECTION("")
    {
        par.sizex = 10;
        par.sizey = 10;
        auto grid = Grid();
        REQUIRE(grid.get({3, 4}) == 0);
    }
}

TEST_CASE("Neighbours", "[grid]")
{
    SECTION("")
    {
        par.sizex = 10;
        par.sizey = 10;
        auto grid = Grid();

        std::vector<PixelDisplacement> v = {{-1, -1}, {0, -1}, {1, -1},
                                            {-1, 0},  {0, 0},  {1, 0},
                                            {-1, 1},  {0, 1},  {1, 1}};
        for (auto x : v)
        {
            grid.set(PixelPos(5, 5) + x, 123);
        }
        auto neighs = grid.neighbours({5, 5});

        for (auto neigh : neighs)
        {
            REQUIRE(grid.get(neigh) == 123);
        }
    }
}
