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

#include <vector>
#include <stdio.h>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <array>
#include <random>
#include <cstddef>
#include <functional>

#include "pde.hpp"
#include "cell.hpp"
#include "adhesion_mover.hpp"
#include "cell_ecm_interactions.hpp"

using namespace std;

#include "parameter.hpp"
#include <vector>

//#define EMPTY -1
#include <math.h>
double sat2 (double x);
double DeltaH_AreaConstraint(vector<Cell> *cell, int sxy, int sxyp);
double DeltaH_Chemotaxis(int x,int y, int xp, int yp, PDE *PDEfield);
double DeltaH_Contactenergy(int n_nb, int x,int y, int xp, int yp, int** sigma, vector<Cell> *cell, int sxy, int sxyp);
double DeltaH(int n_nb, int x, int y, int xp, int yp, int** sigma, vector<Cell> *cell, PDE *PDEfield);

        