// Load the code to be tested
#include "array2d.cpp"


// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>


TEST_CASE("Creating of array2d class", "[array2d]") {
    SECTION("") {
        Array2d<int> array(10,10); 
        auto spin = array.get({5,5}) ;
        REQUIRE(spin == 0);
    }
    SECTION("") {
        Array2d<int> array(10,10, 1); 
        auto spin = array.get({5,5}) ;
        REQUIRE(spin == 0);
    }
    SECTION("") {
        Array2d<int> array(10,10, BoundaryType::periodic); 
        auto spin = array.get({5,5}) ;
        REQUIRE(spin == 0);
    }
    SECTION("") {
        Array2d<int> array(10,10, 1, BoundaryType::wall); 
        auto spin = array.get({5,5}) ;
        REQUIRE(spin == 0);
    }
}

TEST_CASE("Setting of array2d", "[array2d-set]") {
    SECTION("Setting single point") {
        Array2d<int> array(20, 10, BoundaryType::periodic);
        array.set({3, 2}, 5);
        REQUIRE(array.get({3,2}) == 5);
    }
    SECTION("Setting multiple layers") {
        Array2d<int> array(20, 10, 5, BoundaryType::periodic);
        array.set({5,5}, 1, 10); 
        array.set({5,5}, 2, 20); 
        array.set({6,5}, 4, 1); 
        
        REQUIRE( array.get({5,5}) == 0);
        REQUIRE( array.get({5,5}, 1) == 10);
        REQUIRE( array.get({5,5}, 1) == 10);
        REQUIRE( array.get({5,5}, 2) == 20);
        REQUIRE( array.get({6,5}, 4) == 1);
    }
}

TEST_CASE("Boundaries", "[array2d-boundary]") {
    SECTION("Periodic") {
        Array2d<int> array(20, 10, 3, BoundaryType::periodic);
        
        REQUIRE(array.get({-1,-1}, 0) == 0);

        array.set({19, 9}, 2, 5);
        REQUIRE(array.get({-1,-1}, 2) == 5);
    }
    
    SECTION("Wall") {
        Array2d<int> array(20, 10, 3, BoundaryType::wall);
        
        REQUIRE(array.get({-1,-1}, 0) == -1);
        REQUIRE_THROWS_AS(
            array.set({-1,-1}, 2), std::out_of_range
        );
    }
}

TEST_CASE("Initalize", "[array2d-initialise]") {
    SECTION("Upscale") {
        Array2d<int> array;
        
        array.initialise(10, 10, 1, BoundaryType::periodic);
        
        REQUIRE( array.get({4,4}) == 0);
    }

    SECTION("Downscale") {
        Array2d<int> array(10, 10, 1);
        
        array.set({7,7}, 1);
        
        array.initialise(4, 4, 1, BoundaryType::wall);
        
        REQUIRE_THROWS( array.set({7,7}, 5));
        REQUIRE( array.get({3,3}) == 0);

    }

}
