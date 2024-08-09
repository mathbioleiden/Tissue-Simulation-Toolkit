#include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>

#include "cell_direction.cpp"
#include "cell_polarity.cpp"
#include "vec2.cpp"

using Catch::Matchers::WithinAbs;

std::deque<Vec2<double>> get_com_history(CellPolarity &cell_polarity) {
    return cell_polarity.com_history;
}

TEST_CASE("cell polarity adding coms", "[cellpolarity]")
{
    FitEllipse fit_ellipse;
    CellPolarity cell_polarity(3);
    Vec2<double> polarity;

    SECTION("Adding non or one sites does nothing") {
        polarity = cell_polarity.get();
        REQUIRE(polarity == Vec2<double>(0.0, 0.0));
        fit_ellipse.add_site({5, 5});
        cell_polarity.add_com(fit_ellipse.center());
        polarity = cell_polarity.get();
        REQUIRE(polarity == Vec2<double>(0.0, 0.0));
    }

    SECTION("Adding a second site gives polarity") {
        fit_ellipse.add_site({5, 5});
        cell_polarity.add_com(fit_ellipse.center());
        fit_ellipse.add_site({6, 5});
        cell_polarity.add_com(fit_ellipse.center());
        polarity = cell_polarity.get();
        REQUIRE(polarity == Vec2<double>(1.0, 0.0));
    }

    SECTION("Adding a second site gives polarity non-unit") {
        fit_ellipse.add_site({5, 5});
        cell_polarity.add_com(fit_ellipse.center());
        fit_ellipse.add_site({7, 5});
        cell_polarity.add_com(fit_ellipse.center());
        polarity = cell_polarity.get();
        REQUIRE(polarity == Vec2<double>(1.0, 0.0));
    }

    SECTION("Adding a third point works") {
        fit_ellipse.add_site({5, 5});
        cell_polarity.add_com(fit_ellipse.center());
        fit_ellipse.add_site({6, 5});
        cell_polarity.add_com(fit_ellipse.center());
        fit_ellipse.add_site({5, 6});
        cell_polarity.add_com(fit_ellipse.center());
        polarity = cell_polarity.get();
        auto result = Vec2<double>(1.0/std::sqrt(2), 1.0/std::sqrt(2));
        REQUIRE_THAT(polarity.x, Catch::Matchers::WithinAbs(result.x, 0.000001));
        REQUIRE_THAT(polarity.y, Catch::Matchers::WithinAbs(result.y, 0.000001));
    }
}

TEST_CASE("Test that cell polarity keeps history", "[cell polarity history]")
{
    CellPolarity cell_polarity(10);
    Vec2<double> polarity, result;

    SECTION("10 times right is right") {
        for (int i = 0; i < 10; i++){
            cell_polarity.add_com({1.0*i,0.0});
        }
        polarity = cell_polarity.get();

        result = {1.0, 0.0};
        REQUIRE_THAT(polarity.x, Catch::Matchers::WithinAbs(result.x, 0.000001));
        REQUIRE_THAT(polarity.y, Catch::Matchers::WithinAbs(result.y, 0.000001));
    }

    SECTION("5 times east and 5 times north is northeast") {
        for (int i = 0; i < 5; i++){
            cell_polarity.add_com({1.0*i,0.0});
        }
        for (int i = 1; i < 5; i++){
            cell_polarity.add_com({4.0,i*1.0});
        }
        polarity = cell_polarity.get();

        for (auto x : get_com_history(cell_polarity)) {
            std::cout << x;
        }
        std::cout << '\n';

        result = {1.0 / std::sqrt(2), 1.0 / std::sqrt(2)};
        REQUIRE_THAT(polarity.x, Catch::Matchers::WithinAbs(result.x, 0.000001));
        REQUIRE_THAT(polarity.y, Catch::Matchers::WithinAbs(result.y, 0.000001));
    }
    
    SECTION("5 times east and 10 times north is north") {
        for (int i = 0; i < 5; i++){
            cell_polarity.add_com({1.0*i,0.0});
        }
        for (int i = 1; i < 10; i++){
            cell_polarity.add_com({4.0,i*1.0});
        }
        polarity = cell_polarity.get();

        for (auto x : get_com_history(cell_polarity)) {
            std::cout << x;
        }
        std::cout << '\n';

        result = {0.0, 1.0};
        REQUIRE_THAT(polarity.x, Catch::Matchers::WithinAbs(result.x, 0.000001));
        REQUIRE_THAT(polarity.y, Catch::Matchers::WithinAbs(result.y, 0.000001));
    }
}