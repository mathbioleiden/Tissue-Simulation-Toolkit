#include "util/muscle3/settings.hpp"

#include "parameter.hpp"

extern Parameter par;


namespace {

/* The types used by TST for parameters and the ones used by MUSCLE3 for settings
 * almost but don't completely match up. This helper translates from TST type to the
 * corresponding MUSCLE3 type.
 */
template <typename T>
struct Muscle3Type {
    // By default, the types are the same
    typedef T type;
};

template <>
struct Muscle3Type<int> {
    // For ints, MUSCLE3 uses int64_t
    typedef int64_t type;
};

}


void set_parameters_from_settings(libmuscle::Instance const & instance) {

#define SECTION(TEXT)
#define PARAMETER(TYPE, NAME, DEFAULT, DESC)                                    \
    try {                                                                       \
        par.NAME = instance.get_setting_as<Muscle3Type<TYPE>::type>(#NAME);     \
    }                                                                           \
    catch (std::bad_cast const & e) {                                           \
        throw std::runtime_error(                                               \
                std::string("Expected setting ") + #NAME + " to be of type " +  \
                #TYPE + " but it isn't. Please fix the ymmsl file.");           \
    }                                                                           \
    catch (std::out_of_range const & e) {}
#define CONSTRAINT(EXPR, MESSAGE)
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION

    par.Validate();
}

