#include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>

#include "cell_direction.cpp"
#include "vec2.cpp"

using Catch::Matchers::WithinAbs;

TEST_CASE("Adding moment works", "[fitellipse_add]")
{
    FitEllipse fit_ellipse;

    fit_ellipse.add_site({5, 5});

    auto center = fit_ellipse.center();
    Vec2<double> expected_center = {5.0, 5.0};

    REQUIRE(center == expected_center);

    fit_ellipse.clear();

    fit_ellipse.add_site({6, 5});
    center = fit_ellipse.center();
    REQUIRE(center == Vec2<double>(6.0, 5.0));
}

TEST_CASE("Length works", "[fitellipse_length]")
{
    SECTION("At (0,0) ")
    {
        FitEllipse fit_ellipse;
        double x0 = 0.0;
        double y0 = 0.0;
        double A = 3.0;
        double B = 5.0;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = i * 1.0 - x0;
                double y = j * 1.0 - y0;
                if ((x / A) * (x / A) + (y / B) * (y / B) <= 1.0)
                    fit_ellipse.add_site({i, j});
            }
        }

        auto length = fit_ellipse.length();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(B, 0.1));
    }
    SECTION("At (5,10) ")
    {
        FitEllipse fit_ellipse;
        double x0 = 5.0;
        double y0 = 10.0;
        double A = 3.0;
        double B = 5.0;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = i * 1.0 - x0;
                double y = j * 1.0 - y0;
                if ((x / A) * (x / A) + (y / B) * (y / B) <= 1.0)
                    fit_ellipse.add_site({i, j});
            }
        }

        auto length = fit_ellipse.length();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(B, 0.1));

        auto vec = fit_ellipse.major_axis();

        REQUIRE_THAT(vec.x, Catch::Matchers::WithinAbs(0.0, 0.1));
        REQUIRE_THAT(vec.y, Catch::Matchers::WithinAbs(1.0, 0.1));
    }

    SECTION("Rotated 10 degrees")
    {
        FitEllipse fit_ellipse;
        double x0 = 5.0;
        double y0 = 10.0;
        double A = 3.0;
        double B = 5.0;
        double theta = (11.0 / 180.0) * 3.1415;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = (i * 1.0 - x0);
                double y = (j * 1.0 - y0);
                double rotx = x * std::cos(theta) + y * std::sin(theta);
                double roty = x * std::sin(theta) - y * std::cos(theta);
                if ((rotx / A) * (rotx / A) + (roty / B) * (roty / B) <= 1.0)
                    fit_ellipse.add_site({i, j});
            }
        }

        auto length = fit_ellipse.length();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(B, 1));

        //        auto vec = fit_ellipse.major_axis();
        //        if (vec.x < 0)
        //            vec = -1.0 * vec;
        //
        //        REQUIRE_THAT(vec.x,
        //        Catch::Matchers::WithinAbs(std::cos(theta), 0.2));
        //        REQUIRE_THAT(vec.y,
        //        Catch::Matchers::WithinAbs(-std::sin(theta), 0.2));
        //
        //        auto vec_small = fit_ellipse.minor_axis();
        //        if (vec_small.x < 0)
        //            vec_small = -1.0 * vec_small;
        //        REQUIRE_THAT(vec_small.x,
        //        Catch::Matchers::WithinAbs(-std::sin(theta), 0.2));
        //        REQUIRE_THAT(vec_small.y,
        //        Catch::Matchers::WithinAbs(std::cos(theta), 0.2));
    }

    SECTION("Rotated 10 degrees minor axis")
    {
        FitEllipse fit_ellipse;
        double x0 = 5.0;
        double y0 = 10.0;
        double A = 3.0;
        double B = 5.0;
        double theta = (11.0 / 180.0) * 3.1415;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = (i * 1.0 - x0);
                double y = (j * 1.0 - y0);
                double rotx = x * std::cos(theta) + y * std::sin(theta);
                double roty = x * std::sin(theta) - y * std::cos(theta);
                if ((rotx / A) * (rotx / A) + (roty / B) * (roty / B) <= 1.0)
                    fit_ellipse.add_site({i, j});
            }
        }

        auto length = fit_ellipse.minor();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(A, 1));
    }
}

TEST_CASE("Test Major minor axis")
{
    FitEllipse fit_ellipse;
    double x0 = 5.0;
    double y0 = 10.0;
    double A = 3.0;
    double B = 5.0;
    double theta = 0.0; // (11.0/180.0) * 3.1415;

    for (int i = x0 - 10; i < x0 + 11; i++)
    {
        for (int j = y0 - 10; j < y0 + 11; j++)
        {
            double x = (i * 1.0 - x0);
            double y = (j * 1.0 - y0);
            double rotx = x * std::cos(theta) + y * std::sin(theta);
            double roty = x * std::sin(theta) - y * std::cos(theta);
            if ((rotx / A) * (rotx / A) + (roty / B) * (roty / B) <= 1.0)
            {
                fit_ellipse.add_site({i, j});
            }
        }
    }

    auto minor = fit_ellipse.minor_axis();
    auto major = fit_ellipse.major_axis();

    // orthogonal
    REQUIRE_THAT(minor.x * major.x + minor.y * major.y,
                 Catch::Matchers::WithinAbs(0, 0.001));
    if (minor.x < 0)
        minor = -1.0 * minor;
    REQUIRE_THAT(minor.x, Catch::Matchers::WithinAbs(1, 0.001));
    REQUIRE_THAT(minor.y, Catch::Matchers::WithinAbs(0, 0.001));

    if (major.y < 0)
        major = -1.0 * major;

    REQUIRE_THAT(major.x, Catch::Matchers::WithinAbs(0, 0.001));
    REQUIRE_THAT(major.y, Catch::Matchers::WithinAbs(1, 0.001));
}

TEST_CASE("Linear Algebra test")
{

    SECTION("Symmetric matrix")
    {
        double A = GENERATE(-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0,
                            4.0, 5.0);
        double B = GENERATE(-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0,
                            4.0, 5.0);
        double C = GENERATE(-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0,
                            4.0, 5.0);

        if (A * C == B * B and !(A == 0 && B == 0 && C == 0))
        {
            auto solution = solve_symmetric_degenerate_matrix(A, B, C);
            // std::cout << A << ',' << B << ',' << C << "->" << solution <<
            // '\n';
            REQUIRE_THAT(A * solution.x + B * solution.y,
                         Catch::Matchers::WithinAbs(0.0, 0.000001));
            REQUIRE_THAT(B * solution.x + C * solution.y,
                         Catch::Matchers::WithinAbs(0.0, 0.000001));
        }
    }

    SECTION("Eigenvalues")
    {
        // Matrix [[1,3],[3,1]]
        // should have eigen pairs ( [1,1], 4), ([-1,1], -2)
        auto solution = solve_symmetric_degenerate_matrix(1 - 4, 3, 1 - 4);
        REQUIRE(solution.x == solution.y);

        solution = solve_symmetric_degenerate_matrix(1 + 2, 3, 1 + 2);
        REQUIRE(solution.x + solution.y == 0);
    }

    double x0 = 5.0;
    double y0 = 10.0;
    double A = GENERATE(1.0, 2.0, 3.0);
    double B = GENERATE(1.0, 2.0, 3.0);
    double theta = (GENERATE(0.0, 11.0, 60.0) / 180.0) * 3.1415;

    int sum_xx = 0;
    int sum_yy = 0;
    int sum_xy = 0;
    int sum_x = 0;
    int sum_y = 0;
    int area = 0;

    double Ixx = 0.0;
    double Ixy = 0.0;
    double Iyy = 0.0;

    for (int i = x0 - 10; i < x0 + 11; i++)
    {
        for (int j = y0 - 10; j < y0 + 11; j++)
        {
            double x = (i * 1.0 - x0);
            double y = (j * 1.0 - y0);
            double rotx = x * std::cos(theta) + y * std::sin(theta);
            double roty = x * std::sin(theta) - y * std::cos(theta);
            if ((rotx / A) * (rotx / A) + (roty / B) * (roty / B) <= 1.0)
            {
                sum_x += x;
                sum_y += y;
                sum_yy += y * y;
                sum_xx += x * x;
                sum_xy += y * x;
                area++;
            }
        }
    }
    double xbar = 1.0 * sum_x / area;
    double ybar = 1.0 * sum_y / area;

    for (int i = x0 - 10; i < x0 + 11; i++)
    {
        for (int j = y0 - 10; j < y0 + 11; j++)
        {
            double x = (i * 1.0 - x0);
            double y = (j * 1.0 - y0);
            double rotx = x * std::cos(theta) + y * std::sin(theta);
            double roty = x * std::sin(theta) - y * std::cos(theta);
            if ((rotx / A) * (rotx / A) + (roty / B) * (roty / B) <= 1.0)
            {
                Ixx += (y - ybar) * (y - ybar);
                Iyy += (x - ybar) * (x - ybar);
                Ixy += -(x - xbar) * (y - ybar);
            }
        }
    }
    InertiaTensor I(sum_x, sum_y, sum_xx, sum_yy, sum_xy, area);

    SECTION("InertiaMatrix Construction")
    {
        REQUIRE(I.xx == Ixx);
        REQUIRE(I.yy == Iyy);
        REQUIRE(I.xy == Ixy);
    }

    SECTION("InertiaMatrix Eigenvalue is large and small")
    {
        auto max = I.largest_eigenvalue();
        auto min = I.smallest_eigenvalue();
        REQUIRE(max >= min);
    }
}
