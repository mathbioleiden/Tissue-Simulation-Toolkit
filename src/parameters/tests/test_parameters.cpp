// Load the real implementations
#include "parameter_file.cpp"
#include "parameter.cpp"


// Dependencies for the test itself
#include <catch2/catch_test_macros.hpp>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <exception>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unistd.h>


TEST_CASE( "Test default construction", "[parameters]" ) {
    Parameter par;

    // Not testing everything, just one of each supported type
    REQUIRE(par.store);                     // bool
    REQUIRE(par.sizex == 200);              // int
    REQUIRE(par.dt == 2.0);                 // double
    REQUIRE(par.datadir == "data_film");    // std::string
    REQUIRE(par.diff_coeff.size() == 1u);   // std::vector<double>
    REQUIRE(par.diff_coeff == std::vector<double>{1e-13});
}


/* Save contents of buffer to a temp file and return the file's name
 * C++ doesn't have a way to create a temp file, so we have to resort
 * to C and POSIX.
 */
std::string save_to_temp_file(char const * buf, std::size_t len) {
    char temp_file_name[] = "tmp_test_parameters_XXXXXX";
    int fd = mkstemp(temp_file_name);
    ssize_t written = write(fd, buf, len);
    REQUIRE(written == len);
    close(fd);

    return std::string(temp_file_name, strlen(temp_file_name));
}


TEST_CASE( "Test error when input file does not exist", "[parameters]" ) {
    Parameter par;

    REQUIRE_THROWS(par.Read("doesnotexist"));
}


TEST_CASE( "Test loading parameters from file", "[parameters]" ) {
    char pars[] = (
            "# This is a comment\n"
            "      # And we should test empty lines too\n"
            "\n"
            "store = false\n"
            " graphics    =true\n"
            "sizex= 100\n"
            "  sizey   =   123   \n"
            " dt=2.5\n"
            "datadir = data_pictures  \n"
            "n_chem = 5\n"
            "diff_coeff   = 1e-13, 1.0 , 3 ,2e-7,17.8   \n"
            "decay_rate = 1, 2, 3, 4, 5\n"
            "secr_rate = 1, 1, 1, 1, 1\n");
    std::string file = save_to_temp_file(pars, strlen(pars));

    Parameter par;
    par.Read(file);

    // Check values read from file
    REQUIRE_FALSE(par.store);
    REQUIRE(par.graphics);
    REQUIRE(par.sizex == 100);
    REQUIRE(par.sizey == 123);
    REQUIRE(par.dt == 2.5);
    REQUIRE(par.datadir == "data_pictures");
    REQUIRE(par.diff_coeff == std::vector<double>{1e-13, 1.0, 3.0, 2e-7, 17.8});

    // Check that others are still the default
    REQUIRE(par.storage_stride == 10);

    // Clean up the file
    int err = remove(file.c_str());
    REQUIRE(err == 0);
}


TEST_CASE( "Test validating parameter constraints", "[parameters]" ) {
    Parameter par;

    REQUIRE_NOTHROW(par.Validate());

    par.n_chem = 2;
    REQUIRE_THROWS_AS(par.Validate(), std::invalid_argument);
    par.diff_coeff = {1.0, 2.0};
    REQUIRE_THROWS_AS(par.Validate(), std::invalid_argument);
    par.decay_rate = {1.0, 2.0};
    REQUIRE_THROWS_AS(par.Validate(), std::invalid_argument);
    par.secr_rate = {1.0, 2.0};
    REQUIRE_NOTHROW(par.Validate());
}


TEST_CASE( "Test saving parameters to a stream", "[parameters]" ) {
    Parameter par;
    std::ostringstream oss;

    // check that all digits are saved
    // this is brittle, but it rounds the right way it seems
    par.dt = 2.1234567890123;

    par.Write(oss);
    std::string output = oss.str();

    // check all supported types
    REQUIRE(output.find("store = true\n") != output.npos);
    REQUIRE(output.find("sizex = 200\n") != output.npos);
    REQUIRE(output.find("dt = 2.1234567890123\n") != output.npos);
    REQUIRE(output.find("datadir = data_film\n") != output.npos);
    REQUIRE(output.find("diff_coeff = 1e-13\n") != output.npos);

    REQUIRE(output.find("# Cellular Potts Model - Grid\n") != output.npos);
}


TEST_CASE( "Test save-and-load roundtrip", "[parameters]" ) {
    Parameter par;
    par.store = false;
    par.dt = 3.141592653589793;
    par.datadir = "data_pictures";
    par.n_chem = 3;
    par.diff_coeff = {0.125, 7.0, -3.0};
    par.decay_rate = {10.0, 100.5, 1000.0};
    par.secr_rate = {1, 2, 3.25};
    par.J_pol = 13;     // unlucky number to ensure we find any bugs

    std::ostringstream oss;
    par.Write(oss);
    std::string output = oss.str();
    std::string file = save_to_temp_file(output.data(), output.size());

    Parameter par2;
    par2.Read(file);

#define CATCH_SECTION SECTION
#undef SECTION

#define SECTION(TEXT)
#define PARAMETER(TYPE, NAME, DEFAULT, DESC) REQUIRE(par.NAME == par2.NAME);
#define CONSTRAINT(EXPR, MESSAGE)
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION

#define SECTION CATCH_SECTION
#undef CATCH_SECTION

    int err = remove(file.c_str());
    REQUIRE(err == 0);
}

