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
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
//#include <unistd.h>
#include <math.h>
#include "dish.h"
#include "random.h"
#include "cell.h"
#include "info.h"
#include "parameter.h"
#include "sqr.h"

#ifdef QTGRAPHICS
#include "qtgraph.h"
#else
#include "x11graph.h"
#endif


using namespace std;

INIT {

  try {
    // Define initial distribution of cells
    cout<< "Initialization"<< endl;
    CPM->ReadZygotePicture();
    //CPM->GrowInCells(par.n_init_cells,par.size_init_cells,par.subfield);
    CPM->ConstructInitCells(*this);
    CPM->InitializeMatrix(*this);

  } catch(const char* error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }

}

TIMESTEP {
  try {
    static int i=0;
    static Dish *dish=new Dish();
    static Info *info=new Info(*dish, *this);
    dish->CPM->AmoebaeMove(dish->PDEfield);
    if (par.max_Act && par.lambda_Act){
      dish->PDEfield->MILayerCA(3,1.,dish->CPM, dish);
      dish->PDEfield->AgeLayer(2,1.,dish->CPM, dish);
    }
//Writing center of mass and area of each cell
    char buff[400];
    snprintf(buff, sizeof(buff), "%s/cellcenter.txt",par.datadir);
    std::string buffAsStdStr = buff;
    std::ofstream out(buff, ios::app);
    //info->WriteCOMsTorus(out);

//Writing locations of adhesions per cell
  // if (!(i%par.adhesion_storage_stride)) {
  //   char buff3[400];
  // 	 snprintf(buff3, sizeof(buff3), "%s/celladhesion.txt",par.datadir);
  // 	 std::string buffAsStdStr3 = buff3;
  //  	 std::ofstream out3(buff3, ios::app);
  //        info->WriteAdhesionsLocationsPerCell(1, 1, out3);
  //      }
 //

//plot to screen and file
    if (par.graphics && !(i%par.storage_stride)) {
      BeginScene();
      ClearImage();
      dish->Plot(this);
      //dish->PDEfield->PlotInCells (this, dish->CPM,2);

      // You need to call "ClearImage" if no PDE field is plotted,
      // because the CPM medium is considered transparant
      char title[400];
//      snprintf(title,399,"CellularPotts: %.2f hr",dish->PDEfield->TheTime()/3600);
      snprintf(title,399,"CellularPotts: %d MCS",i);
      //ChangeTitle(title);
      EndScene();
      info->Menu();
    }

    if (par.store && !(i%par.storage_stride)) {
      char fname[200];
      sprintf(fname,"%s/extend%05d.png",par.datadir,i);
      BeginScene();
      ClearImage();
      //dish->PDEfield->PlotInCells (this, dish->CPM, 2);
      dish->CPM->SearchNandPlotClear(this);
      EndScene();

      // Write(fnamematrix);
       Write(fname);
    }
    i++;
    } catch(const char* error) {
      cerr << "Caught exception\n";
      std::cerr << error << "\n";
      exit(1);
    }
}

void PDE::Secrete(CellularPotts *cpm) {
  const double dt=par.dt;
  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++) {
      // inside cells
      if (cpm->Sigma(x,y)) {

	sigma[0][x][y]+=par.secr_rate[0]*dt;

      } else {
      // outside cells
	sigma[0][x][y]-=par.decay_rate[0]*dt*sigma[0][x][y];

      }
    }
}


void PDE::InitializeAgeLayer(int l,double value,CellularPotts *cpm){
  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++){
	if(sigma[l][x][y]>0){
	    sigma[l][x][y]=value;}
	else {sigma[l][x][y]=0.;}

    }
}


void PDE::AgeLayer(int l,double value,CellularPotts *cpm, Dish *dish){
  for (const auto elem: cpm->actPixels){
    /* ... process elem ... */
    if(elem.second>0.)
      cpm->actPixels[elem.first]-=value;
  }
}


void PDE::MILayerCA(int l, double value, CellularPotts *cpm, Dish *dish){
  for (const auto &elem: cpm->alivePixels){
    int x=elem[0];
    int y =elem[1];
    int sigma_c=cpm->Sigma(x,y);
    int new_sigma=cpm->matrix[x][y];//elem.second;
    int k=cpm->matrix[x][y];//elem.second;
    //add new matrix adhesion at sites with locally high enough Act,
    //first also check current pixel Act, because if lower than 0.075*par.max_Act
    //the geometric mean will never be higher than 0.75*max_Act
    if(cpm->GetMatrixLevel(x,y)==0){
      if (cpm->GetActLevel(x,y)>0.075*par.max_Act){
        double Act_neighourhood_product=1;
        int nxp =0;
        bool insufficient_act=false;
      	for (int i1=-1;i1<=1;i1++){
          if (insufficient_act==true){
            break;
          }
        		for (int i2=-1;i2<=1;i2++){
            		if (cpm->Sigma(x+i1,y+i2)>=0 && cpm->Sigma(x+i1,y+i2)== cpm->Sigma(x,y) ){
                  double current_act=cpm->GetActLevel(x+i1,y+i2);
                  insufficient_act=(current_act<0.075*par.max_Act);
                  if (insufficient_act==true){
                    break;
                  }
            			Act_neighourhood_product *= current_act;
            			nxp++;
            		}}}
        if (insufficient_act==false){
      	Act_neighourhood_product= pow(Act_neighourhood_product, 1./nxp);
        double act_p=par.spontaneous_p*((Act_neighourhood_product/par.max_Act>0.75)?1:0);
        double rand_spon = rand()/double(RAND_MAX);
        if (rand_spon < act_p){
          new_sigma=1;}
      }}}
      else if (k>0){
          //Do Eden growth
          // take a random neighbour
          int xyp=(int)(8*RANDOM()+1);
          int xp = nx[xyp]+x;
          int yp = ny[xyp]+y;
          int kp;

          //Check if both sites are part of the same cell
          if (cpm->Sigma(x,y)==cpm->Sigma(xp,yp)){
              if ((kp = cpm->GetMatrixLevel(xp,yp)) == 0){
                //Make site part of adhesion complex if next to adhesion complex
                double random_double=rand()/double(RAND_MAX);
                if (random_double<par.eden_p){
                cpm->matrix[xp][yp]=1;
                cpm->getCell(sigma_c).IncrementAdhesiveArea(1);
                }}
            }

        int young_neighbours=0;
        for (int i1=-1;i1<=1;i1++)
          for (int i2=-1;i2<=1;i2++){
            if (cpm->GetMatrixLevel(x+i1,y+i2)<1)// && cpm->Sigma(x,y)==cpm->Sigma(x+i2,y+i2))
              young_neighbours+=1;}

        if (young_neighbours>0){
          double rand_double=rand()/double(RAND_MAX);
          if (rand_double<par.decay_p*young_neighbours*young_neighbours/8.0){
            new_sigma=0;}
      }}
      cpm->matrix[x][y]=new_sigma;
      if (new_sigma==0 && k>0)
        cpm->getCell(sigma_c).DecrementAdhesiveArea(k);
      if (new_sigma>0 && k==0)
        cpm->getCell(sigma_c).IncrementAdhesiveArea(new_sigma);
    }}


int PDE::MapColour(double val) {
  return (((int)((val/((val)+1.))*100))%100)+155;
}

/*
int PDE::MapColour3(double val, int l) {
	int step=0;
	if (l==2){
	step = (240)/par.max_Act;
  return (int)(256-val*step-1);}
	else if (l==3 && val>1){
	step = (256)/2;
  return (int)(500+val*step);}
	else
	return 0;
}*/


int main(int argc, char *argv[]) {


  try {

#ifdef QTGRAPHICS
    // cout<< argv[0] <<" "<< argv[1] <<" "<< argv[2] << endl;
    // argv=
    QApplication a(argc, argv);
    // cout<< argv[0] <<" "<< argv[1] <<" "<< argv[2] << endl;
    // setlocale(LC_NUMERIC, "C");
#endif
    // Read parameters
    par.Read(argv[1]);

    Seed(par.rseed);

    //QMainWindow mainwindow w;
#ifdef QTGRAPHICS

    QtGraphics g(par.sizex*2,par.sizey*2);
    // a.setMainWidget( &g );
    a.connect(&g, SIGNAL(SimulationDone(void)), SLOT(quit(void)) );

    if (par.graphics)
      g.show();

    a.exec();
#else
    X11Graphics g(par.sizex*2,par.sizey*2);
    int t;

    for (t=0;t<par.mcs;t++) {
      g.TimeStep();

    }
#endif

  } catch(const char* error) {
    std::cerr << error << "\n";
    exit(1);
  }
  catch(...) {
    std::cerr << "An unknown exception was caught\n";
  }
  return 0;
}
