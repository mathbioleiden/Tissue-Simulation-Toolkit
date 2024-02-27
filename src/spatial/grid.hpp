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
  Spin get(PixelPos);
  void set(PixelPos, Spin value);
  void resize(int, int);

  // TEMPORY ONLY HAS MOORE NEIGHBOURHOOD
  Neighbors neighbors(PixelPos);

private:
  Array2d<int> spinfield_;
};
