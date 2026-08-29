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
#include <stdio.h>
#ifndef __APPLE__
#include <malloc.h>
#endif
#include "cell.hpp"
#include "dish.hpp"
#include "graph.hpp"
#include "info.hpp"
#include "inputoutput.hpp"
#include "parameter.hpp"
#include "plotter.hpp"
#include "profiler.hpp"
#include "random.hpp"
#include "sqr.hpp"
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <math.h>
#include <filesystem>
#include <iomanip>
#include <memory>
#include "ca.hpp"


using namespace std;

// Function to write cell positions; pass all required variables as parameters
void write_cell_positions(int i, const Parameter& par, const std::string& output_name, int output_per, std::ofstream* cellpos_stream,Info *info) {
  std::string filename = par.datadir + "/" + output_name;
  std::ofstream out;
  out << std::scientific << std::setprecision(6);  // Adjust precision as needed
  if (i == 0) {
    std::cout << "Opening cell position" << std::endl;
    out.open(filename);
    out << "time (MCS),cell id,com_1 (px),com_2 (px), growth_status, N_neighbours" << std::endl;

    if (!out) {
      std::cerr << "Failed to open file!" << std::endl;
    }
  } else if (i % output_per == 0) {
    out.open(filename, std::ios::app);
  }
  info->WriteOutputs(out,std::vector<std::string> {"time","sigma","com_x","com_y","color_id","n_neighbours"}, ",");
}

INIT {
  try {
    // Read initial configuration

    CPM->GrowInCells(par.n_init_cells, par.size_init_cells, par.subfield);
    CPM->ConstructInitCells(*this);
    CPM->SetupCellMembranePixels();

    // int cell_size=5;
    // int x_pos;
    // for (int cell_id=1; cell_id<=11;cell_id++){
    //   x_pos = (cell_id-1)*cell_size+50;
    //   CPM->SquareCell(cell_id,x_pos,3,cell_size);
    //   std::cerr << "added cell: " << cell_id << "\n";
    // }

    // Construct the cells
    //CPM->ConstructInitCells(*dish);

    CPM->InitialiseEdgeList();

  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
}

TIMESTEP {
  try {

    static int i = 0;
    static Dish *dish;
    if (i == 0) {
      dish = new Dish();
    }

    static Info *info = new Info(*dish, *this);
    static Plotter *plotter = new Plotter(dish, this);
    static ofstream *cellpos_stream = nullptr;
    static IO *io = 0;
    if (io == 0 ) {
        io = new IO(*dish);
    }

    dish->CPM->DivideCellsByTargetArea();
    dish->CPM->GrowCells(0, par.area_growth_rate,par.CIP_area_ratio,par.CIP_neighbour_ratio);

    if (par.graphics && !(i % par.storage_stride)) {
      PROFILE(all_plots, plotter->Plot();)
      info->Menu();
      dish->CPM->FindBoundingBox(); // old: Setboundingbox
    }


    if (i == 0 && par.pause_on_start) {
      info->set_Paused();
      i++;
    }

    if (!info->IsPaused()) {
      PROFILE(amoebamove, dish->CPM->AmoebaeMove(dish->PDEfield);)
    }

    if (par.store && !(i % par.storage_stride)) {
      char fname[200], fname_mcds[200];
      snprintf(fname, 199, "%s/snapshot%06d.png", par.datadir.c_str(), i);
      Write(fname);
      write_cell_positions(i,par,"tst.csv",1,cellpos_stream,info);
    }

    int max_cell_count = 1000;
    if (dish->CountCells() > max_cell_count) {
      char fname[200], fname_mcds[200];
      snprintf(fname, 199, "%s/snapshot%06d.png", par.datadir.c_str(), i);
      Write(fname);
      write_cell_positions(i,par,"tst.csv",1,cellpos_stream,info);
      exit(0);
    }

    if (!info->IsPaused()) {
      i++;
    }
  } catch (const char *error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }
  PROFILE_PRINT
}

void CellularPotts::DivideCellsByTargetArea() {
  // Create a vector to keep track of which cells should be divided
  vector<bool> which_cells(cell->size());

  // Iterate through the cells and determine which ones should be divided based on their target area
  vector<Cell>::iterator c = cell->begin();
  ++c;

  for (; c != cell->end(); c++) {
    if (c->TargetArea() >= c->division_area) {
      which_cells[c->Sigma()] = true;
    } else {
      which_cells[c->Sigma()] = false;
    }
  }
  if (which_cells.size() > 0) {
    DivideCellsInheritTargetArea(which_cells);
  }
}
 
void CellularPotts::GrowCells(int cell_type,double growth_rate,double size_threshold,double neighbour_threshold) {
  // TODO: cell_type can be changed into a vector containing all the cell types that should grow
  // growth_rate and size_threshold can be changed into vectors containing growth rates and thresholds of different cell types.
  vector<Cell>::iterator c = cell->begin();
  ++c;
  auto CellContactData =  CellPerimeterContact();
  
  // Writing cell properties
  int N_cells_to_report = 1000;
  bool write_to_file = false;
  std::ofstream file_write;
  std::string filename = par.datadir + "/cell_data_no_inhibition_" + std::to_string(thetime) + ".csv";
  //if ((cell->size()>=N_cells_to_report && cell->size()<N_cells_to_report+50)){
    // Excluding cells that have zero area.
    int cell_count=0;
    for (; c != cell->end(); c++){
	if (c->Area() >0){
		cell_count++;
	}
  //  }
    if (cell_count >= N_cells_to_report || (thetime % 39 == 0)){
    //if (cell_count > N_cells_to_report){
	// Checking if the file already exists (this helps to avoid double writing)
        std::ifstream file_read(filename);
	if (!file_read.good()){
	   file_read.close();
	   // The file does not exist. Now we are writing a header in the file.
	   file_write.open(filename);
	   write_to_file = true;
	   file_write << "x_pos,y_pos,radius_i,a_i,f_i\n";
	}
    }
  }

  c = cell->begin();
  c++;
  double R = sqrt(par.target_area/M_PI); // Cell radius, used for normalization
  double area_fraction=0, surface_fraction = 0;
  for (; c != cell->end(); c++) {
    int cell_id = c->Sigma();
    bool Area_Threshold_Exceeded= false, Neighbour_Threshold_Exceeded= false;

    area_fraction = c->Area()/c->TargetArea();
    surface_fraction = static_cast<double>(CellContactData[cell_id][2])/static_cast<double>(CellContactData[cell_id][1]);
    
    // check if size is larger than the threshold
    if (area_fraction >= size_threshold) {
      Area_Threshold_Exceeded = true;
    }
    if (surface_fraction >= neighbour_threshold) {
      Neighbour_Threshold_Exceeded = true;
    }

    // Writing cell properties
    if (write_to_file && c->Area()>0){
      file_write << c->getCenterX()/R << "," << c->getCenterY()/R << "," << sqrt(c->TargetArea()/M_PI)/R << "," << area_fraction << "," << surface_fraction <<  "\n";
    }

    // Growth and color assignment
    if (Area_Threshold_Exceeded && Neighbour_Threshold_Exceeded) {
        c->SetTargetArea(c->TargetArea() + growth_rate);
        c->SetColour(5);
    } else if (!Area_Threshold_Exceeded && Neighbour_Threshold_Exceeded) {
      c->SetColour(3);
    } else if (!Neighbour_Threshold_Exceeded && Area_Threshold_Exceeded) {
      c->SetColour(4);
      } else {
     c->SetColour(2);
    }
  }
}

void CellularPotts::DivideCellsInheritTargetArea(vector<bool> which_cells) {

  // for the cell directions
  Dir *celldir = 0;

  /* Allocate space for divisionflags */
  int *divflags = (int *)malloc((cell->size() * 2 + 5) * sizeof(int));

  /* Clear divisionflags */
  for (int i = 0; i < (int)(cell->size() * 2 + 5); i++)
    divflags[i] = 0;

  /* Store TargetAreas of the cells */
  vector<float> target_areas_before_division;
  for (size_t i = 0; i < cell->size(); ++i) {
    target_areas_before_division.push_back((*cell)[i].TargetArea());
  }

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
            motherp->SetTargetArea(target_areas_before_division[motherp->Sigma()]/2.0f);
            daughterp->SetTargetArea(target_areas_before_division[motherp->Sigma()]/2.0f);
            motherp->DecrementArea();
            motherp->RemoveSiteFromMoments(i, j);
            sigma[i][j] = daughterp->Sigma();
            daughterp->IncrementArea();
            daughterp->AddSiteToMoments(i, j);
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

void Plotter::Plot() {
  graphics->BeginScene();
  graphics->ClearImage();

  plotCPMCellTypes();
  plotCPMLines();

  graphics->EndScene();
}

void PDE::DerivativesPDE(CellularPotts *cpm, PDEFIELD_TYPE *derivs, int x,
                         int y) {}

int PDE::MapColour(double val) {
  return (((int)((val / ((val) + 1.)) * 100)) % 100) + 155;
}

int main(int argc, char *argv[]) {
  extern Parameter par;
  try {
    par.Read(argv[1]);
    Seed(par.rseed);
    start_graphics(argc, argv);
  } catch (const char *error) {
    std::cerr << error << std::endl;
    return 1;
  }
  return 0;
}

