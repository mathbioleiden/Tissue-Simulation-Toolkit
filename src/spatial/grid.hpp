#pragma once

#include "array2d.hpp"
#include "neighbours.hpp"

typedef int Spin;
typedef std::pair<PixelPos, PixelPos> CopyAttempt;

/**
 * @brief Takes care of the CPM grid and all neighbour related things.
 */
class Grid {

public:
  Grid();
  Spin get(PixelPos) const;
  void set(PixelPos, Spin value);
  void resize(int, int);

  // TEMPORY ONLY HAS MOORE NEIGHBOURHOOD
  Neighbours neighbours(PixelPos);

private:
  Array2d<int> spinfield_;
};

/**
 * \brief Check if the cell is locally connected at (x,y)
 * 
 * From Durand, M., & Guesnet, E. (2016). An efficient Cellular Potts Model
 * algorithm that forbids cell fragmentation. Computer Physics Communications,
 * 208, 54-63. Checks if cell sigma is locally connected at lattice point (x,y)
 * if using LocalConnectedness(x,y,sigma[x][y]) and 
 * LocalConnectedness(x,y,sigma[xp][yp]) both are true This prevents cell
 * fragementation, as well as holes within a cell. 
 * 
 * \param grid Grid that is used.
 * \param pos Position that is checked.
 * \param spin Spin that is checked.
*/
bool LocalConnectedness(const Grid &grid, PixelPos pos, int spin);