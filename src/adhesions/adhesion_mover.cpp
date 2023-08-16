#include "adhesion_mover.hpp"
#include "adhesion_movement.hpp"


AdhesionDisplacements::AdhesionDisplacements(
        PixelDisplacement source, PixelDisplacement target)
    : source(source)
    , target(target)
{}


const PixelDisplacement AdhesionDisplacements::annihilated(
        std::numeric_limits<int>::min(), std::numeric_limits<int>::min());


AdhesionMover::AdhesionMover(CellularPotts const & ca)
    : ca_(ca)
{}


std::tuple<double, AdhesionDisplacements> AdhesionMover::move_dh(
        PixelPos source_pixel, PixelPos target_pixel) const {

    PixelDisplacement source_displacement(0, 0), target_displacement(0, 0);
    double source_dh(0.0), target_dh(0.0);

    auto num_source_adhesions = index_.get_adhesions(source_pixel).size();
    if (num_source_adhesions > 0) {
        auto possible_displacements = extension_displacements(
                ca_, source_pixel, target_pixel);
        std::tie(source_displacement, source_dh) = select_displacement(
                index_, source_pixel, possible_displacements);
    }

    auto num_target_adhesions = index_.get_adhesions(target_pixel).size();
    if (num_target_adhesions > 0) {
        auto possible_displacements = retraction_displacements(
                ca_, source_pixel, target_pixel);
        if (possible_displacements.empty()) {
            target_displacement = AdhesionDisplacements::annihilated;
            target_dh = annihilation_penalty(num_target_adhesions);
        }
        else {
            std::tie(target_displacement, target_dh) = select_displacement(
                    index_, target_pixel, possible_displacements);
        }
    }

    return std::make_tuple(
            source_dh + target_dh,
            AdhesionDisplacements(source_displacement, target_displacement));
}


void AdhesionMover::commit_move(
        PixelPos source_pixel, PixelPos target_pixel,
        AdhesionDisplacements const & displacements
) {
    // Source pixel
    auto const & source_adhesions = index_.get_adhesions(source_pixel);
    if (displacements.source != PixelDisplacement(0, 0))
        index_.move_adhesions(source_pixel, source_pixel + displacements.source);

    // Target pixel
    if (displacements.target != PixelDisplacement(0, 0)) {
        auto const & target_adhesions = index_.get_adhesions(target_pixel);
        if (displacements.target != AdhesionDisplacements::annihilated) {
            index_.move_adhesions(
                    target_pixel, target_pixel + displacements.target);
        }
        else
            index_.remove_adhesions(target_pixel);
    }
}

void AdhesionMover::update(ECMBoundaryState const & ecm_boundary) {
    index_.rebuild(ecm_boundary);
}

