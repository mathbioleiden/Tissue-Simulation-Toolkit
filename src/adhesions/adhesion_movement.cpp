#include "adhesion_movement.hpp"
#include "neighbours.hpp"
#include "parameter.hpp"
#include "random.hpp"

#include <algorithm>
#include <iostream>
#include <string>

extern Parameter par;

using namespace std::string_literals;

int annihilation_penalty(int num_destroyed) {
  return num_destroyed * par.adhesion_annihilation_penalty;
}

int overflow_penalty(int num_present) {
  if (num_present > par.adhesions_per_pixel_overflow)
    return num_present * par.adhesions_per_pixel_overflow_penalty;

  return 0;
}

std::vector<PixelDisplacement> retraction_displacements(CellularPotts const &ca,
                                                        PixelPos source_pixel,
                                                        PixelPos target_pixel) {
  std::vector<PixelDisplacement> displacements;

  int target_cell_id = ca.Sigma(target_pixel.x, target_pixel.y);
  for (PixelPos nb : Neighbours(target_pixel))
    if (ca.Sigma(nb.x, nb.y) == target_cell_id)
      displacements.push_back(nb - target_pixel);

  int source_cell_id = ca.Sigma(source_pixel.x, source_pixel.y);
  if (source_cell_id == target_cell_id)
    displacements.emplace_back(0, 0);

  return displacements;
}

std::vector<PixelDisplacement>
extension_displacements_all(CellularPotts const &ca, PixelPos source_pixel,
                            PixelPos target_pixel) {
  std::vector<PixelDisplacement> displacements = {{0, 0}};

  int source_cell = ca.Sigma(source_pixel.x, source_pixel.y);
  for (PixelPos nb : Neighbours(source_pixel)) {
    if ((ca.Sigma(nb.x, nb.y) == source_cell) || (nb == target_pixel))
      displacements.push_back(nb - source_pixel);
  }

  return displacements;
}

/* Lazy, sticky and mixed are inlined here, because they're really short. That
 * does put this function at the edge of how complex a function should be, so if
 * you add anything more, you should split some part off into a new function.
 */
std::vector<PixelDisplacement> extension_displacements(CellularPotts const &ca,
                                                       PixelPos source_pixel,
                                                       PixelPos target_pixel) {
  std::vector<PixelDisplacement> displacements;

  std::string mechanism(par.adhesion_extension_mechanism);

  if (mechanism == "random")
    // We return all possible displacements here, select_displacement()
    // below will later pick one at random (if it's set to "uniform"),
    // thus justifying the name of the mechanism.
    return extension_displacements_all(ca, source_pixel, target_pixel);
  else {
    if (mechanism == "lazy" || mechanism == "mixed")
      displacements.emplace_back(0, 0);

    if (mechanism == "sticky" || mechanism == "mixed")
      displacements.emplace_back(target_pixel - source_pixel);
  }

  return displacements;
}

std::tuple<PixelDisplacement, double> select_displacement_uniform(
    std::vector<AdhesionWithEnvironment> const &adhesions,
    std::vector<PixelDisplacement> const &possibilities) {
  // RandomNumber has range [1..max] inclusive
  long int item = RandomNumber(possibilities.size()) - 1;
  PixelDisplacement chosen = possibilities[item];

  double dh = 0.0;
  for (auto const &adhesion : adhesions)
    dh += adhesion.move_dh(chosen);
  return std::make_tuple(chosen, dh);
}

std::tuple<PixelDisplacement, double> select_displacement_gradient(
    std::vector<AdhesionWithEnvironment> const &adhesions,
    std::vector<PixelDisplacement> const &possibilities) {
  // calculate DH for each possibility
  std::vector<double> displacement_dh;
  for (PixelDisplacement displacement : possibilities) {
    double total_dh = 0.0;
    for (auto const &awe : adhesions)
      total_dh += awe.move_dh(displacement);
    displacement_dh.emplace_back(total_dh);
  }

  // find minimum DH
  double min_dh =
      *std::min_element(displacement_dh.cbegin(), displacement_dh.cend());

  // find possibilities with the minimum DH
  std::vector<std::size_t> chosen;
  for (std::size_t i = 0u; i < displacement_dh.size(); ++i)
    if (displacement_dh[i] == min_dh)
      chosen.push_back(i);

  // pick one of those at random
  long int item = RandomNumber(chosen.size()) - 1;
  return std::make_tuple(possibilities[chosen[item]],
                         displacement_dh[chosen[item]]);
}

std::tuple<PixelDisplacement, double>
select_displacement(AdhesionIndex const &index, PixelPos target_pixel,
                    std::vector<PixelDisplacement> const &possibilities) {
  auto target_adhesions = index.get_adhesions(target_pixel);

  if (par.adhesion_displacement_selection == "uniform"s)
    return select_displacement_uniform(target_adhesions, possibilities);

  if (par.adhesion_displacement_selection == "gradient"s)
    return select_displacement_gradient(target_adhesions, possibilities);

  throw std::runtime_error(
      "Parameter displacement_selection must be either \"uniform\" or"
      " \"gradient\"");
}
