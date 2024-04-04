#pragma once
#include "vec2.hpp"
#include "grid.hpp"

/**
 * @brief Grow in specified number of cells in the specified rectangle.
 * @param n_cells Number of cells that is grown in.
 * @param cell_size The maximum size the cells have in the beginning.
 * @param upper_left Upper left coordinate of the rectangle.
 * @param lower_right Lower right coordinate of the rectangle.
 * @return Index of the last cell that was inserted.
*/
int GrowInCellsInRectangle(Grid &grid, int n_cells, int cell_size, PixelPos upper_left, PixelPos lower_right);

/**
 * @brief Put rectangular cells in rectangle
 * @param n_cells Number of cells that is grown in.
 * @param cell_size The maximum size the cells have in the beginning.
 * @param upper_left Upper left coordinate of the rectangle.
 * @param lower_right Lower right coordinate of the rectangle.
 * @return Index of the last cell that was inserted.
*/
int PutCellsInRectangle(Grid &grid, int n_cells, int cell_size, PixelPos upper_left, PixelPos lower_right);
  
  
/**
 * @brief Create a wall somewere in the grid.
 * 
 * The function creates a wall at specified positions. 
 * Be sure that there are no cells in a neighbourhood of PixelPos,
 * as this function does not update the edgelist. Meaning that
 * if a wall is added in the neighbourhood of a cell, the MC algorithm
 * will break down.
 *
 * @param pos 
 * @throw std::runtime_error when there is a cell in the neighbourhood pos.
 * @throw std::out_of_range when pos is not within the grid.
*/
void AddWall(Grid &grid, PixelPos pos);

int FillRectangleWithCell(Grid &grid, int spin, PixelPos upper_left, PixelPos lower_right);