#pragma once
#include "vec2.hpp"

/* Lets you iterate through the neighbours of a pixel.
 *
 * Covers the 8 neighbours in a Mealy neighbourhood, excluding the
 * center pixel itself.
 *
 * Note: This should eventually end up in a Grid class used by CellularPotts,
 * but for now we'll put it here where we need it.
 *
 * Usage:
 *
 * for (PixelPos nb : Neighbours(pixel)) ...
 */
class Neighbours {
public:
  class iterator {
  public:
    iterator operator++() {
      ++i_;
      return *this;
    }

    iterator operator++(int) {
      iterator result = *this;
      ++i_;
      return result;
    }

    bool operator==(iterator const &rhs) { return i_ == rhs.i_; }

    bool operator!=(iterator const &rhs) { return i_ != rhs.i_; }

    PixelPos operator*() const { return center_ + d_[i_]; }

  private:
    friend class Neighbours;
    iterator(PixelPos center, int i) : center_(center), i_(i) {}

    PixelPos center_;
    int i_;
  };

  Neighbours(PixelPos center) : center_(center) {}

  iterator begin() const { return iterator(center_, 0); }

  iterator end() const { return iterator(center_, 8); }

private:
  static const PixelDisplacement d_[8];
  PixelPos center_;
};
