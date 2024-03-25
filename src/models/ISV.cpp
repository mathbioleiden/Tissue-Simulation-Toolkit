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
#include <math.h>

#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <libmuscle/libmuscle.hpp>
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
#include "force_calculation.hpp"
#include "graph.hpp"
#include "info.hpp"
#include "parameter.hpp"
#include "plotter.hpp"
#include "profiler.hpp"
#include "random.hpp"
#include "util/muscle3/settings.hpp"
#include "grid.hpp"
#include "domaininit.hpp"
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
std::unordered_map<PixelPos, double> ACT::getValue(ACT::ActField act_field) {
        return act_field.value_;
}

INIT
{
    try
    {
        Grid grid;
        int wall_height =
            par.sizey - static_cast<int>(0.1 * static_cast<double>(par.sizey));
        if (par.n_init_cells > 1) {
         int sq = (std::sqrt(par.size_init_cells) + 1.0);
         int hsq = static_cast<int>( 0.5 * (std::sqrt(par.size_init_cells) + 1.0));
         PutCellsInRectangle(grid, par.n_init_cells - 1, par.size_init_cells,
                                    {2,par.sizey - sq },
                                    {par.sizex-2, par.sizey-2});
         PutCellsInRectangle(grid, 1, par.size_init_cells,
                                    {par.sizex / 2 - hsq, par.sizey - 2 * sq },
                                    {par.sizex / 2 + hsq, par.sizey - sq});
        }
        else{ 
         int hsq = 0.5 * (std::sqrt(par.size_init_cells) + 1.0);
         PutCellsInRectangle(grid, par.n_init_cells, par.size_init_cells,
                                    {par.sizex / 2 - hsq, 
                                    par.sizey/2 -  hsq}, {par.sizex /2+ hsq, par.sizey/2 + hsq});
        }
//        for (int x = 0; x < par.sizex; x++)
//        {
//            PixelPos pos = {x, wall_height};
//            if (x >=50 && x<=150)
//                continue;
//            AddWall(grid, pos);
//        }
//
//         // Define initial distribution of cells
//         PutCellsInRectangle(grid, par.n_init_cells, par.size_init_cells,
//                                    {1, wall_height+1}, {par.sizex-1, par.sizey-1});
//         // PutCellsInRectangle(grid, par.n_init_cells, par.size_init_cells,
//         //                            {1, wall_height+1}, {par.sizex-1, par.sizey-1});

        CPM->setGrid(grid);
        CPM->ConstructInitCells(*this);


        CPM->InitialiseEdgeList();

        // Set all the PDEs to a steady state solution.
        // PDEfield->InitialisePDEvars(nullptr, nullptr);
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
    cout << par.secr_rate[0] << ", " << par.decay_rate[0] << ", "
         << par.diff_coeff[0] << '\n';
    double diffusion_length = par.decay_rate[0] / par.diff_coeff[0];
    cout << "Diffusion length " << diffusion_length << "\n";
    // for (int y = sizey-1; y >= 0; y--)
    for (int y = 0; y < sizey; y++)
    {
        double value =
            par.secr_rate[0] *
            std::exp(-static_cast<double>(y) * diffusion_length);
        for (int x = 0; x < sizex; x++)
        {
            PDEvars[0][x][y] = value;
        }
    }
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
        if (i == 0)
        {
            // request creation of initial adhesions
            auto adh_zone = adhesion_zone(*(dish->CPM));
            interactions.change_type_in_area.change_area = adh_zone;
            interactions.change_type_in_area.num_particles =
                par.num_initial_adhesions;
            interactions.change_type_in_area.from_type = ParticleType::free;
            interactions.change_type_in_area.to_type = ParticleType::adhesion;
        }
        else
        {
            auto adh_zone = dish->CPM->history.get_positions();
            interactions.change_type_in_area.change_area = adh_zone;
            interactions.change_type_in_area.num_particles = adh_zone.size();
            interactions.change_type_in_area.from_type = ParticleType::free;
            interactions.change_type_in_area.to_type = ParticleType::adhesion;
        }

        auto data_mem = encode_cell_ecm_interactions(interactions);
        instance->send("cell_ecm_interactions_out", Message(i, data_mem.first));

        dish->CPM->ResetCellECMInteractions();

        auto ecm_boundary_state_msg =
            instance->receive("ecm_boundary_state_in");
        auto ecm_boundary_state =
            decode_ecm_boundary_state(ecm_boundary_state_msg.data());

        dish->CPM->SetECMBoundaryState(ecm_boundary_state);

        int tipcell = -1;
        for (int j = 0; j < par.sizey; j++) {
            for (int i = 0; i<par.sizex; i++){
                auto spin = dish->CPM->Sigma(i,j);
                if (spin > 0 && tipcell == -1) {
                    tipcell = spin; 
                    break;
                }
            }
            if (tipcell != -1)
                break;
        }
         for (auto & c: dish->cell) {
             c.SetColour(2);
             c.lambda_act = 0.0;
         }
         if (tipcell > 0) {
            dish->cell[tipcell].lambda_act = par.lambda_Act;
            dish->cell[tipcell].SetColour(3);
            std::cout << "Tip cell = " << tipcell << '\n';
         }
        

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
                     static_cast<std::size_t>(pde->SizeY())},
                    {"layer", "x", "y"}, StorageOrder::first_adjacent);
                Data adh_state = Data::dict();
                for (const auto &awe : dish->CPM->getAdhesions())
                {
                    adh_state[std::to_string(awe.par_id)] =
                        Data::dict("size", awe.size, "tension", awe.tension,
                        "myosin", awe.myosin_force_fraction);
                }
                Data act_state = Data::dict();
                for (const auto &actpixel : ACT::getValue(dish->CPM->getActField()) )
                {
                    std::string name = std::to_string(actpixel.first.x) + "," + std::to_string(actpixel.first.y);
                    act_state[name] = actpixel.second;
                }

                Data state = Data::dict("cpm", cpm_state, "pde", pde_state,
                                        "adh", adh_state, "tipcell", tipcell,
                                        "act_state", act_state);
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

    plotPDEDensity();
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
