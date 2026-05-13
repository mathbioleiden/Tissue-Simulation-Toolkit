/*

Copyright 1996-2006 Roeland Merks

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
#include "cell.hpp"
#include "dish.hpp"
#include "graph.hpp"
#include "info.hpp"
#include "inputoutput.hpp"
#include "parameter.hpp"
#include "plotter.hpp"
#include "profiler.hpp"
#include "random.hpp"
#include "sqr.hpp"
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <math.h>
#include <filesystem>
#include <iomanip>
#include <memory>


using namespace std;

// Function to write cell positions; pass all required variables as parameters
void write_cell_positions(int i, Dish* dish, const Parameter& par, const std::string& output_name, int output_per, std::ofstream* cellpos_stream,Info *info) {
  std::string filename = par.datadir + "/" + output_name;
  std::ofstream out;
  out << std::scientific << std::setprecision(6);  // Adjust precision as needed
  if (i == 0) {
    std::cout << "Opening cell position" << std::endl;
    out.open(filename);
    out << "time (MCS),cell id,com_1 (px),com_2 (px),area (px^2),perimeter (px)" << std::endl;

    if (!out) {
      std::cerr << "Failed to open file!" << std::endl;
    }
  } else if (i % output_per == 0) {
    out.open(filename, std::ios::app);
  }
  info->WriteCOMsTorus(out,",");
}

INIT {
  try {
    // Read initial configuration

    io->ReadConfiguration();
    // int cell_size=5;
    // int x_pos;
    // for (int cell_id=1; cell_id<=11;cell_id++){
    //   x_pos = (cell_id-1)*cell_size+50;
    //   CPM->SquareCell(cell_id,x_pos,3,cell_size);
    //   std::cerr << "added cell: " << cell_id << "\n";
    // }

    // Construct the cells
    //CPM->ConstructInitCells(*dish);

    CPM->InitialiseEdgeList();

  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
}

TIMESTEP {
  try {

    static int i = 0;
    static Dish *dish;
    if (i == 0) {
      dish = new Dish();
    }

    if (i == 0){
      dish->SetTargetAreas((int)(par.target_area/2), std::vector<int>{1});
    } else if (i==par.relaxation){
      dish->SetTargetAreas(par.target_area, std::vector<int>{1});
    }


    static Info *info = new Info(*dish, *this);
    static Plotter *plotter = new Plotter(dish, this);
    static ofstream *cellpos_stream = nullptr;
    static IO *io = 0;
    if (io == 0 ) {
        io = new IO(*dish);
    }

    if (par.graphics && !(i % par.storage_stride)) {
      PROFILE(all_plots, plotter->Plot();)
      info->Menu();
      dish->CPM->FindBoundingBox(); // old: Setboundingbox
    }

    if (i == 0 && par.pause_on_start) {
      info->set_Paused();
      i++;
    }

    if (!info->IsPaused()) {
      PROFILE(amoebamove, dish->CPM->AmoebaeMove(dish->PDEfield);)
    }

    if (par.store && !(i % par.storage_stride)) {
      char fname[200], fname_mcds[200];
      snprintf(fname, 199, "%s/snapshot%05d.png", par.datadir.c_str(), i);
      Write(fname);
    }
    // dish->CPM->CalcPeriodicSafeCentroids();
    write_cell_positions(i,dish,par,"tst.csv",1,cellpos_stream,info);

    if (!info->IsPaused()) {
      i++;
    }
  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
  PROFILE_PRINT
}

void Plotter::Plot() {
  graphics->BeginScene();
  graphics->ClearImage();

  plotCPMCellTypes();
  plotCPMLines();

  graphics->EndScene();
}

void PDE::DerivativesPDE(CellularPotts *cpm, PDEFIELD_TYPE *derivs, int x,
                         int y) {}

int PDE::MapColour(double val) {
  return (((int)((val / ((val) + 1.)) * 100)) % 100) + 155;
}

int main(int argc, char *argv[]) {
  extern Parameter par;
  try {
    par.Read(argv[1]);
    Seed(par.rseed);
    start_graphics(argc, argv);
  } catch (const char *error) {
    std::cerr << error << std::endl;
    return 1;
  }
  return 0;
}

