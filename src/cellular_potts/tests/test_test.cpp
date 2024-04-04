#define _MOCK_PARAMETER_HPP_ "mock_parameter.hpp"

#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>

#include "force_calculation.cpp"
#include "novikova_storm.cpp"

using Catch::Matchers::WithinAbs;

TEST_CASE("The test system works", "[test]") { REQUIRE(1 == 1); }

TEST_CASE("Force calcualtion")
{

    SECTION("Linear spring in rest")
    {

        double eps = 0.000001;

        auto forcevector = getLinearHarmonicForceOnB({0, 1}, {0, 0}, 1.0, 1.0);
        auto tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(tension, Catch::Matchers::WithinAbs(0.0, eps));

        forcevector = getLinearHarmonicForceOnB({0, 0}, {1, 0}, 1.0, 1.0);
        tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(tension, Catch::Matchers::WithinAbs(0.0, eps));
    }

    SECTION("Linear spring")
    {
        double eps = 0.000001;

        auto forcevector = getLinearHarmonicForceOnB({1, 1}, {0, 0}, 1.0, 0.0);
        auto tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(forcevector.x, Catch::Matchers::WithinAbs(1, eps));
        REQUIRE_THAT(forcevector.y, Catch::Matchers::WithinAbs(1, eps));
        REQUIRE_THAT(tension, Catch::Matchers::WithinAbs(std::sqrt(2), eps));

        forcevector = getLinearHarmonicForceOnB({0, 0}, {1, 1}, 1.0, 0.0);
        tension = std::sqrt(forcevector.dot(forcevector));
        REQUIRE_THAT(forcevector.x, Catch::Matchers::WithinAbs(-1, eps));
        REQUIRE_THAT(forcevector.y, Catch::Matchers::WithinAbs(-1, eps));
        REQUIRE_THAT(tension, Catch::Matchers::WithinAbs(std::sqrt(2), eps));
    }

    SECTION("Angle spring")
    {
        double eps = 0.0001;
        auto forcevector = getAngularHarmonicForceOnA({0.0, 1.0}, {0.0, 0.0},
                                                      {1.0, 0.0}, 1.0, 3.1415);

        auto magnitude = std::sqrt(forcevector.dot(forcevector));
        auto direction = (1.0 / magnitude) * forcevector;

        REQUIRE_THAT(direction.y, WithinAbs(0.0, eps));
        REQUIRE_THAT(direction.x, WithinAbs(-1.0, eps));
        REQUIRE_THAT(magnitude, WithinAbs(3.1415 * 0.5, 0.0001));

        forcevector = getAngularHarmonicForceOnA({-1.0, 0.0}, {0.0, 0.0},
                                                 {1.0, 0.0}, 1.0, 3.1415);

        magnitude = std::sqrt(forcevector.dot(forcevector));

        REQUIRE_THAT(magnitude, WithinAbs(0.0, 0.0001));
    }

    SECTION("Angle spring in rest")
    {
        double eps = 0.0001;
        auto forcevector = getAngularHarmonicForceOnA({-15.0, 0.0}, {0.0, 0.0},
                                                      {10.0, 0.0}, 1.0, 3.1415);

        auto magnitude = std::sqrt(forcevector.dot(forcevector));
        auto direction = (1.0 / magnitude) * forcevector;

        REQUIRE_THAT(magnitude, WithinAbs(0.0, 0.0001));

        forcevector = getAngularHarmonicForceOnA({-1.0, 0.0}, {0.0, 0.0},
                                                 {1.0, 0.0}, 1.0, 3.1415);

        magnitude = std::sqrt(forcevector.dot(forcevector));

        REQUIRE_THAT(magnitude, WithinAbs(0.0, 0.0001));
    }
}

TEST_CASE("Novikova Storm")
{

    SECTION("integrate")
    {
        NS::Parameter par(1000.0, 5.0, 2.0, 1.0, 1.0, 0.001, 0.1, 50.0, 1.0);

        auto size = NS::integrate(200.0, 50, par);
        std::cout << "size = " << size << std::endl;
    }
}
#include "act.cpp"
std::unordered_map<PixelPos, double> ACT::getValue(ACT::ActField act_field) {
    return act_field.value_;
}
TEST_CASE("Act Model")
{
    SECTION("Setting and Getting values")
    {
        ACT::ActField act_field;

        act_field.SetValue({0, 0}, 1.0);
        auto value = act_field.Value({0, 0});
        REQUIRE_THAT(value, WithinAbs(1.0, 0.00001));

        act_field.Decrease();

        value = act_field.Value({0, 0});
        REQUIRE_THAT(value, WithinAbs(0.0, 0.00001));

        // REQUIRE_THROWS_AS(act_field.Value({1, 0}), std::out_of_range);
        REQUIRE_THAT(act_field.Value({1,0}), WithinAbs(0.0, 0.00001) );
    }
    SECTION("Create ActField and get geo mean of point")
    {
        ACT::ActField act_field;
        
        int** sigma = new int*[4];
        sigma[0] = new int[4]; 
        sigma[1] = new int[4]; 
        sigma[2] = new int[4]; 
        sigma[3] = new int[4]; 
        
        for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            sigma[i][j]=0;

        act_field.SetValue({1+0,  1+0}, 1.0);
        act_field.SetValue({1+1,  1+0}, 1.0);
        act_field.SetValue({1+1,  1+1}, 1.0);
        act_field.SetValue({1+0,  1+1}, 1.0);
        act_field.SetValue({1+-1, 1+1}, 1.0);
        act_field.SetValue({1+-1, 1+0}, 1.0);
        act_field.SetValue({1+-1, 1+-1}, 1.0);
        act_field.SetValue({1+0, 1+-1}, 1.0);
        act_field.SetValue({1+1, 1+-1}, 1.0);

        auto mean = GeoMetricMean(act_field, sigma, {1, 1});
        REQUIRE_THAT(mean, WithinAbs(1.0, 0.00001));

        act_field.SetValue({1+0,  1+0}, 1.0);
        act_field.SetValue({1+1,  1+0}, 2.0);
        act_field.SetValue({1+1,  1+1}, 3.0);
        act_field.SetValue({1+0,  1+1}, 4.0);
        act_field.SetValue({1+-1, 1+1}, 5.0);
        act_field.SetValue({1+-1, 1+0}, 6.0);
        act_field.SetValue({1+-1, 1+-1}, 7.0);
        act_field.SetValue({1+0, 1+-1}, 8.0);
        act_field.SetValue({1+1, 1+-1}, 9.0);

        mean = GeoMetricMean(act_field,sigma, {1, 1});
        REQUIRE_THAT(mean, WithinAbs(4.147166274396913, 0.00000001));
    }
    
    SECTION("Delta H") {
        // This example is straight from the orginal paper.

        ACT::ActField act_field;
        
        par.lambda_Act = 1.0;
        par.max_Act = 20;
        
//        const int sigma_array[4][4] = {
//            {0,0,1,1},
//            {0,0,1,1},
//            {2,2,0,0},
//            {2,2,2,0},
//        };

        int** sigma = new int*[4];
        sigma[0] = new int[4]; 
        sigma[1] = new int[4]; 
        sigma[2] = new int[4]; 
        sigma[3] = new int[4]; 
        
        for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            sigma[i][j]=0;
        
        sigma[2][0] = 1;
        sigma[3][0] = 1;
        sigma[2][1] = 1;
        sigma[3][1] = 1;
        sigma[0][2] = 2;
        sigma[1][2] = 2;
        sigma[0][3] = 2;
        sigma[1][3] = 2;
        sigma[2][3] = 2;

        act_field.SetValue({2,0}, 19);
        act_field.SetValue({3,0}, 11);
        act_field.SetValue({2,1}, 17);
        act_field.SetValue({3,1}, 16);
        act_field.SetValue({0,2}, 18);
        act_field.SetValue({1,2}, 20);
        act_field.SetValue({0,3}, 15);
        act_field.SetValue({1,3}, 17);
        act_field.SetValue({2,3}, 15);

        auto GM_v = GeoMetricMean(act_field, sigma, {2,1});
        auto GM_u = GeoMetricMean(act_field, sigma, {1,2});

        auto dh = ACT::DeltaH(act_field, sigma, {1,2}, {2,1}, par.lambda_Act, par.max_Act); 

        REQUIRE_THAT(dh * par.max_Act, WithinAbs(1.46 , 0.01));
    }
    SECTION ("Test decreasing and deleting of positions") {
        ACT::ActField actin_field;
        
        actin_field.SetValue({10,10}, 10);
        for (int i=0; i < 5; i++)
            actin_field.Decrease();
        REQUIRE(actin_field.Value({10,10}) == 5);

        for (int i=0; i < 5; i++)
            actin_field.Decrease();
        REQUIRE(actin_field.Value({10,10}) == 0.0);

        auto values = getValue(actin_field);
        REQUIRE( values.size() == 0);
        
        actin_field.SetValue({20, 10}, 10.0);
        values = getValue(actin_field);
        REQUIRE( values.size() == 1);

        actin_field.SetValue({20, 10}, 0.0);
        values = getValue(actin_field);
        REQUIRE( values.size() == 0);
        
    }
    SECTION ("Adding value to act") {
        ACT::ActField act_field;

        act_field.SetValue({10,10}, 10);
        act_field.IncreaseValue({10,10}, 5);
        auto value = act_field.Value({10,10});
        REQUIRE( value == 15 );
        act_field.IncreaseValue({5,5}, 123);
        value = act_field.Value({5,5});
        REQUIRE( value == 123);
    }
}