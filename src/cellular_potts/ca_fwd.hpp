/* Header file that forward-declares the CellularPotts class.
 *
 * Just writing class CellularPotts; doesn't work together with the mocking
 * system used for the tests. Include this instead.
 */

#ifdef _MOCK_CA_FWD_HPP_
#include _MOCK_CA_FWD_HPP_
#else
class CellularPotts;
#endif
