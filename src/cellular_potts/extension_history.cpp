#include "extension_history.hpp"
#include <algorithm>

void ExtensionHistory::add_extension(PixelPos pixel, int spin)
{
    extensions_.push_back({pixel, spin});
}

void ExtensionHistory::validate(int** sigma)
{
    extensions_.erase(
        std::remove_if(
            extensions_.begin(),
            extensions_.end(),
            [sigma](const auto& element) {
                 auto pixel = element.first; 
                 auto spin = element.second;
                 return sigma[pixel.x][pixel.y] != spin; 
            }),
        extensions_.end());
}

std::vector<PixelPos> ExtensionHistory::get_positions() {
    std::vector<PixelPos> output;
    for (auto element : extensions_)
        output.push_back(element.first);
    return output;
}

size_t ExtensionHistory::size() {
    return extensions_.size();
}