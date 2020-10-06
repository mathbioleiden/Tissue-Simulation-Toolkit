/* 

Copyright 1996-2006 Roeland Merks, Paulien Hogeweg

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
#include <vector>
#include <list>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <string.h>
#include <errno.h>
#include <math.h>
#include <ctime>
#include "dish.h"
#include "sticky.h"
#include "parameter.h"
#include "info.h"
#include "crash.h"
#include "pde.h"
#include <iterator>

#include <thread>

#include <chrono>
using namespace std::chrono;

#define EXTERNAL_OFF

extern Parameter par;

using namespace std;


Dish::Dish() {
    
    ConstructorBody();

    // Initial cell distribution is defined by user in INIT {} block
    if (par.load_mcds){
      ImportMultiCellDS(par.mcds_input);
    }
    else{
      CPM=new CellularPotts(&cell, par.sizex, par.sizey);
      if (par.n_chem)
        PDEfield=new PDE(par.n_chem,par.sizex, par.sizey);
      Init();
      if (par.target_area>0)
        for (std::vector<Cell>::iterator c=cell.begin();c!=cell.end();c++) {
            c->SetTargetArea(par.target_area);
        }
    } 
}




Dish::~Dish() {
    cell.clear();
    
    delete CPM;
	
 }

void Dish::Plot(Graphics *g) {
    if (sizechange){
      sizechange = false;
      std::cout << "Changing window size" << std::endl;
      g->Resize(par.sizex*2, par.sizey*2);
    }
    if (CPM)
      CPM->Plot(g);
 }


void Dish::ConstructorBody() {
  
  Cell::maxsigma=0;
  
  // Allocate the first "cell": this is the medium (tau=0)
  cell.push_back(*(new Cell(*this,0)));
  
  // indicate that the first cell is the medium
  cell.front().sigma=0; 
  cell.front().tau=0;
  
  CPM=0;
  PDEfield=0;
    
    h_mcds=0;

}


bool Dish::CellLonelyP(const Cell &c, int **neighbours) const {

  int i;

  for (i=0;i<(int)cell.size();i++) {
    if (neighbours[c.sigma][i]==EMPTY) 
      break;
    else
      if (neighbours[c.sigma][i]>0)
	return false;
  }
  
  return true;
  
}


// Based on code by Paulien Hogeweg.
void Dish::CellGrowthAndDivision(void) {
  
  vector<bool> which_cells(cell.size());

  static int mem_area=0;
  
  // if called for the first time: calculate mem_area
  if (!mem_area) {
    mem_area=TargetArea()/CountCells();
  }
  
  int cell_division=0;

  vector<Cell>::iterator c;
  for ( (c=cell.begin(), c++);
	c!=cell.end();
	c++) {
    
    if ( (c->Area()-c->TargetArea())>c->GrowthThreshold() ) {
      c->IncrementTargetArea();
      
    }
    
    if ( (c->TargetArea() > 2 * mem_area ) ) {
      which_cells[c->Sigma()]=true;
      cell_division++;
    }
  }
 
  // Divide scheduled cells
  if (cell_division) {
    CPM->DivideCells(which_cells);
  }

}


int Dish::CountCells(void) const {
  
  int amount=0;
  vector<Cell>::const_iterator i;
  for ( (i=cell.begin(),i++); i!=cell.end(); i++) {
    if (i->AliveP()) {
      amount++;
    } else {
      cerr << "Dead cell\n";
    }
  }
  return amount;
}

 

int Dish::Area(void) const {
  
  int total_area=0;
  
  vector<Cell>::const_iterator i;
  for ( (i=cell.begin(),i++);
	i!=cell.end();
	++i) {
    
    total_area+=i->Area();
    
  }
  return total_area;
}

int Dish::TargetArea(void) const {
  
  int total_area=0;
  
  vector<Cell>::const_iterator i;
  for ( (i=cell.begin(),i++);
	i!=cell.end();
	++i) {
    
    if (i->AliveP()) 
      total_area+=i->TargetArea();
    
  }
  return total_area;
}



void Dish::SetCellOwner(Cell &which_cell) {
  which_cell.owner=this;
}



void Dish::ClearGrads(void) {

  vector<Cell>::iterator i;
  for ( (i=cell.begin(), i++); i!=cell.end(); i++) {
    i->ClearGrad();
  }
}


int Dish::ZygoteArea(void) const {
    return CPM->ZygoteArea();
}

int Dish::Time(void) const {
    return CPM->Time();
}


void Dish::MeasureChemConcentrations(void) {
 
  // clear chemical concentrations
  for (vector<Cell>::iterator c=cell.begin();
       c!=cell.end();
       c++) {
    for (int ch=0;ch<par.n_chem;ch++) 
      c->chem[ch]=0.;
  }

  // calculate current ones
  for (int ch=0;ch<par.n_chem;ch++)
    for (int i=0;i<SizeX()*SizeY();i++) {
      
      int cn=CPM->Sigma(0,i);
      if (cn>=0) 
	cell[cn].chem[ch]+=PDEfield->Sigma(ch,0,i);
	
    }

    for (vector<Cell>::iterator c=cell.begin();
       c!=cell.end();
       c++) {
      for (int ch=0;ch<par.n_chem;ch++) 
	c->chem[ch]/=(double)c->Area();
    }

}

/* void Dish::ExportMultiCellDS (const char *fname) {
    
    FILE *fp=fopen(fname,"w");
    // Export CA field
    CPM->ExportMultiCellDS(fp);
    
    // Export PDE field
    PDEfield->ExportMultiCellDS(fp);
    
    fclose(fp);
    
}*/

double round(double v, int n) {
    double ten_pow_n=pow(10,n);
    v*=ten_pow_n;
    return round(v)/ten_pow_n;
}


void Dish::MCDS_import_poly(MCDS_io * mcds, int face_id, int id_add){
  int offsetx = (par.sizex / 2) - (mcds->get_highest_x() - ((mcds->get_highest_x() - mcds->get_lowest_x())/2));
  int offsety = (par.sizey / 2) - (mcds->get_highest_y() - ((mcds->get_highest_y() - mcds->get_lowest_y())/2));
  io_face * face = mcds->face_by_id(face_id);
  int** sigma = CPM->getSigma();
  double intersection_points[face->edge_ids.size()+1];
  int id = mcds->face_by_id(face_id)->cell_ids[0];
  std::cout << "poly_add face: " << face_id << std::endl; 
  for (int y = face->lowest_y; y < face->highest_y; y++){
    double ym = y+0.5;
    double lowest = -1;
    double highest = -1;
    int point_index = 0; 
    std:: cout << "Y level: " << y << std::endl;
    for (int edge_id : face->edge_ids){
        io_edge * edge = mcds->edge_by_id(edge_id);
        if(y > edge->lowest_y  && y < edge->highest_y ){
	  std::cout << "Edge_id: " << edge_id << std::endl; 
          double x1 = mcds->node_by_id(edge->node_ids[0])->x;
          double x2 = mcds->node_by_id(edge->node_ids[1])->x;
          double y1 = mcds->node_by_id(edge->node_ids[0])->y;
          double y2 = mcds->node_by_id(edge->node_ids[1])->y;
	  std::cout << "x1: " << x1 << " y1: " << y1 <<  " x2: " << x2 << " y2: " << y2 << std::endl;
	  if (y1 != y2){
	    double res;
	    if(x1 == x2){
	      res = x1;
            }
	    else{
	      double f = (y1-y2)/(x1-x2);
              double a = y1 - x1*f;
              res = (ym-a)/((y2-y1)/(x2-x1));
	    }
            if (res < face->lowest_x){ res = face->lowest_x;}
            if (res > face->highest_x){ res = face->highest_x;}
            if (edge_id == *face->edge_ids.begin()){lowest = res; highest = res;}
            if (res < lowest){ lowest = res;}
            if (res > highest){ highest = res;}
	    std::cout << "Intersection point: " << res << std::endl;
	    intersection_points[point_index] = res;
            point_index++;
	  } 
        }
      }
    intersection_points[point_index+1] = -1;
    for (int x = lowest; x <= highest; x++){
      double xm = x + 0.5;
      int evenodd = 0;
      for (int index =0; index < point_index && intersection_points[index] != -1; index++){ 
         if ((xm - intersection_points[index]) > 0){
            evenodd++;
          }
      }
      if (evenodd%2 == 1){
        int fx = x + offsetx;
        int fy = y + offsety;
        if (fx < 0 || fy < 0 || fx > par.sizex-1 || fy > par.sizey-1){ 
            std::cerr << "OOPS! Polygon outside of mesh!" << std::endl ;continue;} 
        sigma[fx][fy] = id + id_add;
        cell[id + id_add].IncrementTargetArea();
        cell[id + id_add].IncrementArea();
        cell[id + id_add].AddSiteToMoments(fx,fy);
      } 
    }
  }
}


void Dish::MCDS_import_cell(MCDS_io *mcds, int cell_id, int id_add){
  std::cout << "Cell: " << cell_id << std::endl; 
  io_cell * iocell = mcds->cell_by_id(cell_id);
  Cell * n_cell = new  Cell(*this, iocell->mcds_obj->phenotype_dataset().ID());
  n_cell->setSigma(iocell->mcds_obj->ID() + id_add);
  cell.push_back(*n_cell);
  n_cell->setTau(0);
  n_cell->SetTargetArea(0); 
}

void Dish::ImportMultiCellDS(const char *fname){
  MCDS_io mcds(fname);
  mcds.map_cellshape();
  par.sizex = (mcds.get_highest_x() - mcds.get_lowest_x()) * 1.5;
  par.sizey =  (mcds.get_highest_y() - mcds.get_lowest_y()) * 1.5;
  
  int id_add = 0;
  CPM=new CellularPotts(&cell, par.sizex, par.sizey);
    if (par.n_chem)
      PDEfield=new PDE(par.n_chem,par.sizex, par.sizey);
  
  std::map<int, io_cell>* cells = mcds.get_cells();
  for (auto iocell : *cells){
    if (iocell.first == 0){ id_add = 1;}
    int cell_id = iocell.second.mcds_obj->ID();
    MCDS_import_cell( &mcds, cell_id, id_add);
    for (int face_id : iocell.second.face_ids){
      MCDS_import_poly(&mcds, face_id, id_add);
    }
  }
  sizechange = true;
}


void Dish::MCDS_export_cell(MCDS_io *mcds, Cell * cell){
  int cell_id = cell->Sigma();
  std::cout << "Cell_id: " << cell_id << std::endl;
  io_cell * iocell  = mcds->get_new_cell(cell_id);
  
  cell::cell * cell_ds = new cell::cell; 
  phenotype_dataset::phenotype_dataset * p_set = new phenotype_dataset::phenotype_dataset();
  p_set->ID(cell->tau);
 
  phenotype_base::phenotype_type pt = phenotype_base::phenotype_type::current;

  phenotype::phenotype * p = new phenotype::phenotype ;
  p->type(pt);
  phenotype_common::geometrical_properties *gp = new phenotype_common::geometrical_properties; 
 
  common::units_decimal_nonnegative *volume = new common::units_decimal_nonnegative;
  phenotype_common::volumes *volumes = new phenotype_common::volumes; 

  volume->units("square micron");
  volume->base_value(cell->TargetArea());
  volumes->total_volume(volume); 
  gp->volumes(volumes);
 
  phenotype_common::lengths * lengths = new phenotype_common::lengths();
  common::units_decimal_nonnegative * ma_ax = new common::units_decimal_nonnegative;
  common::units_decimal_nonnegative * mi_ax = new common::units_decimal_nonnegative; 
  ma_ax->units("micron");
  mi_ax->units("micron");

  double major_axis, minor_axis;
  double ovx,ovy;
  cell->MajorMinorAxis(&major_axis, &minor_axis, &ovx, &ovy);  
  ma_ax->base_value(major_axis);
  mi_ax->base_value(minor_axis);
  lengths->major_axis(ma_ax);
  lengths->minor_axis(mi_ax);

  gp->lengths(lengths);

  p->geometrical_properties(gp);
  p_set->phenotype().push_back(p);
  cell_ds->phenotype_dataset(p_set);
  cell_ds->ID(cell_id); 
  iocell->mcds_obj = cell_ds;
}

int Dish::MCDS_get_next_node(MCDS_io * mcds, int ** sigma,  vector<int> * nodes, int current, int prev, int startnode, int cell_id){
  io_node * curnode = mcds->node_by_id(current);
  int lowest = -1;
  int lowest_id = -1;
  bool first_round = true;
  //startnode = false;
  int count = 0;
  std::cout << "nodes size: " << nodes->size()  << std::endl;
  for (unsigned long int index = 0; index < nodes->size() + 1; index++){
    count ++;
    if(count > 1000){std::cout << "Loop!" << std::endl; exit(1);}
    int node_id;
    if (index == nodes->size()){
      if (lowest_id == -1){
        node_id = startnode;
      }
      else{
        break;
      }
      //startnode = true;
    }
    else{ 
      node_id = (*nodes)[index];
    }
    std::cout << "Node: " << node_id << std::endl;
    io_node * node = mcds->node_by_id(node_id);
    io_node * prevnode = mcds->node_by_id(prev);
    int dxprev = curnode->x - prevnode->x;
    int dyprev = curnode->y - prevnode->y;
    int startx = curnode->x + 0.5;
    int starty = curnode->y + 0.5; 
    int stopx = node->x + 0.5;
    int stopy = node->y + 0.5;
    int dx = startx - stopx;
    int dy = starty - stopy;
    int xstep = 1, ystep = 1,  addx = 0, addy = 0;
    std::cout << "startx: " << startx << " stopx: " << stopx << " starty: " << starty << " stopy: " << stopy << " xstep: " << xstep << " ystep: "<< ystep  << std::endl;
    if (dx > 0){ if(dxprev > 0){continue;} xstep = -1; addx = -1;}
    if (dy > 0){ if(dyprev > 0){continue;} ystep = -1; addy = -1;}
    if(dxprev < 0 && dx < 0){continue;}
    if(dyprev < 0 && dy < 0){continue;}
    dx = abs(dx);
    dy = abs(dy);
    bool found = false;
    if (dx && !dy){
      found = true;
      for(int xpos = startx + addx; xpos != stopx+addx; xpos+=xstep){ 
        int a = sigma[xpos][starty];
        int b = sigma[xpos][starty-1];
        std::cout << "CheckingX: x: " << xpos << " Y: " << starty << " a: " << a << " b: " << b << std::endl;
        if( a == b || !( a == cell_id || b == cell_id )){found = false; std::cout << "Nope!" << std::endl; break;}
      }
    }
    else if (!dx && dy){
      found = true;
      for(int ypos = starty + addy; ypos != stopy+addy; ypos+=ystep){
        int a = sigma[startx][ypos];
        int b = sigma[startx-1][ypos];
        std::cout << "Checking: x: " << startx << " Y: " << ypos << " a: " << a << " b: " << b <<  std::endl;
        if(a == b || !(a == cell_id || b == cell_id)){found = false; std::cout << "Nope!" << std::endl;break;}
      }
    }
    if (found){
      std::cout << "dx: " << dx << " dy: " << dy << " lowest: " << lowest << std::endl; 
      if (first_round || ((dx + dy) < lowest)){std::cout << "Updated values!" << std::endl; lowest = dx+dy; lowest_id = node_id; first_round = false;}
    }
  }
  if (lowest_id == -1){std::cout << "Failed to find connecting node! Most likely caused by strange geometry." << std::endl; exit(1);}
  return lowest_id;
}


void Dish::MCDS_export_edges_faces(MCDS_io * mcds, int ** sigma){
  int face_id = 0;
  //int amount = 0;
  for (auto cell_it : (*mcds->get_cells())){
    io_cell * cell = mcds->cell_by_id(cell_it.first);
    vector<int> cell_nodes = cell->node_ids;
    vector<int> cell_nodes_track = cell->node_ids;
    std::cout << "==============Cell: " << cell_it.first << " size: " << cell_nodes.size() << std::endl; 
    if(cell_nodes.size() == 0){continue;}
    int startnode = cell_nodes[0];
    std::cout << "Starting node: " << startnode << std::endl; 
    cell_nodes.erase(std::remove(cell_nodes.begin(), cell_nodes.end(), startnode), cell_nodes.end());
    cell_nodes_track.erase(std::remove(cell_nodes_track.begin(), cell_nodes_track.end(), startnode), cell_nodes_track.end());
    int prev = startnode;
    int curnode = -1;
    io_face * face = mcds->get_new_face(face_id);
    cell->face_ids.push_back(face_id);
    face_id++;
    bool startnode_connected = false; 
    while(cell_nodes.size() > 0  || !startnode_connected){
      if (cell_nodes.size() == 0){startnode_connected = true;}
      if (curnode == startnode){
          startnode = cell_nodes[0];
	  curnode = startnode;
	  cell_nodes_track = cell->node_ids;
          cell_nodes_track.erase(std::remove(cell_nodes_track.begin(), cell_nodes_track.end(), startnode), cell_nodes_track.end());
	  cell_nodes.erase(std::remove(cell_nodes.begin(), cell_nodes.end(), startnode), cell_nodes.end());
	  face = mcds->get_new_face(face_id);
          face_id++;
          cell->face_ids.push_back(face_id);
	  std::cout << "=======Face: " << face_id << std::endl;
	  std::cout << "New starting node: " << startnode << std::endl;
      }
      if (curnode == -1){curnode = startnode;}
      std::cout << "Processing node: " << curnode << std::endl;
      int nextnode = MCDS_get_next_node(mcds, sigma, &cell_nodes_track, curnode, prev, startnode, cell_it.first);
      std::cout << "Next node: " << nextnode << std::endl;
      int edge_id = mcds->get_new_edge_uniq(curnode, nextnode);
      face->edge_ids.push_back(edge_id);
      prev = curnode;
      curnode = nextnode; 
      cell_nodes.erase(std::remove(cell_nodes.begin(), cell_nodes.end(), curnode), cell_nodes.end());
      cell_nodes_track.erase(std::remove(cell_nodes_track.begin(), cell_nodes_track.end(), curnode), cell_nodes_track.end());
      //amount ++;
      //if(amount > 1000){std::cout << "Exit due to possible loop" << std::endl; exit(0);};
    } 
  }
}

void Dish::MCDS_export_nodes(MCDS_io * mcds, int ** sigma){
  int node_id = 0;
  for (int y = 0; y <= par.sizey; y++){
    for (int x = 0; x <= par.sizex; x++){
	    std::cout << "export x: " << x << " y: " << y << std::endl; 
      double a = 0, b = 0, c = 0, d = 0;
      if (x > 0 && y > 0){                a = sigma[x-1][y-1];}
      if (y > 0 && x < par.sizex){        b = sigma[x][y-1];}
      if (x > 0 && y < par.sizey){        c = sigma[x-1][y];}
      if (x < par.sizex && y < par.sizey){d = sigma[x][y];}
      if (a > 0 || b > 0 || c > 0 || d > 0){
      std::cout << "X: " << x << " Y: " << y << " A: " << a << " B: " << b << " C: " << c << " D: " << d << std::endl;
      std::cout << " [ "<< a <<"\t] [ " << b << "\t]\n [ " << c << "\t] [ " << d << "\t]\n";}
      set<int> cells;
      if(a>0) {cells.insert(a);}    
      if(b>0) {cells.insert(b);}
      if(c>0) {cells.insert(c);}
      if(d>0) {cells.insert(d);}
      if (cells.size() > 0){
	if (!((a == b && a != c && c == d) ||
	    (b == d && b != a && a == c) ||
	    (d == c && d != b && b == a) ||
	    (c == a && c != d && d == b) ||
	    (a == b && a == c && a == d))){
          io_node * node = mcds->get_new_node(node_id);
          node->x = x -0.5;
          node->y = y -0.5;
          for(int cell_id : cells){
            mcds->cell_by_id(cell_id)->node_ids.push_back(node_id);
            std::cout << "adding: " << node_id << " to cell: " << cell_id << std::endl;
          }
          node->cell_ids = vector<int>(cells.begin(), cells.end()); 
          node_id ++;
        }
      }
    }
  }
}


void Dish::MCDS_export_edges(MCDS_io * mcds, int ** sigma){
  for (auto cell_i : (*mcds->get_cells())){
    int cell_id = cell_i.first;
    io_cell * cell = mcds->cell_by_id(cell_id); 
    std::cout << " cell_id: " << cell_id << std::endl;
    for(int node_id_a : cell->node_ids) {
      std::cout << " node_id_a: " << node_id_a << std::endl;
      io_node * node_a = mcds->node_by_id(node_id_a);
      int closest_x = -1;
      int distance_x = -1;
      int closest_y = -1;
      int distance_y = -1;
      int sx = node_a->x +0.5;
      int sy = node_a->y +0.5;
      for(int node_id_b : cell->node_ids){
        std::cout << " node_id_b: " << node_id_b << std::endl;
	io_node * node_b = mcds->node_by_id(node_id_b);
	double dx = node_a->x - node_b->x;
	double dy = node_a->y - node_b->y;
	int  b = 0, c = 0, d = 0;
        if (sy > 0 && sx < par.sizex){        b = sigma[sx][sy-1];}
        if (sx > 0 && sy < par.sizey){        c = sigma[sx-1][sy];}
        if (sx < par.sizex && sy < par.sizey){d = sigma[sx][sy];}
        std::cout << " [ -\t] [ " << b << "\t]\n [ " << c << "\t] [ " << d << "\t]\n";
	bool going_right = (dx < 0 && dy == 0);
	bool going_down = (dy < 0 && dx == 0);
	bool is_on_edge_down = going_down  && ((c != d) && (c == cell_id || d == cell_id));
	bool is_on_edge_right = going_right && ((b != d) && (b == cell_id || d == cell_id));
        	
        std::cout << " going_right: " << going_right << " going_down: " << going_down << " is_on_edge_right: " << is_on_edge_right << " is_on_edge_down: " << is_on_edge_down << " dx: " << dx << " dy: " << dy << " sx: " << sx << " sy: " << sy << std::endl;
	if ((abs(dx) < distance_x || closest_x == -1) && is_on_edge_right){
          distance_x = abs(dx); closest_x = node_id_b;
	  std::cout << "Added X!" << std::endl;
	}
	if((abs(dy) < distance_y || closest_y == -1) && is_on_edge_down){
	  distance_y = abs(dy); closest_y = node_id_b;
	  std::cout << "Added Y!" << std::endl;
	}
      }
      if(closest_x != -1){
        int edge_id = mcds->get_new_edge_uniq(node_id_a, closest_x);
        cell->edge_ids.push_back(edge_id);
        mcds->edge_by_id(edge_id)->cell_ids.push_back(cell_i.first);  
      }
      if(closest_y != -1){
        int edge_id = mcds->get_new_edge_uniq(node_id_a, closest_y);
        cell->edge_ids.push_back(edge_id);
        mcds->edge_by_id(edge_id)->cell_ids.push_back(cell_i.first);
      }

    }
  }
}

void Dish::MCDS_export_faces(MCDS_io * mcds){
  int face_id = 0;
  for (auto cell_i : (*mcds->get_cells())){
    io_cell * cell = mcds->cell_by_id(cell_i.first);
    io_face * face = mcds->get_new_face(face_id);
    for (int edge_id : cell->edge_ids){
      face->edge_ids.push_back(edge_id);
    }
    cell->face_ids.push_back(face_id);
    face_id++;
  }
}

void Dish::MCDS_denoise_CPM(int ** sigma_in, int ** sigma_out){
  std::cout << "sizex: " << par.sizex << " sizey: " << par.sizey << std::endl;
  for (int y = 0; y < par.sizey; y++){
    for (int x = 0; x < par.sizex; x++){
      std::cout << "denoise x: " << x << " y: " << y << std::endl;
      std::cout << sigma_in[x][y] << std::endl;
      int most = 0;
      std::map<int, int> count;
      for (int y_eye = y-1; y_eye <= y+1; y_eye++){
        for (int x_eye = x-1; x_eye <= x+1; x_eye++){
	  int val = -1;
	  if (x_eye < par.sizex && x_eye > 0 && y_eye < par.sizey && x_eye > 0)
            val = sigma_in[x_eye][y_eye];
	  if (count.find(val) == count.end()) count[val] = 0;
	  else count[val] += 1;
	  if (count[val] >= count[most]){most = val;}
	}
      }
      std::cout << "Ratio: " << (float)count[most] / 9 << std::endl;
      if(most != -1){
        std::cout << "Replacing with most!" << std::endl;
        sigma_out[x][y] = most;
      } 
      else{
	std::cout << "Leaving it!" << std::endl;
        sigma_out[x][y] = sigma_in[x][y];
      }
    }
  }
}



int** Dish::MCDS_AllocateTmpSigma(){
  int ** sigma;

  int sizex=par.sizex; int sizey=par.sizey;

  sigma=(int **)malloc(sizex*sizeof(int *));
  if (sigma==NULL)
    MemoryWarning();

  sigma[0]=(int *)malloc(sizex*sizey*sizeof(int));
  if (sigma[0]==NULL)
    MemoryWarning();


  {for (int i=1;i<sizex;i++)
    sigma[i]=sigma[i-1]+sizey;}
  return sigma;
}

void Dish::ExportMultiCellDS(const char *fname){
  int ** sigma = CPM->getSigma();
  int ** tmpsigma = MCDS_AllocateTmpSigma();
  for (int i = 0; i < 30; i++)
    CPM->AmoebaeMove(0, true); 
  MCDS_denoise_CPM(sigma, tmpsigma); 
  MCDS_denoise_CPM(tmpsigma, sigma);
  MCDS_io mcds;
  for (vector<Cell>::iterator c = cell.begin()+1; c != cell.end(); c++){
    MCDS_export_cell( &mcds, &(*c));
  }
  MCDS_export_nodes(&mcds, sigma);
  //for (auto cell_test: (*mcds.get_cells())){
  //  std::cout << "Cell: " << cell_test.first << std::endl;
  //  for (int node_id: cell_test.second.node_ids){
  //   io_node * node = mcds.node_by_id(node_id);
  //   std::cout << "node: " << node_id << " x: " << node->x << " y: " << node->y << std::endl;
  //  }
  //}
  MCDS_export_edges_faces(&mcds, sigma); 
  MCDS_export_edges(&mcds, sigma);
  MCDS_export_faces(&mcds);
  mcds.finalize_cellshapes(); 
  mcds.add_metadata("tst_metadata.xml");
  mcds.add_time();
  mcds.write(fname);
  std::cout << "Done exporting!" << std::endl; 
  //sigma = tmpsigma;
  delete tmpsigma;
}

//void OLDExportMultiCellDS (const char *fname) {
//    
//    // Setup for MultiCellDS output
//    MultiCellDS *h = new MultiCellDS;
//
//    // Create a list of individual cells for MultiCellDS
//    cell::cell_population_individual *cpi = new cell::cell_population_individual;
// 
//    //mesh::list_of_voxels = new mesh::list_of_voxels;
//    mesh::mesh *mesh = CPM->CreateMultiCellDSMesh();
//    
//    // Create a phenotype for target areas and so forth
//    dei
//    phenotype::phenotype *p; p = new phenotype::phenotype;
//    phenotype_base::phenotype_type pt = phenotype_base::phenotype_type::target; // Select the current phenotype instead of target or expected
//    p->type(pt); // Place the phenotype type into the phenotype
//    
//    
//    /*phenotype_common::geometrical_properties *gp = new phenotype_common::geometrical_properties;
//    common::units_decimal_nonnegative *target_area_dec = new common::units_decimal_nonnegative;
//    phenotype_common::target_areas_3D *areas_xml = new phenotype_common::target_areas_3D;
//    double target_area = round(par.target_area*par.dx*par.dx)*1e+12); // convert to square microns
//    target_area_dec->units("square micron");
//    area_dec->base_value(area);
//    areas_xml->total_surface_area(area_dec);
//    cout << area << "\n";
//
//    gp->*/
//    
//    
//   // p->geometrical_properties(gp); // Place geometric properties in phenotype
//    
//    /*mesh::bounding_box bb= new mesh::bounding_box;
//    mesh::double_list bb_udl=new mesh::units_double_list;
//    
//    common::units_decimal *bb_dec = new common::units_decimal;
//    bb_dec->units("micron");
//    bb_dec->base_value(sizex*par.dx);*/
//    
//    
//    // get pixels from cells and push to mesh
//    vector < list < pair< int, int > > > cellpixels(cell.size());
//    mesh::list_of_voxels *voxlist = new mesh::list_of_voxels;
//   // voxlist->choice_arm(mesh::list_of_voxels::voxel_tag);
//    for (int x=1;x<CPM->SizeX()-1;x++) {
//        for (int y=1;y<CPM->SizeY()-1;y++) {
//            
//            int ID=CPM->Sigma(x,y);
//            // add voxel to mesh
//            /*mesh::voxel *vox = new mesh::voxel;
//            common::units_double_list *center = new common::units_double_list;
//            center->units("micron");
//            center->push_back(x*par.dx*1e+6);
//            center->push_back(y*par.dx*1e+6);
//            center->push_back(0.);
//            vox->center(center);
//            static common::units_decimal_nonnegative *vol = new common::units_decimal_nonnegative;
//            vol->base_value(par.dx*par.dx*1e+12);
//            vol->units("micron cubed");
//            vox->volume(vol);
//            vox->ID(ID);*/
//            
//            
//            // HELP: how do I add the voxels to a voxellist?
//            //cerr << "trying to push_back voxel" << endl;
//  
//           // voxlist->voxel().push_back(vox);
//           
//            
//            // store the list of voxels per cell
//            if (ID) {
//                cellpixels[ID].push_back(pair<int, int>(x,y));
//            }
//        }
//    }
//    //mesh->voxels(voxlist);
//    
//    // For each individual cell ...
//    for (vector<Cell>::iterator c=cell.begin();
//         c!=cell.end();
//         c++) {
//    
//        if (c->Sigma()==0) continue;
//            // Create a new cell for MultiCellDS
//        cell::cell *mcds_cell = new cell::cell;
//        cout  << "Created an mcds_cell for cell " << c->Sigma() << "\n";
//        // Setup for obtaining different aspects of cellular data
//        phenotype_dataset::phenotype_dataset *pds = new phenotype_dataset::phenotype_dataset;
//        phenotype_common::geometrical_properties *gp = new phenotype_common::geometrical_properties;
//       
//        pds->ID(c->tau); 
//        // Translate cell radius from CPM to MultiCellDS
//        common::units_decimal_nonnegative *major_axis_dec = new common::units_decimal_nonnegative; // Setup a units_decimal element
//        common::units_decimal_nonnegative *minor_axis_dec = new common::units_decimal_nonnegative; // Setup a units_decimal element
//        phenotype_common::lengths *lengths_xml = new phenotype_common::lengths; // Setup up the parent container of radius
//       
//        double major_axis, minor_axis;
//        double ovx,ovy;
//        c->MajorMinorAxis(&major_axis, &minor_axis, &ovx, &ovy);
//       
//        // store major and minor axis
//        major_axis=round(major_axis*par.dx*1e+6,1);
//        minor_axis=round(minor_axis*par.dx*1e+6,1);
//        major_axis_dec->units("micron"); // Get and the units
//        major_axis_dec->base_value(major_axis); // Set the radius
//        lengths_xml->major_axis(major_axis_dec); // Place the radius in lengths
//        minor_axis_dec->units("micron"); // Get and the units
//        minor_axis_dec->base_value(minor_axis); // Set the radius
//        lengths_xml->minor_axis(minor_axis_dec); // Place the radius in lengths
//        
//        // store orientation
//        state::orientation *orientation=new state::orientation;
//        orientation->formalism(state::orientation_formalism::Unit_Vector);
//        
//        orientation->units("");
//        orientation->push_back(ovx);
//        orientation->push_back(ovy);
//        
//        
//
//        gp->lengths(lengths_xml); // Place lengths in geometric properties
//        //cout << radius << "\n" << endl;
//        
//        
//        // Translate cell volume from CPM to MultiCellDS
//       // cout << "Calculating volume... ";
//        common::units_decimal_nonnegative *volume_dec = new common::units_decimal_nonnegative;
//        phenotype_common::volumes *volumes_xml = new phenotype_common::volumes;
//        double volume = round((c->Area()*par.dx*par.dx)*1e+12); // convert to square microns
//        volume_dec->units("square micron");
//        volume_dec->base_value(volume);
//        volumes_xml->total_volume(volume_dec);
//        
//        /*cout << "Calculating area... ";
//        common::units_decimal_nonnegative *area_dec = new common::units_decimal_nonnegative;
//        phenotype_common::areas_3D *areas_xml = new phenotype_common::areas_3D;
//        double area = round((c->Area()*par.dx*par.dx)*1e+12); // convert to square microns
//        area_dec->units("square micron");
//        area_dec->base_value(area);
//        areas_xml->total_surface_area(area_dec);
//        cout << area << "\n";
//         */
//
//        // Places volumes in geometric properties
//        //gp->areas(areas_xml);
//        gp->volumes(volumes_xml);
//        
//        // Create a phenotype
//        phenotype::phenotype *p; p = new phenotype::phenotype;
//        p->geometrical_properties(gp); // Place geometric properties in phenotype
//        phenotype_base::phenotype_type pt = phenotype_base::phenotype_type::current; // Select the current phenotype instead of target or expected
//        p->type(pt); // Place the phenotype type into the phenotype
//        
//        // Put the phenotype into the phenotype dataset
//        for(int i=0; i<1; i++)
//            pds->phenotype().push_back(p);
//
//        // Add the phenotype dataset to the cell
//        mcds_cell->phenotype_dataset(pds);
//        
//        // Work on the cell state
//        state::state *state = new state::state;
//        common::units_string *str = new common::units_string;
//        common::units_double_list *udl = new common::units_double_list;
//        
//        
//        // Translate position from CPM to MultiCellDS
//        double cx, cy, cz;
//        cz=0.; // 2D
//        c->GetCentroid(&cx, &cy);
//
//        
//        // convert from pixel to micron
//        cx=round((cx*par.dx)*1e+6,2);
//        cy=round((cy*par.dx)*1e+6,2);
//        
//        udl->push_back(cx); udl->push_back(cy); udl->push_back(cz);
//        udl->units("micron");
//        state->position(udl);
//        state->orientation(orientation);
//        // store orientation (calculated above in "MajorMinorAxis"
//        
//       // state->orientation(
//     
//        //cell::population_vector = new cell::population_vector;
//        
//         mesh::int_list_xpath *voxels = new mesh::int_list_xpath;
//         for (list< pair<int, int> >::const_iterator v=cellpixels[c->Sigma()].begin();
//         v!=cellpixels[c->Sigma()].end();
//         v++) {
//         voxels->push_back((unsigned int)v->first);
//         voxels->push_back((unsigned int)v->second);
//         voxels->push_back(0);
//         voxels->grouping_number(3); // How many numbers are grouped to make an index
//         voxels->xpath("/MultiCellDS/cellular_information/mesh/voxels/"); // Where to find the voxels that the index uses. Use XPATH to navigate through the XML tree.
//         
//         }
//        state->voxels(voxels);
//
//        cout << "(" << cx << ")" << endl;
//        // Add state to the cell
//        mcds_cell->state(state);
//        
//        // Add an ID number to the cell
//        mcds_cell->ID(c->Sigma());
//        
//        // Add the cell to the cell population list
//        cpi->cell().push_back(mcds_cell);
//        
//     
//    }
//    
//    
//    // Allow cell populations to have a population of individual cells.
//    cell::cell_populations *cps = new cell::cell_populations;
//    cps->cell_population(cpi);
//    cout << "So far so good" << endl;
//    
//    // Allow cellular information to have cell populations
//    cell::cellular_information *ci = new cell::cellular_information;
//    ci->cell_populations(cps);
//    cout << "So far so good" << endl;
//    //mesh->voxels(voxels);
//    ci->mesh(mesh);
//    
//    // Allow the root MultiCellDS element to have cellular information
//    h->cellular_information(ci);
//    
//    MCDS_type mcds_type;// = new MCDS_type;
//    mcds_type.value(MCDS_type::value_type::snapshot_simulation); // This is a simulation snapshot (vs experiemnt or clinical)
//    h->type(mcds_type); // Assign the type over to the MultiCellDS element
//    h->version("0.5.0"); // State the MultiCellDS version number
//    
//    // Add PDE fields
//    cout << "Trying to add PDE field\n";
//    PDEfield->AddToMultiCellDS(h);
//    
//    //############################################################
//    // Adding metadata. Read it in from a file. Easier than
//    // declaring all kinds of objects.
//    //############################################################
//    
//    // Parse the metadata file.
//    //
//    MultiCellDS_paggr MultiCellDS_p;
//    xml_schema::document_pimpl doc_p (MultiCellDS_p.root_parser (),
//                                      MultiCellDS_p.root_name ());
//    MultiCellDS_p.pre ();
//    
//    // Adding metadata
//    doc_p.parse("tst_metadata.xml");
//    MultiCellDS* h_meta = MultiCellDS_p.post ();
//    
//    // Update the created and last_modified_times
//    //auto current_time = std::chrono::system_clock::now();
//    std::time_t t = std::time(NULL);
//    struct tm lt = *std::localtime(&t);
//    
//    // Handle timezones
//    time_t offset_second(lt.tm_gmtoff);
//    tm off_t = *std::gmtime(&offset_second);
//    short timezone_hour = (off_t.tm_hour+12)%24-12, timezone_minute = off_t.tm_min;
//    
//    xml_schema::date_time new_times(lt.tm_year+1900, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec, timezone_hour, timezone_minute);
//    h_meta->metadata().created(new_times); // Copy time over
//    h_meta->metadata().last_modified(new_times); // Copy time over
//    h->metadata(&h_meta->metadata()); // Copy metadata over. Could also use _clone()
//    
//    
//    // Setup for printing the MultiCellDS file
//    MultiCellDS_saggr MultiCellDS_s, MultiCellDS_s2;
//    
//    // doc_s is intended for printing to the screen
//    // doc_s2 is intended for printing to a file
//    
//    // XSD/e setup for printing
//    xml_schema::document_simpl doc_s (MultiCellDS_s.root_serializer (),
//                                      MultiCellDS_s.root_name ());
//    //xml_schema::document_simpl doc_s2 (MultiCellDS_s2.root_serializer (),
////                                       MultiCellDS_s2.root_name ());
//    
//    // Initialization
//    MultiCellDS_s.pre (*h);
//    //MultiCellDS_s2.pre (*h);
//    // Print to the screen
//    //doc_s.serialize (cout, xml_schema::document_simpl::pretty_print);
//    
//    // Pick a file to write
//    ofstream ofs(fname);
//    // Print to the file
//    
//    doc_s.serialize (ofs, xml_schema::document_simpl::pretty_print);
//    ofs << endl; // Add an extra newline at the end of the file
//    
//    // Cleanup of the writing
//    MultiCellDS_s.post ();
//    //MultiCellDS_s2.post ();
//}


//void Dish::SetMultiCellDSImport (const char *fname) {
//    // Parse the MultiCellDS file
//    //
//    MultiCellDS_paggr MultiCellDS_p;
//    xml_schema::document_pimpl doc_p (MultiCellDS_p.root_parser (),
//                                      MultiCellDS_p.root_name ());
//    MultiCellDS_p.pre ();
//    
//    doc_p.parse(fname);
//    h_mcds = MultiCellDS_p.post ();
//    
//    // get grid size
//    int sx=h_mcds->cellular_information().mesh().x_coordinates().size();
//    int sy=h_mcds->cellular_information().mesh().y_coordinates().size();
//    int sz=h_mcds->cellular_information().mesh().z_coordinates().size();
//   
//    if (sz>1) {
//        cerr << "No 3D meshes supported. (Adapt implementation of ImportMultiCellDS to choose a slice)" << endl;
//    }
//  
//par.sizex=sx;
//par.sizey=sy;
//    
//}


//int Dish::SetMultiCellDSCells(void) {
//    
//    if (h_mcds) {
//    // loop over all cells
//    for (cell::cell_population_individual::cell_iterator c =
//         h_mcds->cellular_information().cell_populations().cell_population().cell().begin();
//         c != h_mcds->cellular_information().cell_populations().cell_population().cell().end();
//         c++) {
//        Cell * n_cell = new  Cell(*this, c->phenotype_dataset().ID());
//        n_cell->setSigma(c->ID());
//        cout << "CellID: " << c->ID() << endl; 
//        cell.push_back(*n_cell);
//        CPM->SetMultiCellDSCell(*c);
//        n_cell->setTau(0);
//        n_cell->SetTargetArea(par.target_area); 
//        //n_cell->MeasureCellSize(*n_cell);
//        }
//    // Get fields
//        PDEfield->ReadFromMultiCellDS(h_mcds);
//        CPM->MeasureCellSizes();
//        return 0;
//    }
//    return 1; // error
//}



int Dish::SizeX(void) { return CPM->SizeX(); }
int Dish::SizeY(void) { return CPM->SizeY(); }	
