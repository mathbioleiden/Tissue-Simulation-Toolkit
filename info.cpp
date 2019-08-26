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
#include <iostream>
#include <math.h>
#include <fstream>
#ifndef __APPLE__
#include <malloc.h>
#endif
#include "dish.h"
#include "graph.h"
#include "info.h"
#include "parameter.h"
#include "misc.h"
#include "parse.h"

extern Parameter par;

using namespace std;

Info::Info(Dish &d, Graphics &g, std::ostream &out) {

  dish=&d;
  graphics=&g;
  os=&out;

  /*
  g=&graphics;
  beast=&dish;
  os=&out;*/
}

void Info::Menu() {

  // Graphics should be defined
  if (!graphics) return;

  int x,y;
  char key=(char)graphics->GetXYCoo(&x,&y);

  switch (key) {

    /*  case RESIZE:
	dish->CPM->Replace(graphics);
	break;
    */


  case 'M':
    {
      extern Parameter par;
      *os << "lambda = " << par.lambda << endl;
      *os << "lambda = "; ReadDouble(stdin,&par.lambda);
      *os << "lambda = " << par.lambda << endl;
    }
    break;

  case 'v':
    {
      cout << "Areas and deviations from target area:\n";

      int t=0;
      vector<Cell>::const_iterator i;
      for ( (i=dish->cell.begin(), i++); i!=dish->cell.end(); i++) {
	t+=i->Area() - i->TargetArea();
	*os << i->Sigma() << " " << i->Area()-i->TargetArea() << " "
	    << i->Area() << " " << i->TargetArea();
	if (!i->AliveP()) {
	  *os << " Dead. ";
	}
	*os << "\n";
      }
      *os << "Mean deviation from target: " << (double)t/((double)dish->cell.size()-1) << "\n";
    }
    break;

  case 'V':

    {
      int t=0;
      vector<Cell>::iterator i;
      for ( (i=dish->cell.begin(), i++); i!=dish->cell.end(); i++) {

	//extern double lambda; int ll; char tempstring[100];
	t+=i->Area() - i->TargetArea();
	*os << i->Sigma() << " " << i->Area() - i->TargetArea() << " "
	    << i->Area() << " " << i->TargetArea() << "\n";
	i->SetTargetArea(i->Area());
      }

      *os << "Mean deviation from target: " << (double)t/((double)dish->cell.size()-1) << "\n";
    }
    break;

  case 'L':
    {
      extern Parameter par;
      *os << "lambda = " << par.lambda << ", new lambda? \n";
      ReadDouble(stdin,&par.lambda);
      *os << "lambda = " << par.lambda << "\n";
    }
    break;


  case 'o':
    {
      printf("Click cell to dump... Click Medium to quit.\n");

      Cell *dumpcell;
      do {
	while (graphics->GetXYCoo(&x,&y)!=1);
	dumpcell=&dish->cell[dish->CPM->Sigma(x/2,y/2)];
	printf("Colour of cell %d is %d.\n",dumpcell->Sigma(), dumpcell->Colour());
	printf("Volume of cell %d is %d.\nTarget area is %d.\nArea deviation %d.\n",
	       dumpcell->Sigma(),dumpcell->Area(),
	       dumpcell->TargetArea(),
	       dumpcell->Area()-dumpcell->TargetArea() );
	printf("----------------------------------------------\n\n");
      } while (dumpcell->Sigma()!=0);
    }
    break;

  case 'c':
    {
      printf("Introduce tumor cell into the grid...\n");
      fflush(stdin);
      while (graphics->GetXYCoo(&x, &y)!=1);

      //dish->ClickCell(x/2,y/2);
      printf("Introducing cell at %d %d\n",x/2,y/2);
      int tumorcell=dish->CPM->GrowInCells(1, par.size_init_cells, x/2, y/2, 0,0 );
      Cell &tcell = dish->CPM->AddCell(*dish);
      dish->CPM->MeasureCellSize(tcell);

      tcell.setTau(2);
      tcell.SetTargetLength(10);
      tcell.SetTargetArea(50);

      cerr << "tumorcell = " << tumorcell << endl;
      cerr << "tcell.Sigma() = " << tcell.Sigma() << endl;
    }
    break;
  case 'N':
    {
      cerr << "Getting neighbors\n";
      int **neighbours=dish->CPM->SearchNeighbours();
      vector<Cell>::iterator i;
      for ( (i=dish->cell.begin(),i++); i!=dish->cell.end(); i++){
	printf("Neighbours of cell %d are : ",i->Sigma());
	for (int j=0; j<=(signed int)(dish->cell.size()); j++){
	  if (neighbours[i->Sigma()][j]>=0)
	    printf("%d ",neighbours[i->Sigma()][j]);

	}
	printf("\n");
      }
      printf(" \n");
      free (neighbours[0]);
      free (neighbours);
    }
    break;

  case '#':
    printf("number of (living) cells = %d \n",dish->CountCells());
    break;


  case 'A':
    {
      vector<Cell>::const_iterator i;
      for ( (i=dish->cell.begin(),i++);
	    i!=dish->cell.end(); i++) {

	printf("Cell: %d, mother: %d\n time of birth: %d\n divisions: %d\n type at birth: %d\n current type: %d\n daughter: %d\n",
	       i->Sigma(),i->Mother(),i->DateOfBirth(),i->TimesDivided(),
	       i->ColourOfBirth(),i->Colour(),i->Daughter());

	if (i->Daughter()>0) {
	  printf("colour of daughter: %d\n",
		 dish->cell[i->Daughter()].Colour());
	}

	if (!i->AliveP())
	  printf(" Dead \n");

      }
    }
    break;

  case 'q':
    if (YesNoP("Quit: are you sure?"))
      throw "Exiting program";
    break;
  }

  //  AuxMenu(key);
}



Cell &Info::ClickCell(Graphics *graphics) {

  int x,y;
  while (graphics->GetXYCoo(&x,&y)!=1);
  return dish->cell[dish->CPM->Sigma(x/2,y/2)];
}


void Info::WriteCOM(int cell_id, std::ostream &out) {

  // Write the center of mass to "out"

  static int t=0;
  double com_x=0.;
  double com_y=0.;
  int n=0;
  for (int x=1;x<dish->SizeX()-1;x++)
    for (int y=1;y<dish->SizeY()-1;y++) {
      if (dish->CPM->Sigma(x,y)==cell_id) {
	com_x+=x;
	com_y+=y;
	n++;
      }
    }

  com_x/=(double)n;
  com_y/=(double)n;

  out << t++ << " " << cell_id << " " << com_x << " " << com_y << "\n";

}

void Info::WriteCOMs(std::ostream &out) {

  // Write the center of mass to "out"



  int cell_number=par.n_init_cells;
  static int t;
  for (int s=1;s<cell_number+1;s++){
  double com_x=0.;
  double com_y=0.;
  int n=0;
  for (int x=1;x<dish->SizeX()-1;x++)
    for (int y=1;y<dish->SizeY()-1;y++) {
      if (dish->CPM->Sigma(x,y)==s) {
	com_x+=x;
	com_y+=y;
	n++;
      }
    }

  com_x/=n;
  com_y/=n;

  out << t << " " << s << " " << com_x << " " << com_y << " " << n << "\n";}
  t++;

}

void Info::WriteCOMsTorus(std::ostream &out) {

  // Write the center of mass to "out" based on the internal COMs
  int cell_number=par.n_init_cells;
  static int t;
  for (int s=1;s<cell_number+1;s++){
  double com_x= (double)dish->getCell(s).sum_x/(double) dish->getCell(s).area;
  double com_y= (double)dish->getCell(s).sum_y/(double) dish->getCell(s).area;
  double vector_x=dish->getCell(s).getVectorActX();
  double vector_y=dish->getCell(s).getVectorActY();
  int n =dish->getCell(s).Area();

  out << t << " " << s << " " << com_x << " " << com_y << " " << n <<  " " << vector_x << " " << vector_y << "\n";}
  t++;

}

void Info::WriteCOMsTorusFresh(std::ostream &out) {

  // Write the center of mass to "out"



  int cell_number=par.n_init_cells;
  static int t;
  for (int s=1;s<cell_number+1;s++){
  double com_x;
  double com_y;
  double com_x_left=0.;
  double com_x_right=0.;
  double com_y_top=0.;
  double com_y_bottom=0.;
  bool top_row=false;
  bool bottom_row=false;
  bool left_row=false;
  bool right_row=false;
  int n_bottom=0;
  int n_top=0;
  int n_left=0;
  int n_right=0;
  //check bottom left quadrant
  for (int x=1;x<(dish->SizeX()-1)/2;x++){
    for (int y=1;y<(dish->SizeY()-1)/2;y++) {
      if (dish->CPM->Sigma(x,y)==s) {
        if (x==1){ left_row=true;}
        if (y==1){ bottom_row=true;}
      com_x_left+=x;
      com_y_bottom+=y;
      n_left++;
      n_bottom++;
      }
    }}
    //check top left quadrant
  for (int x=1;x<(dish->SizeX()-1)/2;x++){
    for (int y=(dish->SizeY()-1)/2;y<dish->SizeY()-1;y++) {
      if (dish->CPM->Sigma(x,y)==s) {
        if (x==1){ left_row=true;}
        if (y==dish->SizeY()-2){ top_row=true;}
      com_x_left+=x;
      com_y_top+=y;
      n_left++;
      n_top++;
      }
    }}
    //check bottom right quadrant
    for (int x=(dish->SizeX()-1)/2;x<dish->SizeX()-1;x++){
      for (int y=1;y<(dish->SizeY()-1)/2;y++) {
        if (dish->CPM->Sigma(x,y)==s) {
          if (x==dish->SizeX()-2){ right_row=true;}
          if (y==1){ bottom_row=true;}
        com_x_right+=x;
        com_y_bottom+=y;
        n_right++;
        n_bottom++;
        }
      }}
    //check top right quadrant
    for (int x=(dish->SizeX()-1)/2;x<dish->SizeX()-1;x++){
      for (int y=(dish->SizeY()-1)/2;y<dish->SizeY()-1;y++) {
        if (dish->CPM->Sigma(x,y)==s) {
          if (x==dish->SizeX()-2){ right_row=true;}
          if (y==dish->SizeY()-2){ top_row=true;}
        com_x_right+=x;
        com_y_top+=y;
        n_right++;
        n_top++;
        }
      }}
  if (right_row==true && left_row && true){
    com_x=(double)(com_x_left+com_x_right+n_left*dish->SizeX())/(double)(n_left+n_right);
  }
  else{
    com_x=(double)(com_x_left+com_x_right)/(double)(n_left+n_right);
  }
  if (top_row==true && bottom_row && true){
    com_y=(double)(com_y_top+com_y_bottom+n_bottom*dish->SizeY())/(double)(n_top+n_bottom);
  }
  else{
    com_y=(double)(com_y_top+com_y_bottom)/(double)(n_top+n_bottom);
  }

  if (abs(dish->getCell(s).getCenterX()-com_x)>10){
      double new_x = com_x-round( (com_x-dish->getCell(s).getCenterX() )/ dish->SizeX()) * dish->SizeX();
      com_x=new_x;
  }
  if (abs(dish->getCell(s).getCenterY()-com_y)>10){
      double new_y = com_y-round((com_y-dish->getCell(s).getCenterY())/dish->SizeY()) * dish->SizeY();
      com_y=new_y;
  }


  out << t << " " << s << " " << com_x << " " << com_y << " " << n_left+n_right << "\n";}
  t++;

}

void Info::WriteCellLocations(int cell_id, int field_id, std::ostream &out){
	static int t=0;
	for (int x=1;x<dish->SizeX()-1;x++)
	    for (int y=1;y<dish->SizeY()-1;y++) {
	       if (dish->CPM->Sigma(x,y)==cell_id) {
			out << t << " " << x << " " << y << " " << dish->PDEfield->Sigma(field_id,x,y) << "\n";
		}}
	t++;
}
