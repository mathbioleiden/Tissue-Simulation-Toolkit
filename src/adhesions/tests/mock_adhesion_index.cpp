#include "mock_adhesion_index.hpp"


MockAdhesionWithEnvironment::MockAdhesionWithEnvironment(
        ParId par_id, ParPos const & position)
    : par_id(par_id)
    , position(position)
{}


double MockAdhesionWithEnvironment::move_dh(PixelDisplacement move) const {
    return move_dh_return_values.at(move);
}


std::vector<MockAdhesionWithEnvironment> const &
MockAdhesionIndex::get_adhesions(PixelPos pixel) const {
    return get_adhesions_return_values.at(pixel);
}


std::unordered_map<
    PixelPos,
    std::vector<MockAdhesionWithEnvironment>
>
MockAdhesionIndex::get_adhesions_return_values;


void MockAdhesionIndex::move_adhesions(PixelPos from, PixelPos to) {}

void MockAdhesionIndex::remove_adhesions(PixelPos pixel) {}

void MockAdhesionIndex::rebuild(ECMBoundaryState const & ecm) {}

