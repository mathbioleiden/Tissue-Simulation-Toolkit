#pragma once
#include "vec2.hpp"
#include <vector>

/**
 * @brief Keep track of extensions made by cells during a MCS.
 */
class ExtensionHistory
{
public:
    /**
     * @brief Add a extension to remember. Call this after every copy attempt
     * @param pos The position
     * @param spin The spin of the extension that was made
     */
    void add_extension(PixelPos pos, int spin);

    /**
     * @brief Removes all extensions that might have been retracted during a
     * MCS. Call this after each MCS.
     */
    void validate(int **sigma);
    /**
     * @brief Removes all extensions, call before a MCS.
     */
    void clear();

    /**
     * @brief The total amount of extensions.
     * @return The amount of extensions.
     */
    size_t size();

    /**
     * @brief Return all extensions made by the cells
     * @return A vector with positions of extensions of non-medium cells.
     */
    std::vector<PixelPos> get_positions();

    /**
     * @brief Return all extensions made by the cells excluding cell by tau.
     * @param spins_to_exclude The spins of cells to exclude the extensions
     * from.
     * @return A vector with positions of extensions of non-medium cells.
     */
    std::vector<PixelPos> get_positions(std::vector<int> spins_to_exclude);

private:
    std::vector<std::pair<PixelPos, int>> extensions_;
};
