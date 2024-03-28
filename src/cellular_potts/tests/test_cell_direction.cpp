#include <catch2/catch_test_macros.hpp>
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
    SECTION("At (0,0) ") {
        FitEllipse fit_ellipse;
        double x0 = 0.0;
        double y0 = 0.0;
        double A = 3.0;
        double B = 5.0;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = i*1.0 - x0;
                double y = j*1.0 - y0;
                if ( (x/A) * (x/A) + (y/B)* (y/B) <= 1.0 )
                    fit_ellipse.add_site({i,j});
            }
        }

        auto length = fit_ellipse.length();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(B, 0.1));
    }
    SECTION("At (5,10) ") {
        FitEllipse fit_ellipse;
        double x0 = 5.0;
        double y0 = 10.0;
        double A = 3.0;
        double B = 5.0;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = i*1.0 - x0;
                double y = j*1.0 - y0;
                if ( (x/A) * (x/A) + (y/B)* (y/B) <= 1.0 )
                    fit_ellipse.add_site({i,j});
            }
        }

        auto length = fit_ellipse.length();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(B, 0.1));
        

        auto vec = fit_ellipse.major_axis();
        
        REQUIRE_THAT(vec.x, Catch::Matchers::WithinAbs(1.0, 0.1));
        REQUIRE_THAT(vec.y, Catch::Matchers::WithinAbs(0.0, 0.1));
    }
    
    SECTION("Rotated 10 degrees") {
        FitEllipse fit_ellipse;
        double x0 = 5.0;
        double y0 = 10.0;
        double A = 3.0;
        double B = 5.0;
        double theta = (11.0/180.0) * 3.1415;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = (i*1.0 - x0);
                double y = (j*1.0 - y0);
                double rotx = x * std::cos(theta) + y * std::sin(theta);
                double roty = x * std::sin(theta) - y * std::cos(theta);
                if ( (rotx/A) * (rotx/A) + (roty/B)* (roty/B) <= 1.0 )
                    fit_ellipse.add_site({i,j});
            }
        }

        auto length = fit_ellipse.length();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(B, 1));
        
        
//        auto vec = fit_ellipse.major_axis();
//        if (vec.x < 0)
//            vec = -1.0 * vec;
//        
//        REQUIRE_THAT(vec.x, Catch::Matchers::WithinAbs(std::cos(theta), 0.2));
//        REQUIRE_THAT(vec.y, Catch::Matchers::WithinAbs(-std::sin(theta), 0.2));
//        
//        auto vec_small = fit_ellipse.minor_axis();
//        if (vec_small.x < 0)
//            vec_small = -1.0 * vec_small;
//        REQUIRE_THAT(vec_small.x, Catch::Matchers::WithinAbs(-std::sin(theta), 0.2));
//        REQUIRE_THAT(vec_small.y, Catch::Matchers::WithinAbs(std::cos(theta), 0.2));
    }

    SECTION("Rotated 10 degrees minor axis") {
        FitEllipse fit_ellipse;
        double x0 = 5.0;
        double y0 = 10.0;
        double A = 3.0;
        double B = 5.0;
        double theta = (11.0/180.0) * 3.1415;

        for (int i = x0 - 10; i < x0 + 11; i++)
        {
            for (int j = y0 - 10; j < y0 + 11; j++)
            {
                double x = (i*1.0 - x0);
                double y = (j*1.0 - y0);
                double rotx = x * std::cos(theta) + y * std::sin(theta);
                double roty = x * std::sin(theta) - y * std::cos(theta);
                if ( (rotx/A) * (rotx/A) + (roty/B)* (roty/B) <= 1.0 )
                    fit_ellipse.add_site({i,j});
            }
        }

        auto length = fit_ellipse.minor();
        REQUIRE_THAT(length, Catch::Matchers::WithinAbs(A, 1));
        
    }

}