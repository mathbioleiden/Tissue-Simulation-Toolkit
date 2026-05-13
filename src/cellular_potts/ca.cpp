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

#include <cstdlib>
#include <cstring>
#include <fstream>
#include <math.h>
#include <stdio.h>

#include "ca.hpp"
#include "crash.hpp"
#include "dish.hpp"
#include "graph.hpp"
#include "hull.hpp"
#include "parameter.hpp"
#include "random.hpp"
#include "sqr.hpp"
#include "sticky.hpp"

#define ZYGFILE(Z) <Z.xpm>
#define XPM(Z) Z##_xpm
#define ZYGXPM(Z) XPM(Z)

/* define default zygote */
/* NOTE: ZYGOTE is normally defined in Makefile!!!!!! */
#ifndef ZYGOTE
#define ZYGOTE init
#include "xpm/1.xpm"
#else
#include ZYGFILE(ZYGOTE)
#endif

/* STATIC DATA MEMBER INITIALISATION */
double copyprob[BOLTZMANN];

const int CellularPotts::nx[21] = {0, 0,  1, 0, -1, 1, 1,  -1, -1, 0, 2,
                                   0, -2, 1, 2, 2,  1, -1, -2, -2, -1};
const int CellularPotts::ny[21] = {0, -1, 0,  1,  0, -1, 1, 1, -1, -2, 0,
                                   2, 0,  -2, -1, 1, 2,  2, 1, -1, -2};

const int CellularPotts::nbh_level[4] = {0, 4, 8, 20};
int CellularPotts::shuffleindex[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};

extern Parameter par;

/** PRIVATE **/

using namespace std;
void CellularPotts::BaseInitialisation(vector<Cell> *cells) {
  CopyProb(par.T);
  cell = cells;
  if (par.neighbours >= 1 && par.neighbours <= 4)
    n_nb = nbh_level[par.neighbours];
  else
    throw "Panic in CellularPotts: parameter neighbours invalid (choose "
          "[1-4]).";
}

CellularPotts::CellularPotts(vector<Cell> *cells, const int sx, const int sy)
    : adhesion_mover(*this) {
  sigma = 0;
  frozen = false;
  thetime = 0;
  zygote_area = 0;

  edgelist = nullptr;
  orderedgelist = nullptr;

  BaseInitialisation(cells);
  sizex = sx;
  sizey = sy;

  AllocateSigma(sx, sy);

  // fill borders with special border state
  for (int x = 0; x < sizex; x++) {
    sigma[x][0] = -1;
    sigma[x][sizey - 1] = -1;
  }
  for (int y = 0; y < sizey; y++) {
    sigma[0][y] = -1;
    sigma[sizex - 1][y] = -1;
  }

  if (par.neighbours >= 1 && par.neighbours <= 4)
    n_nb = nbh_level[par.neighbours];
  else
    throw "Panic in CellularPotts: parameter neighbours invalid (choose [1-4])";
}

CellularPotts::CellularPotts(void) : adhesion_mover(*this) {
  sigma = 0;
  sizex = 0;
  sizey = 0;
  frozen = false;
  thetime = 0;
  zygote_area = 0;

  edgelist = nullptr;
  orderedgelist = nullptr;

  CopyProb(par.T);

  // fill borders with special border state
  for (int x = 0; x < sizex; x++) {
    sigma[x][0] = -1;
    sigma[x][sizey - 1] = -1;
  }
  for (int y = 0; y < sizey; y++) {
    sigma[0][y] = -1;
    sigma[sizex - 1][y] = -1;
  }
  if (par.neighbours >= 1 && par.neighbours <= 4)
    n_nb = nbh_level[par.neighbours];
  else
    throw "Panic in CellularPotts: parameter neighbours invalid (choose [1-4])";
}

// destructor (virtual)
CellularPotts::~CellularPotts(void) {
  if (sigma) {
    free(sigma[0]);
    free(sigma);
    sigma = 0;
  }

  if (edgelist) {
    delete edgelist;
  }

  if (orderedgelist) {
    delete orderedgelist;
  }
}

void CellularPotts::AllocateSigma(int sx, int sy) {

  sizex = sx;
  sizey = sy;

  sigma = (int **)malloc(sizex * sizeof(int *));
  if (sigma == NULL)
    MemoryWarning();

  sigma[0] = (int *)malloc(sizex * sizey * sizeof(int));
  if (sigma[0] == NULL)
    MemoryWarning();

  {
    for (int i = 1; i < sizex; i++)
      sigma[i] = sigma[i - 1] + sizey;
  }

  /* Clear CA plane */
  {
    for (int i = 0; i < sizex * sizey; i++)
      sigma[0][i] = 0;
  }
}

void CellularPotts::AllocateMatrix(Dish &beast) {
  // sizex; sizey=sy;

  matrix = (int **)malloc(sizex * sizeof(int *));
  if (matrix == NULL)
    MemoryWarning();

  matrix[0] = (int *)malloc(sizex * sizey * sizeof(int));
  if (matrix[0] == NULL)
    MemoryWarning();

  {
    for (int i = 1; i < sizex; i++)
      matrix[i] = matrix[i - 1] + sizey;
  }

  /* Clear CA plane */
  {
    for (int i = 0; i < sizex * sizey; i++)
      matrix[0][i] = 0;
  }
}

void CellularPotts::InitialiseEdgeList(void) {
  edgelist =
      new int[(par.sizex - 2) * (par.sizey - 2) * nbh_level[par.neighbours]];
  orderedgelist =
      new int[(par.sizex - 2) * (par.sizey - 2) * nbh_level[par.neighbours]];
  sizeedgelist = 0;
  int pixel;
  int neighbour;
  int x, y;
  int xp, yp;
  int c, cp;

  // Initialise both edgelist and orderedgelist to have -1 everywhere
  for (int k = 0;
       k < (par.sizex - 2) * (par.sizey - 2) * nbh_level[par.neighbours]; k++) {
    edgelist[k] = -1;
    orderedgelist[k] = -1;
  }

  for (int k = 0;
       k < (par.sizex - 2) * (par.sizey - 2) * nbh_level[par.neighbours]; k++) {
    // Loop over all edges
    // Outermost loop is over the y-coordinate
    // Middle loop is over the x-coordinate
    // Innermost loop is over the neighbours.

    pixel = k / nbh_level[par.neighbours];
    neighbour = k % nbh_level[par.neighbours] + 1;
    x = pixel % (sizex - 2) + 1;
    y = pixel / (sizex - 2) + 1;
    c = sigma[x][y];
    xp = nx[neighbour] + x;
    yp = ny[neighbour] + y;

    if (par.periodic_boundaries) {
      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xp <= 0)
        xp = sizex - 2 + xp;
      if (yp <= 0)
        yp = sizey - 2 + yp;
      if (xp >= sizex - 1)
        xp = xp - sizex + 2;
      if (yp >= sizey - 1)
        yp = yp - sizey + 2;
      cp = sigma[xp][yp];
    } else if (xp <= 0 || yp <= 0 || xp >= sizex - 1 || yp >= sizey - 1)
      cp = -1;
    else
      cp = sigma[xp][yp];
    if (cp != c && cp != -1) {
      // if a pixel and its neighbour have a different sigma, add a unique
      // interger to edgelist
      edgelist[k] = sizeedgelist;
      // also add a unique integer to the end of orderedgelist, making a
      // bijection between the lists
      orderedgelist[sizeedgelist] = k;
      sizeedgelist++;
    }
  }
}

double sat(double x) {
  return x / (par.saturation * x + 1.);
  // return x;
}

int CellularPotts::FixPeriodic(int CoordP,int SizeCoord){
  if (par.periodic_boundaries) {
    if (CoordP <= 0)
      CoordP = SizeCoord - 2 + CoordP;
    if (CoordP >= SizeCoord - 1)
      CoordP = CoordP - SizeCoord + 2;
  }
  return CoordP;
}

vector<array<int, 3>> CellularPotts::CellPerimeterContact() {
  vector<array<int, 3>> perimeter_contact;
  // perimeter_contact[cell_id][0] = cell_id
  // perimeter_contact[cell_id][1] = perimeter length
  // perimeter_contact[cell_id][2] = contact with medium

  // The method 1 calculates the pixels inside the cells. The method 2 calculates the pixels outside the cells.
  // and method 3 calculates the edges connecting two cells (consistent with other CPMs). 
  int method = 3;

  perimeter_contact.resize(cell->size());
  for (int i = 0; i < cell->size(); i++) {
    perimeter_contact[i] = {static_cast<int>(i), 0, 0};
  }

  // Get membrane data for all cells
  for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); ++c) {
    auto membrane_data = c->GetMembranePixels();
    int cell_id = c->Sigma();

    if (method ==1){
      perimeter_contact[cell_id][1] = membrane_data.size();
      for (auto &pixel_info : membrane_data) {
        for (int n = 1; n <= n_nb; n++) {
            int xn = FixPeriodic(pixel_info[0] + nx[n], sizex);
            int yn = FixPeriodic(pixel_info[1] + ny[n], sizey);
          if (sigma[xn][yn] == 0){
            perimeter_contact[cell_id][2] += 1;
            break; // Count each membrane pixel only once for contact with medium
            }
          }
        }

    } else if (method ==2) {
      std::vector<std::array<int, 2>> outside_pixels;// A vector containing outisde pixels
      for (auto &pixel_info : membrane_data) {
        int x = pixel_info[0];
        int y = pixel_info[1];

        for (int n = 1; n <= n_nb; n++) {
            int xn = FixPeriodic(x + nx[n], sizex);
            int yn = FixPeriodic(y + ny[n], sizey);
          if (sigma[xn][yn] != cell_id){
            outside_pixels.push_back({xn,yn});
          }
        }
      }

      // sorting and making a unique list of outside pixels
      std::sort(outside_pixels.begin(), outside_pixels.end());
      outside_pixels.erase(std::unique(outside_pixels.begin(), outside_pixels.end()), outside_pixels.end());
      perimeter_contact[cell_id][1] = outside_pixels.size();

      for (auto &pixel_info : outside_pixels){
        if (sigma[pixel_info[0]][pixel_info[1]] == 0){
          perimeter_contact[cell_id][2] += 1;
        }
      }

    } else if (method ==3) {
      for (auto &pixel_info : membrane_data) {
        for (int n = 1; n <= n_nb; n++) {
            int xn = FixPeriodic(pixel_info[0] + nx[n], sizex);
            int yn = FixPeriodic(pixel_info[1] + ny[n], sizey);

          // If pixel does not belong to the same cell
          if (sigma[xn][yn] != cell_id){
            perimeter_contact[cell_id][1] += 1;

            // If pixel belongs to medium
            if (sigma[xn][yn] == 0){
              perimeter_contact[cell_id][2] += 1;
            }
          }
        }
      }
    }
  }
  return perimeter_contact;
}

int CellularPotts::IsingDeltaH(int x, int y, PDE *PDEfield) {
  int DH = 0, H_before = 0, H_after = 0;
  int i, sxy;
  int neigh_sxy;
  int J = par.lambda;

  /* Compute energydifference *IF* the flip were to occur */
  sxy = sigma[x][y];

  /* DH due to spin alignment */
#ifdef DBG_KAWASAKI
  std::cerr << "[ x = {" << x << ", " << y << "}, xp = {" << xp << ", " << yp
            << "}, ";
#endif
  for (i = 1; i <= n_nb; i++) {
    int xn, yn;
    xn = x + nx[i];
    yn = y + ny[i];

    if (par.periodic_boundaries) {

      // since we are asynchronic, we cannot just copy the borders once
      // every MCS

      if (xn <= 0)
        xn = sizex - 2 + xn;
      if (yn <= 0)
        yn = sizey - 2 + yn;
      if (xn >= sizex - 1)
        xn = xn - sizex + 2;
      if (yn >= sizey - 1)
        yn = yn - sizey + 2;

      neigh_sxy = sigma[xn][yn];

    }      // periodic boundaries
    else { // closed boundaries

      if (xn <= 0 || yn <= 0 || xn >= sizex - 1 || yn >= sizey - 1)
        neigh_sxy = -1;
      else
        neigh_sxy = sigma[xn][yn];
    }

    if (neigh_sxy == -1) { // border
      cerr << "Only periodic boundaries implemented for Kawasaki dynamics "
              "sofar.\n";
      exit(1);
      //  DH += (sxyp==0?0:par.border_energy)-
      //  (sxy==0?0:par.border_energy);
    } else {
      H_before += -J * (sxy == 0 ? -1 : 1) * (neigh_sxy == 0 ? -1 : 1);
      H_after += -J * (sxy == 0 ? 1 : -1) * (neigh_sxy == 0 ? -1 : 1);
    }
  }

  DH = H_after - H_before;

  return DH;
}

int CellularPotts::PottsDeltaH(int x, int y, int new_state) {
  int DH = 0, H_before = 0, H_after = 0;
  int i, sxy;
  int neigh_sxy;
  int J = par.lambda;

  /* Compute energydifference *IF* the flip were to occur */
  sxy = sigma[x][y];

  /* DH due to spin alignment */

  for (i = 1; i <= n_nb; i++) {
    int xn, yn;
    xn = x + nx[i];
    yn = y + ny[i];

    if (par.periodic_boundaries) {

      // since we are asynchronic, we cannot just copy the borders once
      // every MCS

      if (xn <= 0)
        xn = sizex - 2 + xn;
      if (yn <= 0)
        yn = sizey - 2 + yn;
      if (xn >= sizex - 1)
        xn = xn - sizex + 2;
      if (yn >= sizey - 1)
        yn = yn - sizey + 2;

      neigh_sxy = sigma[xn][yn];

    }      // periodic boundaries
    else { // closed boundaries

      if (xn <= 0 || yn <= 0 || xn >= sizex - 1 || yn >= sizey - 1)
        neigh_sxy = -1;
      else
        neigh_sxy = sigma[xn][yn];
    }

    if (neigh_sxy == -1) { // border
      cerr
          << "Only periodic boundaries implemented for Potts dynamics sofar.\n";
      exit(1);
      //  DH += (sxyp==0?0:par.border_energy)-
      //  (sxy==0?0:par.border_energy);
    } else {
      /*
      H_before += -J*(sxy==0?-1:1)*(neigh_sxy==0?-1:1);
      H_after += -J*(sxy==0?1:-1)*(neigh_sxy==0?-1:1);*/
      H_before += J * ((sxy != neigh_sxy) ? 1 : 0);
      H_after += J * ((new_state != neigh_sxy) ? 1 : 0);
    }
  }
  DH = H_after - H_before;
  return DH;
}

int CellularPotts::KawasakiDeltaH(int x, int y, int xp, int yp, PDE *PDEfield) {
  int DH = 0, H_before = 0, H_after = 0;
  int i, sxy, sxyp;
  int neigh_sxy, neigh_sxyp;

  /* Compute energydifference *IF* the copying were to occur */
  sxy = sigma[x][y];
  sxyp = sigma[xp][yp];

  /* DH due to cell adhesion */
#ifdef DBG_KAWASAKI
  std::cerr << "[ x = {" << x << ", " << y << "}, xp = {" << xp << ", " << yp
            << "}, ";
#endif
  for (i = 1; i <= n_nb; i++) {
    int xn, yn;
    xn = x + nx[i];
    yn = y + ny[i];

    int xpn, ypn;
    xpn = xp + nx[i];
    ypn = yp + ny[i];

    if (par.periodic_boundaries) {

      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xn <= 0)
        xn = sizex - 2 + xn;
      if (yn <= 0)
        yn = sizey - 2 + yn;
      if (xn >= sizex - 1)
        xn = xn - sizex + 2;
      if (yn >= sizey - 1)
        yn = yn - sizey + 2;

      neigh_sxy = sigma[xn][yn];

      if (xpn <= 0)
        xpn = sizex - 2 + xpn;
      if (ypn <= 0)
        ypn = sizey - 2 + ypn;
      if (xpn >= sizex - 1)
        xpn = xpn - sizex + 2;
      if (ypn >= sizey - 1)
        ypn = ypn - sizey + 2;

      neigh_sxyp = sigma[xpn][ypn];

    }      // periodic boundaries
    else { // closed boundaries

      if (xn <= 0 || yn <= 0 || xn >= sizex - 1 || yn >= sizey - 1)
        neigh_sxy = -1;
      else
        neigh_sxy = sigma[xn][yn];

      if (xpn <= 0 || ypn <= 0 || xpn >= sizex - 1 || ypn >= sizey - 1)
        neigh_sxyp = -1;
      else
        neigh_sxyp = sigma[xpn][ypn];
    }

    if (neigh_sxy == -1) { // border
      cerr << "Only periodic boundaries implemented for Kawasaki dynamics "
              "sofar.\n";
      exit(1);
      //  DH += (sxyp==0?0:par.border_energy)-
      //  (sxy==0?0:par.border_energy);
    } else {
      H_before += (*cell)[sxy].EnergyDifference((*cell)[neigh_sxy]) +
                  (*cell)[sxyp].EnergyDifference((*cell)[neigh_sxyp]);
      int aft = (*cell)[sxyp].EnergyDifference((*cell)[neigh_sxy]) +
                (*cell)[sxy].EnergyDifference((*cell)[neigh_sxyp]);
#ifdef DBG_KAWASAKI
      cerr << aft << ", ";
#endif
      H_after += aft;
    }
  }
  H_after += 2 * (*cell)[sxy].EnergyDifference((*cell)[sxyp]);
#ifdef DBG_KAWASAKI
  cerr << H_after << ", " << H_before << " ]";
#endif
  DH = H_after - H_before;
  // the rest we will do later - in any case no volume constraint :-)
  return DH;
}

int CellularPotts::DeltaH(int x, int y, int xp, int yp, PDE *PDEfield,
                          AdhesionDisplacements *adh_disp) {
  int DH = 0;
  int i, sxy, sxyp;
  int neighsite;

  /* Compute energydifference *IF* the copying were to occur */
  sxy = sigma[x][y];
  sxyp = sigma[xp][yp];

  /* DH due to cell adhesion */
  for (i = 1; i <= n_nb; i++) {
    int xp2, yp2;
    xp2 = x + nx[i];
    yp2 = y + ny[i];
    if (par.periodic_boundaries) {
      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xp2 <= 0)
        xp2 = sizex - 2 + xp2;
      if (yp2 <= 0)
        yp2 = sizey - 2 + yp2;
      if (xp2 >= sizex - 1)
        xp2 = xp2 - sizex + 2;
      if (yp2 >= sizey - 1)
        yp2 = yp2 - sizey + 2;
      neighsite = sigma[xp2][yp2];
    } else {
      if (xp2 <= 0 || yp2 <= 0 || xp2 >= sizex - 1 || yp2 >= sizey - 1)
        neighsite = -1;
      else
        neighsite = sigma[xp2][yp2];
    }
    if (neighsite == -1) {
      // border
      DH += (sxyp == 0 ? 0 : par.border_energy) -
            (sxy == 0 ? 0 : par.border_energy);
    } else {
      DH += (*cell)[sxyp].EnergyDifference((*cell)[neighsite]) -
            (*cell)[sxy].EnergyDifference((*cell)[neighsite]);
    }
  }
  // lambda is determined by chemical 0
  // cerr << "[" << lambda << "]";
  if (sxyp == MEDIUM) {
    DH += (int)(par.lambda * (1. - 2. * (double)((*cell)[sxy].Area() -
                                                 (*cell)[sxy].TargetArea())));
  } else if (sxy == MEDIUM) {
    DH +=
        (int)((par.lambda * (1. + 2. * (double)((*cell)[sxyp].Area() -
                                                (*cell)[sxyp].TargetArea()))));
  } else
    DH += (int)((
        par.lambda *
        (2. + 2. * (double)((*cell)[sxyp].Area() - (*cell)[sxyp].TargetArea() -
                            (*cell)[sxy].Area() + (*cell)[sxy].TargetArea()))));
    
    //! Perimeter constraint, only available when par.area_constraint_type==0, ??? - RM -???
       //! in other words,
       // when the target area constraint is in place
       int DH_perimeter = 0;
       if (par.lambda_perimeter>0)
       {
           // cerr << "Applying perimeter constraint...: ";
           if (sxyp == MEDIUM)
           {
               DH_perimeter -= par.lambda_perimeter *
               (DSQR((*cell)[sxy].Perimeter() -
                     (*cell)[sxy].TargetPerimeter()) -
                DSQR(GetNewPerimeterIfXYWereRemoved(sxy, x, y) -
                     (*cell)[sxy].TargetPerimeter()));
           }
           else if (sxy == MEDIUM)
           {
               
               DH_perimeter -= par.lambda_perimeter *
               (DSQR((*cell)[sxyp].Perimeter() -
                     (*cell)[sxyp].TargetPerimeter()) -
                DSQR(GetNewPerimeterIfXYWereAdded(sxyp, x, y) -
                     (*cell)[sxyp].TargetPerimeter()));
           }
           // they're both cells
           else
           {
               
               DH_perimeter -= par.lambda_perimeter *
               ((DSQR((*cell)[sxyp].Perimeter() -
                      (*cell)[sxyp].TargetPerimeter()) -
                 DSQR(GetNewPerimeterIfXYWereAdded(sxyp, x, y) -
                      (*cell)[sxyp].TargetPerimeter())));
               
               DH_perimeter -= par.lambda_perimeter *
               (DSQR((*cell)[sxy].Perimeter() -
                     (*cell)[sxy].TargetPerimeter()) -
                DSQR(GetNewPerimeterIfXYWereRemoved(sxy, x, y) -
                     (*cell)[sxy].TargetPerimeter()));
           }
       }
    DH += DH_perimeter;

  /* Chemotaxis */
  if (PDEfield && (par.vecadherinknockout || (sxyp == 0 || sxy == 0))) {
    // copying from (xp, yp) into (x,y)
    // If par.extensiononly == true, apply CompuCell's method, i.e.
    // only chemotactic extensions contribute to energy change
    if (!(par.extensiononly && sxyp == 0)) {
      int DDH = (int)(par.chemotaxis * (sat(PDEfield->get_PDEvars(0, x, y)) -
                                        sat(PDEfield->get_PDEvars(0, xp, yp))));
      DH -= DDH;
    }
  }

  /* Individual adhesions with ECM */
  if (par.adhesions_enabled) {
    if (adh_disp) {
      double adh_dh = adhesion_mover.move_dh({xp, yp}, {x, y}, *adh_disp);
      DH += static_cast<int>(round(adh_dh));
    } else {
      throw std::runtime_error(
          "Adhesions are enabled but not adh_disp argument was passed to"
          " CellularPotts::DeltaH()");
    }
  }

  const double lambda2 = par.lambda2;
  /* Length constraint */
  // sp is expanding cell, s is retracting cell
  if (sxyp == MEDIUM) {
    DH -= (int)(lambda2 *
                (DSQR((*cell)[sxy].Length() - (*cell)[sxy].TargetLength()) -
                 DSQR((*cell)[sxy].GetNewLengthIfXYWereRemoved(x, y) -
                      (*cell)[sxy].TargetLength())));
  } else if (sxy == MEDIUM) {
    DH -= (int)(lambda2 *
                (DSQR((*cell)[sxyp].Length() - (*cell)[sxyp].TargetLength()) -
                 DSQR((*cell)[sxyp].GetNewLengthIfXYWereAdded(x, y) -
                      (*cell)[sxyp].TargetLength())));
  } else {
    DH -= (int)(lambda2 *
                ((DSQR((*cell)[sxyp].Length() - (*cell)[sxyp].TargetLength()) -
                  DSQR((*cell)[sxyp].GetNewLengthIfXYWereAdded(x, y) -
                       (*cell)[sxyp].TargetLength())) +
                 (DSQR((*cell)[sxy].Length() - (*cell)[sxy].TargetLength()) -
                  DSQR((*cell)[sxy].GetNewLengthIfXYWereRemoved(x, y) -
                       (*cell)[sxy].TargetLength()))));
  }
  // Done in AmoebaeMove as we need 'real' neighbors for periodic boundaries:
    //double dh_move;
    //if (par.lambda_move>0) dh_move = VectorMoveDeltaH(x,y,xp,yp);
    //fprintf(stderr, "dh_move = %lf\n", dh_move);
    
    //DH -= dh_move;
  return DH;
}

double CellularPotts::VectorMoveDeltaH(int x, int y, int xp, int yp) {
    
    double vec_move[2] = {0.,0.};
    vec_move[0]=(double)x-(double)xp;
    vec_move[1]=(double)y-(double)yp;

    // average
    int sxy=sigma[x][y];
    int sxyp=sigma[xp][yp];
    
    //cerr << "cells: " << sxy << ", " << sxyp << endl;
    double cv[2]={0.,0.};
    // extension-retraction
   /* if (sxy && sxyp) {
        cv[0]=((*cell)[sxy].v[0]+(*cell)[sxyp].v[0])/2.;
        cv[1]=((*cell)[sxy].v[1]+(*cell)[sxyp].v[1])/2.;
    } else {
        if (sxy) {
            cv[0]=(*cell)[sxy].v[0];
            cv[1]=(*cell)[sxy].v[1];
        } else {
            if (sxyp) {
                cv[0]=(*cell)[sxyp].v[0];
                cv[1]=(*cell)[sxyp].v[1];
            } else {
                return 0.;
            }
        }
    }*/
    
    // extension only
    if (sxyp) {
        cv[0]=(*cell)[sxyp].v[0];
        cv[1]=(*cell)[sxyp].v[1];
    } else {
        if (sxy) {
            return 0.;
        }
    }
    
    
    //cerr << "cv = " << cv[0] << ", "  << cv[1] << endl;
    double dotproduct = cv[0] * vec_move[0] + cv[1] * vec_move[1];
    
    return par.lambda_move * dotproduct;
    
}

int CellularPotts::Act_AmoebaeMove(PDE *PDEfield) {
  int loop, p;
  thetime++;
  int SumDH = 0;
  if (frozen)
    return 0;
  loop = (sizex - 2) * (sizey - 2);
  for (int i = 0; i < loop; i++) {
    // take a random site
    int xy = (int)(RANDOM() * (sizex - 2) * (sizey - 2));
    int x = xy % (sizex - 2) + 1;
    int y = xy / (sizex - 2) + 1;
    // take a random neighbour
    int xyp = (int)(n_nb * RANDOM() + 1);
    int xp = nx[xyp] + x;
    int yp = ny[xyp] + y;
    int k = sigma[x][y];
    int kp;
    if (par.periodic_boundaries) {
      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xp <= 0)
        xp = sizex - 2 + xp;
      if (yp <= 0)
        yp = sizey - 2 + yp;
      if (xp >= sizex - 1)
        xp = xp - sizex + 2;
      if (yp >= sizey - 1)
        yp = yp - sizey + 2;
      kp = sigma[xp][yp];
    } else {
      if (xp <= 0 || yp <= 0 || xp >= sizex - 1 || yp >= sizey - 1) {
        kp = -1;
      } else {
        kp = sigma[xp][yp];
      }
    }
    // test for border state (relevant only if we do not use
    // periodic boundaries)
    if (kp != -1) {
      // Don't even think of copying the special border state into you!
      if (k >= 0 && k != kp) {
        if (par.cluster_connectivity == false ||
            ConnectivityPreservedPCluster(x, y)) {
          /* Try to copy if sites do not belong to the same cell */
          // connectivity dissipation:
          int H_diss = 0;
          if (!ConnectivityPreservedP(x, y))
            H_diss = par.conn_diss;
          int D_H = Act_DeltaH(x, y, xp, yp, PDEfield);
          if ((p = CopyvProb(D_H, H_diss, false)) > 0) {
            ConvertSpin(x, y, xp, yp);
            SumDH += D_H;
            if (par.lambda_Act > 0) {
              // Update actin field
              if (sigma[x][y] > 0) {
                actPixels[{x, y}] = par.max_Act;
                std::unordered_set<std::array<int, 2>>::const_iterator it =
                    (alivePixels.find({x, y}));
                if (it == alivePixels.end()) {
                  alivePixels.insert({x, y});
                }
              } else {
                std::unordered_set<std::array<int, 2>>::const_iterator it =
                    (alivePixels.find({x, y}));
                if (it != alivePixels.end()) {
                  alivePixels.erase({x, y});
                }
                std::unordered_map<std::array<int, 2>, int>::const_iterator ap =
                    (actPixels.find({x, y}));
                if (ap != actPixels.end()) {
                  actPixels.erase({x, y});
                }
              }
            }
            // Update adhesive areas
            if (kp == 0) {
              getCell(k).DecrementAdhesiveArea(GetMatrixLevel(x, y));
            } else if (k == 0) {
              // getCell(kp).IncrementAdhesiveArea(1);
            } else {
              getCell(k).DecrementAdhesiveArea(GetMatrixLevel(x, y));
              // getCell(kp).IncrementAdhesiveArea(1);
            }
            if (par.lambda_matrix > 0) {
              // Update matrix interaction field
              if (sigma[x][y] > 0) {
                // matrixPixels[{x,y}]=0;
                matrix[x][y] = 0;
              } else {
                // matrixPixels.erase({x,y});
                matrix[x][y] = 0;
              }
            }
          }
        }
      }
    }
  }
  return SumDH;
}

int CellularPotts::Act_DeltaH(int x, int y, int xp, int yp, PDE *PDEfield) {
  int DH = 0;
  int i, sxy, sxyp;
  int neighsite;

  /* Compute energydifference *IF* the copying were to occur */
  int DH_adhesive_energy = 0;
  sxy = sigma[x][y];
  sxyp = sigma[xp][yp];
  if (sxyp <= -1) {
    sxyp = 0;
  } // allow for medium to copy in from box border or pillars

  /* DH due to cell adhesion */
  // also compute changes in neighbours for alignment with newneighbours
  std::vector<int> xy_neighbour_changes(cell->size(), 0);
  std::vector<int> xyp_neighbour_changes(cell->size(), 0);
  for (i = 1; i <= n_nb; i++) {
    int xp2, yp2;
    xp2 = x + nx[i];
    yp2 = y + ny[i];
    if (par.periodic_boundaries) {

      // since we are asynchronic, we cannot just copy the borders once
      // every MCS

      if (xp2 <= 0)
        xp2 = sizex - 2 + xp2;
      if (yp2 <= 0)
        yp2 = sizey - 2 + yp2;
      if (xp2 >= sizex - 1)
        xp2 = xp2 - sizex + 2;
      if (yp2 >= sizey - 1)
        yp2 = yp2 - sizey + 2;

      neighsite = sigma[xp2][yp2];

    } else {

      if (xp2 <= 0 || yp2 <= 0 || xp2 >= sizex - 1 || yp2 >= sizey - 1)
        neighsite = -1;
      else
        neighsite = sigma[xp2][yp2];
    }
    if (neighsite == -1) { // border
      DH_adhesive_energy += (sxyp == 0 ? 0 : par.border_energy) -
                            (sxy == 0 ? 0 : par.border_energy);
    } else {
      DH_adhesive_energy += (*cell)[sxyp].EnergyDifference((*cell)[neighsite]) -
                            (*cell)[sxy].EnergyDifference((*cell)[neighsite]);
      if ((i <= 4) | par.extended_neighbour_border) {
        if (neighsite != sxy)
          xy_neighbour_changes[neighsite] -= 1;
        if (neighsite != sxyp)
          xyp_neighbour_changes[neighsite] += 1;
      }
    }
  }

  DH += DH_adhesive_energy;

  // lambda is determined by chemical 0
  int DH_area = 0;
  if (par.area_constraint_type == 0) {
    // cerr << "[" << lambda << "]";
    if (sxyp == MEDIUM) {
      DH_area +=
          (int)(par.lambda * (1. - 2. * (double)((*cell)[sxy].Area() -
                                                 (*cell)[sxy].TargetArea())));
    } else if (sxy == MEDIUM) {
      DH_area += (int)((par.lambda *
                        (1. + 2. * (double)((*cell)[sxyp].Area() -
                                            (*cell)[sxyp].TargetArea()))));
    } else
      DH_area +=
          (int)(par.lambda * (2. + 2. * (double)((*cell)[sxyp].Area() -
                                                 (*cell)[sxyp].TargetArea() -
                                                 (*cell)[sxy].Area() +
                                                 (*cell)[sxy].TargetArea())));
  }

  DH += DH_area;

  //! Perimeter constraint, only available when par.area_constraint_type==0, in
  //! other words,
  // when the target area constraint is in place
  int DH_perimeter = 0;
  if (par.area_constraint_type == 0) {
    if (sxyp == MEDIUM) {

      DH_perimeter -=
          par.lambda_perimeter *
          (DSQR((*cell)[sxy].Perimeter() - (*cell)[sxy].TargetPerimeter()) -
           DSQR(GetNewPerimeterIfXYWereRemoved(sxy, x, y) -
                (*cell)[sxy].TargetPerimeter()));

    } else if (sxy == MEDIUM) {

      DH_perimeter -=
          par.lambda_perimeter *
          (DSQR((*cell)[sxyp].Perimeter() - (*cell)[sxyp].TargetPerimeter()) -
           DSQR(GetNewPerimeterIfXYWereAdded(sxyp, x, y) -
                (*cell)[sxyp].TargetPerimeter()));

    }
    // they're both cells
    else {

      DH_perimeter -=
          par.lambda_perimeter *
          ((DSQR((*cell)[sxyp].Perimeter() - (*cell)[sxyp].TargetPerimeter()) -
            DSQR(GetNewPerimeterIfXYWereAdded(sxyp, x, y) -
                 (*cell)[sxyp].TargetPerimeter())));

      DH_perimeter -=
          par.lambda_perimeter *
          (DSQR((*cell)[sxy].Perimeter() - (*cell)[sxy].TargetPerimeter()) -
           DSQR(GetNewPerimeterIfXYWereRemoved(sxy, x, y) -
                (*cell)[sxy].TargetPerimeter()));
    }
  }
  DH += DH_perimeter;
  /* Chemotaxis */
  int DDH = 0;
  if (PDEfield && (par.vecadherinknockout || (sxyp == 0 || sxy == 0))) {

    // copying from (xp, yp) into (x,y)
    // If par.extensiononly == true, apply CompuCell's method, i.e.
    // only chemotactic extensions contribute to energy change
    if (!(par.extensiononly && sxyp == 0)) {
      DDH = (int)(par.chemotaxis * (sat(PDEfield->get_PDEvars(0, x, y)) -
                                    sat(PDEfield->get_PDEvars(0, xp, yp))));

      DH -= DDH;
    }
  }

  const double lambda2 = par.lambda2;

  /* Length constraint */
  // sp is expanding cell, s is retracting cell

  int DH_length = 0;
  if (sxyp == MEDIUM) {
    DH_length -=
        (int)(lambda2 *
              (DSQR((*cell)[sxy].Length() - (*cell)[sxy].TargetLength()) -
               DSQR((*cell)[sxy].GetNewLengthIfXYWereRemoved(x, y) -
                    (*cell)[sxy].TargetLength())));

  } else if (sxy == MEDIUM) {
    DH_length -=
        (int)(lambda2 *
              (DSQR((*cell)[sxyp].Length() - (*cell)[sxyp].TargetLength()) -
               DSQR((*cell)[sxyp].GetNewLengthIfXYWereAdded(x, y) -
                    (*cell)[sxyp].TargetLength())));

  } else {
    DH_length -=
        (int)(lambda2 *
              ((DSQR((*cell)[sxyp].Length() - (*cell)[sxyp].TargetLength()) -
                DSQR((*cell)[sxyp].GetNewLengthIfXYWereAdded(x, y) -
                     (*cell)[sxyp].TargetLength())) +
               (DSQR((*cell)[sxy].Length() - (*cell)[sxy].TargetLength()) -
                DSQR((*cell)[sxy].GetNewLengthIfXYWereRemoved(x, y) -
                     (*cell)[sxy].TargetLength()))));
  }
  DH += DH_length;

  /************************The Act model****************/
  // let the cell extend with
  int DH_act = 0;
  if (par.lambda_Act) {
    double Act_expanding = 1, Act_retracting = 1;
    int nxp = 0, nret = 0;

    for (int i1 = -1; i1 <= 1; i1++)
      for (int i2 = -1; i2 <= 1; i2++) {

        if (sigma[xp + i1][yp + i2] >= 0 &&
            sigma[xp + i1][yp + i2] == sigma[xp][yp]) {
          Act_expanding *= GetActLevel(xp + i1, yp + i2);
          nxp++;
        }

        if (sigma[x + i1][y + i2] >= 0 &&
            sigma[x + i1][y + i2] == sigma[x][y]) {
          Act_retracting *= GetActLevel(x + i1, y + i2);
          nret++;
        }
      }

    // apply the smoothing
    // Act_expanding*= pow( PDEfield->get_PDEvars(2,xp,yp), w-1);
    // Act_retracting*= pow(PDEfield->get_PDEvars(2,x,y), w-1);
    // nxp += w-1;
    // nret += w-1;

    Act_expanding = pow(Act_expanding, 1. / nxp);
    Act_retracting = pow(Act_retracting, 1. / nret);

    // Act model activation dependent on total adhesion area of the cell
    // If adhesion area exceeds threshold, Act model is fully functional,
    // otherwise, it starts at base*lambda_Act and for increasing adhesion areas
    // it increases linearly to lambda_Act.
    double threshold = par.threshold;
    double base = par.start_level;
    double strength;
    if ((*cell)[sxyp].sigma > 0) {
      double adhesion_fraction =
          (double)(*cell)[sxyp].GetAdhesiveArea() / (double)(*cell)[sxyp].area;
      if (adhesion_fraction >= threshold) {
        strength = 1;
      } else {
        strength = base + ((1 - base) / threshold) * adhesion_fraction;
      }
      DH_act -= (par.lambda_Act * strength) / par.max_Act * Act_expanding;
    }

    if ((*cell)[sxy].sigma > 0) {
      double adhesion_fraction =
          (double)(*cell)[sxy].GetAdhesiveArea() / (double)(*cell)[sxy].area;
      if (adhesion_fraction >= threshold) {
        strength = 1;
      } else {
        strength = base + ((1 - base) / threshold) * adhesion_fraction;
      }
      DH_act += (par.lambda_Act * strength) / par.max_Act * Act_retracting;
    }
  }
  DH += DH_act;

  /****** Matrix interaction retraction yield energy ****/
  // Retractiong of lattice sites that contain an adhesion is penalized with
  // lambda_matrix
  int DH_matrix_interaction = 0;
  if (sxyp == MEDIUM &&
      par.lambda_matrix) { // should be done for all retractions, I assume.
    DH_matrix_interaction += par.lambda_matrix * (GetMatrixLevel(x, y));
  }
  DH += DH_matrix_interaction;
  // std::cout << "DH_matrix: " << DH_matrix_interaction << std::endl;
  return DH;
}

void CellularPotts::ConvertSpin(int x, int y, int xp, int yp) {
  int tmpcell;
  if ((tmpcell = sigma[x][y])) { // if tmpcell is not MEDIUM
    (*cell)[tmpcell].DecrementArea();
    (*cell)[tmpcell].RemoveSiteFromMoments(x, y);
    (*cell)[tmpcell].SetPerimeter(
        GetNewPerimeterIfXYWereRemoved(tmpcell, x, y));
    RemoveMembranePixel(tmpcell,std::array<int, 2> {x, y});
    if (!(*cell)[tmpcell].Area()) {
      (*cell)[tmpcell].Apoptose();
    }
  }

  if ((tmpcell = sigma[xp][yp])) { // if tmpcell is not MEDIUM
    (*cell)[tmpcell].IncrementArea();
    (*cell)[tmpcell].AddSiteToMoments(x, y);
    (*cell)[tmpcell].SetPerimeter(GetNewPerimeterIfXYWereAdded(tmpcell, x, y));
    AddMembranePixel(tmpcell,std::array<int, 2> {x, y});
  }
  sigma[x][y] = sigma[xp][yp];
}

void CellularPotts::ExchangeSpin(int x, int y, int xp, int yp) {
  int tmpcell;
  if ((tmpcell = sigma[x][y])) { // if tmpcell is not MEDIUM
    //(*cell)[tmpcell].DecrementArea();
    (*cell)[tmpcell].RemoveSiteFromMoments(x, y);
  }

  if ((tmpcell = sigma[xp][yp])) { // if tmpcell is not MEDIUM
    //(*cell)[tmpcell].DecrementArea();
    (*cell)[tmpcell].RemoveSiteFromMoments(x, y);
  }

  if ((tmpcell = sigma[x][y])) { // if tmpcell is not MEDIUM
    //(*cell)[tmpcell].IncrementArea();
    (*cell)[tmpcell].AddSiteToMoments(x, y);
  }

  if ((tmpcell = sigma[xp][yp])) { // if tmpcell is not MEDIUM
    //(*cell)[tmpcell].IncrementArea();
    (*cell)[tmpcell].AddSiteToMoments(x, y);
  }

  // Exchange spins
  tmpcell = sigma[x][y];
  sigma[x][y] = sigma[xp][yp];
  sigma[xp][yp] = tmpcell;
}

/** PUBLIC **/
int CellularPotts::CopyvProb(int DH, double stiff, bool anneal) {
  double dd;
  int s;
  s = (int)stiff;
  if (DH <= -s)
    return 2;
  if (anneal)
    return 0;
  // if DH becomes extremely large, calculate probability on-the-fly
  if (DH + s > BOLTZMANN - 1)
    dd = exp(-((double)(DH + s) / par.T));
  else
    dd = copyprob[DH + s];

  if (RANDOM() < dd)
    return 1;
  else
    return 0;
}

void CellularPotts::CopyProb(double T) {
  int i;
  for (i = 0; i < BOLTZMANN; i++)
    copyprob[i] = exp(-((double)(i) / T));
}

void CellularPotts::FreezeAmoebae(void) {
  if (frozen)
    frozen = FALSE;
  else
    frozen = TRUE;
}

//! Monte Carlo Step. Returns summed energy change
int CellularPotts::AmoebaeMove(PDE *PDEfield, bool anneal) {
  int p;
  float loop;
  thetime++;
  int SumDH = 0;

  int positionedge;
  int targetedge;
  int targetsite;
  int targetneighbour;
  int x, y;
  int xp, yp;

  int H_diss;
  int D_H;

  int edgeadjusting;
  int xn, yn; // neighbour cells

  if (frozen)
    return 0;

  loop = static_cast<float>(sizeedgelist) / static_cast<float>(n_nb);
  for (int i = 0; i < loop; i++) {
    // take a random entry of the edgelist
    positionedge = (int)(RANDOM() * sizeedgelist);
    // find the corresponding edge
    targetedge = orderedgelist[positionedge];
    // find the lattice site corresponding to this edge
    targetsite = targetedge / n_nb;
    // find the neighbour corresponding to this edge
    targetneighbour = (targetedge % n_nb) + 1;

    // find the x and y coordinate corresponding to the target site
    x = targetsite % (sizex - 2) + 1;
    y = targetsite / (sizex - 2) + 1;

    // find the neighbouring site corresponding to this edge
    xp = nx[targetneighbour] + x;
    yp = ny[targetneighbour] + y;

    // keep track of 'real' neighboring site, before corrections due to periodic boundaries
    int xpr=xp, ypr=yp;

    if (par.periodic_boundaries) {
      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xp <= 0)
        xp = sizex - 2 + xp;
      if (yp <= 0)
        yp = sizey - 2 + yp;
      if (xp >= sizex - 1)
        xp = xp - sizex + 2;
      if (yp >= sizey - 1)
        yp = yp - sizey + 2;
    }

    // connectivity dissipation:
    H_diss = 0;
    if (!ConnectivityPreservedP(x, y))
      H_diss = par.conn_diss;

    AdhesionDisplacements adh_disp;
    D_H = DeltaH(x, y, xp, yp, PDEfield, &adh_disp) - VectorMoveDeltaH(x, y, xpr,ypr);

    if ((p = CopyvProb(D_H, H_diss, anneal)) > 0) {
      if (par.adhesions_enabled)
        adhesion_mover.commit_move({xp, yp}, {x, y}, adh_disp);
      ConvertSpin(x, y, xp,
                  yp); // sigma(x,y) will get the same value as sigma(xp,yp)
      for (int j = 1; j <= n_nb; j++) {
        xn = nx[j] + x;
        yn = ny[j] + y;
        edgeadjusting = targetsite * n_nb + j - 1;

        if (par.periodic_boundaries) {
          // since we are asynchronic, we cannot just copy the borders once
          // every MCS
          if (xn <= 0)
            xn = sizex - 2 + xn;
          if (yn <= 0)
            yn = sizey - 2 + yn;
          if (xn >= sizex - 1)
            xn = xn - sizex + 2;
          if (yn >= sizey - 1)
            yn = yn - sizey + 2;
        }
        if (xn > 0 && yn > 0 && xn < sizex - 1 &&
            yn < sizey - 1) { // if the neighbour site is within the lattice
          if (edgelist[edgeadjusting] == -1 && sigma[xn][yn] != sigma[x][y]) {
            // if there should be an edge between (x,y) and (xn,yn) and it is
            // not there yet, add it
            AddEdgeToEdgelist(edgeadjusting);
            // adjust loop because two edges were removeed
            loop += 2.0 / n_nb;
          }
          if (edgelist[edgeadjusting] != -1 && sigma[xn][yn] == sigma[x][y]) {
            // if there should be no edge between (x,y) and (xn,yn), but there
            // is an edge remove it
            RemoveEdgeFromEdgelist(edgeadjusting);
            // adjust loop because two edges were removed
            loop -= 2.0 / n_nb;
          }
        }
      }
      SumDH += D_H;
    }
  }
  return SumDH;
}

void CellularPotts::AddEdgeToEdgelist(
    int edge) { // add an edge to the end of edgelist
  int counteredge = CounterEdge(edge);

  // assign a unique integer to position 'edge' in the edgelist
  edgelist[edge] = sizeedgelist;
  // assign a unique integer at the end of orderedgelist, maintaining the
  // bijection between the lists
  orderedgelist[sizeedgelist] = edge;
  // Increase the size of the array
  sizeedgelist++;

  // Repeat for the counteredge
  edgelist[counteredge] = sizeedgelist;
  orderedgelist[sizeedgelist] = counteredge;
  sizeedgelist++;
}

void CellularPotts::RemoveEdgeFromEdgelist(
    int edge) { // remove an edge from the edgelist
  int counteredge = CounterEdge(edge);

  if (edgelist[edge] !=
      sizeedgelist - 1) { // if edge is not the last edge in orderedgelist
    // move the edge in the last position to the position of the edge that must
    // be deleted
    orderedgelist[edgelist[edge]] = orderedgelist[sizeedgelist - 1];
    edgelist[orderedgelist[sizeedgelist - 1]] = edgelist[edge];
  }
  // remove the edge from the edgelist
  edgelist[edge] = -1;
  // free the last position of orderedgelist
  orderedgelist[sizeedgelist - 1] = -1;
  // decrease the size of the edgelist
  sizeedgelist--;

  // Repeat for counteredge
  if (edgelist[counteredge] != sizeedgelist - 1) {
    orderedgelist[edgelist[counteredge]] = orderedgelist[sizeedgelist - 1];
    edgelist[orderedgelist[sizeedgelist - 1]] = edgelist[counteredge];
  }
  edgelist[counteredge] = -1;
  orderedgelist[sizeedgelist - 1] = -1;
  sizeedgelist--;
}

int CellularPotts::CounterEdge(int edge) {
  // For an edge from (x,y) to (xn,yn), this function returns the edge from
  // (xn,yn) to (x,y)

  // find the corresponding lattice site and neighbour for the edge.
  int which_site = edge / n_nb;
  int which_neighbour = edge % n_nb + 1;
  int counterneighbour = 0;

  // find the x and y coordinate corresponding to the lattice site
  int x = which_site % (sizex - 2) + 1;
  int y = which_site / (sizex - 2) + 1;

  // find the x and y coordinate corresponding at the other end of the edge
  int xp = nx[which_neighbour] + x;
  int yp = ny[which_neighbour] + y;

  // correct for periodic boundaries of necessary
  if (par.periodic_boundaries) {
    // since we are asynchronic, we cannot just copy the borders once
    // every MCS
    if (xp <= 0)
      xp = sizex - 2 + xp;
    if (yp <= 0)
      yp = sizey - 2 + yp;
    if (xp >= sizex - 1)
      xp = xp - sizex + 2;
    if (yp >= sizey - 1)
      yp = yp - sizey + 2;
  }
  // lattice site corresponding to other site of the edge
  int neighbourlocation = xp - 1 + (yp - 1) * (par.sizex - 2);

  // find the neighbour pointing the other direction
  const int counterneighbourlist[20] = {3, 4,  1,  2,  7,  8,  5,  6,  11, 12,
                                        9, 10, 17, 18, 19, 20, 13, 14, 15, 16};
  counterneighbour = counterneighbourlist[which_neighbour - 1];
  // compute the final counteredge
  int counteredge = neighbourlocation * n_nb + counterneighbour - 1;
  return counteredge;
}

//! Monte Carlo Step. Returns summed energy change
int CellularPotts::KawasakiMove(PDE *PDEfield) {
  int loop, p;
  // int updated=0;
  thetime++;
  int SumDH = 0;

  if (frozen)
    return 0;

  loop = (sizex - 2) * (sizey - 2);
  for (int i = 0; i < loop; i++) {
    // take a random site
    int xy = (int)(RANDOM() * (sizex - 2) * (sizey - 2));
    int x = xy % (sizex - 2) + 1;
    int y = xy / (sizex - 2) + 1;

    // take a random neighbour
    int xyp = (int)(n_nb * RANDOM() + 1);
    int xp = nx[xyp] + x;
    int yp = ny[xyp] + y;

    int k = sigma[x][y];

    int kp;
    if (par.periodic_boundaries) {
      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xp <= 0)
        xp = sizex - 2 + xp;
      if (yp <= 0)
        yp = sizey - 2 + yp;
      if (xp >= sizex - 1)
        xp = xp - sizex + 2;
      if (yp >= sizey - 1)
        yp = yp - sizey + 2;
      kp = sigma[xp][yp];
    } else {
      if (xp <= 0 || yp <= 0 || xp >= sizex - 1 || yp >= sizey - 1)
        kp = -1;
      else
        kp = sigma[xp][yp];
    }
    // test for border state (relevant only if we do not use
    // periodic boundaries)
    if (kp != -1) {
      // Don't even think of copying the special border state into you!
      if (k != kp) {
        /* Try to exchange sites if sites do not belong to the same cell */
        // connectivity dissipation:
        int H_diss = 0;
        // if (!ConnectivityPreservedP(x,y)) H_diss=par.conn_diss;
        int D_H = KawasakiDeltaH(x, y, xp, yp, PDEfield);
        if (D_H != 0 && (p = CopyvProb(D_H, H_diss, false)) > 0) {
          ExchangeSpin(x, y, xp, yp);
          SumDH += D_H;
        }
        // std::cerr << "[ " << D_H << ", p = " << p << " ]";
      }
    }
  }
  return SumDH;
}

//! Monte Carlo Step. Returns summed energy change
int CellularPotts::IsingMove(PDE *PDEfield) {
  int loop, p;
  // int updated=0;
  thetime++;
  int SumDH = 0;

  loop = (sizex - 2) * (sizey - 2);

  for (int i = 0; i < loop; i++) {

    // take a random site
    int xy = (int)(RANDOM() * (sizex - 2) * (sizey - 2));
    int x = xy % (sizex - 2) + 1;
    int y = xy / (sizex - 2) + 1;

    int D_H = IsingDeltaH(x, y, PDEfield);

    if (D_H != 0 && (p = CopyvProb(D_H, 0, false) > 0)) {

      sigma[x][y] = sigma[x][y] == 0 ? 1 : 0;
      SumDH += D_H;
    }
    // std::cerr << "[ " << D_H << ", p = " << p << " ]";
  }

  return SumDH;
}

//! Monte Carlo Step. Returns summed energy change
int CellularPotts::PottsMove(PDE *PDEfield) {
  int loop, p;
  // int updated=0;
  thetime++;
  int SumDH = 0;
  loop = (sizex - 2) * (sizey - 2);

  for (int i = 0; i < loop; i++) {
    // take a random site
    int xy = (int)(RANDOM() * (sizex - 2) * (sizey - 2));
    int x = xy % (sizex - 2) + 1;
    int y = xy / (sizex - 2) + 1;

    int new_state = (int)(RANDOM() * par.n_init_cells);
    int D_H = PottsDeltaH(x, y, new_state);
    // cerr << "D_H = " << D_H << endl;
    if (D_H < 0 || (p = CopyvProb(D_H, 0, false) > 0)) {
      sigma[x][y] = new_state;
      // cerr << "[ " << x << ", " << y << "]";
      SumDH += D_H;
    }
    // std::cerr << "[ " << D_H << ", p = " << p << " ]";
  }
  return SumDH;
}

//! Monte Carlo Step. Returns summed energy change
int CellularPotts::PottsNeighbourMove(PDE *PDEfield) {
  int loop, p;
  // int updated=0;
  thetime++;
  int SumDH = 0;

  loop = (sizex - 2) * (sizey - 2);

  for (int i = 0; i < loop; i++) {
    // take a random site
    int xy = (int)(RANDOM() * (sizex - 2) * (sizey - 2));
    int x = xy % (sizex - 2) + 1;
    int y = xy / (sizex - 2) + 1;
    // take a random neighbour
    int xyp = (int)(n_nb * RANDOM() + 1);
    int xp = nx[xyp] + x;
    int yp = ny[xyp] + y;

    int kp;
    if (par.periodic_boundaries) {

      // since we are asynchronic, we cannot just copy the borders once
      // every MCS
      if (xp <= 0)
        xp = sizex - 2 + xp;
      if (yp <= 0)
        yp = sizey - 2 + yp;
      if (xp >= sizex - 1)
        xp = xp - sizex + 2;
      if (yp >= sizey - 1)
        yp = yp - sizey + 2;

      kp = sigma[xp][yp];

    } else {
      if (xp <= 0 || yp <= 0 || xp >= sizex - 1 || yp >= sizey - 1)
        kp = -1;
      else
        kp = sigma[xp][yp];
    }

    int D_H = PottsDeltaH(x, y, kp);
    // cerr << "D_H = " << D_H << endl;
    if (D_H < 0 || (p = CopyvProb(D_H, 0, false) > 0)) {
      sigma[x][y] = kp;
      // cerr << "[ " << x << ", " << y << "]";
      SumDH += D_H;
    }
    // std::cerr << "[ " << D_H << ", p = " << p << " ]";
  }
  return SumDH;
}

CellECMInteractions CellularPotts::GetCellECMInteractions() const {
  return adhesion_mover.get_cell_ecm_interactions();
}

void CellularPotts::ResetCellECMInteractions() {
  return adhesion_mover.reset_cell_ecm_interactions();
}

void CellularPotts::SetECMBoundaryState(
    ECMBoundaryState const &ecm_boundary_state) {
  return adhesion_mover.update(ecm_boundary_state);
}

/** A simple method to plot all sigma's in window
    without the black lines */
void CellularPotts::PlotSigma(Graphics *g, int mag) {
  for (int x = 1; x < sizex - 1; x++)
    for (int y = 1; y < sizey - 1; y++) {
      for (int xm = 0; xm < mag; xm++)
        for (int ym = 0; ym < mag; ym++)
          g->Point(sigma[x][y], mag * x + xm, mag * y + ym);
    }
}

/** Plot in black & white for the Ising model **/
void CellularPotts::PlotIsing(Graphics *g, int mag) {
  for (int x = 1; x < sizex - 1; x++)
    for (int y = 1; y < sizey - 1; y++) {
      for (int xm = 0; xm < mag; xm++)
        for (int ym = 0; ym < mag; ym++)
          g->Point(sigma[x][y] == 0 ? 0 : 1, mag * x + xm, mag * y + ym);
    }
}

int CellularPotts::CountNeighours(int sig){
  vector<int> neighbour_sigmas;
  auto membrane_pixels = (*cell)[sig].GetMembranePixels();
  int xn, yn, neigh_sig;
  for (const auto& pixel : membrane_pixels){
    for (int i=0; i<n_nb; i++){
      xn = FixPeriodic(nx[i] + pixel[0], sizex);
      yn = FixPeriodic(ny[i] + pixel[1], sizey);
      neigh_sig = sigma[xn][yn];
      if (neigh_sig != sig && neigh_sig != 0 && std::find(neighbour_sigmas.begin(), neighbour_sigmas.end(), neigh_sig) == neighbour_sigmas.end()){
        neighbour_sigmas.push_back(neigh_sig);
      }
    }
  }
  return neighbour_sigmas.size();
}

int **CellularPotts::SearchNandPlot(Graphics *g, bool get_neighbours) {
  int i, j, q;
  int **neighbours = 0;

  /* Allocate neighbour matrix */
  if (get_neighbours) {
    neighbours = (int **)malloc((cell->size() + 1) * sizeof(int *));
    if (neighbours == NULL)
      MemoryWarning();

    neighbours[0] =
        (int *)malloc((cell->size() + 1) * (cell->size() + 1) * sizeof(int));
    if (neighbours[0] == NULL)
      MemoryWarning();

    for (i = 1; i < (int)cell->size() + 1; i++)
      neighbours[i] = neighbours[i - 1] + (cell->size() + 1);

    /* Clear this matrix */
    for (i = 0; i < ((int)cell->size() + 1) * ((int)cell->size() + 1); i++)
      neighbours[0][i] = EMPTY;
  }

  for (i = 0; i < sizex - 1; i++)
    for (j = 0; j < sizey - 1; j++) {
      int colour;
      if (sigma[i][j] <= 0) {
        colour = 0;
      } else {
        colour = (*cell)[sigma[i][j]].Colour();
        // colour = sigma[i][j];
      }

      if (g && sigma[i][j] > 0) /* if draw */
        g->Point(colour, i, j);

      if (sigma[i][j] != sigma[i + 1][j]) /* if cellborder */ /* etc. etc. */
      {
        if (g)
          g->Point(1, i + 1, j);
        if (get_neighbours) {
          if (sigma[i][j] > 0) {
            for (q = 0; q < (int)cell->size(); q++)
              if (neighbours[sigma[i][j]][q] == EMPTY) {
                neighbours[sigma[i][j]][q] = sigma[i + 1][j];
                break;
              } else if (neighbours[sigma[i][j]][q] == sigma[i + 1][j])
                break;
          }
          if (sigma[i + 1][j] > 0) {
            for (q = 0; q < (int)cell->size(); q++)
              if (neighbours[sigma[i + 1][j]][q] == EMPTY) {
                neighbours[sigma[i + 1][j]][q] = sigma[i][j];
                break;
              } else if (neighbours[sigma[i + 1][j]][q] == sigma[i][j])
                break;
          }
        }
      } else if (g && sigma[i][j] > 0)
        g->Point(colour, i + 1, j);

      if (sigma[i][j] != sigma[i][j + 1]) {

        if (g)
          g->Point(1, i, j + 1);

        if (get_neighbours) {
          if (sigma[i][j] > 0) {
            for (q = 0; q < (int)cell->size(); q++)
              if (neighbours[sigma[i][j]][q] == EMPTY) {
                neighbours[sigma[i][j]][q] = sigma[i][j + 1];
                break;
              } else if (neighbours[sigma[i][j]][q] == sigma[i][j + 1])
                break;
          }

          if (sigma[i][j + 1] > 0) {

            for (q = 0; q < (int)cell->size(); q++)
              if (neighbours[sigma[i][j + 1]][q] == EMPTY) {
                neighbours[sigma[i][j + 1]][q] = sigma[i][j];
                break;
              } else if (neighbours[sigma[i][j + 1]][q] == sigma[i][j])
                break;
          }
        }
      } else if (g && sigma[i][j] > 0)
        g->Point(colour, i, j + 1);

      /* Cells that touch eachother's corners are NO neighbours */

      if (sigma[i][j] != sigma[i + 1][j + 1] ||
          sigma[i + 1][j] != sigma[i][j + 1]) {
        if (g)
          g->Point(1, i + 1, j + 1);
      } else if (g && sigma[i][j] > 0)
        g->Point(colour, i + 1, j + 1);
    }

  if (get_neighbours)
    return neighbours;
  else
    return 0;
}

void CellularPotts::SearchNandPlotClear(Graphics *g) {
  for (int i = 0; i < sizex - 1; i++) {
    for (int j = 0; j < sizey - 1; j++) {
      /* if cellborder */ /* etc. etc. */
      if (sigma[i][j] != sigma[i + 1][j]) {
        if (g)
          g->Point(1, i + 1, j);
      }
      if (sigma[i][j] != sigma[i][j + 1]) {
        if (g)
          g->Point(1, i, j + 1);
      }
      /* Cells that touch eachother's corners are NO neighbours */
      if (sigma[i][j] != sigma[i + 1][j + 1] ||
          sigma[i + 1][j] != sigma[i][j + 1]) {
        if (g)
          g->Point(1, i + 1, j + 1);
      }
    }
  }
}

int **CellularPotts::SearchNeighboursMatrix() {
  int i, j;
  int **neighbours = new int *[cell->size() + 1];
  for (int i = 0; i < (int)cell->size() + 1; i++) {
    neighbours[i] = new int[cell->size() + 1];
  }
  for (i = 0; i < ((int)cell->size() + 1); i++) {
    for (j = 0; j < ((int)cell->size() + 1); j++) {
      neighbours[i][j] = 0;
    }
  }
  for (i = 0; i < sizex - 1; i++) {
    for (j = 0; j < sizey - 1; j++) {
      int iplus = i + 1;
      int jplus = j + 1;
      if (par.periodic_boundaries) {
        if (iplus <= 0) {
          iplus = sizex - 2 + iplus;
        }
        if (jplus <= 0) {
          jplus = sizey - 2 + jplus;
        }
        if (iplus >= sizex - 1) {
          iplus = iplus - sizex + 2;
        }
        if (jplus >= sizey - 1) {
          jplus = jplus - sizey + 2;
        }

        /* if cellborder */ /* etc. etc. */
        if (sigma[i][j] != sigma[i + 1][j]) {
          neighbours[sigma[i][j]][sigma[iplus][j]] += 1;
          neighbours[sigma[iplus][j]][sigma[i][j]] += 1;
        }
        if (sigma[i][j] != sigma[i][j + 1]) {
          neighbours[sigma[i][j]][sigma[i][jplus]] += 1;
          neighbours[sigma[i][jplus]][sigma[i][j]] += 1;
        }
        // if extended_neighbour_border is true, also count cells touching by a
        // corner.
        if (par.extended_neighbour_border) {
          if (sigma[i][j] != sigma[i + 1][j + 1]) {
            neighbours[sigma[i][j]][sigma[iplus][jplus]] += 1;
          }
          if (sigma[i + 1][j] != sigma[i][j + 1]) {
            neighbours[sigma[iplus][j]][sigma[i][jplus]] += 1;
          }
        }
      }
    }
  }
  return neighbours;
}

int CellularPotts::GetNewPerimeterIfXYWereAdded(int sxyp, int x, int y) {

  /*int n_nb;

   if (par.neighbours>=1 && par.neighbours<=4)
     n_nb=nbh_level[par.neighbours];
  */
  int perim = (*cell)[sxyp].Perimeter();
  // Increase of perimeter due to addition of x,y
  perim++;
  /* the cell with sigma sxyp wants to extend by adding lattice site (x, y).
 This means that the sxyp neighbours of (x,y) will not be borders anymore,so
 they can be subtracted from the perimeter of sxyp.
*/
  for (int i = 1; i <= n_nb; i++) {

    int xp2, yp2;

    xp2 = x + nx[i];
    yp2 = y + ny[i];

    xp2 = FixPeriodic(xp2,sizex);
    yp2 = FixPeriodic(yp2,sizey);

    if (sigma[xp2][yp2] == sxyp) {
      bool interior_pixel2 = true;

      // looping through neighbours of xp2,yp2
        for (int j = 1; j <= n_nb; j++){
          int xp3, yp3;
          xp3 = xp2 + nx[j];
          yp3 = yp2 + ny[j];
          xp3 = FixPeriodic(xp3,sizex);
          yp3 = FixPeriodic(yp3,sizey);

          // Jump to the next loop if you see pixels of other cells except for the x,y pixel
          if ((sigma[xp3][yp3] != sxyp) && (xp3 != x || yp3 != y)){
            interior_pixel2 = false;
            break;
          }
      	}
      if (interior_pixel2){
	    perim--; // The pixel xp2,yp2 will be removed from membrane
	  }
	}
    }

  return perim;
}

void CellularPotts::AddMembranePixel(int sxyp, array<int, 2> pixel) {

  /*int n_nb;

   if (par.neighbours>=1 && par.neighbours<=4)
     n_nb=nbh_level[par.neighbours];
  */
  // int perim = (*cell)[sxyp].Perimeter();
  // Increase of perimeter due to addition of x,y
  (*cell)[sxyp].AddPixelToMembrane(pixel);

  int x = pixel[0];
  int y = pixel[1];

  /* the cell with sigma sxyp wants to extend by adding lattice site (x, y).
 This means that the sxyp neighbours of (x,y) will not be borders anymore,so
 they can be subtracted from the perimeter of sxyp.
*/
  for (int i = 1; i <= n_nb; i++) {

    int xp2, yp2;

    xp2 = x + nx[i];
    yp2 = y + ny[i];

    xp2 = FixPeriodic(xp2,sizex);
    yp2 = FixPeriodic(yp2,sizey);

    if (sigma[xp2][yp2] == sxyp) {
      bool interior_pixel2 = true;

      // looping through neighbours of xp2,yp2
        for (int j = 1; j <= n_nb; j++){
          int xp3, yp3;
          xp3 = xp2 + nx[j];
          yp3 = yp2 + ny[j];
          xp3 = FixPeriodic(xp3,sizex);
          yp3 = FixPeriodic(yp3,sizey);

          // Jump to the next loop if you see pixels of other cells except for the x,y pixel
          if ((sigma[xp3][yp3] != sxyp) && (xp3 != x || yp3 != y)){
            interior_pixel2 = false;
            break;
          }
      	}
        if (interior_pixel2){
          (*cell)[sxyp].RemovePixelFromMembrane(array<int, 2>{xp2, yp2}); // The pixel xp2,yp2 will be removed from membrane
        }
  	}
  }
}

int CellularPotts::GetNewPerimeterIfXYWereRemoved(int sxy, int x, int y) {
  /*int n_nb;
   if (par.neighbours>=1 && par.neighbours<=4)
    int n_nb=nbh_level[par.neighbours];
  */
  int perim = (*cell)[sxy].Perimeter();
  /* the cell with sigma sxy loses xy
   */
  // Reduction of perimeter due to deletion of x,y

  perim--;
  for (int i = 1; i <= n_nb; i++) {

    int xp2, yp2;
    xp2 = x + nx[i];
    yp2 = y + ny[i];

    xp2 = FixPeriodic(xp2,sizex);
    yp2 = FixPeriodic(yp2,sizey);

      if (sigma[xp2][yp2] == sxy){
	bool membrane_pixel2 = false;

        // looping through neighbours of xp2,yp2
        for (int j = 1; j <= n_nb; j++){
          int xp3, yp3;
          xp3 = xp2 + nx[j];
          yp3 = yp2 + ny[j];
          xp3 = FixPeriodic(xp3,sizex);
          yp3 = FixPeriodic(yp3,sizey);

          // Jump to the next loop if you see pixels of other cells
          if (sigma[xp3][yp3] != sxy){
	    membrane_pixel2 = true;
            break;
          }
	}
      if (!membrane_pixel2){
	  // The pixel xp2,yp2 will be a new membrane pixel!
          perim++;
      }
    }
  }
return perim;
}

void CellularPotts::RemoveMembranePixel(int sxy, std::array<int, 2> pixel) {
  /*int n_nb;
   if (par.neighbours>=1 && par.neighbours<=4)
    int n_nb=nbh_level[par.neighbours];
  */
  int perim = (*cell)[sxy].Perimeter();

  int x = pixel[0];
  int y = pixel[1];

  /* the cell with sigma sxy loses xy
   */
  // Reduction of perimeter due to deletion of x,y

  (*cell)[sxy].RemovePixelFromMembrane(pixel);
  for (int i = 1; i <= n_nb; i++) {

    int xp2, yp2;
    xp2 = x + nx[i];
    yp2 = y + ny[i];

    xp2 = FixPeriodic(xp2,sizex);
    yp2 = FixPeriodic(yp2,sizey);

      if (sigma[xp2][yp2] == sxy){
      	bool membrane_pixel2 = false;

        // looping through neighbours of xp2,yp2
        for (int j = 1; j <= n_nb; j++){
          int xp3, yp3;
          xp3 = xp2 + nx[j];
          yp3 = yp2 + ny[j];
          xp3 = FixPeriodic(xp3,sizex);
          yp3 = FixPeriodic(yp3,sizey);

          // Jump to the next loop if you see pixels of other cells
          if (sigma[xp3][yp3] != sxy){
      	    membrane_pixel2 = true;
            break;
          }
	      }   
      if (!membrane_pixel2){
    	  // The pixel xp2,yp2 will be a new membrane pixel!
        (*cell)[sxy].AddPixelToMembrane(std::array<int, 2> {xp2, yp2});
      }
    }
  }
}

int CellularPotts::GetActLevel(int x, int y) {
  if (sigma[x][y] > 0)
    return (actPixels[{x, y}]);
  else
    return (0);
}

// matrix array implementation
int CellularPotts::GetMatrixLevel(int x, int y) {
  if (matrix[x][y] > 0) {
    return (matrix[x][y]);
  } else {
    return (0);
  }
}

void CellularPotts::ReadZygotePicture(void) {
  int pix, cells, i, j, c, p, checkx, checky;
  char **pixelmap;
  char pixel[3];

  sscanf(ZYGXPM(ZYGOTE)[0], "%d %d %d %d", &checkx, &checky, &cells, &pix);

  if ((checkx > sizex) || (checky > sizey)) {
    std::cerr
        << "ReadZygote: The included xpm picture is smaller than the grid!\n";
    std::cerr << "\n Please adjust either the grid size or the picture size.\n";
    std::cerr << sizex << "," << sizey << "," << checkx << "," << checky
              << "\n";
    exit(1);
  }
  pixelmap = (char **)malloc(cells * sizeof(char *));
  if (pixelmap == NULL)
    MemoryWarning();

  pixelmap[0] = (char *)malloc(cells * 3 * sizeof(char));
  if (pixelmap[0] == NULL)
    MemoryWarning();

  for (i = 1; i < cells; i++)
    pixelmap[i] = pixelmap[i - 1] + 3;

  for (i = 0; i < cells; i++) {
    for (j = 0; j < pix; j++)
      pixelmap[i][j] = ZYGXPM(ZYGOTE)[i + 1][j];
    pixelmap[i][pix] = '\0';
  }

  for (i = 0; i < sizex * sizey; i++)
    sigma[0][i] = 0;
  fprintf(stderr, "[%d %d]\n", checkx, checky);

  int offs_x, offs_y;
  offs_x = (sizex - checkx) / 2;
  offs_y = (sizey - checky) / 2;

  for (i = 0; i < checkx; i++)
    for (j = 0; j < checky; j++) {
      for (p = 0; p < pix; p++)
        pixel[p] = ZYGXPM(ZYGOTE)[cells + 1 + j][i * pix + p];

      pixel[pix] = '\0';

      for (c = 0; c < cells; c++) {
        if (!(strcmp(pixelmap[c], pixel))) {
          if ((sigma[offs_x + i][offs_y + j] = c)) {

            // if c is _NOT_ medium (then c=0)
            // assign pixel values from "sigmamax"
            sigma[offs_x + i][offs_y + j] += (Cell::MaxSigma() - 1);
          }
        }
      }
    }
  free(pixelmap[0]);
  free(pixelmap);
}

void CellularPotts::ConstructInitCells(Dish &beast) {

  // Get the maximum cell ID (mostly equal to the cell number)
  int loop = sizex * sizey;
  int cells = 0;
  for (int i = 0; i < loop; i++) {
    if (cells < sigma[0][i])
      cells = sigma[0][i];
  }

  cerr << "[ cells = " << cells << "]\n";

  // construct enough cells for the zygote.  "cells", contains the
  // number of colours (excluding background).
  {
    for (int i = 0; i < cells; i++) {
      cell->push_back(Cell(beast));
    }
  }

  // Set the area and target area of the cell
  // makes use of the pointer to the Cell pointer of Dish
  // which is a member of CellularPotts
  MeasureCellSizes();

  // set zygote_area to mean cell area.
  int mean_area = 0;
  for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); c++) {
    mean_area += c->Area();
  }
  if (cells != 0)
    mean_area /= cells;

  zygote_area = mean_area;

  cout << "mean_area = " << mean_area << "\n";
  // set all cell areas to the mean area
  {
    for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); c++) {
      if (par.target_area >= 0) {
        c->SetTargetArea(par.target_area);
      } else {
        c->SetTargetArea(mean_area);
      }
    }
  }
}

void CellularPotts::MeasureCellSizes(void) {
  // Clean areas of all cells, including medium
  for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); c++) {
    c->SetTargetArea(0);
    c->area = 0;
  }

  // calculate the area of the cells
  for (int x = 1; x < sizex - 1; x++) {
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y] > 0) {
        (*cell)[sigma[x][y]].IncrementTargetArea();
        (*cell)[sigma[x][y]].IncrementArea();
        (*cell)[sigma[x][y]].AddSiteToMoments(x, y);
      }
    }
  }

  // set the actual area to the target area
  for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); c++) {
    c->SetAreaToTarget();
  }
}

void CellularPotts::MeasureCellSize(Cell &c) {
  c.CleanMoments();
  // calculate the area of the cell
  for (int x = 1; x < sizex - 1; x++) {
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y] == c.sigma) {
        (*cell)[sigma[x][y]].IncrementTargetArea();
        (*cell)[sigma[x][y]].IncrementArea();
        (*cell)[sigma[x][y]].AddSiteToMoments(x, y);
      }
    }
  }
}

std::vector<PixelPos> CellularPotts::GetCellMembranePixels2() {
  std::vector<PixelPos> pixels;
  int loop = static_cast<float>(sizeedgelist) / static_cast<float>(n_nb);
  std::cerr << "loop = " << loop << "\n";
  for (int i = 0; i < loop; i++) {
    // find the corresponding edge
    int targetedge = orderedgelist[i];
    // find the lattice site corresponding to this edge
    int targetsite = targetedge / n_nb;

    // find the x and y coordinate corresponding to the target site
    int x = targetsite % (sizex - 2) + 1;
    int y = targetsite / (sizex - 2) + 1;

    PixelPos pixel(x, y);
    pixels.push_back(pixel);
  }
  return pixels;
}


std::vector<PixelPos> CellularPotts::GetCellMembranePixels() {
  std::vector<PixelPos> pixels;
  for (int x = 1; x < sizex - 1; x++) {
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y] > 0) {
        for (int i = 1; i <= n_nb; i++) {
          int xp2, yp2;
          xp2 = x + nx[i];
          yp2 = y + ny[i];

          xp2 = FixPeriodic(xp2,sizex);
          yp2 = FixPeriodic(yp2,sizey);

          // did we find a border?
          if (sigma[xp2][yp2] != sigma[x][y]) {
            // add to the perimeter of the cell
            PixelPos pixel(x, y);
            pixels.push_back(pixel);
            break; // to avoid double conunting
          }
        }
      }
    }
  }
  return pixels;
}

void CellularPotts::MeasureCellPerimeters() {
  for (int x = 1; x < sizex - 1; x++) {
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y] > 0) {
        for (int i = 1; i <= n_nb; i++) {
          int xp2, yp2;
          xp2 = x + nx[i];
          yp2 = y + ny[i];

          xp2 = FixPeriodic(xp2,sizex);
          yp2 = FixPeriodic(yp2,sizey);

          // did we find a border?
          if (sigma[xp2][yp2] != sigma[x][y]) {
            // add to the perimeter of the cell
            (*cell)[sigma[x][y]].IncrementPerimeter();
            break; // to avoid double conunting
          }
        }
      }
    }
  }
}

void CellularPotts::SetupCellMembranePixels() {
  for (int x = 1; x < sizex - 1; x++) {
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y] > 0) {
        for (int i = 1; i <= n_nb; i++) {
          int xp2, yp2;
          xp2 = x + nx[i];
          yp2 = y + ny[i];

          xp2 = FixPeriodic(xp2,sizex);
          yp2 = FixPeriodic(yp2,sizey);

          // did we find a border?
          if (sigma[xp2][yp2] != sigma[x][y]) {
            // add to the perimeter of the cell
            (*cell)[sigma[x][y]].AddPixelToMembrane(array<int, 2>{x, y});
            break; // to avoid double conunting
          }
        }
      }
    }
  }
}

void CellularPotts::ReportCellData() {
  std::cout << "Cell Data at time " << thetime << "\n";
  std::cout << "Cell\tSigma\tArea\tTargetArea\tPerimeter\tTargetPerimeter\n";
  for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); c++) {
    if (c->sigma == 0)
      continue;
    std::cout << c->sigma << "\t" << c->Area() << "\t" << c->TargetArea()
              << "\t" << c->Perimeter() << "\t" << c->TargetPerimeter()
              << "\n";
    std::cout << "Pixels: ";
    for (int x = 1; x < sizex - 1; x++) {
      for (int y = 1; y < sizey - 1; y++) {
        if (sigma[x][y] == c->sigma) {
          std::cout << "[" << x << "\t" << y << "]\n";
        }
      }
    }
    }
}

Dir *CellularPotts::FindCellDirections(void) const {
  double *sumx = 0, *sumy = 0;
  double *sumxx = 0, *sumxy = 0, *sumyy = 0;
  double *n = 0;
  double xmean = 0, ymean = 0, sxx = 0, sxy = 0, syy = 0;
  double D, lb1 = 0, lb2 = 0;

  Dir *celldir;

  /* Allocation of sufficient memory space */
  if ((sumx = (double *)malloc(cell->size() * sizeof(double))) == NULL)
    MemoryWarning();
  else if ((sumy = (double *)malloc(cell->size() * sizeof(double))) == NULL)
    MemoryWarning();
  else if ((sumxx = (double *)malloc(cell->size() * sizeof(double))) == NULL)
    MemoryWarning();
  else if ((sumxy = (double *)malloc(cell->size() * sizeof(double))) == NULL)
    MemoryWarning();
  else if ((sumyy = (double *)malloc(cell->size() * sizeof(double))) == NULL)
    MemoryWarning();
  else if ((n = (double *)malloc(cell->size() * sizeof(double))) == NULL)
    MemoryWarning();

  if (!(celldir = new Dir[cell->size()]))
    MemoryWarning();

  /* Initialisation of the variables */
  for (int i = 0; i < (int)cell->size(); i++) {
    sumx[i] = 0.;
    sumy[i] = 0.;
    sumxx[i] = 0.;
    sumxy[i] = 0.;
    sumyy[i] = 0.;
    n[i] = 0L;
  }

  /* Find sumx, sumy, sumxx and sumxy for all cells */
  for (int x = 0; x < sizex; x++)
    for (int y = 0; y < sizey; y++)
      if (sigma[x][y] > 0) {
        sumx[0] += (double)x;
        sumy[0] += (double)y;
        sumxx[0] += (double)x * x;
        sumxy[0] += (double)x * y;
        sumyy[0] += (double)y * y;

        n[0]++;

        sumx[sigma[x][y]] += (double)x;
        sumy[sigma[x][y]] += (double)y;

        sumxx[sigma[x][y]] += (double)x * x;
        sumxy[sigma[x][y]] += (double)x * y;
        sumyy[sigma[x][y]] += (double)y * y;

        n[sigma[x][y]]++;
      }

  /* Compute the principal axes for all cells */
  for (int i = 0; i < (int)cell->size(); i++) {
    if (n[i] > 10) {
      xmean = ((double)sumx[i]) / ((double)n[i]);
      ymean = ((double)sumy[i]) / ((double)n[i]);

      sxx = (double)(sumxx[i]) - ((double)(sumx[i] * sumx[i])) / (double)n[i];
      sxx = sxx / (double)(n[i] - 1);

      sxy = (double)(sumxy[i]) - ((double)(sumx[i] * sumy[i])) / (double)n[i];
      sxy = sxy / (double)(n[i] - 1);

      syy = (double)(sumyy[i]) - ((double)(sumy[i] * sumy[i])) / (double)n[i];
      syy = syy / (double)(n[i] - 1);

      D = sqrt((sxx + syy) * (sxx + syy) - 4. * (sxx * syy - sxy * sxy));
      lb1 = (sxx + syy + D) / 2.;
      lb2 = (sxx + syy - D) / 2.;
      celldir[i].lb1 = lb1;
      celldir[i].lb2 = lb2;
    }
    if (sxy == 0.0)
      celldir[i].bb1 = 1.;
    else
      celldir[i].bb1 = sxy / (lb1 - syy);

    if (fabs(celldir[i].bb1) < .00001) {
      if (celldir[i].bb1 > 0.)
        celldir[i].bb1 = .00001;
      else
        celldir[i].bb1 = -.00001;
    }
    celldir[i].aa1 = ymean - xmean * celldir[i].bb1;
    celldir[i].bb2 = (-1.) / celldir[i].bb1;
    celldir[i].aa2 = ymean - celldir[i].bb2 * xmean;
  }

  /* free allocated memory */
  free(sumx);
  free(sumy);
  free(sumxx);
  free(sumxy);
  free(sumyy);
  free(n);

  return celldir;
}

void CellularPotts::ShowDirections(Graphics &g, const Dir *celldir) const {
  int i;
  if (cell->size() > 1)
    for (i = 1; i < (int)cell->size(); i++)
      g.Line(0, (int)(2 * celldir[i].aa1), sizex * 2,
             (int)((celldir[i].aa1 + celldir[i].bb1 * sizey) * 2), 2);
}

void CellularPotts::DivideCells(vector<bool> which_cells) {

  // for the cell directions
  Dir *celldir = 0;

  /* Allocate space for divisionflags */
  int *divflags = (int *)malloc((cell->size() * 2 + 5) * sizeof(int));

  /* Clear divisionflags */
  for (int i = 0; i < (int)(cell->size() * 2 + 5); i++)
    divflags[i] = 0;

  if (!(which_cells.size() == 0 || which_cells.size() >= cell->size())) {
    throw "In CellularPotts::DivideCells, Too few elements in vector<int> "
          "which_cells.";
  }

  /* division */
  for (int i = 0; i < sizex; i++) {
    for (int j = 0; j < sizey; j++)
      if (sigma[i][j] > 0) { // i.e. not medium and not border state (-1)
        // Pointer to mother. Warning: Renew pointer after a new
        // cell is added (push_back). Then, the array *cell is relocated and
        // the pointer will be lost...

        Cell *motherp = &((*cell)[sigma[i][j]]);
        Cell *daughterp;

        /* Divide if NOT medium and if DIV bit set or divide_always is set */
        // if which_cells is given, divide only if the cell
        // is marked in which_cells.
        if (!which_cells.size() || which_cells[motherp->sigma]) {
          if (!(divflags[motherp->Sigma()])) {
            // add daughter cell, copying states of mother
            daughterp = new Cell(*(motherp->owner));
            daughterp->CellBirth(*motherp);
            cell->push_back(*daughterp);

            // renew pointer to mother
            motherp = &((*cell)[sigma[i][j]]);

            divflags[motherp->Sigma()] = daughterp->Sigma();
            delete daughterp;

            // array may be relocated after "push_back"

            // renew daughter pointers
            daughterp = &(cell->back());

            /* administration on the onset of mitosis */

            /* Ancestry is taken care of in copy constructor of Cell
               see cell.hh: Cell(const Cell &src, bool newcellP=false) :
               Cytoplasm(src) {} */

            /* inherit  polarity of mother */
            // All that needs to be copied is copied in the copy constructor
            // of Cell and in the default copy constr. of its base class
            // Cytoplasm note: also the celltype is inherited
          } else {
            daughterp = &((*cell)[divflags[motherp->Sigma()]]);
          }

          /* Now the actual division takes place */

          /* If celldirections where not yet computed: do it now */
          if (!celldir)
            celldir = FindCellDirections();

          /* if site is below the minor axis of the cell: sigma of new cell */
          if (j > ((int)(celldir[motherp->sigma].aa2 +
                         celldir[motherp->sigma].bb2 * (double)i))) {
            motherp->DecrementArea();
            motherp->DecrementTargetArea();
            motherp->RemoveSiteFromMoments(i, j);
            sigma[i][j] = daughterp->Sigma();
            daughterp->AddSiteToMoments(i, j);
            daughterp->IncrementArea();
            daughterp->IncrementTargetArea();
          }
        }
      }
  }
  if (celldir)
    delete[](celldir);

  if (divflags)
    free(divflags);

  for (vector<Cell>::iterator c = cell->begin(); c != cell->end(); c++) {
    int sig = c->Sigma();
    if (which_cells[sig] || sig > which_cells.size()-1) {
      UpdateMembraneOnDivision(sig);
    }
  }
}

bool CellularPotts::isMembranePixel(int x, int y){
  // Check if the pixel at (x,y) is a membrane pixel
  int sigma_xy = sigma[x][y];
  for (int i = 1; i <= n_nb; i++) {
    int xp2 = FixPeriodic(x + nx[i], sizex);
    int yp2 = FixPeriodic(y + ny[i], sizey);
    if (sigma[xp2][yp2] != sigma_xy) {
      return true;
    }
  }
  return false;
}

void CellularPotts::UpdateMembraneOnDivision(int sig) {
  // Update the cell's membrane pixels after division
  std::vector<std::array<int, 2>> updated_membrane_pixels;

  auto old_membrane_pixels = (*cell)[sig].GetMembranePixels();

  // remove pixels that do not belong anymore to the cell
  for (const auto& pixel : old_membrane_pixels) {
    if (sigma[pixel[0]][pixel[1]] == sig) {
      updated_membrane_pixels.push_back(pixel);
    }
  }

  // Loop through existing membrane pixels to find where divisions occurred
  int xn, yn, x_search, y_search;
  bool division_found = false;

  if (updated_membrane_pixels.size()==0) {
    throw std::runtime_error("No membrane pixels found for cell with sigma " + std::to_string(sig));
  }

  for (const auto& pixel : updated_membrane_pixels) {
    x_search = pixel[0];
    y_search = pixel[1];
    for (int i = 1; i <= n_nb; i++) {
      xn = FixPeriodic(x_search + nx[i], sizex);
      yn = FixPeriodic(y_search + ny[i], sizey);
      if (sigma[xn][yn] == sig && isMembranePixel(xn, yn) && \
          std::find(updated_membrane_pixels.begin(), updated_membrane_pixels.end(), std::array<int, 2>{xn, yn}) == updated_membrane_pixels.end()) {
        division_found = true;
        break; // Found a division pixel, no need to check further
      }
    }
    if (division_found) {
      break; // Exit outer loop as well
    }
  }

  bool AllMembranePixelsUpdated = false;
  // list of new membrane pixels to be added
  std::vector<std::array<int, 2>> new_membrane_pixels;
  std::vector<std::array<int, 2>> search_front_pixels;
  search_front_pixels.push_back({x_search, y_search});
  int loop_size = search_front_pixels.size();
  for (int j = 0; j < loop_size; j++){
    auto pixel = search_front_pixels[j];
      int px = pixel[0];
      int py = pixel[1];
      for (int i = 1; i <= n_nb; i++) {

        int x_new = FixPeriodic(px + nx[i], sizex);
        int y_new = FixPeriodic(py + ny[i], sizey);
      if (sigma[x_new][y_new] == sig && isMembranePixel(x_new, y_new) && \
          std::find(updated_membrane_pixels.begin(), updated_membrane_pixels.end(), std::array<int, 2>{x_new, y_new}) == updated_membrane_pixels.end()) {
          new_membrane_pixels.push_back({x_new, y_new});
        search_front_pixels.push_back({x_new, y_new});
        loop_size++;
        }
      }
      if (new_membrane_pixels.size() == 0) {
        AllMembranePixelsUpdated = true;
      } else {
        for (const auto& new_pixel : new_membrane_pixels) {
          updated_membrane_pixels.push_back(new_pixel);
      }
    }
    new_membrane_pixels.clear();
  }
  (*cell)[sig].SetMembranePixels(updated_membrane_pixels);
}

/**! Fill the plane with initial cells
 \return actual amount of cells (some are not draw due to overlap) */
int CellularPotts::ThrowInCells(int n, int cellsize) {

  //  int gapx=(sizex-nx*cellsize)/(nx+1);
  // int gapy=(sizey-ny*cellsize)/(ny+1);

  int cellnum = 1;

  for (int i = 0; i < n; i++) {
    // draw a circle at x0, y0
    int x0 = RandomNumber(sizex);
    int y0 = RandomNumber(sizey);

    bool overlap = false;

    // check overlap
    for (int x = 0; x < cellsize; x++)
      for (int y = 0; y < cellsize; y++)
        if ((((x - cellsize / 2) * (x - cellsize / 2) +
              (y - cellsize / 2) * (y - cellsize / 2)) <
             ((cellsize / 2) * (cellsize / 2))) &&
            (x0 + x < sizex && y0 + y < sizey))
          if (sigma[x0 + x][y0 + y]) {
            overlap = true;
            break;
          }

    if (!overlap) {
      for (int x = 0; x < cellsize; x++)
        for (int y = 0; y < cellsize; y++)
          if ((((x - cellsize / 2) * (x - cellsize / 2) +
                (y - cellsize / 2) * (y - cellsize / 2)) <
               ((cellsize / 2) * (cellsize / 2))) &&
              (x0 + x < sizex && y0 + y < sizey))
            sigma[x0 + x][y0 + y] = cellnum;
      cellnum++;
    }
  }
  cerr << "[ cellnum = " << cellnum << "]";

  // repair borders
  // fill borders with special border state
  for (int x = 0; x < sizex - 1; x++) {
    sigma[x][0] = -1;
    sigma[x][sizey - 1] = -1;
  }
  for (int y = 0; y < sizey - 1; y++) {
    sigma[0][y] = -1;
    sigma[sizex - 1][y] = -1;
  }
  for (int x = 1; x < sizex - 2; x++) {
    sigma[x][1] = 0;
    sigma[x][sizey - 2] = 0;
  }
  for (int y = 1; y < sizey - 2; y++) {
    sigma[1][y] = 0;
    sigma[sizex - 2][y] = 0;
  }
  return cellnum;
}

int CellularPotts::GrowInCells(int n_cells, int cell_size, double subfield,
                               int posx, int posy) {
  int sx = (int)((sizex - 2) / subfield);
  int sy = (int)((sizey - 2) / subfield);

  int offset_x = (sizex - 2 - sx) / 2;
  int offset_y = (sizey - 2 - sy) / 2;

  if (n_cells == 1) {
    if (posx < 0)
      posx = sizex / 2;
    if (posy < 0)
      posy = sizey / 2;
    return GrowInCells(1, cell_size, posx, posy, 0, 0);
  } else {
    return GrowInCells(n_cells, cell_size, sx, sy, offset_x, offset_y);
  }
}

void CellularPotts::RandomSpins(double prob) {
  for (int x = 1; x <= sizex - 2; x++) {
    for (int y = 1; y < sizey - 2; y++) {
      sigma[x][y] = (RANDOM() < prob) ? 0 : 1;
    }
  }
  cerr << "RandomSpins done" << endl;
}

int CellularPotts::GrowInCells(int n_cells, int cell_size, int sx, int sy,
                               int offset_x, int offset_y) {

  // make initial cells using Eden Growth

  int **new_sigma = (int **)malloc(sizex * sizeof(int *));
  if (new_sigma == NULL)
    MemoryWarning();

  new_sigma[0] = (int *)malloc(sizex * sizey * sizeof(int));
  if (new_sigma[0] == NULL)
    MemoryWarning();

  for (int i = 1; i < sizex; i++)
    new_sigma[i] = new_sigma[i - 1] + sizey;

  /* Clear CA plane */
  {
    for (int i = 0; i < sizex * sizey; i++)
      new_sigma[0][i] = 0;
  }

  // scatter initial points, or place a cell in the middle
  // if only one cell is desired
  int cellnum = cell->size() - 1;

  if (n_cells > 1) {

    {
      for (int i = 0; i < n_cells; i++) {

        sigma[RandomNumber(sx) + offset_x][RandomNumber(sy) + offset_y] =
            ++cellnum;
      }
    }
  } else {
    sigma[sx][sy] = ++cellnum;
  }

  // Do Eden growth for a number of time steps
  {
    for (int i = 0; i < cell_size; i++) {
      for (int x = 1; x < sizex - 1; x++)
        for (int y = 1; y < sizey - 1; y++) {

          if (sigma[x][y] == 0) {
            // take a random neighbour
            int xyp = (int)(8 * RANDOM() + 1);
            int xp = nx[xyp] + x;
            int yp = ny[xyp] + y;
            int kp;
            //  NB removing this border test yields interesting effects :-)
            // You get a ragged border, which you may like!
            if ((kp = sigma[xp][yp]) != -1)
              if (kp > (cellnum - n_cells))
                new_sigma[x][y] = kp;
              else
                new_sigma[x][y] = 0;
            else
              new_sigma[x][y] = 0;

          } else {
            new_sigma[x][y] = sigma[x][y];
          }
        }

      // copy sigma to new_sigma, but do not touch the border!
      {
        for (int x = 1; x < sizex - 1; x++) {
          for (int y = 1; y < sizey - 1; y++) {
            sigma[x][y] = new_sigma[x][y];
          }
        }
      }
    }
  }
  free(new_sigma[0]);
  free(new_sigma);

  return cellnum;
}

/** Draw a square cell in at (cx,cy) */
int CellularPotts::SquareCell(int sig, int cx, int cy, int size) {
  int xmin, xmax;
  xmin = cx - size / 2;
  if (xmin < 1)
    xmin = 1;
  xmax = cx + size / 2;
  if (xmax > sizex - 1)
    xmax = sizex - 1;

  int ymin, ymax;
  ymin = cy - size / 2;
  if (ymin < 1)
    ymin = 1;
  ymax = cy + size / 2;
  if (ymax > sizey - 1)
    ymax = sizey - 1;

  for (int x = xmin; x <= xmax; x++) {
    for (int y = ymin; y <= ymax; y++) {
      sigma[x][y] = sig;
    }
  }
  return 1;
}

// Predicate returns true when connectivity is locally preserved
// if the value of the central site would be changed
bool CellularPotts::ConnectivityPreservedP(int x, int y) {
  // Use local nx and ny in a cyclic order (starts at upper left corner)
  // first site is repeated, for easier looping
  const int cyc_nx[10] = {-1, -1, 0, 1, 1, 1, 0, -1, -1, -1};
  const int cyc_ny[10] = {0, -1, -1, -1, 0, 1, 1, 1, 0, -1};

  int sxy = sigma[x][y]; // the central site
  if (sxy == 0)
    return true;

  int n_borders =
      0; // to count the amount of sites in state sxy bordering a site !=sxy

  static int stack[8]; // stack to count number of different surrounding cells
  int stackp = -1;
  bool one_of_neighbours_medium = false;
  for (int i = 1; i <= 8; i++) {
    int s_nb = sigma[x + cyc_nx[i]][y + cyc_ny[i]];
    int s_next_nb = sigma[x + cyc_nx[i + 1]][y + cyc_ny[i + 1]];

    if ((s_nb == sxy || s_next_nb == sxy) && (s_nb != s_next_nb)) {
      // check whether s_nb is adjacent to non-identical site,
      // count it
      n_borders++;
    }
    int j;
    bool on_stack_p = false;

    // we need the next heuristic to prevent stalling at
    // cell-cell borders
    // do not enforce constraint at two cell interface(no medium)
    if (s_nb) {
      for (j = stackp; j >= 0; j--) {
        if (s_nb == stack[j]) {
          on_stack_p = true;
          break;
        }
      }
      if (!on_stack_p) {
        if (stackp > 6) {
          cerr << "Stack overflow, stackp=" << stackp << "\n";
        }
        stack[++stackp] = s_nb;
      }
    } else {
      one_of_neighbours_medium = true;
    }
  }

  // number of different neighbours is stackp+1;
  if (n_borders > 2 && ((stackp + 1) > 2 || one_of_neighbours_medium)) {
    return false;
  } else
    return true;
}

// Predicate returns true when cluster connectivity is locally preserved
// if the value of the central site would be changed
bool CellularPotts::ConnectivityPreservedPCluster(int x, int y) {

  // Use local nx and ny in a cyclic order (starts at upper left corner)
  // first site is repeated, for easier looping
  const int cyc_nx[10] = {-1, -1, 0, 1, 1, 1, 0, -1, -1, -1};
  const int cyc_ny[10] = {0, -1, -1, -1, 0, 1, 1, 1, 0, -1};

  int sxy = sigma[x][y]; // the central site
  if (sxy == 0)
    return true;

  int n_borders =
      0; // to count the amount of sites in state sxy bordering a site !=sxy

  static int stack[8]; // stack to count number of different surrounding cells
  int stackp = -1;
  bool one_of_neighbours_medium = false;

  for (int i = 1; i <= 8; i++) {
    int xcn = x + cyc_nx[i];
    int ycn = y + cyc_ny[i];
    int xncn = x + cyc_nx[i + 1];
    int yncn = y + cyc_ny[i + 1];

    if (par.periodic_boundaries) {
      if (xcn <= 0)
        xcn = sizex - 2 + xcn;
      if (ycn <= 0)
        ycn = sizey - 2 + ycn;
      if (xcn >= sizex - 1)
        xcn = xcn - sizex + 2;
      if (ycn >= sizey - 1)
        ycn = ycn - sizey + 2;
      if (xncn <= 0)
        xncn = sizex - 2 + xncn;
      if (yncn <= 0)
        yncn = sizey - 2 + yncn;
      if (xncn >= sizex - 1)
        xncn = xncn - sizex + 2;
      if (yncn >= sizey - 1)
        yncn = yncn - sizey + 2;
    }

    int s_nb = sigma[xcn][ycn];
    int s_next_nb = sigma[xncn][yncn];

    if ((s_nb > 0 || s_next_nb > 0) && (s_nb == 0 || s_next_nb == 0)) {

      // check whether s_nb is adjacent to non-identical site,
      // count it
      n_borders++;
    }
    int j;
    bool on_stack_p = false;
    // we need the next heuristic to prevent stalling at
    // cell-cell borders
    // do not enforce constraint at two cell interface(no medium)
    if (s_nb) {
      for (j = stackp; j >= 0; j--) {
        if (s_nb == stack[j]) {
          on_stack_p = true;
          break;
        }
      }
      if (!on_stack_p) {
        if (stackp > 6) {
          cerr << "Stack overflow, stackp=" << stackp << "\n";
        }
        stack[++stackp] = s_nb;
      }
    } else {
      one_of_neighbours_medium = true;
    }
  }

  // number of different neighbours is stackp+1;
  if (n_borders > 2 && ((stackp + 1) > 2 || one_of_neighbours_medium)) {
    return false;
  } else
    return true;
}

double CellularPotts::CellDensity(void) const {
  // return the density of cells
  int sum = 0;
  for (int i = 0; i < sizex * sizey; i++) {
    if (sigma[0][i]) {
      sum++;
    }
  }
  return (double)sum / (double)(sizex * sizey);
}

double CellularPotts::MeanCellArea(void) const {
  int sum_area = 0, n = 0;
  double sum_length = 0.;
  vector<Cell>::iterator c = cell->begin();
  ++c;

  for (; c != cell->end(); c++) {
    sum_area += c->Area();
    sum_length += c->Length();
    n++;
  }
  cerr << "Mean cell length is " << sum_length / ((double)n) << endl;
  return (double)sum_area / (double)n;
}

void CellularPotts::ResetTargetLengths(void) {
  vector<Cell>::iterator c = cell->begin();
  ++c;
  for (; c != cell->end(); c++) {
    c->SetTargetLength(par.target_length);
  }
}

void CellularPotts::SetRandomTypes(void) {
  // each cell gets a random type 1..maxtau
  vector<Cell>::iterator c = cell->begin();
  ++c;
  for (; c != cell->end(); c++) {
    int celltype = RandomNumber(Cell::maxtau);
    // cerr << "Setting celltype " << celltype << endl;
    c->setTau(celltype);
  }
}

void CellularPotts::GrowAndDivideCells(int growth_rate) {
  vector<Cell>::iterator c = cell->begin();
  ++c;
  vector<bool> which_cells(cell->size());
  for (; c != cell->end(); c++) {
    // only tumor cells grow and divide
    if (c->getTau() == 2) {
      c->SetTargetArea(c->TargetArea() + growth_rate);

      if (c->Area() > par.target_area) {
        which_cells[c->Sigma()] = true;
      } else {
        which_cells[c->Sigma()] = false;
      }
      if (c->chem[1] < 0.9) { // arbitrary oxygen threshold for the moment
        c->setTau(3);
      }
    } else {
      which_cells[c->Sigma()] = false;
    }
  }
  DivideCells(which_cells);
}

void CellularPotts::GrowCells(int cell_type,int growth_rate) {
  GrowCells(cell_type,static_cast<double>(growth_rate));
}

void CellularPotts::GrowCells(int cell_type,double growth_rate) {
  // TODO: cell_type can be changed into a vector containing all the cell types that should grow
  // growth_rate can be changed into a vector containing growth rates of different cell types.
  vector<Cell>::iterator c = cell->begin();
  ++c;
  for (; c != cell->end(); c++) {
    // grow specific cell type or all cells
    if (c->getTau() == cell_type || cell_type == 0) {
      c->SetTargetArea(c->TargetArea() + growth_rate);
    }
  }
}

void CellularPotts::GrowCells(int cell_type,double growth_rate,double size_threshold) {
  // TODO: cell_type can be changed into a vector containing all the cell types that should grow
  // growth_rate and size_threshold can be changed into vectors containing growth rates and thresholds of different cell types.
  vector<Cell>::iterator c = cell->begin();
  ++c;
  for (; c != cell->end(); c++) {
    // grow specific cell type or all cells
    if (c->getTau() == cell_type || cell_type == 0) {
      if (c->Area() >= size_threshold) {
        // only grow if the cell is larger than the threshold
        c->SetTargetArea(c->TargetArea() + growth_rate);
      }
    }
  }
}

std::unordered_map<int, int> CellularPotts::MembraneMediumEdgeCount() {
  std::unordered_map<int, int> MediumEdgeCount;
  auto membrane_pixels = GetCellMembranePixels();
  for (const auto &pixel : membrane_pixels) {
    int x = pixel.x;
    int y = pixel.y;
    int cell_type = sigma[x][y];
    MediumEdgeCount[cell_type] = 0; // initialize the free fraction for this cell type
    for (int i = 1; i <= n_nb; i++) {
      int xp2, yp2;
      xp2 = x + nx[i];
      yp2 = y + ny[i];

      xp2 = FixPeriodic(xp2,sizex);
      yp2 = FixPeriodic(yp2,sizey);

      // did we find a medium in the neighbourhood?
      if (sigma[xp2][yp2] == 0) { // medium state
        // increment the free fraction for this cell type
        MediumEdgeCount[cell_type]++;
        break; // to avoid double conunting
      }
    }
  }
  return MediumEdgeCount;
}

void CellularPotts::DivideCellsByArea(int cell_type,int area_threshold) {
  // TODO: cell_type can be changed into a vector containing all the cell types that can divide
  // area_threshold can be changed into a vector containing area_thresholds for different cell types.
  vector<Cell>::iterator c = cell->begin();
  ++c;
  vector<bool> which_cells(cell->size());

  for (; c != cell->end(); c++) {
    if (c->getTau() == cell_type || cell_type == 0) {
      if (c->Area() >= area_threshold) {
        which_cells[c->Sigma()] = true;
      } else {
        which_cells[c->Sigma()] = false;
      }
    } else {
      which_cells[c->Sigma()] = false;
    }
  }
  DivideCells(which_cells);
}

vector<bool> CellularPotts::DivideCellsByRandomArea(int cell_type) {
  // TODO: cell_type can be changed into a vector containing all the cell types that can divide
  // area_threshold can be changed into a vector containing area_thresholds for different cell types.
  vector<Cell>::iterator c = cell->begin();
  ++c;
  vector<bool> which_cells(cell->size());

  for (; c != cell->end(); c++) {
    if (c->getTau() == cell_type || cell_type == 0) {
      if (c->Area() >= c->division_area) {
        which_cells[c->Sigma()] = true;
      } else {
        which_cells[c->Sigma()] = false;
      }
    } else {
      which_cells[c->Sigma()] = false;
    }
  }
  return which_cells;
}

void CellularPotts::DivideCellsWithRule(std::string method,int cell_type) {
  // TODO: cell_type can be changed into a vector containing all the cell types that can divide
  // if cell_type=0, all cell types can divide
  vector<bool> which_cells(cell->size());
  if (method == "random_area") {
    which_cells = DivideCellsByRandomArea(cell_type);
  } else {
    throw "In CellularPotts::DivideCellsWithRule, unknown method.";
  }
  if (which_cells.size() > 0) {
    DivideCells(which_cells);
  }
}


double CellularPotts::DrawConvexHull(Graphics *g, int color) {
  // Draw the convex hull of the cells
  // using Andrew's Monotone Chain Algorithm (see hull.cpp)

  // Step 1. Prepare data for 2D hull code

  // count number of points to determine size of array
  int np = 0;
  for (int x = 1; x < sizex - 1; x++)
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y]) {
        np++;
      }
    }

  Point *p = new Point[np];
  int pc = 0;
  for (int x = 1; x < sizex - 1; x++) {
    for (int y = 1; y < sizey - 1; y++) {
      if (sigma[x][y]) {
        p[pc++] = Point(x, y);
      }
    }
  }
  // Step 2: call 2D Hull code
  Point *hull = new Point[np];
  int nph = chainHull_2D(p, np, hull);

  // Step 3: draw it
  for (int i = 0; i < nph - 1; i++) {
    g->Line(hull[i].x, hull[i].y, hull[i + 1].x, hull[i + 1].y, color);
  }

  // Step 4: calculate area of convex hull
  double hull_area = 0.;
  for (int i = 0; i < nph - 1; i++) {
    hull_area += hull[i].x * hull[i + 1].y - hull[i + 1].x * hull[i].y;
  }
  hull_area /= 2.;
  // cerr << "Area = " << hull_area << "\n";

  delete[] p;
  delete[] hull;
  return hull_area;
}

double CellularPotts::Compactness(void) {
  int bounds[4];
  bounds[0] = 1;
  bounds[1] = sizey - 2;
  bounds[2] = 1;
  bounds[3] = sizex - 2;
  // Calculate compactness using the convex hull of the cells, including the
  // corner points of pixels We use Andrew's Monotone Chain Algorithm (see
  // hull.cpp)

  // Step 1: calculate total cell area

  double cell_area = 0;
  for (int x = bounds[2]; x < bounds[3] + 1; x++) // count only within the box
    for (int y = bounds[0]; y < bounds[1] + 1; y++) {
      if (sigma[x][y]) // Only consider one celltype
      {
        cell_area++;
      }
    }

  int np = 0;
  // Step 2. Prepare data for 2D hull code

  // Step 2a. Count number of corner points to determine size of array

  // First consider the left-most column, a corner point if there is a pixel (or
  // to the bottom of it)
  if (sigma[bounds[2]][bounds[0]]) // bottom row separately
    np++;
  for (int y = bounds[0] + 1; y < bounds[1] + 1; y++)
    if (sigma[bounds[2]][y] ||
        sigma[bounds[2]][y - 1]) // Only consider one celltype
                                 // add corner point only if a pixel is present
                                 // at this location or below it.
    {
      np++;
    }
  if (sigma[bounds[2]][bounds[1]]) // add top-left most corner points if there
                                   // is a pixel there
    np++;

  // Add all 'inner' corner points
  for (int x = bounds[2] + 1; x < bounds[3] + 1; x++) {
    if (sigma[x][bounds[0]] || sigma[x - 1][bounds[0]])
      np++; // special case for bottom row is required
    for (int y = bounds[0] + 1; y < bounds[1] + 1;
         y++) // loop over all other rows
    {
      if (sigma[x][y] || sigma[x - 1][y] || sigma[x][y - 1] ||
          sigma[x - 1][y - 1]) // Only consider one celltype
      // and add a corner point on the bottom left of the current pixel if one
      // of the adjacent pixels is present
      {
        np++;
      }
    }
    if (sigma[x][bounds[1]] || sigma[x - 1][bounds[1]])
      np++;
    // add the top-most corner point only if there is a pixel on the top row (or
    // to the left of this pixel)
  }

  // Consider the right-most column separately, only add a corner point if there
  // is a pixel in this column (or to the bottom of it)
  if (sigma[bounds[3]][bounds[0]]) // bottom row separately
    np++;
  for (int y = bounds[0] + 1; y < bounds[1] + 1; y++)
    if (sigma[bounds[3]][y] ||
        sigma[bounds[3]][y - 1]) // Only consider one celltype
                                 // add corner point only if a pixel is present
                                 // at this location or below it.
    {
      np++;
    }
  if (sigma[bounds[3]][bounds[1]])
    np++;

  // Step 2b. Create array which will contain all corner points

  Point *p = new Point[np];

  // Step 2c. Fill the array with all lattice points ordered, x-first.
  int pc = 0;

  // First consider the left-most column, a corner point if there is a pixel (or
  // to the bottom of it)
  if (sigma[bounds[2]][bounds[0]]) // bottom row separately
    p[pc++] = Point(bounds[2] - 0.5, bounds[0] - 0.5);
  for (int y = bounds[0] + 1; y < bounds[1] + 1; y++)
    if (sigma[bounds[2]][y] ||
        sigma[bounds[2]][y - 1]) // Only consider one celltype
                                 // add corner point only if a pixel is present
                                 // at this location or below it.
    {
      p[pc++] = Point(bounds[2] - 0.5, y - 0.5);
    }
  if (sigma[bounds[2]][bounds[1]]) // add top-left most corner points if there
                                   // is a pixel there
    p[pc++] = Point(bounds[2] - 0.5, bounds[1] + 0.5);

  // Add all 'inner' corner points
  for (int x = bounds[2] + 1; x < bounds[3] + 1; x++) {
    if (sigma[x][bounds[0]] || sigma[x - 1][bounds[0]])
      p[pc++] = Point(
          x - 0.5, bounds[0] - 0.5); // special case for bottom row is required
    for (int y = bounds[0] + 1; y < bounds[1] + 1;
         y++) // loop over all other rows
    {
      if (sigma[x][y] || sigma[x - 1][y] || sigma[x][y - 1] ||
          sigma[x - 1][y - 1]) // Only consider one celltype
      // and add a corner point on the bottom left of the current pixel if one
      // of the adjacent pixels is present
      {
        p[pc++] = Point(x - 0.5, y - 0.5);
      }
    }
    if (sigma[x][bounds[1]] || sigma[x - 1][bounds[1]])
      p[pc++] = Point(x - 0.5, bounds[1] + 0.5);
    // add the top-most corner point only if there is a pixel on the top row (or
    // to the left of this pixel)
  }

  // Consider the right-most column separately, only add a corner point if there
  // is a pixel in this column (or to the bottom of it)
  if (sigma[bounds[3]][bounds[0]]) // bottom row separately
    p[pc++] = Point(bounds[3] + 0.5, bounds[0] - 0.5);
  for (int y = bounds[0] + 1; y < bounds[1] + 1; y++)
    if (sigma[bounds[3]][y] ||
        sigma[bounds[3]][y - 1]) // Only consider one celltype
                                 // add corner point only if a pixel is present
                                 // at this location or below it.
    {
      p[pc++] = Point(bounds[3] + 0.5, y - 0.5);
    }
  if (sigma[bounds[3]][bounds[1]])
    p[pc++] = Point(bounds[3] + 0.5, bounds[1] + 0.5);

  // Step 3: call 2D Hull code
  Point *hull = new Point[np];
  int nph = chainHull_2D(p, np, hull);

  // Step 4: calculate area of convex hull

  double hull_area = 0.;
  for (int i = 0; i < nph - 1; i++) {
    hull_area += hull[i].x * hull[i + 1].y - hull[i + 1].x * hull[i].y;
  }
  hull_area /= 2.;

  delete[] p;
  delete[] hull;

  // return compactness
  // cout << "cell_area = " << cell_area << endl;
  // cout << "hull_area = " << hull_area << endl;
  return cell_area / hull_area;
}

void CellularPotts::FindBoundingBox(void) {
  int min_x = sizex + 2, max_x = 0;
  int min_y = sizey + 2, max_y = 0;
  for (int x = 1; x <= sizex - 2; x++) {
    for (int y = 1; y <= sizey - 2; y++) {
      if (sigma[x][y]) {
        if (x < min_x) {
          min_x = x;
        }
        if (x > max_x) {
          max_x = x;
        }
        if (y < min_y) {
          min_y = y;
        }
        if (y > max_y) {
          max_y = y;
        }
      }
    }
  }
}

// useful to demonstrate large q-Potts
void CellularPotts::RandomSigma(int n_cells) {
  for (int x = 0; x < sizex; x++) {
    for (int y = 0; y < sizey; y++) {
      sigma[x][y] = (int)(n_cells * RANDOM());
    }
  }
}

bool CellularPotts::plotPos(int x, int y, Graphics *graphics) {
  int self = sigma[x][y];
  if (self <= 0)
    return true;
  graphics->Rectangle((*cell)[self].Colour(), x, y);
  return false;
}

void CellularPotts::linePlotPos(int x, int y, Graphics *graphics) {
  int self = sigma[x][y];
  int a = self, b = self, c = self, d = self;
  if (x != 0)
    a = sigma[x - 1][y];
  if (y != 0)
    b = sigma[x][y - 1];
  if (x != par.sizex - 1)
    c = sigma[x + 1][y];
  if (y != par.sizey - 1)
    d = sigma[x][y + 1];
  if (self != a)
    graphics->Line(x, y, x, y + 1, 1);
  if (self != b)
    graphics->Line(x, y, x + 1, y, 1);
  if (self != c)
    graphics->Line(x + 1, y, x + 1, y + 1, 1);
  if (self != d)
    graphics->Line(x, y + 1, x + 1, y + 1, 1);
}

void CellularPotts::anneal(int steps) {
  for (int i = 0; i < steps; i++)
    AmoebaeMove(0, true);
}

int **CellularPotts::get_annealed_sigma(int steps) {
  int **tmp_a = sigma;
  int **tmp_b;
  AllocateSigma(par.sizex, par.sizey);
  std::copy(*tmp_a, (*tmp_a) + (par.sizex * par.sizey), *sigma);
  anneal(steps);
  tmp_b = sigma;
  sigma = tmp_a;
  return tmp_b;
}

void CellularPotts::CalcPeriodicSafeCentroids(void) {

    Cell::sizex=sizex;
    Cell::sizey=sizey;

    const double two_pi = 2.0 * M_PI;
    for (Cell &c : *cell) {
        c.sum_sin_x=0.;
        c.sum_cos_x=0.;
        c.sum_sin_y=0.;
        c.sum_cos_y=0.;
    }

    for (int x=1;x<=sizex-2;x++) {
        for (int y=1;y<=sizey-2;y++) {
            if (sigma[x][y]>0) {

                        double theta_x = two_pi * static_cast<double>(x) / (sizex-2);
                        double theta_y = two_pi * static_cast<double>(y) / (sizey-2);
                        (*cell)[sigma[x][y]].sum_cos_x += std::cos(theta_x);
                        (*cell)[sigma[x][y]].sum_sin_x += std::sin(theta_x);
                        (*cell)[sigma[x][y]].sum_cos_y += std::cos(theta_y);
                        (*cell)[sigma[x][y]].sum_sin_y += std::sin(theta_y);
                    }

                    //double avg_theta = std::atan2(sum_sin, sum_cos);
                    //if (avg_theta < 0) avg_theta += two_pi;  // normalize to [0, 2π)

                    //return domain_size * avg_theta / two_pi;
                }
            }
        }

