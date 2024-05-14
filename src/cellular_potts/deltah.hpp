#pragma once
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

// mainpage.hpp contains no C++ code, it is for the main page of the
// documentation
#include "mainpage.hpp"

#include <array>
#include <cstddef>
#include <functional>
#include <random>
#include <stdio.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "adhesion_mover.hpp"
#include "cell.hpp"
#include "cell_ecm_interactions.hpp"
#include "pde.hpp"

#include "parameter.hpp"
#include <vector>

// #define EMPTY -1
#include <math.h>

struct DeltaH
{
    static double sat2(double x);
    static double area_constraint(std::vector<Cell> *cell, int sxy, int sxyp);
    static double linear_area_constraint(std::vector<Cell> *cell, int sxy, int sxyp);
    static double chemotaxis(int x, int y, int xp, int yp, PDE *PDEfield);
    static double contact_energy(int n_nb, int x, int y, int xp, int yp,
                                 int **sigma, std::vector<Cell> *cell, int sxy,
                                 int sxyp);
    static double length_constraint(int n_nb, int x, int y, int xp, int yp,
                                    int **sigma, std::vector<Cell> *cell, int sxy,
                                    int sxyp);
    static double spreading_constraint(std::vector<Cell> *cell, int sxy, int sxyp);

    static double classical(int n_nb, int x, int y, int xp, int yp, int **sigma,
                            std::vector<Cell> *cell, PDE *PDEfield);
};