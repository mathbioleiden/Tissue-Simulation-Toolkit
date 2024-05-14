/*

Copyright 1996-2006 Roeland Merks, Paulien Hogeweg

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
#include "dish.hpp"
#include "crash.hpp"
#include "info.hpp"
#include "inputoutput.hpp"
#include "parameter.hpp"
#include "pde.hpp"
#include "sticky.hpp"
#include <algorithm>
#include <errno.h>
#include <fstream>
#include <iostream>
#include <list>
#include <math.h>
#include <string.h>
#include <vector>

#include "../lib/json/json.hpp"
using json = nlohmann::json_abi_v3_11_2::json;

#define EXTERNAL_OFF

extern Parameter par;

using namespace std;

Dish::Dish() {
  ConstructorBody();

  if (par.load_mcds) {
    ImportMultiCellDS(par.mcds_input);
  } else {
    // Initial cell distribution is defined by user in INIT {} block
    CPM = new CellularPotts(&cell, par.sizex, par.sizey);
    io = new IO(*this);

    if (par.n_chem)
      PDEfield = new PDE(par.n_chem, par.sizex, par.sizey);
    Init();
    if (par.target_area > 0) {
      for (std::vector<Cell>::iterator c = cell.begin(); c != cell.end(); c++) {
        c->SetTargetArea(par.target_area);
      }
    }
  }
  if (par.target_area > 0)
    for (std::vector<Cell>::iterator c = cell.begin(); c != cell.end(); c++) {
      c->SetTargetArea(par.target_area);
      c->SetTargetPerimeter(par.target_perimeter);
    }

  if (par.ref_adhesive_area > 0)
    for (std::vector<Cell>::iterator c = cell.begin(); c != cell.end(); c++) {
      c->SetReferenceAdhesiveArea(par.ref_adhesive_area);
    }
}

Dish::~Dish() {
  cell.clear();
  delete CPM;
  delete io;
}

void Dish::Plot(Graphics *g) {
  if (sizechange) {
    sizechange = false;
    g->Resize(par.sizex * 2, par.sizey * 2);
  }
  if (CPM)
    CPM->Plot(g);
}

void Dish::ConstructorBody() {
  Cell::maxsigma = 0;

  // Allocate the first "cell": this is the medium (tau=0)
  cell.push_back(Cell(*this, 0));

  // indicate that the first cell is the medium
  cell.front().sigma = 0;
  cell.front().tau = 0;

  CPM = 0;
  PDEfield = 0;
}

bool Dish::CellIsolated(const Cell &c, int **neighbours) const {
  int i;
  for (i = 0; i < (int)cell.size(); i++) {
    if (neighbours[c.sigma][i] == EMPTY)
      break;
    else if (neighbours[c.sigma][i] > 0)
      return false;
  }
  return true;
}

// Based on code by Paulien Hogeweg.
void Dish::CellGrowthAndDivision(void) {
  vector<bool> which_cells(cell.size());

  static int mem_area = 0;

  // if called for the first time: calculate mem_area
  if (!mem_area) {
    mem_area = TargetArea() / CountCells();
  }
  int cell_division = 0;

  vector<Cell>::iterator c;
  for ((c = cell.begin(), c++); c != cell.end(); c++) {

    if ((c->Area() - c->TargetArea()) > c->GrowthThreshold()) {
      c->IncrementTargetArea();
    }

    if ((c->Area() > 2 * mem_area)) {
      which_cells[c->Sigma()] = true;
      cell_division++;
    }
  }
  // Divide scheduled cells
  if (cell_division) {
    CPM->DivideCells(which_cells, cell);
  }
}

int Dish::CountCells(void) const {
  int amount = 0;
  vector<Cell>::const_iterator i;
  for ((i = cell.begin(), i++); i != cell.end(); i++) {
    if (i->AliveP()) {
      amount++;
    } else {
      cerr << "Dead cell\n";
    }
  }
  return amount;
}

int Dish::Area(void) const {
  int total_area = 0;
  vector<Cell>::const_iterator i;
  for ((i = cell.begin(), i++); i != cell.end(); ++i) {
    total_area += i->Area();
  }
  return total_area;
}

int Dish::TargetArea(void) const {
  int total_area = 0;
  vector<Cell>::const_iterator i;
  for ((i = cell.begin(), i++); i != cell.end(); ++i) {
    if (i->AliveP())
      total_area += i->TargetArea();
  }
  return total_area;
}

void Dish::SetCellOwner(Cell &which_cell) { which_cell.owner = this; }

void Dish::ClearGrads(void) {
  vector<Cell>::iterator i;
  for ((i = cell.begin(), i++); i != cell.end(); i++) {
    i->ClearGrad();
  }
}


int Dish::Time(void) const { return CPM->Time(); }

void Dish::MeasureChemConcentrations(void) {
  // clear chemical concentrations
  for (vector<Cell>::iterator c = cell.begin(); c != cell.end(); c++) {
    for (int ch = 0; ch < par.n_chem; ch++)
      c->chem[ch] = 0.;
  }

  // calculate current ones
  for (int ch = 0; ch < par.n_chem; ch++) {
    for (int i = 0; i < SizeX() * SizeY(); i++) {
      int cn = CPM->Sigma(0, i);
      if (cn >= 0)
        cell[cn].chem[ch] += PDEfield->get_PDEvars(ch, 0, i);
    }
  }

  for (vector<Cell>::iterator c = cell.begin(); c != cell.end(); c++) {
    for (int ch = 0; ch < par.n_chem; ch++)
      c->chem[ch] /= (double)c->Area();
  }
}

double round(double v, int n) {
  double ten_pow_n = pow(10, n);
  v *= ten_pow_n;
  return round(v) / ten_pow_n;
}

void Dish::MCDS_import_cell(MCDS_io *mcds, int cell_id) {
}

void Dish::ImportMultiCellDS(std::string const &fname) {
}

void Dish::MCDS_export_cell(MCDS_io *mcds, Cell *cell) {
}

void Dish::ExportMultiCellDS(std::string const &fname) {
}

int Dish::SizeX(void) { return CPM->SizeX(); }
int Dish::SizeY(void) { return CPM->SizeY(); }
