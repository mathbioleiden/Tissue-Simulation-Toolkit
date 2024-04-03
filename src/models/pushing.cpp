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
#include "cell.hpp"
#include "dish.hpp"
#include "graph.hpp"
#include "info.hpp"
#include "parameter.hpp"
#include "random.hpp"
#include "sqr.hpp"
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <malloc.h>
#include <math.h>
#include <stdio.h>

using namespace std;

INIT {

  try {

    // Define initial distribution of cells
    CPM->GrowInCells(par.n_init_cells, par.size_init_cells, par.subfield);
    CPM->ConstructInitCells(*this);

    // If we have only one big cell and divide it a few times
    // we start with a nice initial clump of cells.
    //
    // The behavior can be changed in the parameter file using
    // parameters n_init_cells, size_init_cells and divisions
    for (int i = 0; i < par.divisions; i++) {
      CPM->DivideCells(cell);
    }

    // Assign a random type to each of the cells
    CPM->SetRandomTypes();

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

    dish->CPM->AmoebaeMove(dish->PDEfield);

    // cerr << "Done\n";
    if (par.graphics && !(i % par.storage_stride)) {

      int tx, ty;
      BeginScene();
      ClearImage();
      dish->Plot(this);

      // char title[400];
      // snprintf(title,399,"CellularPotts: %d MCS",i);
      // ChangeTitle(title);
      EndScene();
      info->Menu();
    }

    if (par.store && !(i % par.storage_stride)) {
      char fname[200], fname_mcds[200];
      snprintf(fname, 199, "%s/extend%05d.png", par.datadir.c_str(), i);

      BeginScene();

      dish->Plot(this);

      EndScene();

      Write(fname);
    }

    i++;
  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
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
