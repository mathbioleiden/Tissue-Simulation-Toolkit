
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

Spin Grid::get(PixelPos coordinate) const { return spinfield_.get(coordinate); }

void Grid::set(PixelPos coordinate, Spin value) {
  spinfield_.set(coordinate, value);
}

Neighbours Grid::neighbours(PixelPos coordinate) {
  return Neighbours(coordinate);
}



bool LocalConnectedness(const Grid &grid, PixelPos pos, int spin)
{
    // Algorithm from Durand, M., & Guesnet, E. (2016). An efficient Cellular
    // Potts Model algorithm that forbids cell fragmentation. Computer Physics
    // Communications, 208, 54-63. Checks if cell sigma is locally connected at
    // lattice point (x,y) if using LocalConnectedness(x,y,sigma[x][y]) and
    // LocalConnectedness(x,y,sigma[xp][yp] both are true

    // Use local nx and ny in a cyclic order (starts at upper left corner)
    const int cyc_nx[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
    const int cyc_ny[8] = {0, -1, -1, -1, 0, 1, 1, 1};
    const PixelPos cyc[8] = {
      { -1,  0}, { -1, -1}, {  0, -1}, {  1, -1}, {  1,  0}, {  1,  1},
      {  0,  1}, { -1,  1}
    };     
    bool connected_component = false;
    // Currently in a connected component
    int nr_connected_components = 0;
    // Total number of conncected components around x,y
    for (int i = 0; i <= 7; i++)
    {
        int s_nb = grid.get(pos + cyc[i]);
        if (s_nb == spin && !connected_component)
        {
            // start of a connected component
            connected_component = true;
            nr_connected_components++;
        }
        else if (s_nb != spin && connected_component)
        {
            // end of a conencted component
            connected_component = false;
        }
    }
    bool looped = false;
    if (grid.get(pos + cyc[0]) == spin &&
        grid.get(pos + cyc[7]) == spin)
        looped = true;
    // Check if the first and last element are connected
    if ((nr_connected_components >= 2 && !looped) ||
        nr_connected_components >= 3 && looped)
        // permit one more component when the first and last element are
        // connected
        return false;
    else
        return true;
}