#pragma once

#include "libmuscle/libmuscle.hpp"
#include "ymmsl/ymmsl.hpp"


/** Helper class for accessing grids/matrices received via MUSCLE3
 *
 * This makes it easier to access individual elements of a grid/matrix. I'm going
 * to add that feature to the libmuscle API and then this won't be needed any more,
 * but until then here we are.
 *
 * The object, once created, references the data object that was passed in, so you
 * need to make sure that that still exists for as long as you use the Muscle3Grid
 * object.
 */
template <typename T>
class Muscle3Grid {
    public:
        /** Create a Muscle3Grid
         *
         * @param data A MUSCLE3 data object containing a grid
         */
        Muscle3Grid(libmuscle::DataConstRef const & data);

        /** Return the i'th element of the shape of the matrix */
        std::size_t shape(std::size_t i) const;

        /** Element access for 1D arrays
         *
         * We're not using square brackets to stay consistent with the 2D version.
         *
         * @param i0 The index of the desired element
         * @return The value of the requested array element
         */
        T operator()(std::size_t i0) const;

        /** Element access for 2D arrays
         *
         * @param i0 The first index of the desired element
         * @param i1 The second index of the desired element
         * @return The value of the requested array element
         */
        T operator()(std::size_t i0, std::size_t i1) const;

    private:
        std::vector<std::size_t> shape_;
        std::vector<std::size_t> strides_;
        T const * elements_;
};


#include "muscle3/muscle3_grid.tpp"

