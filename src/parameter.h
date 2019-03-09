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
#ifndef _PARAMETER_H_
#define _PARAMETER_H_

#include <iostream>
using namespace std;
class Parameter {
  
 public: 
  Parameter();
  ~Parameter();
  void CleanUp(void);
  void Read(const char *filename);
  void Write(ostream &os) const;
  double T;
  int target_area;
  int target_length;
  double lambda;
  double lambda2;
  char * Jtable;
  int conn_diss;
  bool vecadherinknockout;
  bool extensiononly;
  int chemotaxis;
  int border_energy;
  int neighbours;
  bool periodic_boundaries;
  int n_chem;
  double * diff_coeff;
  double * decay_rate;
  double * secr_rate;
  double saturation;
  double dt;
  double dx;
  int pde_its;
  int n_init_cells;
  int size_init_cells;
  int sizex;
  int sizey;
  int divisions;
  int mcs;
  int rseed;
  double subfield;
  int relaxation;
  int storage_stride;
  bool graphics;
  bool store;
  char * datadir;
 private:
};

ostream &operator<<(ostream &os, Parameter &p);
const char *sbool(const bool &p);


#endif
