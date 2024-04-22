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

Cell::~Cell(void)
{

    amount--;
    if (amount == 0)
    {
        // clear J if last cell has been destructed
        free(J[0]);
        free(J);
        capacity = 0;
        maxsigma = 0;
        J = 0;
    }
    delete[] chem;
}

void Cell::CellBirth(Cell &mother_cell)
{

    colour = mother_cell.colour;
    alive = mother_cell.alive;
    v[0] = mother_cell.v[0];
    v[1] = mother_cell.v[1];

    // Administrate ancestry
    mother_cell.daughter = this->sigma;
    mother = mother_cell.sigma;
    times_divided = ++mother_cell.times_divided;

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
}

void Cell::ConstructorBody(int settau) {
  // Note: Constructor of Cytoplasm will be called first
  alive = true;
  colour = settau + 1; // undifferentiated

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

    if (!J)
    {
        ReadStaticJTable(par.Jtable);
    }

    tau = settau;
    area = 0;
    target_area = 0;

    perimeter = 0;
    target_perimeter = 0;

    target_length = par.target_length;
    border = 0;

    //  growth_threshold=par.dthres;
    growth_threshold = 0;
    v[0] = 0.;
    v[1] = 0.;
    n_copies = 0;

  chem = new double[par.n_chem];
  
  lambda_act = par.lambda_Act;
  polarity = {0.0, 0.0};
  previous_center_of_mass = {0.0, 0.0};
}

/*! \brief Read a table of static Js.
 First line: number of types (including medium)
 Next lines: diagonal matrix, starting with 1 element (0 0)
 ending with n elements */
void Cell::ReadStaticJTable(std::string const &fname)
{
    cerr << "Reading J's...\n";
    ifstream jtab(fname);
    if (!jtab)
    {
        perror(fname.c_str());
        exit(1);
    }

    int n; // number of taus
    jtab >> n;
    cerr << "Number of celltypes:" << n << endl;
    maxtau = n - 1;

    // Allocate
    if (J)
    {
        free(J[0]);
        free(J);
    }
    J = (int **)malloc(n * sizeof(int *));
    J[0] = (int *)malloc(n * n * sizeof(int));
    for (int i = 1; i < n; i++)
    {
        J[i] = J[i - 1] + n;
    }

    capacity = n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            jtab >> J[i][j];
            // symmetric...
            J[j][i] = J[i][j];
            std::cerr << "J[" << i << "][" << j << "] = " << J[i][j] << '\n';
        }
    }
}

int Cell::EnergyDifference(const Cell &cell2) const
{
    if (sigma == cell2.sigma)
        return 0;
    return J[tau][cell2.tau];
}

void Cell::ClearJ(void)
{
    for (int i = 0; i < capacity * capacity; i++)
    {
        J[0][i] = EMPTY;
    }
}

Vec2<double> Cell::CenterVector() const { return fit_ellipse.center(); }

Vec2<double> Cell::MajorAxisVector() { return fit_ellipse.major_axis(); }

Vec2<double> Cell::MinorAxisVector() { return fit_ellipse.minor_axis(); }

double Cell::MajorAxis() { return Length(); }

double Cell::MinorAxis() { return fit_ellipse.minor(); }