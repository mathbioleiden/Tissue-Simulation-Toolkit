/*

Copyright 1995-2006 Roeland Merks, Nick Savill

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


/* CA.cpp: implementation of Glazier & Graner's Cellular Potts Model */

// This code derives from a Cellular Potts implementation written around 1995
// by Nick Savill

#include <cstdio>
#include <math.h>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include "sticky.hpp"
#include "random.hpp"
#include "ca.hpp"
#include "parameter.hpp"
#include "dish.hpp"
#include "sqr.hpp"
#include "crash.hpp"
#include "hull.hpp"
#include <vector>

#include "deltah.hpp"



/* STATIC DATA MEMBER INITIALISATION */
const int nx2[21] = {0, 0, 1, 0,-1, 1, 1,-1,-1, 0, 2, 0, -2, 1, 2, 2, 1,-1,-2,-2,-1 };
const int ny2[21] = {0,-1, 0, 1, 0,-1, 1, 1,-1,-2, 0, 2,  0,-2,-1, 1, 2, 2, 1,-1,-2 };

extern Parameter par;


/** PRIVATE **/

using namespace std;

double DeltaH_AreaConstraint(vector<Cell> *cell, int sxy, int sxyp){
  double DH;
// lambda is determined by chemical 0
  //cerr << "[" << lambda << "]";
  if ( sxyp == MEDIUM ) {
    DH = (double)(par.lambda *  (1. - 2. *   
             (double) ( (*cell)[sxy].Area() - (*cell)[sxy].TargetArea()) ));
  }
  else if ( sxy == MEDIUM ) {
    DH = (double)((par.lambda * (1. + 2. *  
             (double) ( (*cell)[sxyp].Area() - (*cell)[sxyp].TargetArea()) )));
  }
  else
    DH = (double)((par.lambda * (2.+  2.  * (double) 
             (  (*cell)[sxyp].Area() - (*cell)[sxyp].TargetArea()
             - (*cell)[sxy].Area() + (*cell)[sxy].TargetArea() )) ));

return DH;
}

double DeltaH_Chemotaxis(int x,int y, int xp, int yp, PDE *PDEfield){
  double DDH;
  DDH= - (double)(par.chemotaxis*(sat2(PDEfield->get_PDEvars(0,x,y))-sat2(PDEfield->get_PDEvars(0,xp,yp))));
  return DDH;
}

double DeltaH_Contactenergy(int n_nb, int x,int y, int xp, int yp, int** sigma, vector<Cell> *cell, int sxy, int sxyp){
  double DH;
  int i;
  int neighsite;
  DH=0;
  for (i=1;i<=n_nb;i++) {
    int xp2,yp2;
    xp2=x+nx2[i]; yp2=y+ny2[i];
    if (par.periodic_boundaries) {
      // since we are asynchronic, we cannot just copy the borders once 
      // every MCS
      if (xp2<=0)
        xp2=par.sizex-2+xp2;
      if (yp2<=0)
        yp2=par.sizey-2+yp2;
      if (xp2>=par.sizex-1)
        xp2=xp2-par.sizex+2;
      if (yp2>=par.sizey-1)
        yp2=yp2-par.sizey+2;
      neighsite=sigma[xp2][yp2];
    } else {
      if (xp2<=0 || yp2<=0 || xp2>=par.sizex-1 || yp2>=par.sizey-1)
        neighsite=-1;
      else
        neighsite=sigma[xp2][yp2];
    }
    if (neighsite==-1) { 
      // border 
      DH += (sxyp==0?0:par.border_energy) - (sxy==0?0:par.border_energy);
    } else {
      DH += (*cell)[sxyp].EnergyDifference((*cell)[neighsite]) 
            - (*cell)[sxy].EnergyDifference((*cell)[neighsite]);
    }
  }
  return DH;
}

//double DeltaH_LengthConstraint
//double DeltaH_AreaConstraintRescaled





//double DeltaH_
double sat2(double x) {
  return x/(par.saturation*x+1.);
  //return x;

}

double DeltaH(int n_nb, int x,int y, int xp, int yp, int** sigma, vector<Cell> *cell, PDE *PDEfield) {      

  double DH = 0;
  int i, sxy, sxyp;
  int neighsite;

  /* Compute energydifference *IF* the copying were to occur */
  sxy = sigma[x][y];
  sxyp = sigma[xp][yp];
    

  DH += DeltaH_Contactenergy(n_nb, x, y, xp, yp, sigma, cell, sxy, sxyp);

  DH += DeltaH_AreaConstraint(cell, sxy, sxyp);

  if (PDEfield && (par.vecadherinknockout || (sxyp==0 || sxy==0))) {
    // copying from (xp, yp) into (x,y)
    // If par.extensiononly == true, apply CompuCell's method, i.e.
    // only chemotactic extensions contribute to energy change
    if (!( par.extensiononly && sxyp==0)) {
      DH += DeltaH_Chemotaxis(x, y, xp, yp, PDEfield);
    }
  }

  return DH;
}

