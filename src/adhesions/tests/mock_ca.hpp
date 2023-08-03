#pragma once

#include <tuple>
#include <unordered_map>

#include "vec2.hpp"


class MockCellularPotts {
    public:
        int Sigma(int x, int y) const;

        std::unordered_map<PixelPos, int> sigma_return_values;
};


using CellularPotts = MockCellularPotts;

