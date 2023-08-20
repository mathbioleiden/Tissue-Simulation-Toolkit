#pragma once


class MockParameter {
    public:
        double adhesion_zone_radius;
        int num_adhesions;

        char const * adhesion_extension_mechanism;
        char const * adhesion_displacement_selection;
        int adhesion_annihilation_penalty;
        int adhesions_per_pixel_overflow;
        int adhesions_per_pixel_overflow_penalty;

        int n_chem;
        int sizex;
        int sizey;
};

using Parameter = MockParameter;

