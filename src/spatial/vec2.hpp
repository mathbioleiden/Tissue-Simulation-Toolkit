#pragma once

#include <initializer_list>
#include <iostream>
#include <limits>

/** 2D vector class template.
 *
 * @tparam Coordinate Type of the elements
 * @attribute x Left-to-right location
 * @attribute y Top-to-bottom location
 */
template <typename Coordinate> struct Vec2 {
  Coordinate x, y;

  /** Create a Vec2 at the origin.
   */
  constexpr Vec2() : x(Coordinate()), y(Coordinate()) {}

  /** Create a Vec2 from coordinates.
   *
   * @param x The x coordinate.
   * @param y The y coordinate.
   */
  constexpr Vec2(Coordinate x, Coordinate y) : x(x), y(y) {}

  /** Convert from a different coordinate type.
   *
   * Currently only implemented for Vec2<int> to Vec2<float> and
   * Vec2<int> to Vec2<double> conversion.
   */
  template <typename OtherCoordinate> Vec2(Vec2<OtherCoordinate> const &);

  /* Copying, moving and assignment as per defaults. */
  Vec2(Vec2 const &) = default;
  Vec2(Vec2 &&) = default;
  Vec2 &operator=(Vec2 const &) = default;
  Vec2 &operator=(Vec2 &&) = default;

  /** Return the length (L2 norm).
   *
   * This is only implemented for float and double template arguments.
   */
  constexpr Coordinate length() const;

  /** Add two vectors. */
  constexpr Vec2 &operator+=(Vec2 const &rhs);

  /** Subtract two vectors. */
  constexpr Vec2 &operator-=(Vec2 const &rhs);

  /** Return the dot product.
   *
   * @param rhs The vector to multiply with.
   */
  constexpr Coordinate dot(Vec2 const &rhs) const;
};

// Declare the specific types for which conversion is implemented
template <> template <> Vec2<float>::Vec2(Vec2<int> const &v);

template <> template <> Vec2<double>::Vec2(Vec2<int> const &v);

/** Add two vectors together. */
template <typename Coordinate>
Vec2<Coordinate> operator+(Vec2<Coordinate> const &lhs,
                           Vec2<Coordinate> const &rhs);

/** Subtract a vector from another. */
template <typename Coordinate>
Vec2<Coordinate> operator-(Vec2<Coordinate> const &lhs,
                           Vec2<Coordinate> const &rhs);

/** Compare for equality. */
template <typename Coordinate>
bool operator==(Vec2<Coordinate> const &lhs, Vec2<Coordinate> const &rhs);

/** Compare for inequality. */
template <typename Coordinate>
bool operator!=(Vec2<Coordinate> const &lhs, Vec2<Coordinate> const &rhs);

/** Stream a vector. */
template <typename Coordinate>
std::ostream &operator<<(std::ostream &os, Vec2<Coordinate> v);

/** Coordinates of a pixel in the Cellular Potts grid.
 */
using PixelPos = Vec2<int>;

/** Allow use in unordered_map. */
template <> struct std::hash<PixelPos> {
  std::size_t operator()(PixelPos const &p) const noexcept {
    std::hash<int> hasher;
    return hasher(p.x) ^ (hasher(p.y) * 257);
  }
};

/** Difference of two PixelPos's.
 *
 * Note that this is the same type as PixelPos, and you can use them
 * interchangeably. The different names are just to make it clearer what is
 * what in the code: a PixelPos is an absolute position on the grid, a
 * PixelDisplacement a position relative to some other pixel.
 *
 * This could be made type-safe, disallowing addition of two PixelPos values,
 * but it doesn't seem worth the extra complexity.
 */
using PixelDisplacement = Vec2<int>;

/** Constant representing a displacement to nowhere. */
const PixelDisplacement annihilation(std::numeric_limits<int>::lowest(),
                                     std::numeric_limits<int>::lowest());

/** Position of an arbitrary point in the Cellular Potts domain.
 */
using ParPos = Vec2<double>;

/** Difference of two ParPos's. */
using ParDisplacement = Vec2<double>;

// Include the implementation, as this is a template and it must be available
// to users of this template.

#include "vec2.tpp"
