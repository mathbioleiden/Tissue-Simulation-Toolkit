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


#include "parameter.h"
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cerrno>
#include <iostream>
#include "output.h"
#include "parse.h"

Parameter::Parameter() {

  T = 50.;
  target_area = 100;
  ref_adhesive_area = 100;
  target_length = 60;
  lambda = 50;
  lambda2 = 5.0;
  Jtable = strdup("J.dat");
  conn_diss = 2000;
  cluster_connectivity = false;
  vecadherinknockout = false;
  extensiononly = false;
  chemotaxis = 1000;
  border_energy = 100;
  neighbours = 2;
  periodic_boundaries = false;
  extended_neighbour_border = false;
  n_chem = 1;
  diff_coeff = new double[1];
  diff_coeff[0] = 1e-13;
  decay_rate = new double[1];
  decay_rate[0] = 1.8e-4;
  secr_rate = new double[1];
  secr_rate[0] = 1.8e-4;
  saturation = 0;
  dt = 2.0;
  dx = 2.0e-6;
  pde_its = 15;
  n_init_cells = 100;
  size_init_cells = 10;
  sizex = 200;
  sizey = 200;
  divisions = 0;
  mcs = 10000;
  rseed = -1;
  subfield = 1.0;
  relaxation = 0;
  storage_stride = 10;
  adhesion_storage_stride=mcs+1;
  graphics = true;
  store = false;
  datadir = strdup("data_film");
	// Act model
	double lambda_Act =0;
	int max_Act = 0;
	//lymphocyte matrix interaction
	double lambda_matrix =0;
	int max_matrix = 0;
	int age_saturation = 1;
	bool geometric_mean = false;
	double single_site_power = 1;
	lambda_c = 600;
	double spontaneous_p = 0.001;
	double decay_p = 0.02;
	double eden_p = 0.25;
  double lambda_schooling = 0.0;
  int J_pol = 0;
  double pillar_r = 0;
  double pillar_distance = 0;
  double pillar_radius = 0;
  int pillar_energy =0;
  int pillar_energy_odd =0;
  bool checkerboard = false;
  double lambda_persistence = 0;
  int tau = 0;
  double threshold = 0.1;
  double start_level = 0.1;


}

Parameter::~Parameter() {

  // destruct parameter object

  // free string parameter

  CleanUp();

}

void Parameter::CleanUp(void) {
  if (Jtable)
     free(Jtable);
  if (diff_coeff)
     free(diff_coeff);
  if (decay_rate)
     free(decay_rate);
  if (secr_rate)
     free(secr_rate);
  if (datadir)
     free(datadir);

}

void Parameter::Read(const char *filename) {

  static bool ReadP=false;

  if (ReadP) {

    //throw "Run Time Error in parameter.cpp: Please Read parameter file only once!!";
    CleanUp();

  } else
    ReadP=true;

  FILE *fp=OpenReadFile(filename);


  T = fgetpar(fp, "T", 50., true);
  target_area = igetpar(fp, "target_area", 100, true);
  ref_adhesive_area = igetpar(fp, "ref_adhesive_area", 100, true);
  target_length = igetpar(fp, "target_length", 60, true);
  lambda = fgetpar(fp, "lambda", 50, true);

  area_constraint_type = igetpar(fp, "area_constraint_type",0, true);
  lambda2 = fgetpar(fp, "lambda2", 5.0, true);
  Jtable = sgetpar(fp, "Jtable", "J.dat", true);
  conn_diss = igetpar(fp, "conn_diss", 2000, true);
  cluster_connectivity = bgetpar(fp, "cluster_connectivity", false, true);
  vecadherinknockout = bgetpar(fp, "vecadherinknockout", false, true);
  extensiononly = bgetpar(fp, "extensiononly", false, true);
  chemotaxis = igetpar(fp, "chemotaxis", 1000, true);
  border_energy = igetpar(fp, "border_energy", 100, true);
  neighbours = igetpar(fp, "neighbours", 2, true);
  periodic_boundaries = bgetpar(fp, "periodic_boundaries", false, true);
  extended_neighbour_border = bgetpar(fp, "extended_neighbour_border", false, true);
  n_chem = igetpar(fp, "n_chem", 1, true);
  diff_coeff = dgetparlist(fp, "diff_coeff", n_chem, true);
  decay_rate = dgetparlist(fp, "decay_rate", n_chem, true);
  secr_rate = dgetparlist(fp, "secr_rate", n_chem, true);
  saturation = fgetpar(fp, "saturation", 0, true);
  dt = fgetpar(fp, "dt", 2.0, true);
  dx = fgetpar(fp, "dx", 2.0e-6, true);
  pde_its = igetpar(fp, "pde_its", 15, true);
  n_init_cells = igetpar(fp, "n_init_cells", 1, true);
  size_init_cells = igetpar(fp, "size_init_cells", 10, true);
  sizex = igetpar(fp, "sizex", 200, true);
  sizey = igetpar(fp, "sizey", 200, true);
  divisions = igetpar(fp, "divisions", 0, true);
  mcs = igetpar(fp, "mcs", 10000, true);
  rseed = igetpar(fp, "rseed", -1, true);
  subfield = fgetpar(fp, "subfield", 1.0, true);
  relaxation = igetpar(fp, "relaxation", 0, true);
  storage_stride = igetpar(fp, "storage_stride", 10, true);
  adhesion_storage_stride = igetpar(fp, "storage_stride", mcs+1, true);
  graphics = bgetpar(fp, "graphics", true, true);
  store = bgetpar(fp, "store", false, true);
  datadir = sgetpar(fp, "datadir", "data_film", true);
	// Act model
	lambda_Act = fgetpar(fp, "lambda_Act", 0, true);
	max_Act = igetpar(fp, "max_Act", 0, true);
	lambda_perimeter = igetpar(fp, "lambda_perimeter",0, true);
	target_perimeter = igetpar(fp, "target_perimeter", 0, true);
	//lymphocyte matrix interaction
	lambda_matrix = fgetpar(fp, "lambda_matrix", 0, true);
	max_matrix = igetpar(fp, "max_matrix", 0, true);
	age_saturation = igetpar(fp, "age_saturation", 1, true);
	geometric_mean = bgetpar(fp, "geometric_mean", false, true);
	single_site_power = fgetpar(fp, "single_site_power", 1, true);
	lambda_c = fgetpar(fp, "lambda_c" , 600, true);
	spontaneous_p = fgetpar(fp, "spontaneous_p", 0.001, true);
	decay_p = fgetpar(fp,"decay_p", 0.02, true);
	eden_p = fgetpar(fp,"eden_p", 0.25, true);
  lambda_schooling = fgetpar( fp, "lambda_schooling", 0, true);
  J_pol = igetpar( fp,"J_pol", 0 , true);
  pillar_r = fgetpar(fp, "pillar_r",0,true);
  pillar_distance = fgetpar(fp, "pillar_distance", 0,true);
  pillar_radius = fgetpar(fp, "pillar_radius", 0 ,true);
  pillar_energy = igetpar(fp, "pillar_energy", 0, true);
  pillar_energy_odd = igetpar(fp, "pillar_energy_odd", 0, true);
  checkerboard = bgetpar(fp, "checkerboard", 0, true);
  lambda_persistence = fgetpar(fp, "lambda_persistence", 0 , true);
  tau = igetpar(fp, "tau", 0, true);
  threshold = fgetpar(fp, "threshold", 0 , true);
  start_level = fgetpar(fp, "start_level", 0, true);


}

const char *sbool(const bool &p) {

  const char *true_str="true";
  const char *false_str="false";
  if (p)
    return true_str;
  else
    return false_str;
}

void Parameter::Write(ostream &os) const {
  setlocale(LC_NUMERIC, "C");

  os << " T = " << T << endl;
  os << " target_area = " << target_area << endl;
  os << " ref_adhesive_area = " << ref_adhesive_area << endl;
  os << " target_length = " << target_length << endl;
  os << " lambda = " << lambda << endl;
  os << " area_constraint_type = " << area_constraint_type << endl;
  os << " lambda2 = " << lambda2 << endl;

  if (Jtable)
    os << " Jtable = " << Jtable << endl;
  os << " conn_diss = " << conn_diss << endl;
  os << " cluster_connectivity = " << cluster_connectivity << endl;
  os << " vecadherinknockout = " << sbool(vecadherinknockout) << endl;
  os << " extensiononly = " << sbool(extensiononly) << endl;
  os << " chemotaxis = " << chemotaxis << endl;
  os << " border_energy = " << border_energy << endl;
  os << " neighbours = " << neighbours << endl;
  os << " periodic_boundaries = " << sbool(periodic_boundaries) << endl;
  os << " extended_neighbour_border = " << sbool(extended_neighbour_border) << endl;
  os << " n_chem = " << n_chem << endl;
  os << " diff_coeff = "<< diff_coeff[0] << endl;
  os << " decay_rate = "<< decay_rate[0] << endl;
  os << " secr_rate = "<< secr_rate[0] << endl;
  os << " saturation = " << saturation << endl;
  os << " dt = " << dt << endl;
  os << " dx = " << dx << endl;
  os << " pde_its = " << pde_its << endl;
  os << " n_init_cells = " << n_init_cells << endl;
  os << " size_init_cells = " << size_init_cells << endl;
  os << " sizex = " << sizex << endl;
  os << " sizey = " << sizey << endl;
  os << " divisions = " << divisions << endl;
  os << " mcs = " << mcs << endl;
  os << " rseed = " << rseed << endl;
  os << " subfield = " << subfield << endl;
  os << " relaxation = " << relaxation << endl;
  os << " storage_stride = " << storage_stride << endl;
  os << " adhesion_storage_stride = " << adhesion_storage_stride << endl;
  os << " graphics = " << sbool(graphics) << endl;
  os << " store = " << sbool(store) << endl;
	//Act model
	os << " lambda_Act = " << lambda_Act << endl;
	os << " max_Act = " << max_Act << endl;
	os << " lambda_perimeter = " << lambda_perimeter << endl;
	os << " target_perimeter = " << target_perimeter << endl;
	//lymphocyte matrix interaction
	os << " lambda_matrix = " << lambda_matrix << endl;
	os << " max_matrix = " << max_matrix << endl;
	os << " age_saturation = " << age_saturation << endl;
	os << " geometric_mean = " << geometric_mean << endl;
	os << " single_site_power = " << single_site_power << endl;
	os << " lambda_c = " << lambda_c << endl;
os << " spontaneous_p = " << spontaneous_p << endl;
os << " decay_p = " << decay_p << endl;
os << " eden_p = " << eden_p << endl;
  os << " lambda_schooling = " << lambda_schooling << endl;
  os << " J_pol = " << J_pol << endl;

  if (datadir)
    os << " datadir = " << datadir << endl;
}


ostream &operator<<(ostream &os, Parameter &p) {
  p.Write(os);
  return os;
}

Parameter par;
