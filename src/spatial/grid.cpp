
#include "grid.hpp"
#include "parameter.hpp"

extern Parameter par;

Grid::Grid() {
  auto boundary_type = BoundaryType::periodic;
  if (!par.periodic_boundaries)
    boundary_type = BoundaryType::wall;

  spinfield_.initialise(par.sizex, par.sizey, 1, boundary_type);
}

void Grid::resize(int sizex, int sizey) {
  auto boundary_type = BoundaryType::periodic;
  if (!par.periodic_boundaries)
    boundary_type = BoundaryType::wall;
  spinfield_.initialise(sizex, sizey, 1, boundary_type);
}

Spin Grid::get(PixelPos coordinate) { return spinfield_.get(coordinate); }

void Grid::set(PixelPos coordinate, Spin value) {
  spinfield_.set(coordinate, value);
}

Neighbours Grid::neighbours(PixelPos coordinate) {
  return Neighbours(coordinate);
}
