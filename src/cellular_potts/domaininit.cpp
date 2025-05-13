#include "domaininit.hpp"
#include "neighbours.hpp"
#include "parameter.hpp"
#include "random.hpp"
#include "grid.hpp"
#include <unordered_map>
#include <vector>
#include <exception>
#include <unordered_set>
#include <random>
#include <algorithm>

extern Parameter par;

namespace {
    /**
     * This class keeps track of the border of a cell. 
     */
    class EdenGrowthHelper {
        std::unordered_map<int, std::unordered_set<PixelPos>> border_pixels;
        Grid &grid;
    
    public:
        EdenGrowthHelper(Grid &g) : grid(g) {}
    
        void add_pixel(int cell_id, const PixelPos &pos) {
            for (const auto &nbr : Neighbours(pos)) {
                if (grid.get(nbr) == 0) {
                    border_pixels[cell_id].insert(pos);
                    return;
                }
            }
        }
    
        void remove_pixel(int cell_id, const PixelPos &pos) {
            border_pixels[cell_id].erase(pos);
        }
    
        PixelPos get_random_border(int cell_id) {
            const auto &borders = border_pixels[cell_id];
            if (borders.empty())
                return {-1, -1};
            auto it = borders.begin();
            std::advance(it, RandomNumber(borders.size()) - 1);
            return *it;
        }
    
        void update_border(int cell_id, const PixelPos &new_pixel) {
            remove_pixel(cell_id, new_pixel);
            for (const auto &nbr : Neighbours(new_pixel)) {
                if (grid.get(nbr) == 0) {
                    border_pixels[cell_id].insert(new_pixel);
                    break;
                }
            }
        }
    
        bool has_border(int cell_id) const {
            return !border_pixels.at(cell_id).empty();
        }
    };
}

// Function doesn't work when there are already cells in the dish.
int GrowInCellsInRectangle(Grid &grid, int init_cells, int cell_size,
                                          PixelPos upper_left,
                                          PixelPos lower_right)
{
    std::unordered_map<int, int> cell_sizes;
    EdenGrowthHelper growth(grid);

    // Put in inital cells, then do Eden Growth
    // Index is also the cell_number.
    int offset_x = upper_left.x;
    int offset_y = upper_left.y;
    for (int i = 1; i <= init_cells; i++)
    {
        auto deltaX = lower_right.x - upper_left.x;
        auto deltaY = lower_right.y - upper_left.y;
        int x = RandomNumber(deltaX) + offset_x - 1;
        int y = RandomNumber(deltaY) + offset_y - 1;

        growth.add_pixel(i, {x,y});
    }

    std::mt19937 rng(par.rseed); 

    bool any_cell_can_grow = true; // If there is a single cell that can grow, we try to grow it
    while (any_cell_can_grow) {
        any_cell_can_grow = false; // Turn it to true if we find a cell that can grow another step.
        for (int c = 1; c <= init_cells; c++) {
            if (cell_sizes[c] >= cell_size) // Cell is big enough
                continue;
            if (!growth.has_border(c)) // No space to grow
                continue; 

            PixelPos from = growth.get_random_border(c);
            if (from.x == -1) { // encodes case that there is no border, should be caught already but just in case
                continue;
            }

            std::vector<PixelPos> nbhs;
            for (auto n : Neighbours(from)) {
                nbhs.push_back(n);
            }
            std::shuffle(nbhs.begin(), nbhs.end(), rng);
            for (const auto &nbh : nbhs) {
                if (nbh.x < upper_left.x || nbh.y < upper_left.y ||
                    nbh.x >= lower_right.x || nbh.y >= lower_right.y)
                    continue;
                if (grid.get(nbh) != 0)
                    continue;
                grid.set(nbh, c);
                cell_sizes[c]++;
                growth.add_pixel(c, nbh);
                growth.update_border(c, from);
                any_cell_can_grow = true;
                break;
            }
            
        }

    }
    return 0;
}

int FillRectangleWithCell(Grid &grid, int spin, PixelPos upper_left, PixelPos lower_right) {
    //std::cout << "Filling " << upper_left << " to " << lower_right << '\n';
    for (int i = upper_left.x; i < lower_right.x; i++) {
        for (int j = upper_left.y; j<lower_right.y; j++) {
            // std::cout << "Putting " << PixelPos(i,j) << ' ';
            grid.set({i,j}, spin);
        }
    }
}

int PutCellsInRectangle(Grid &grid, int n_cells, int cell_size, PixelPos upper_left, PixelPos lower_right) {
    int cell_num = 1; // Find the largest spin already in the grid
    for (int i = 0 ; i < par.sizex; i++)  
    for (int j = 0 ; j < par.sizey; j++)  
        {
            auto spin = grid.get({i,j});
            if (spin == cell_num)
                cell_num++;
        }

    int rect_x = std::abs(lower_right.x - upper_left.x);
    int rect_y = std::abs(lower_right.y - upper_left.y);
    int rectangle_size = std::abs(upper_left.y - lower_right.y) * std::abs(upper_left.x - lower_right.x);

    int size_of_cell_side = 1+static_cast<int>(std::sqrt(cell_size));
    int num_cell_x = rect_x / size_of_cell_side ;
    int num_cell_y = rect_y / size_of_cell_side ;
    
    std::cerr << "size_of_cell_side " << size_of_cell_side << std::endl;
    std::cerr << "num_cell_x " << num_cell_x << std::endl;
    std::cerr << "num_cell_y " << num_cell_y << std::endl;
    std::cerr << "cell_num " << cell_num << std::endl;

    for (int y = upper_left.y; y < lower_right.y; y++) 
        for (int x = upper_left.x; x < lower_right.x; x++){
            int spin = cell_num + (x - upper_left.x) / size_of_cell_side
                       + ((y-upper_left.y) / size_of_cell_side) * num_cell_x;
            std::cerr << "(" << x << ',' << y << ':' << spin << ')';
            if (spin < cell_num + n_cells)  {
                if (x>0 && y> 0 && x< par.sizex-1 && y < par.sizey-1)
                    grid.set({x,y}, spin);
                // std::cout << "Setted cell " << spin << " at " << PixelPos(x,y) << '\n';
            }
        }
}

void AddWall(Grid &grid, PixelPos pos)
{
    if (pos.x < 0 || pos.y < 0 || pos.x > par.sizex || pos.y > par.sizey)
    {
        throw std::out_of_range("AddWall: position is Out of range");
    }

    for (auto const &nbh : Neighbours(pos))
    {
        if (nbh.x < 0 || nbh.y < 0 || nbh.x >= par.sizex || nbh.y >= par.sizey)
            continue;
        std::cerr << "Wall at " << nbh.x << "," << nbh.y << "has value"
                  << grid.get(nbh) << "\n";
        if (grid.get(nbh) > 0 || grid.get(pos) > 0)
            throw std::runtime_error(
                "AddWall: Can't create wall next to (or on) cell.");
    }
    grid.set(pos, -1);
}