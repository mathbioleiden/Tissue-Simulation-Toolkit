#pragma once

/** \file adhesion_movement.hpp
 *  \brief Algorithms for moving adhesions.
 *
 * As the CPM evolves, cells move around and their adhesions have to be updated.
 * This can be done in different ways, which are implemented as functions in
 * this file.
 */

#include "adhesion_index.hpp"
#include "ca.hpp"

/** Calculate annihilation penalty.
 *
 * If an adhesion needs to be moved, but has nowhere to go, then it gets
 * annihilated. This takes work (energy), the amount of which is calculated
 * here.
 *
 * @param num_destroyed The number of adhesions to be destroyed in the copy.
 */
int annihilation_penalty(int num_destroyed);


/** Calculate overflow penalty.
 *
 * Stuffing too many adhesions into a single pixel takes work (energy), the
 * amount of which is calculated here based on the parameters
 * adhesions_per_pixel_overflow and adhesions_per_pixel_overflow_penalty.
 *
 * @param num_present The number of adhesions that will be present in the target
 *                    pixel post-copy.
 */
int overflow_penalty(int num_present);


/** Find all possible adhesion displacements for a to-be-overwritten pixel.
 *
 * If a copy attempt copies onto a pixel containing adhesions, then those
 * adhesions need to be moved. This returns a list of possible displacements
 * for those adhesions.
 *
 * @param ca A CPM grid to use to find suitable pixels to move to
 * @param source_pixel The pixel that will be copied from
 * @param target_pixel The pixel it will be copied to
 */
std::vector<PixelDisplacement> retraction_displacements(
        CellularPotts const & ca,
        PixelPos source_pixel, PixelPos target_pixel);


/** List all possible displacements.
 *
 * This finds all neighbours of the source pixel which post-copy will belong to
 * the same cell as the source pixel.
 *
 * @param ca A CPM grid to use to find suitable pixels to move to
 * @param source_pixel The pixel that will be copied from
 * @param target_pixel The pixel that will be copied to
 */
std::vector<PixelDisplacement> extension_displacements_all(
        CellularPotts const & ca,
        PixelPos source_pixel, PixelPos target_pixel);


/** Find all possible adhesion displacements for a newly added pixel
 *
 * If a copy attempt copies a pixel containing adhesions, then those
 * adhesions may move along, depending on settings. This returns a list of
 * possible displacements for those adhesions, according to an algorithm
 * selected in the parameters.
 *
 * @param ca A CPM grid to use to find suitable pixels to move to
 * @param source_pixel The pixel that will be copied from
 * @param target_pixel The pixel that will be copied to
 */
std::vector<PixelDisplacement> extension_displacements(
        CellularPotts const & ca,
        PixelPos source_pixel, PixelPos target_pixel);


/* Choose where displacements will go during the copy.
 *
 * This implements a scenario where all adhesions are moved to the same
 * neighbor, which is picked randomly from the possibilities given.
 *
 * Returns the chosen displacement and the DH for moving all adhesions, doesn't
 * actually update anything.
 *
 * At least one possible displacement must be given!
 *
 * @param adhesions Adhesions that must be moved
 * @param possibilities Possible displacements
 */
std::tuple<PixelDisplacement, double> select_displacement_uniform(
        std::vector<AdhesionWithEnvironment> const & adhesions,
        std::vector<PixelDisplacement> const & possibilities);


/* Choose where displacements will go during the copy.
 *
 * This implements a scenario where all adhesions are moved to the same
 * neighbor, the one for which it is energetically most favorable to do so.
 *
 * Returns the chosen displacement and the DH for moving all adhesions, doesn't
 * update anything.
 *
 * At least one possible displacement must be given!
 *
 * @param adhesions Adhesions that are to be moved
 * @param possibilities Possible directions in which they can be moved
 * @return The chosen displacement and corresponding DH
 */
std::tuple<PixelDisplacement, double> select_displacement_gradient(
        std::vector<AdhesionWithEnvironment> const & adhesions,
        std::vector<PixelDisplacement> const & possibilities);


/* Choose where displacements will go during the copy.
 *
 * This checks the settings, and then calls either of the above selection
 * algorithms. There must be at least one possibility.
 *
 * Returns the chosen displacement and the corresponding DH.
 *
 * At least one possible displacement must be given!
 *
 * @param index The adhesion index to get adhesions from
 * @param target_pixel Pixel whose adhesions are to be moved
 * @param possibilities Possible directions to move them in
 * @return The chosen displacement and corresponding DH
 */
std::tuple<PixelDisplacement, double> select_displacement(
        AdhesionIndex const & index, PixelPos target_pixel,
        std::vector<PixelDisplacement> const & possibilities);

double compute_yielding_penalty(const std::vector<AdhesionWithEnvironment> adh);
        