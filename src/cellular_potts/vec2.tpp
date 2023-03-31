template <typename Coordinate>
constexpr Vec2<Coordinate> & Vec2<Coordinate>::operator+=(Vec2 const & rhs) {
    x += rhs.x;
    y += rhs.y;
    return *this;
}


template <typename Coordinate>
constexpr Vec2<Coordinate> & Vec2<Coordinate>::operator-=(Vec2 const & rhs) {
    x -= rhs.x;
    y -= rhs.y;
    return *this;
}


template <typename Coordinate>
Vec2<Coordinate> operator+(
        Vec2<Coordinate> const & lhs, Vec2<Coordinate> const & rhs
) {
    Vec2 result(lhs);
    result += rhs;
    return result;
}


template <typename Coordinate>
Vec2<Coordinate> operator-(
        Vec2<Coordinate> const & lhs, Vec2<Coordinate> const & rhs
) {
    Vec2 result(lhs);
    result -= rhs;
    return result;
}

