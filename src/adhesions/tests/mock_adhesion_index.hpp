#pragma once

#include "vec2.hpp"
#include "ecm.hpp"

#include <unordered_map>
#include <vector>


struct MockAdhesionWithEnvironment {
    MockAdhesionWithEnvironment(ParId par_id, ParPos const & position);

    ParId par_id;

    ParPos position;

    double move_dh(PixelDisplacement move) const;

    std::unordered_map<PixelDisplacement, double> move_dh_return_values;
};


class MockAdhesionIndex {
    public:
        MockAdhesionIndex(ExtraCellularMatrix & ecm);

        std::vector<MockAdhesionWithEnvironment> const & get_adhesions(
                PixelPos pixel) const;

        static std::unordered_map<
            PixelPos, std::vector<MockAdhesionWithEnvironment>
        >
            get_adhesions_return_values;

        void move_adhesions(PixelPos from, PixelPos to);

        void remove_adhesions(PixelPos pixel);

        void rebuild(ExtraCellularMatrix const & ecm);
};


using AdhesionWithEnvironment = MockAdhesionWithEnvironment;
using AdhesionIndex = MockAdhesionIndex;

