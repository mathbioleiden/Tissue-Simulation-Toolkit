#pragma once

#include <libmuscle/libmuscle.hpp>

#include "cell_ecm_interactions.hpp"
#include "ecm_boundary_state.hpp"

#include <utility>

/* Helper class that owns memory for encoded CellECMInteractions
 *
 * To convert a CellECMInteractions to a MUSCLE3 data object, we need to make
 * some auxiliary arrays that need to be kept in memory until the data has been
 * sent. This class holds those arrays, and is returned along with the object.
 *
 * I'm going to extend the MUSCLE3 API to make this unneccessary, but in the
 * mean time this will ensure we don't have memory leaks. The naming is
 * intentionally obscure, the caller is not supposed to do anything with this.
 */
struct AutoMemory {
  std::vector<int32_t> m0;
  std::vector<double> m1;
  std::vector<double> m2;
};

/** Encode a CellECMInteractions object
 *
 * The result will reference memory in the CellECMInteractions object passed to
 * this function, so that needs to be kept around for as long as the result is
 * used. Also, new memory will be allocated, which is owned by the second item
 * in the result. Likewise, that needs to be kept alive.
 *
 * @param interactions The object to encode
 */
std::pair<libmuscle::Data, AutoMemory>
encode_cell_ecm_interactions(CellECMInteractions const &interactions);

/** Decode an ECM boundary state into an ECMBoundaryState object
 *
 * @param data A data object received using MUSCLE3 that contains an ECM
 * boundary state.
 */
ECMBoundaryState decode_ecm_boundary_state(libmuscle::DataConstRef const &data);
