#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>

#include "novikova_storm.cpp"
#include "force_calculation.cpp"

using Catch::Matchers::WithinAbs;

TEST_CASE("The test system works", "[test]") {
    REQUIRE(1 == 1);
}

TEST_CASE("Force calcualtion") {

    SECTION("Linear spring in rest") {

        double eps = 0.000001;

        auto forcevector = getLinearHarmonicForceOnB(
            {0, 1},
            {0, 0},
            1.0,
            1.0);
        auto tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(
            tension, Catch::Matchers::WithinAbs(0.0, eps));

        forcevector = getLinearHarmonicForceOnB(
            {0, 0},
            {1, 0},
            1.0,
            1.0);
        tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(
            tension, Catch::Matchers::WithinAbs(0.0, eps));
    }

    SECTION("Linear spring") {
        double eps = 0.000001;

        auto forcevector = getLinearHarmonicForceOnB(
            {1, 1},
            {0, 0},
            1.0,
            0.0);
        auto tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(
            forcevector.x, Catch::Matchers::WithinAbs(1, eps));
        REQUIRE_THAT(
            forcevector.y, Catch::Matchers::WithinAbs(1, eps));
        REQUIRE_THAT(
            tension, Catch::Matchers::WithinAbs(std::sqrt(2), eps));

        forcevector = getLinearHarmonicForceOnB(
            {0, 0},
            {1, 1},
            1.0,
            0.0);
        tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(
            forcevector.x, Catch::Matchers::WithinAbs(-1, eps));
        REQUIRE_THAT(
            forcevector.y, Catch::Matchers::WithinAbs(-1, eps));
        REQUIRE_THAT(
            tension, Catch::Matchers::WithinAbs(std::sqrt(2), eps));
    }

    SECTION("Angle spring") {
        double eps = 0.0001;
        auto forcevector = getAngularHarmonicForceOnA(
            {0.0, 1.0},
            {0.0, 0.0},
            {1.0, 0.0},
            1.0,
            3.1415);

        auto magnitude = std::sqrt(forcevector.dot(forcevector));
        auto direction = (1.0/magnitude) * forcevector;
        

        REQUIRE_THAT(direction.y, WithinAbs(0.0, eps));
        REQUIRE_THAT(direction.x, WithinAbs(-1.0, eps));
        REQUIRE_THAT(
            magnitude, WithinAbs(3.1415 * 0.5, 0.0001));

        forcevector = getAngularHarmonicForceOnA(
            {-1.0, 0.0},
            {0.0, 0.0},
            {1.0, 0.0},
            1.0,
            3.1415);

        magnitude = std::sqrt(forcevector.dot(forcevector));

        REQUIRE_THAT(
            magnitude, WithinAbs(0.0, 0.0001));
        
    }

    SECTION("Angle spring in rest") {
        double eps = 0.0001;
        auto forcevector = getAngularHarmonicForceOnA(
            {-15.0, 0.0},
            {0.0, 0.0},
            {10.0, 0.0},
            1.0,
            3.1415);

        auto magnitude = std::sqrt(forcevector.dot(forcevector));
        auto direction = (1.0/magnitude) * forcevector;
        

        REQUIRE_THAT(
            magnitude, WithinAbs(0.0, 0.0001));

        forcevector = getAngularHarmonicForceOnA(
            {-1.0, 0.0},
            {0.0, 0.0},
            {1.0, 0.0},
            1.0,
            3.1415);

        magnitude = std::sqrt(forcevector.dot(forcevector));

        REQUIRE_THAT(
            magnitude, WithinAbs(0.0, 0.0001));
        
    }
}

TEST_CASE("Novikova Storm") {

    SECTION("integrate") {
        NS::Parameter par(1000.0, 5.0, 2.0, 1.0, 1.0, 0.001, 0.1, 50.0, 1.0);
        
        auto size = NS::integrate(200.0, 50, par);
        std::cout << "size = " << size << std::endl;
    }


}
