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
#include "morphometry.hpp"
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

    static Dish *beast = new Dish();

    beast->CPM->AmoebaeMove(beast->PDEfield);

    // cerr << "Done\n";
    if (par.graphics && !(i % 10)) {

      int tx, ty;
      BeginScene();
      ClearImage();
      beast->Plot(this);

      // char title[400];
      // snprintf(title,399,"CellularPotts: %d MCS",i);
      // ChangeTitle(title);
      EndScene();
    }

    if (par.store && !(i % par.storage_stride)) {
      char fname[200], fname_mcds[200];
      snprintf(fname, 199, "%s/extend%05d.png", par.datadir.c_str(), i);

      BeginScene();

      beast->Plot(this);

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
