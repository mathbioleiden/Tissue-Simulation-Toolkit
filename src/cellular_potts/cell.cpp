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
#include <fstream>
#include <list>
#include <stdio.h>
#include <vector>
#ifndef __APPLE__
#include <malloc.h>
#endif
#include "cell.hpp"
#include "dish.hpp"
#include "parameter.hpp"
#include "sticky.hpp"
#include "MovementTracker.hpp"

#define HASHCOLNUM 255

extern Parameter par;

int **Cell::J = 0;
int Cell::amount = 0;
int Cell::capacity = 0;
int Cell::maxsigma = 0;
int Cell::maxtau = 0;

// Cell::Cell(const Dish &who) : Cytoplasm(who);
//  Note: g++ wants to have the body of this constructor in cell.hh
//  body is defined in "ConstructorBody" below
class Dish;

using namespace std;

Cell::~Cell(void) {

  amount--;
  if (amount == 0) {
    // clear J if last cell has been destructed
    free(J[0]);
    free(J);
    capacity = 0;
    maxsigma = 0;
    J = 0;
  }
  delete[] chem;
    delete mov_tracker;
}

void Cell::CellBirth(Cell &mother_cell) {

  colour = mother_cell.colour;
  alive = mother_cell.alive;
  v[0] = mother_cell.v[0];
  v[1] = mother_cell.v[1];

  // Administrate ancestry
  mother_cell.daughter = this->sigma;
  mother = mother_cell.sigma;
  times_divided = ++mother_cell.times_divided;
  owner = mother_cell.owner;

  date_of_birth = owner->Time();

  colour_of_birth = mother_cell.colour;
  colour = mother_cell.colour;

  alive = mother_cell.alive;

  tau = mother_cell.tau;
  target_length = mother_cell.target_length;

  for (int ch = 0; ch < par.n_chem; ch++)
    chem[ch] = mother_cell.chem[ch];

  n_copies = 0;

  grad[0] = mother_cell.grad[0];
  grad[1] = mother_cell.grad[1];
  membrane_pixels = mother_cell.membrane_pixels;

  if (par.cell_division_area_mean >= 0) {
    division_area = generateGaussianNoise(par.cell_division_area_mean, par.cell_division_area_std)*par.target_area;
    // Ensure positive division area
    while (division_area < 0) {
        division_area = generateGaussianNoise(par.cell_division_area_mean, par.cell_division_area_std)*par.target_area;
    }
    mother_cell.division_area = generateGaussianNoise(par.cell_division_area_mean, par.cell_division_area_std)*par.target_area;
    // Ensure positive division area
    while (mother_cell.division_area < 0) {
        mother_cell.division_area = generateGaussianNoise(par.cell_division_area_mean, par.cell_division_area_std)*par.target_area;
    }
  }
}

void Cell::ConstructorBody(int settau) {
  // Note: Constructor of Cytoplasm will be called first
  alive = true;
  colour = 1; // undifferentiated

  colour_of_birth = 1;
  date_of_birth = 0;
  times_divided = 0;
  mother = 0;
  daughter = 0;

  // add new elements to each of the dimensions of "J"

  // amount gives the total number of Cell instantiations (including copies)
  amount++;

  // maxsigma keeps track of the last cell identity number given out to a cell
  sigma = maxsigma++;

  if (!J) {
    ReadStaticJTable(par.Jtable);
  }

  tau = settau;
  area = 0;
  target_area = 0;

  perimeter = 0;
  target_perimeter = 0;

  length = 0;
  target_length = par.target_length;
  sum_x = 0;
  sum_y = 0;
  sum_xx = 0;
  sum_yy = 0;
  sum_xy = 0;
  border = 0;
  sum_sin_x = 0.;
  sum_cos_x = 0.;
  sum_sin_y = 0.;
  sum_cos_y = 0.;
  std::vector<std::array<int, 2>> membrane_pixels = std::vector<std::array<int, 2>>();

  if (par.cell_division_area_mean >= 0) {
    division_area = generateGaussianNoise(par.cell_division_area_mean, par.cell_division_area_std)*par.target_area;
    // Ensure positive division area
    while (division_area < 0) {
      division_area = generateGaussianNoise(par.cell_division_area_mean, par.cell_division_area_std)*par.target_area;
    }
  }

  //  growth_threshold=par.dthres;
  growth_threshold = 0;
  v[0] = 0.;
  v[1] = 0.;
  n_copies = 0;

  chem = new double[par.n_chem];
    mov_tracker = new MovementTracker(par.cell_move_dt);
}

/*! \brief Read a table of static Js.
 First line: number of types (including medium)
 Next lines: diagonal matrix, starting with 1 element (0 0)
 ending with n elements */
void Cell::ReadStaticJTable(std::string const &fname) {
  cerr << "Reading J's...\n";
  ifstream jtab(fname);
  if (!jtab) {
    perror(fname.c_str());
    exit(1);
  }

  int n; // number of taus
  jtab >> n;
  cerr << "Number of celltypes:" << n << endl;
  maxtau = n - 1;

  // Allocate
  if (J) {
    free(J[0]);
    free(J);
  }
  J = (int **)malloc(n * sizeof(int *));
  J[0] = (int *)malloc(n * n * sizeof(int));
  for (int i = 1; i < n; i++) {
    J[i] = J[i - 1] + n;
  }

  capacity = n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i; j++) {
      jtab >> J[i][j];
      // symmetric...
      J[j][i] = J[i][j];
    }
  }
}

void Cell::AddPixelToMembrane(std::array<int, 2> pix) {
    membrane_pixels.push_back(pix);
}

void Cell::RemovePixelFromMembrane(std::array<int, 2> pix) {
    auto it = std::find(membrane_pixels.begin(), membrane_pixels.end(), pix);
    if (it != membrane_pixels.end()) {
        membrane_pixels.erase(it);
    }
}

std::vector<std::array<int,2>>& Cell::GetMembranePixels() {
    return membrane_pixels;
}

void Cell::SetMembranePixels(std::vector<std::array<int, 2>> pixels) {
    membrane_pixels = pixels;
}

int Cell::EnergyDifference(const Cell &cell2) const {
  if (sigma == cell2.sigma)
    return 0;
  return J[tau][cell2.tau];
}

void Cell::ClearJ(void) {
  for (int i = 0; i < capacity * capacity; i++) {
    J[0][i] = EMPTY;
  }
}

int Cell::sizex=0.;
int Cell::sizey=0.;

void Cell::GetCentroid(double *cx, double *cy) {
    const double two_pi = 2.0 * M_PI;
    if (par.periodic_boundaries) {
        double avg_theta_x = std::atan2(sum_sin_x, sum_cos_x);
        if (avg_theta_x < 0) avg_theta_x += two_pi;  // normalize to [0, 2π)
        *cx = (sizex-2) * avg_theta_x / two_pi;
        double avg_theta_y = std::atan2(sum_sin_y, sum_cos_y);
        if (avg_theta_y < 0) avg_theta_y += two_pi;  // normalize to [0, 2π)
        *cy = (sizey-2) * avg_theta_y / two_pi;
    } else { // fast method
        *cx = sum_x / area;
        *cy = sum_y / area;
    }
}
