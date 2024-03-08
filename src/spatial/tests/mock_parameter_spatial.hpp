#pragma once

class MockParameter {
    public:
        int sizex;
        int sizey;
        bool periodic_boundaries;
};

using Parameter = MockParameter;