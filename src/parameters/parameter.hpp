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
#ifndef _PARAMETER_HPP_
#define _PARAMETER_HPP_

#ifdef _MOCK_PARAMETER_HPP_
#include _MOCK_PARAMETER_HPP_
#else

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
  int ref_adhesive_area;
  int area_constraint_type;
  bool cluster_connectivity;
  bool vecadherinknockout;
  bool extensiononly;
  int chemotaxis;
  int border_energy;
  int neighbours;
  bool periodic_boundaries;
  bool gradient;
  bool extended_neighbour_border;
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
  bool load_mcds;
  char * mcds_output;
  char * mcds_input;
  int mcds_anneal_steps;
  int mcds_denoise_steps;
  bool pause_on_start; 
  bool useopencl;
  char * opencl_core_path;
  int opencl_pref_platform;
  int adhesion_storage_stride;

  // Adhesions

  /** Whether to use the adhesion simulation. */
  bool adhesions_enabled;

  /** Radius of the adhesion creation zone
   *
   * Adhesions are created in the adhesion creation zone, which contains all
   * pixels that are in a cell and within a certain radius from the edge of the
   * cell. This parameter specifies that radius.
   */
  double adhesion_zone_radius;

  /** Number of adhesions to initially create */
  int num_adhesions;

  /** How to move adhesions at the source pixel of a copy attempt.
   *
   * lazy: Leave them where they are.
   * sticky: Move them to the target pixel.
   * mixed: Randomly either leave them where they are, or move them to the target pixel.
   * random: Move them in a random direction within the cell.
   */
  char * adhesion_extension_mechanism;

  /** How to select an adhesion displacement
   *
   * If there are multiple possibilities for where an adhesion can be moved,
   * one is chosen based on this parameter:
   *
   * uniform: Pick one at random from the available possibilities
   * gradient: Pick the one with the lowest DH
   *
   * Formerly called nbhd_selection.
   */
  char * adhesion_displacement_selection;

  /// Work required to annihilate an adhesion (in DH units)
  int adhesion_annihilation_penalty;

  /// Number of adhesions per pixel above which a crowding penalty is applied
  int adhesions_per_pixel_overflow;

  /// Per-adhesion penalty (in DH units) in case of crowding
  int adhesions_per_pixel_overflow_penalty;

  //Act model
  double lambda_Act;
  int max_Act;
  int lambda_perimeter;
  int target_perimeter;
  //Lymphocyte matrix interaction
  double lambda_matrix;
  double spontaneous_p;
  double decay_p;
  double eden_p;
  int J_pol;
  double threshold;
  double start_level;
  char * colortable;
 private:
};

ostream &operator<<(ostream &os, Parameter &p);
const char *sbool(const bool &p);

#endif
#endif

