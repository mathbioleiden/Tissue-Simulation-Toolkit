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
    cout << "Initialisation" << endl;
    CPM->ReadZygotePicture();
    // CPM->GrowInCells(par.n_init_cells,par.size_init_cells,par.subfield);
    CPM->ConstructInitCells(*this);
    CPM->MeasureCellPerimeters();
    CPM->AllocateMatrix(*this);
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
    dish->CPM->Act_AmoebaeMove(dish->PDEfield);
    if (par.max_Act && par.lambda_Act) {
      dish->PDEfield->MILayerCA(3, 1., dish->CPM, dish);
      dish->PDEfield->AgeLayer(2, 1., dish->CPM, dish);
    }
    // Writing center of mass and area of each cell
    char buff[400];
    snprintf(buff, sizeof(buff), "%s/cellcenter.txt", par.datadir.c_str());
    std::string buffAsStdStr = buff;
    std::ofstream out(buff, ios::app);
    // info->WriteCOMsTorus(out);
    // plot to screen and file
    if (par.graphics && !(i % par.storage_stride)) {
      plotter->Plot();
      char title[400];
      snprintf(title, 399, "CellularPotts: %d MCS", i);
      info->Menu();
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

void PDE::InitialiseAgeLayer(int l, double value, CellularPotts *cpm) {
  for (int x = 0; x < sizex; x++) {
    for (int y = 0; y < sizey; y++) {
      if (PDEvars[l][x][y] > 0) {
        PDEvars[l][x][y] = value;
      } else {
        PDEvars[l][x][y] = 0.;
      }
    }
  }
}

void PDE::AgeLayer(int l, double value, CellularPotts *cpm, Dish *dish) {
  for (const auto elem : cpm->actPixels) {
    /* ... process elem ... */
    if (elem.second > 0.) {
      cpm->actPixels[elem.first] -= value;
    }
  }
}

void PDE::MILayerCA(int l, double value, CellularPotts *cpm, Dish *dish) {
  for (const auto &elem : cpm->alivePixels) {
    int x = elem[0];
    int y = elem[1];
    int sigma_c = cpm->Sigma(x, y);
    int new_sigma = cpm->matrix[x][y]; // elem.second;
    int k = cpm->matrix[x][y];         // elem.second;
    // add new matrix adhesion at sites with locally high enough Act,
    // first also check current pixel Act, because if lower than
    // 0.075*par.max_Act the geometric mean will never be higher than
    // 0.75*max_Act
    if (cpm->GetMatrixLevel(x, y) == 0) {
      if (cpm->GetActLevel(x, y) > 0.075 * par.max_Act) {
        double Act_neighourhood_product = 1;
        int nxp = 0;
        bool insufficient_act = false;
        for (int i1 = -1; i1 <= 1; i1++) {
          if (insufficient_act == true) {
            break;
          }
          for (int i2 = -1; i2 <= 1; i2++) {
            if (cpm->Sigma(x + i1, y + i2) >= 0 &&
                cpm->Sigma(x + i1, y + i2) == cpm->Sigma(x, y)) {
              double current_act = cpm->GetActLevel(x + i1, y + i2);
              insufficient_act = (current_act < 0.075 * par.max_Act);
              if (insufficient_act == true) {
                break;
              }
              Act_neighourhood_product *= current_act;
              nxp++;
            }
          }
        }
        if (insufficient_act == false) {
          Act_neighourhood_product = pow(Act_neighourhood_product, 1. / nxp);
          double act_p =
              par.spontaneous_p *
              ((Act_neighourhood_product / par.max_Act > 0.75) ? 1 : 0);
          double rand_spon = rand() / double(RAND_MAX);
          if (rand_spon < act_p) {
            new_sigma = 1;
          }
        }
      }
    } else if (k > 0) {
      // Do Eden growth
      //  take a random neighbour
      int xyp = (int)(8 * RANDOM() + 1);
      int xp = nx[xyp] + x;
      int yp = ny[xyp] + y;
      int kp;
      // Check if both sites are part of the same cell
      if (cpm->Sigma(x, y) == cpm->Sigma(xp, yp)) {
        if ((kp = cpm->GetMatrixLevel(xp, yp)) == 0) {
          // Make site part of adhesion complex if next to adhesion complex
          double random_double = rand() / double(RAND_MAX);
          if (random_double < par.eden_p) {
            cpm->matrix[xp][yp] = 1;
            cpm->getCell(sigma_c).IncrementAdhesiveArea(1);
          }
        }
      }
      int young_neighbours = 0;
      for (int i1 = -1; i1 <= 1; i1++) {
        for (int i2 = -1; i2 <= 1; i2++) {
          if (cpm->GetMatrixLevel(x + i1, y + i2) <
              1) { // && cpm->Sigma(x,y)==cpm->Sigma(x+i2,y+i2))
            young_neighbours += 1;
          }
        }
      }
      if (young_neighbours > 0) {
        double rand_double = rand() / double(RAND_MAX);
        if (rand_double <
            par.decay_p * young_neighbours * young_neighbours / 8.0) {
          new_sigma = 0;
        }
      }
    }
    cpm->matrix[x][y] = new_sigma;
    if (new_sigma == 0 && k > 0) {
      cpm->getCell(sigma_c).DecrementAdhesiveArea(k);
    }
    if (new_sigma > 0 && k == 0) {
      cpm->getCell(sigma_c).IncrementAdhesiveArea(new_sigma);
    }
  }
}

void PDE::DerivativesPDE(CellularPotts *cpm, PDEFIELD_TYPE *derivs, int x,
                         int y) {}

int PDE::MapColour(double val) {
  return (((int)((val / ((val) + 1.)) * 100)) % 100) + 155;
}

/*
int PDE::MapColour3(double val, int l) {
        int step=0;
        if (l==2){
        step = (240)/par.max_Act;
  return (int)(256-val*step-1);}
        else if (l==3 && val>1){
        step = (256)/2;
  return (int)(500+val*step);}
        else
        return 0;
}*/

void Plotter::Plot() {
  graphics->BeginScene();
  graphics->ClearImage();
  // plotPDEDensity();

  plotCPMCellTypes();
  dish->PDEfield->PlotInCells(graphics, dish->CPM, 2);
  plotCPMLines();

  graphics->EndScene();
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
