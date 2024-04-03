#include "cell_division.hpp"
#include "cell.hpp"
#include "parameter.hpp"
#include <unordered_map>
#include <vector>

extern Parameter par;
namespace
{
    Cell *CreateNewCell(std::vector<Cell> &cells, int mother)
    {
        Cell new_cell;
        new_cell.CellBirth(cells[mother]);
        cells.push_back(new_cell);
        return &cells.back();
    }

    struct CellToDivide
    {
        CellToDivide() : divide_axis(), center(), daughter_spin(){};
        Vec2<double> divide_axis;
        Vec2<double> center;
        int daughter_spin;
    };
}

void DivideCells(std::vector<bool> which_cells, std::vector<Cell> &cells,
                 int **sigma)
{

    std::vector<CellToDivide> division_flags(cells.size());

    for (int i = 0; i < par.sizex; i++)
        for (int j = 0; j < par.sizey; j++)
        {
            auto spin = sigma[i][j];
            if (spin <= 0 || !which_cells[spin])
                continue;

            Cell *daughter = nullptr;
            Cell *mother = &cells[spin];

            if (division_flags[spin].daughter_spin == 0)
            {
                daughter = CreateNewCell(cells, spin);
                mother = &cells[spin];
                division_flags[spin].daughter_spin = daughter->Sigma();
                division_flags[spin].divide_axis = mother->MinorAxisVector();
                division_flags[spin].center = mother->CenterVector();
            }
            else
            {
                int daughter_spin = division_flags[spin].daughter_spin;
                daughter = &cells[daughter_spin];
            }
            // Needs to be put here, CreateNewCell invalidates all pointers
            // because it might resize the cells vector
            mother = &cells[spin];
            auto const &div_flag = division_flags[spin];
            auto relativecoords =
                Vec2<double>(1.0 * i, 1.0 * j) - div_flag.center;

            if (div_flag.divide_axis.y * relativecoords.x -
                    div_flag.divide_axis.x * relativecoords.y >
                0)
            {
                mother->DecrementArea();
                mother->DecrementTargetArea();
                mother->RemoveSiteFromMoments(i, j);
                sigma[i][j] = daughter->Sigma();
                daughter->AddSiteToMoments(i, j);
                daughter->IncrementArea();
                daughter->IncrementTargetArea();
            }
        }
}