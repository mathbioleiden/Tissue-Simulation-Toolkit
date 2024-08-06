#include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>

#include "cell_direction.cpp"
#include "cell_polarity.cpp"
#include "vec2.cpp"

using Catch::Matchers::WithinAbs;

std::vector<Vec2<double>> get_com_history(CellPolarity &cell_polarity) {
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