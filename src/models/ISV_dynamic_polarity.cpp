/*

Copyright 1996-2006 Roeland Merks
Copyright 2023 Netherlands eScience Center

This file is part of Tissue Simulation Toolkit.

Tissue Simulation Toolkit is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

Tissue Simulation Toolkit is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tissue Simulation Toolkit; if not, write to the Free
Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
02110-1301 USA

*/

#include <stdio.h>
#ifndef __APPLE__
#include <malloc.h>
#endif
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <libmuscle/libmuscle.hpp>
#include <math.h>
#include <memory>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>
#include <ymmsl/ymmsl.hpp>

#include "adhesion_creation.hpp"
#include "cell.hpp"
#include "cpm_ecm/io.hpp"
#include "dish.hpp"
#include "domaininit.hpp"
#include "force_calculation.hpp"
#include "graph.hpp"
#include "grid.hpp"
#include "info.hpp"
#include "parameter.hpp"
#include "plotter.hpp"
#include "profiler.hpp"
#include "random.hpp"
#include "util/muscle3/settings.hpp"
#include "erlang.hpp"
#include <sstream>

using namespace std;

using libmuscle::Data;
using libmuscle::DataConstRef;
using libmuscle::Instance;
using libmuscle::Message;
using libmuscle::PortsDescription;
using libmuscle::StorageOrder;
using ymmsl::Operator;

extern Parameter par;

std::unique_ptr<Instance> instance;
#include "act.hpp"
std::unordered_map<PixelPos, double> ACT::getValue(ACT::ActField act_field)
{
    return act_field.value_;
}

INIT
{
    try
    {
        Grid grid;
        int wall_height =
            par.sizey - static_cast<int>(0.1 * static_cast<double>(par.sizey));
        if (par.n_init_cells > 1)
        {
            int offset_from_boundary = 1; // >= 1!
            int breedte = 20;
            int lengte = 40;
            int middel = par.sizex / 2;
            FillRectangleWithCell(
                grid, 1,
                {middel-breedte, par.sizey-offset_from_boundary - lengte},
                {middel, par.sizey - offset_from_boundary}
            );
             FillRectangleWithCell(
                 grid, 2,
                 {middel, par.sizey- offset_from_boundary - lengte  - lengte / 2},
                 {middel+breedte, par.sizey - offset_from_boundary - lengte /2}
             );
             FillRectangleWithCell(
                 grid, 3,
                 {middel-breedte, par.sizey-offset_from_boundary - 2*lengte},
                 {middel, par.sizey - offset_from_boundary - lengte}
             );

//            int number_of_ecs = 1; // .number_of_somites - 1;
//            auto ec_area_hq = 15;
//            auto ec_vertical = 15;
//            int spin = 1;
//            for (int i = 1; i<=number_of_ecs; i++) {
//                int x = par.sizex/ 2; // somite_offset_from_boundary + somite_width*i + somite_somite_distance*(i-1) + somite_somite_distance*0.5;
//                for (int j = 0; j < par.n_init_cells; j++){
//                    int x_offset = (-1 + 2* (j % 2) ) * ec_area_hq / 3;
//                    x_offset = 0;
//                    FillRectangleWithCell(grid, spin,
//                        {x - ec_area_hq/2 + x_offset, par.sizey - ec_vertical* (j+1)},
//                        {x + ec_area_hq/2 + x_offset, (int)(par.sizey-1 - ec_vertical*j)}
//                    );
//                    spin++;
//                }
//            }
        }
        else
        {
            int hsq = 0.5 * (std::sqrt(par.size_init_cells) + 1.0);
            PutCellsInRectangle(grid, par.n_init_cells, par.size_init_cells,
                                {par.sizex / 2 - hsq, par.sizey / 2 - hsq},
                                {par.sizex / 2 + hsq, par.sizey / 2 + hsq});
        }

        CPM->setGrid(grid);
        CPM->ConstructInitCells(*this);

        for (int i = 0; i < par.divisions; i++)
            CPM->DivideCells(cell);

        CPM->InitialiseEdgeList();

        for (auto &c : *(CPM->getCellArray()))
        {
            if (c.Sigma() == 0)
                continue;
            if (c.Sigma() == par.n_init_cells)
            {
                double theta = RANDOM() * 2 * 3.1415;
                c.FixPolarity({std::cos(theta), std::sin(theta)});
                // c.FixPolarity({0.0, -1.0});
                c.SetTargetArea(par.target_area);
                c.setTau(3);
                // c.setTau(2);
            }
            else
            {
                c.FixPolarity(false); // remove polarity
                c.setTau(2);
            }
        }

        // Set all the PDEs to a steady state solution.
        PDEfield->InitialisePDEvars(nullptr, nullptr);
    }
    catch (const char *error)
    {
        cerr << "Caught exception\n";
        std::cerr << error << "\n";
        exit(1);
    }
    catch (const std::exception &err)
    {
        std::cerr << err.what() << std::endl;
        exit(1);
    }
}

// Set a fixed gradient for the whole simulation. Say VEGF?
void PDE::InitialisePDEvars(CellularPotts *cpm, int *celltypes)
{
    cout << par.secr_rate[1] << ", " << par.decay_rate[1] << ", "
         << par.diff_coeff[1] << '\n';
    double diffusion_length = par.decay_rate[1] / par.diff_coeff[1];
    cout << "Diffusion length " << diffusion_length << "\n";
    // for (int y = sizey-1; y >= 0; y--)
    for (int y = 0; y < sizey; y++)
    {
        double value = par.secr_rate[1] *
                       std::exp(-static_cast<double>(y) * diffusion_length);
        for (int x = 0; x < sizex; x++)
        {
            // cout << "x,y,value" << x << ',' << y << ',' << value << '\n';
            PDEvars[1][x][y] = value;
            PDEvars[0][x][y] = 0;
        }
    }
     diffusion_length = par.decay_rate[0] / par.diff_coeff[0];
     cout << "Diffusion length " << diffusion_length << "\n";
     for (int x = 0; x < sizex; x++)
     {
         double value_left = par.secr_rate[0] *
                        std::exp(-static_cast<double>(x) * diffusion_length);
         double value_right = par.secr_rate[0] *
                        std::exp(-static_cast<double>(sizex - 1 -x) * diffusion_length);
         for (int y = 0; y < sizey; y++)
         {
         PDEvars[0][x][y] = value_left + value_right;
         }
     }
}

void add_bias_to_act(const std::vector<Vec2<double>> biasdirections,
                     ACT::ActField &act_field, const vector<Cell> &cells,
                     int **sigma)
{
    // Used to compute the max length of every cell
    // i.e. the denominator in Figure 5.2 blz 126 thesis of Daipeng
    std::vector<double> max_length(cells.size());
    std::unordered_map<PixelPos, double> values_to_increase;
    for (int i = 0; i < par.sizex; i++)
    {
        for (int j = 0; j < par.sizey; j++)
        {
            const int spin = sigma[i][j];
            auto biasdirection = biasdirections[spin];
            if (spin <= 0)
                continue;
            const Vec2<double> pixel = {1.0 * i, 1.0 * j};
            const auto center = cells[spin].CenterVector();
            const auto relative_position = pixel - center;
            const auto length = relative_position.length();
            if (length > max_length[spin])
                max_length[spin] = length;

            values_to_increase[{i, j}] = biasdirection.dot(relative_position);
        }
    }

    /*
     * We can delay dividing out the factor max_i=1^n |x_i - x_0|
     * because the innerproduct is a linear operation.
     */
    for (const auto &pixelvalue : values_to_increase)
    {
        const auto pixel = pixelvalue.first;
        const auto scale = max_length[sigma[pixel.x][pixel.y]];
        const auto value = values_to_increase[pixel] / scale;
        if (value > act_field.Value(pixel))
        {
            // act_field.IncreaseValue(pixel, value);
            act_field.SetValue(pixel, value);
        }
    }
}

/**
 * \brief My interpertation of part of eq 5.5 of the thsis of Daipeng blz 127.
 *
 *
 */
void add_vegf_bias_in_act(const Vec2<double> biasdirection,
                          ACT::ActField &act_field, const vector<Cell> &cells,
                          int **sigma)
{
    std::vector<Vec2<double>> biasdirections(cells.size(), biasdirection);
    add_bias_to_act(biasdirections, act_field, cells, sigma);
}

std::vector<PixelPos>
filter_adh_zone(const std::vector<PixelPos> adh_zone_to_filter,
                std::vector<Cell> &cell, int **sigma)
{
    std::vector<PixelPos> adh_zone;
    for (auto pos : adh_zone_to_filter)
    {
        auto spin = sigma[pos.x][pos.y];
        auto c = cell[spin];
        if (!par.only_tipcell_adh || c.getTau() == 3) 
        {
            auto com = c.CenterVector();
            adh_zone.push_back(pos);
        }
    }
    return adh_zone;
}

TIMESTEP
{
    try
    {
        static int i = 0;
        static Dish *dish = new Dish();
        static Info *info = new Info(*dish, *this);
        static Plotter plotter = Plotter(dish, this);

        CellECMInteractions interactions = dish->CPM->GetCellECMInteractions();
        if (i == par.relaxation_time)
        {
            // request creation of initial adhesions
            auto adh_zone = adhesion_zone(*(dish->CPM));
            interactions.change_type_in_area.change_area = adh_zone;
            interactions.change_type_in_area.num_particles =
                par.num_initial_adhesions;
            interactions.change_type_in_area.from_type = ParticleType::free;
            interactions.change_type_in_area.to_type = ParticleType::adhesion;
        }
        else if (i > par.relaxation_time)
        {
            // auto adh_zone = dish->CPM->history.get_positions();
                     auto adh_zone_to_filter =
                     dish->CPM->history.get_positions();
            auto adh_zone = filter_adh_zone(adh_zone_to_filter, dish->cell, dish->CPM->getSigma());
            interactions.change_type_in_area.change_area = adh_zone;
            interactions.change_type_in_area.num_particles = adh_zone.size();
            interactions.change_type_in_area.from_type = ParticleType::free;
            interactions.change_type_in_area.to_type = ParticleType::adhesion;
        }

        if (par.polarity_bias and i == par.cell_polarity_history)
        {
            for (auto &c : *(dish->CPM->getCellArray()))
            {
                c.FixPolarity({0.0, 0.0}); // remove polarity
            }
        }

        auto data_mem = encode_cell_ecm_interactions(interactions);
        instance->send("cell_ecm_interactions_out", Message(i, data_mem.first));

        dish->CPM->ResetCellECMInteractions();

        auto ecm_boundary_state_msg =
            instance->receive("ecm_boundary_state_in");
        auto ecm_boundary_state =
            decode_ecm_boundary_state(ecm_boundary_state_msg.data());
        // std::cout << "Got here 1\n";
        dish->CPM->SetECMBoundaryState(ecm_boundary_state);
        // std::cout << "Got here 2\n";
        if (i>0 and par.division_algo == "time") {
            std::vector<bool> which_cells(dish->cell.size());
            for (auto &cell : dish->cell) {
                if (cell.getTau() == 3 and cell.cell_division_time.can_divide) {
                    double when_to_divide = erlang(par.division_rate_erlang_k, par.division_rate_erlang_lambda);
                        cell.cell_division_time.time_from_division = when_to_divide;
                        cell.cell_division_time.can_divide = false;
                }
                else if (cell.cell_division_time.time_from_division > 0) {
                    cell.cell_division_time.time_from_division--;
                }
                if (cell.cell_division_time.time_from_division == 1) {
                    cell.cell_division_time.can_divide = true;
                    which_cells[cell.Sigma()] = true;
                }
                if (cell.getTau() > 1 and cell.TargetArea() < par.target_area) {
                    cell.IncrementTargetArea();
                }
            }
            dish->CPM->DivideCells(which_cells, dish->cell);
        }
        // Tip cell selection
        int tipcell;
        for (int j = 0; j < par.sizey; j++)
        {
            for (int i = 0; i < par.sizex; i++)
            {
                auto spin = dish->CPM->Sigma(i, j);
                auto thiscell = dish->CPM->getCell(spin);
                if (spin > 0 and thiscell.getTau() > 1) {
                    tipcell = spin;
                    j = par.sizey;
                    i = par.sizex;
                }
            }
        }
         for (auto &c : dish->cell)
         {
            if (c.Sigma()>0) {
             c.setTau(2);
             c.FixPolarity(false); 
            }
         }
         dish->cell[tipcell].setTau(3);
         dish->cell[tipcell].FixPolarity(true); // Turn polarity back on!
         // std::cout << "Tip cell = " << tipcell << '\n';

        PROFILE(amoebamove, dish->CPM->AmoebaeMove(dish->PDEfield);)

        if (par.adhesion_yielding)
            dish->CPM->MoveAdhesions();

        if (instance->is_connected("state_out"))
        {
            if (i % instance->get_setting_as<int64_t>(
                        "state_output_interval") ==
                0)
            {
                std::cerr << "i = " << i << ", sending on state_out"
                          << std::endl;
                auto *cpm_sigma = dish->CPM->getSigma()[0];
                Data cpm_state =
                    Data::grid(cpm_sigma,
                               {static_cast<std::size_t>(dish->CPM->SizeX()),
                                static_cast<std::size_t>(dish->CPM->SizeY())},
                               {"x", "y"}, StorageOrder::last_adjacent);
                auto const &pde = dish->PDEfield;
                auto *pde_sigma = pde->getPDEvars()[0][0];
                Data pde_state = Data::grid(
                    pde_sigma,
                    {static_cast<std::size_t>(pde->Layers()),
                     static_cast<std::size_t>(pde->SizeX()),
                     static_cast<std::size_t>(pde->SizeY())
                     },
                    {"layer", "x", "y"}, StorageOrder::last_adjacent);
                Data adh_state = Data::dict();
                for (const auto &awe : dish->CPM->getAdhesions())
                {
                    adh_state[std::to_string(awe.par_id)] =
                        Data::dict("size", awe.size, "tension", awe.tension,
                                   "myosin", awe.myosin_force_fraction);
                }
                Data act_state = Data::dict();
                for (const auto &actpixel :
                     ACT::getValue(dish->CPM->getActField()))
                {
                    std::string name = std::to_string(actpixel.first.x) + "," +
                                       std::to_string(actpixel.first.y);
                    act_state[name] = actpixel.second;
                }
                Data cellpolarity = Data::dict();
                for (auto c : dish->cell)
                {
                    auto vec = c.CenterVector();
                    cellpolarity[std::to_string(c.Sigma())] =
                        Data::dict("x", vec.x, "y", vec.y);
                }

                Data state =
                    Data::dict("cpm", cpm_state, "pde", pde_state, "adh",
                               adh_state, "tipcell", tipcell, "act_state", act_state);
                instance->send("state_out", Message(i, state));
            }
        }

        if (par.graphics && !(i % par.storage_stride))
        {
            PROFILE(all_plots, plotter.Plot();)
            char title[400];
            snprintf(title, 399, "CellularPotts: %.2f hr",
                     dish->PDEfield->TheTime() / 3600);
            info->Menu();
        }

        i++;
    }
    catch (const char *error)
    {
        cerr << "Caught exception\n";
        std::cerr << error << "\n";
        exit(1);
    }
    catch (std::exception const &e)
    {
        // ensure we crash if there's a problem, Qt swallows exceptions
        std::terminate();
    }
    PROFILE_PRINT
}
void PDE::DerivativesPDE(CellularPotts *cpm, PDEFIELD_TYPE *derivs, int x,
                         int y)
{
}

void PDE::Secrete(CellularPotts *cpm)
{
    const double dt = par.dt;
    for (int x = 0; x < sizex; x++)
    {
        for (int y = 0; y < sizey; y++)
        {
            // inside cells
            if (cpm->Sigma(x, y))
            {
                PDEvars[0][x][y] += par.secr_rate[0] * dt;
            }
            else
            {
                // outside cells
                PDEvars[0][x][y] -= par.decay_rate[0] * dt * PDEvars[0][x][y];
            }
        }
    }
    PROFILE_PRINT
}

int PDE::MapColour(double val)
{
    return (((int)((val / ((val) + 1.)) * 100)) % 100) + 155;
}

void Plotter::Plot()
{
    graphics->BeginScene();
    graphics->ClearImage();

    // plotPDEDensity();
    plotCPMCellTypes();
    plotCPMLines();
    plotPDEContourLines();
    // plotActModel();

    graphics->EndScene();
}

int main(int argc, char *argv[])
{
    PortsDescription ports(
        {{Operator::O_I, {"cell_ecm_interactions_out", "state_out"}},
         {Operator::S, {"ecm_boundary_state_in"}}});
    instance = std::make_unique<Instance>(0, nullptr, ports);

    instance->reuse_instance();
    set_parameters_from_settings(*instance);

    par.Write(std::cout);

    Seed(par.rseed);

    try
    {
        start_graphics(argc, argv);
    }
    catch (const char *error)
    {
        std::cerr << error << std::endl;
        return 1;
    }
    catch (...)
    {
        std::cerr << "An unknown exception was caught" << std::endl;
        return 1;
    }

    // This is a hack, the whole model is really supposed to be inside a while
    // loop guarded by this statement. The architecture here won't allow that
    // and fortunately we don't need to actually run more than once, but
    // the function still needs to be called here for MUSCLE3 to shut down
    // correctly.
    instance->reuse_instance();

    return 0;
}
