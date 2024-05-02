#include "domaininit.hpp"
#include "neighbours.hpp"
#include "parameter.hpp"
#include "random.hpp"
#include "grid.hpp"
#include <unordered_map>
#include <vector>
#include <exception>

extern Parameter par;


// Function doesn't work when there are already cells in the dish.
int GrowInCellsInRectangle(Grid &grid, int init_cells, int cell_size,
                                          PixelPos upper_left,
                                          PixelPos lower_right)
{
    std::unordered_map<int, std::vector<PixelPos>> initial_positions;

    // Put in inital cells, then do Eden Growth
    // Index is also the cell_number.
    int offset_x = upper_left.x;
    int offset_y = upper_left.y;
    for (int i = 1; i <= init_cells; i++)
    {
        auto deltaX = lower_right.x - upper_left.x;
        auto deltaY = lower_right.y - upper_left.y;
        std::cerr << "deltaX " << deltaX << "deltaY " << deltaY << "offsetX "
                  << offset_x << "offsetY " << offset_y << "\n";
        int x = RandomNumber(deltaX) + offset_x - 1;
        int y = RandomNumber(deltaY) + offset_y - 1;

        std::cerr << "Initial positions for cell " << i << " = "
                  << PixelPos(x, y) << "\n";
        initial_positions[i] = {{x, y}};
    }

    for (int i = 0; i < cell_size; i++)
    {
        for (int c = 1; c <= init_cells; c++)
        {
            // Get a random position of cell c.
            auto positions = initial_positions[c];
            auto pos = positions[RandomNumber(positions.size()) - 1];

            auto neighbour_iterator = Neighbours(pos).begin();
            for (int k = 1; k < RandomNumber(7); k++)
                neighbour_iterator++;
            auto neighbour_pos = *neighbour_iterator;
            if (neighbour_pos.x < upper_left.x || neighbour_pos.y < upper_left.y ||
                neighbour_pos.x >= lower_right.x || neighbour_pos.y >= lower_right.y)
                continue;

            auto neighbour_spin = grid.get(neighbour_pos);

            // Skip if the neighbour not medium
            if (neighbour_spin != 0)
                continue;

            // Assert that the cell stay simpliy connected.
            // Trying to copy pos into neighbour_pos
            if (not(LocalConnectedness(grid,neighbour_pos, neighbour_spin) &&
                         LocalConnectedness(grid,neighbour_pos, c)))
                 {
                     continue;
                 }
            initial_positions[c].push_back(neighbour_pos);
            grid.set(neighbour_pos, c);
            std::cerr << "\nConsidering: (" << pos << "->" << neighbour_pos
                      << ") ";
        }
    }
    
//    // Now copy the new data to the grid.
//    for (auto const &spinpos : initial_positions)
//    {
//        auto spin = spinpos.first;
//        auto positions = spinpos.second;
////        if (positions.size() < cell_size*0.9)
////          continue;
//        for (auto const &pos : positions)
//        {
//            grid.set(pos, spin);
//        }
//    }
}

int FillRectangleWithCell(Grid &grid, int spin, PixelPos upper_left, PixelPos lower_right) {
    std::cout << "Filling " << upper_left << " to " << lower_right << '\n';
    for (int i = upper_left.x; i < lower_right.x; i++) {
        for (int j = upper_left.y; j<lower_right.y; j++) {
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
                grid.set({x,y}, spin);
                std::cout << "Setted cell " << spin << " at " << PixelPos(x,y) << '\n';
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