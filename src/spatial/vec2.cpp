#include "vec2.hpp"

template <>
template <>
Vec2<float>::Vec2(Vec2<int> const &v)
    : x(static_cast<float>(v.x)), y(static_cast<float>(v.y)) {}

template <>
template <>
Vec2<double>::Vec2(Vec2<int> const &v)
    : x(static_cast<double>(v.x)), y(static_cast<double>(v.y)) {}
