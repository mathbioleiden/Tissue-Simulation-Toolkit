#include <cmath>

template <> constexpr float Vec2<float>::length() const {
  return sqrtf(x * x + y * y);
}

template <> constexpr double Vec2<double>::length() const {
  return sqrt(x * x + y * y);
}

template <typename Coordinate>
constexpr Vec2<Coordinate> &Vec2<Coordinate>::operator+=(Vec2 const &rhs) {
  x += rhs.x;
  y += rhs.y;
  return *this;
}

template <typename Coordinate>
constexpr Vec2<Coordinate> &Vec2<Coordinate>::operator-=(Vec2 const &rhs) {
  x -= rhs.x;
  y -= rhs.y;
  return *this;
}

template <typename Coordinate>
constexpr Coordinate Vec2<Coordinate>::dot(Vec2 const &rhs) const {
  return x * rhs.x + y * rhs.y;
}



template <typename Coordinate>
Vec2<Coordinate> operator+(Vec2<Coordinate> const &lhs,
                           Vec2<Coordinate> const &rhs) {
  Vec2<Coordinate> result(lhs);
  result += rhs;
  return result;
}

template <typename Coordinate>
Vec2<Coordinate> operator*(Coordinate const &lhs,
                           Vec2<Coordinate> const &rhs) {
  Vec2<Coordinate> result(rhs);
  result.x *= lhs;
  result.y *= lhs;
  return result;
}

template <typename Coordinate>
Vec2<Coordinate> operator-(Vec2<Coordinate> const &lhs,
                           Vec2<Coordinate> const &rhs) {
  Vec2<Coordinate> result(lhs);
  result -= rhs;
  return result;
}

template <typename Coordinate>
bool operator==(Vec2<Coordinate> const &lhs, Vec2<Coordinate> const &rhs) {
  return (lhs.x == rhs.x) && (lhs.y == rhs.y);
}

template <typename Coordinate>
bool operator!=(Vec2<Coordinate> const &lhs, Vec2<Coordinate> const &rhs) {
  return (lhs.x != rhs.x) || (lhs.y != rhs.y);
}

template <typename Coordinate>
std::ostream &operator<<(std::ostream &os, Vec2<Coordinate> v) {
  return os << "(" << v.x << ", " << v.y << ")";
}
