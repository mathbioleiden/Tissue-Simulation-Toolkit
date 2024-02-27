#pragma once

#include "ca.hpp"
#include "vec2.hpp"

#include <vector>

/** Find the adhesion zone.
 *
 * The adhesion zone is the area close to the edge of a cell where adhesions
 * are created. It consists of all the pixels that are in a cell but within
 * a given distance of its border. That distance is set by the
 * **adhesion_zone_radius** parameter.
 *
 * This was called the boundary neighbourhood (boundary_nbhd) in TST-MD-V2, but
 * we already have a boundary around the edge of the box containing boundary
 * particles that are fixed in place. To avoid confusion, it's been renamed.
 *
 * @param ca The (initialised) CPM to calculate the adhesion zone of
 * @return The list of all pixels in the adhesion zone
 */
std::vector<PixelPos> adhesion_zone(CellularPotts const &ca);
