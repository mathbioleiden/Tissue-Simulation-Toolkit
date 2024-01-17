#pragma once
#include "vec2.hpp"
#include <vector>


class ExtensionHistory {
    public:
        void add_extension(PixelPos, int);
        void validate(int**);
        
        size_t size();
        std::vector<PixelPos> get_positions(); 
    private:
        std::vector<std::pair<PixelPos, int>> extensions_;
};








