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
#include "parameter.hpp"
#include "plotter.hpp"
#include "random.hpp"
#include "sqr.hpp"
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

INIT {

  try {

    // Define initial distribution of cells
    CPM->GrowInCells(par.n_init_cells, par.size_init_cells, par.subfield);
    cerr << "About to RandomSigma\n";
    // CPM->RandomSigma(par.n_init_cells);
    cerr << "About to ConstructInitCells\n";

    CPM->ConstructInitCells(*this);
    CPM->SetRandomTypes();
    CPM->InitialiseEdgeList();
    cerr << "Done init\n";

  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
}

TIMESTEP {
  try {
    static int i = 0;

    static Dish *dish = new Dish();
    static Info *info = new Info(*dish, *this);
    static Plotter *plotter = new Plotter(dish, this);

    dish->CPM->PottsNeighbourMove(dish->PDEfield);
    // dish->CPM->AmoebaeMove(dish->PDEfield);
    if (par.graphics && !(i % par.storage_stride)) {
      // cerr << "Plot " << i << endl;
      plotter->Plot();
      info->Menu();
      // dish->CPM->SetBoundingBox();
    }
    if (par.store && !(i % par.storage_stride)) {
      char fname[200], fname_mcds[200];
      snprintf(fname, 199, "%s/extend%05d.png", par.datadir.c_str(), i);
      plotter->Plot();
      Write(fname);
    }
    i++;
  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
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
