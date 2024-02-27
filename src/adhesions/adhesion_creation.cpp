#include "adhesion_creation.hpp"
#include "ca.hpp"
#include "parameter.hpp"
#include "sqr.hpp"
#include "vec2.hpp"

extern Parameter par;

/* Return a list of coordinates of pixels in range.
 *
 * The range is set by the **adhesion_zone_radius** parameter.
 *
 * Note that there's some overlap in functionality between this an the
 * Neighbours class in adhesion_movement.cpp. They're kept separate however
 * because that class is very performance-sensitive, and calculating the list
 * dynamically as is done here will likely be quite a bit slower. That doesn't
 * matter here, but it does there, so we have one fast and one flexible
 * implementation.
 */
std::vector<PixelDisplacement> neighbour_list() {
  std::vector<PixelDisplacement> result;
  int radius = static_cast<int>(ceil(par.adhesion_zone_radius));
  for (int dy = -radius; dy <= radius; ++dy) {
    for (int dx = -radius; dx <= radius; ++dx) {
      if (sqr(dy) + sqr(dx) <= sqr(par.adhesion_zone_radius))
        result.emplace_back(dx, dy);
    }
  }
  return result;
}

std::vector<PixelPos> adhesion_zone(CellularPotts const &ca) {
  std::vector<PixelPos> result;

  auto neighbours = neighbour_list();

  for (int y = 0; y < par.sizey; ++y) {
    for (int x = 0; x < par.sizex; ++x) {
      PixelPos pixel(x, y);

      int cur_cell = ca.Sigma(x, y);
      if (cur_cell > 0) {
        for (PixelDisplacement nb : neighbours) {
          PixelPos np = pixel + nb;
          if ((np.x >= 0) && (np.x < par.sizex) && (np.y >= 0) &&
              (np.y < par.sizey) && (ca.Sigma(np.x, np.y) != cur_cell)) {
            result.push_back(pixel);
            break;
          }
        }
      }
    }
  }

  return result;
}
