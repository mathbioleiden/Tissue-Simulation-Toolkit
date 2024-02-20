#include "mock_ca.hpp"

#include <stdexcept>
#include <string>


int MockCellularPotts::Sigma(int x, int y) const {
    if (sigma_return_values.count({x, y}) == 0)
        throw std::runtime_error(
                "Sigma read at " + std::to_string(x) + ", " +
                std::to_string(y) + " for which we have no value");

    return sigma_return_values.at({x, y});
}

