// Load the code to be tested
#include "vec2.cpp"


// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>


TEST_CASE("Default-constructing Vec2 values", "[vec2]") {
    Vec2<int> a;
    REQUIRE(a.x == 0);
    REQUIRE(a.y == 0);

    Vec2<double> b;
    REQUIRE(b.x == 0.0);
    REQUIRE(b.y == 0.0);
}

TEST_CASE("Creating a Vec2 with given coordinates", "[vec2]") {
    Vec2<int> a(1, 2);
    REQUIRE(a.x == 1);
    REQUIRE(a.y == 2);
}

TEST_CASE("Converting Vec2<int> to Vec2<float>", "[vec2]") {
    Vec2<int> a(1, 2);
    Vec2<float> b(a);
}

void fn(Vec2<float> const & x) {}

TEST_CASE("Vec2 constants with curly brackets", "[vec2]") {
    Vec2<int> a;
    a = {1, 2};

    fn({1.0f, 3.0f});
    fn({1, 3});
}

TEST_CASE("Vec2 add onto", "[vec2]") {
    Vec2<float> a(1.0f, 2.0f), b(3.0f, 4.0f);

    a += b;

    REQUIRE(a.x == 4.0f);
    REQUIRE(a.y == 6.0f);
}

TEST_CASE("Vec2 subtract from", "[vec2]") {
    Vec2<float> a(1.0f, 2.0f), b(3.0f, 4.0f);

    a -= b;

    REQUIRE(a.x == -2.0f);
    REQUIRE(a.y == -2.0f);
}

TEST_CASE("Vec2 addition", "[vec2]") {
    Vec2<float> a(3.0f, 2.0f), b(4.0f, 6.0f), c;

    c = a + b;

    REQUIRE(c.x == 7.0f);
    REQUIRE(c.y == 8.0f);
}

TEST_CASE("Vec2 subtraction", "[vec2]") {
    Vec2<float> a(3.0f, 2.0f), b(4.0f, 6.0f), c;

    c = a - b;

    REQUIRE(c.x == -1.0f);
    REQUIRE(c.y == -4.0f);
}

