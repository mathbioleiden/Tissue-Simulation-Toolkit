
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
    // cout << "Pillar present " << CPM->AnyPillar() << endl;
   CPM->GrowInCells(par.n_init_cells,par.size_init_cells,par.subfield);
// cout << "Pillar present " << CPM->AnyPillar() << endl;
// CPM->ReadZygotePicture();
  CPM->ConstructInitCells(*this, 1, par.target_area, par.target_perimeter);
// cout << "Pillar present " << CPM->AnyPillar() << endl;
// cout << "Pillar nearby (0,0)" << CPM->IsPillar(0,0)<< endl;
CPM->InitializeEdgeList();
  } catch(const char* error) {
    cerr << "Caught exception\n";
    std::cerr << error << "\n";
    exit(1);
  }

}

TIMESTEP {

  try {

    // cout << "new timestep" << endl;
    static int i=0;

    static Dish *dish=new Dish();
    static Info *info=new Info(*dish, *this);


		//if (i==par.relaxation){
		//	dish->PDEfield->InitializeAgeLayer(2,0.,dish->CPM);
			//dish->PDEfield->InitializeMILayer(3,1.,dish->CPM);
	//	}
    int number_of_cells=dish->CountCells();
    for (int s=1;s<number_of_cells+1;s++){
      // cout << "compute cell matrix adhesion" << endl;

      //for matrix adhesion
      int new_area=dish->CPM->ComputeCellMatrixAdhesion(s);//,dish->PDEfield);
      dish->getCell(s).SetAdhesiveArea(new_area);
      // cout << dish->getCell(s).AdhesiveArea() << endl;

      // cout << "compute act vector" << endl;
      // schooling vector
      // dish->CPM->ComputeActVector(dish->getCell(s),dish->PDEfield);

    }
      // cout << "Cell 1, cell 2 neighbours: " << dish->CPM->GetNeighbourMatrix()[1][2] << endl;
      // cout << "Cell 2, cell 1 neighbours: " << dish->CPM->GetNeighbourMatrix()[2][1] << endl;}
      // for (int i=0;i<=number_of_cells;i++){
      //   for (int j=0;j<=number_of_cells;j++){
      //     cout << dish->CPM->GetNeighbourMatrix()[i][j] << " ";
      //   }
      //   cout << endl;
      // }
      // cout << " " << endl;

      dish->CPM->AmoebaeMove(dish->PDEfield);
  //  cout << dish->getCell(1).AdhesiveArea() << ", " << dish->CPM->ComputeCellMatrixAdhesion(1,dish->PDEfield)<< endl;
  if (par.max_Act && par.lambda_Act){
    dish->PDEfield->MILayerCA(3,1.,dish->CPM, dish);
    dish->PDEfield->AgeLayer(2,1.,dish->CPM, dish);}
    if (par.lambda_persistence){
    dish->CPM->ChangeThetas(dish);}

    // schooling vector
      // dish->CPM->ComputeActVector(dish->getCell(1),dish->PDEfield);

    // cout << "Updated pdefiels" << endl;

//Writing center of mass and area of each cell
    char buff[400];
  	 snprintf(buff, sizeof(buff), "%s/cellcenter.txt",par.datadir);
  	 std::string buffAsStdStr = buff;
 	//cout<<buffAsStdStr<<"\n";
   	 std::ofstream out(buff, ios::app);
         info->WriteCOMsTorus(out);

         // cout << "Pillar present " << dish->CPM->AnyPillar() << endl;
         // cout << "COMs written" << endl;
 //Writing theta of each cell
     char buff2[400];
   	 snprintf(buff2, sizeof(buff2), "%s/celltheta.txt",par.datadir);
   	 std::string buffAsStdStr2 = buff2;
  	//cout<<buffAsStdStr<<"\n";
    	 std::ofstream out2(buff2, ios::app);
          info->WriteTheta(out2);
 //
 //  //Writing center of mass and area of each cell
 //      char buff3[400];
 //    	 snprintf(buff3, sizeof(buff3), "%s/cellcenter_old.txt",par.datadir);
 //    	 std::string buffAsStdStr3 = buff3;
 //   	//cout<<buffAsStdStr<<"\n";
 //     	 std::ofstream out3(buff3, ios::app);
 //           info->WriteCOMs(out3);

//writing neighbours of each cell
// char fname[400];
//  sprintf(fname, "%s/neighbours.txt",par.datadir);
//  ofstream pFile;
//  pFile.open (fname, ios::app);
//
// int **neighbours=dish->CPM->SearchNeighbours();
// for (int k=0; k<number_of_cells+1; k++){
// for (int j=0; j<=number_of_cells+1; j++){
//   if (neighbours[k][j]>0)
// pFile << dish->CPM->Time()-1 << " " << k << " " << neighbours[k][j] << endl;
// }}
// pFile.close();
  // cout << "Neighbours written " << endl;
// int **newneighbours=dish->CPM->SearchNeigbhoursMatrix();
//     for (int i = 0; i < number_of_cells+1; ++i)
//     {
//         for (int j = 0; j < number_of_cells+1; ++j)
//         {
//             cout << newneighbours[i][j] << ' ';
//         }
//         cout << endl;
//     }

//output cell and act field at time=1600
// char buff2[400];
//  snprintf(buff2, sizeof(buff2), "%s/celllocation.txt",par.datadir);
//  std::string buffAsStdStr2 = buff2;
// //cout<<buffAsStdStr<<"\n";
//  std::ofstream outt(buff2, ios::app);
//      info->WriteCellLocations(1,2,outt);

//plot to screen and file

    if (par.graphics && !(i%par.storage_stride)) {


      int tx,ty;
      BeginScene();

      //dish->PDEfield->Plot(this,0);
      ClearImage();

			dish->Plot(this);
			dish->PDEfield->PlotInCells (this, dish->CPM,2);
//       if (par.lambda_matrix>0){
//         			dish->PDEfield->PlotInCells (this, dish->CPM,2);
// }

      // You need to call "ClearImage" if no PDE field is plotted,
      // because the CPM medium is considered transparant




//       if (i>=par.relaxation)
//       dish->PDEfield->ContourPlot(this,0,7);

      char title[400];
//       snprintf(title,399,"CellularPotts: %.2f hr",dish->PDEfield->TheTime()/3600);
      snprintf(title,399,"CellularPotts: %d MCS",i);
      //ChangeTitle(title);
      EndScene();
      info->Menu();



    }

    // cout << "in between graphics" << endl;
    if (par.store && !(i%par.storage_stride)) {
      char fname[200];
      sprintf(fname,"%s/extend%05d.png",par.datadir,i);

      BeginScene();

 ClearImage();
      dish->PDEfield->PlotInCells (this, dish->CPM, 2);
           dish->CPM->SearchNandPlotClear(this);

 // EndScene();
 //
 // Write(fname);
 //
 // char fnamematrix[200];
 // sprintf(fnamematrix,"%s/matrix%05d.png",par.datadir,i);
 //       BeginScene();
 //            ClearImage();
     //  dish->PDEfield->PlotInCells (this, dish->CPM, 3);
     // dish->CPM->SearchNandPlotClear(this);


      // dish->CPM->PlotVectors(this);

      // cout << "vectors plotted" << endl;
			//ClearImage();
    //  dish->Plot(this);
//       if (i>=par.relaxation)
//       dish->PDEfield->ContourPlot(this,0,7);

      EndScene();

      // Write(fnamematrix);
       Write(fname);

    }
    // cout << "after graphics" << endl;
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

void CellularPotts::ChangeThetas(Dish *dish){
  int number_of_cells=dish->CountCells();
  double dt=0.1*par.tau;
  for (int s=1;s<number_of_cells+1;s++){
    dish->getCell(s).SetTheta(dish->getCell(s).theta + sqrt(2.0/par.tau)*generateGaussianNoise(0, sqrt(2*dt/par.tau)));
  }
}


void PDE::AgeLayer(int l,double value,CellularPotts *cpm, Dish *dish){
// for (const auto& elem: cpm->alivePixels) {
//     /* ... process elem ... */
//     int x= elem[0];
//     int y= elem[1];
//     if(sigma[l][x][y]>0.)
//       sigma[l][x][y]-=value;
//     // // do not allow young lattice sites outside the T cells
//     // if (dish->getCell(cpm->Sigma(x,y)).getTau() ==0 )
//     //   sigma[l][x][y]= 0.;
//   }
  for (const auto elem: cpm->actPixels){
    /* ... process elem ... */
    if(elem.second>0.)
      cpm->actPixels[elem.first]-=value;
  }


}

void PDE::InitializeMILayer(int l,double value,CellularPotts *cpm){
  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++){
 //cout << "Anything..." << endl;
    if (cpm->Sigma(x,y)==0 ){
	     sigma[l][x][y]=0;
	//cout << cpm->Sigma(x,y) << " has now value " << sigma[l][x][y] << endl;
}
    else{
	//cout << cpm->Sigma(x,y);
	int rand_value=RandomNumber(par.max_matrix/4);
	sigma[l][x][y]=rand_value;
	//cout << " has now value " << sigma[l][x][y] << endl;
}

    }
}


void PDE::MILayer(int l,double value,CellularPotts *cpm, Dish *dish){
for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++){

    if(sigma[l][x][y]>=0.&&sigma[l][x][y]<par.max_matrix-1)
      sigma[l][x][y]+=value;
	double rand_value=RandomNumber(par.max_matrix);
	if (0.999<=rand_value/par.max_matrix){
		sigma[l][x][y]=1.;}
    // do not allow young lattice sites outside the cells
    if (dish->getCell(cpm->Sigma(x,y)).getTau() ==0 )
      sigma[l][x][y]= 0.;

    }

}

void PDE::MILayerCA(int l, double value, CellularPotts *cpm, Dish *dish){
  // First set pixels outside cells to 0, and new pixels within cells to 1
  int map_counter=0;
  for (const auto &elem: cpm->matrixPixels){
    map_counter+=1;
    int x=elem.first[0];
    int y =elem.first[1];
    //Delete pixels that are not cells
    if (cpm->Sigma(x,y)<=0){
      cpm->matrixPixels.erase({x,y});}
    //Make adhesions
    else{
    int adh_area = 0;
    int new_sigma=elem.second;
    int k=elem.second;
    if(cpm->matrixPixels[{x,y}]==0){
      // //Do Eden growth
      // // take a random neighbour
      // int xyp=(int)(8*RANDOM()+1);
      // int xp = nx[xyp]+x;
      // int yp = ny[xyp]+y;
      // int kp;

      //Check if both sites are part of the same cell
      // if (cpm->Sigma(x,y)==cpm->Sigma(xp,yp)){
      //   cout << x << " " << y << " " << xp << " " << yp << endl;
      //   if (kp=cpm->GetMatrixLevel(xp,yp)!=-1){
      //     // cout << "neighbour in cell" << endl;
      //     cout << kp<< endl;
      //     if (kp>1){
      //       //Make site part of adhesion complex if next to adhesion complex
      //       double random_double=rand()/double(RAND_MAX);
      //       cout << random_double<< endl;
      //       if (random_double<par.eden_p){
      //         cout << "eden" << endl;
      //         new_sigma=2;}}
      //       else{
      //         new_sigma=1;
      //     }}
      //     else{
      //       new_sigma=1;}
      //   }

        //spontaneous formation of new adhesion
        // double extra_p;
        // double w=par.spontaneous_p;
        //option i
        // extra_p=w*cpm->GetActLevel(x,y)/par.max_Act;
        double Act_neighourhood_product=1;
        double Act_neighourhood_sum=0;
        int nxp =0;


          	for (int i1=-1;i1<=1;i1++)
          		for (int i2=-1;i2<=1;i2++){

            		if (cpm->Sigma(x+i1,y+i2)>=0 && cpm->Sigma(x+i1,y+i2)== cpm->Sigma(x,y) ){
            			Act_neighourhood_product *= cpm->GetActLevel(x+i1, y+i2);
                  Act_neighourhood_sum += cpm->GetActLevel(x+i1, y+i2);
            			nxp++;
            		}}
                	Act_neighourhood_product= pow(Act_neighourhood_product, 1./nxp);

        //circular
        // double act_p=par.spontaneous_p*(1-std::sqrt(1-(Act_neighourhood_product/par.max_Act)*(Act_neighourhood_product/par.max_Act)));
        //sigmoid
        // double act_p=par.spontaneous_p*(std::exp(Act_neighourhood_product/par.max_Act-0.5))/(std::exp(Act_neighourhood_product/par.max_Act-0.5)+1);
        //step neighbourhood
        double act_p=par.spontaneous_p*((Act_neighourhood_product/par.max_Act>0.75)?1:0);
        //step pixel
        // double act_p=par.spontaneous_p*((cpm->GetActLevel(x,y)/par.max_Act>0.75)?1:0);

        //option ii
        // if (cpm->GetActLevel(x,y)>0)
        //   extra_p=w;
        // else
        //   extra_p=0;

        double rand_spon = rand()/double(RAND_MAX);
        // if (rand_spon < par.spontaneous_p+extra_p){
        if (rand_spon < act_p){
          // cout << "Act_neighourhood_product " << Act_neighourhood_product << endl;
          new_sigma=1;}
      }
    //Rejuvenate adhesions or age them further or do eden growth
      else if (k>0){

        // if(cpm->matrixPixels[{x,y}]==1){
          //Do Eden growth
          // take a random neighbour
          int xyp=(int)(8*RANDOM()+1);
          int xp = nx[xyp]+x;
          int yp = ny[xyp]+y;
          int kp;

          //Check if both sites are part of the same cell
          if (cpm->Sigma(x,y)==cpm->Sigma(xp,yp)){
            // if (kp=cpm->GetMatrixLevel(xp,yp)!=-1){
              // cout << "neighbour in cell" << endl;
              if (kp=cpm->GetMatrixLevel(xp,yp)==0){
                //Make site part of adhesion complex if next to adhesion complex
                double random_double=rand()/double(RAND_MAX);
                if (random_double<par.eden_p){
                cpm->matrixPixels[{xp,yp}]=1;}}
              //   else{
              //     new_sigma_p=1;
              // }
            // }
              // else{
              //   new_sigma=1;}
            }
          // }
        // aging, an abandoned idea
        // if (k<par.max_matrix-1){
        //   new_sigma=k+value;}

        int young_neighbours=0;
        for (int i1=-1;i1<=1;i1++)
          for (int i2=-1;i2<=1;i2++){
            if (cpm->GetMatrixLevel(x+i1,y+i2)<1)
              young_neighbours+=1;}

        if (young_neighbours>0){
          double rand_double=rand()/double(RAND_MAX);
          if (rand_double<par.decay_p){
            new_sigma=0;}
      }}
      cpm->matrixPixels[{x,y}]=new_sigma;
      adh_area+=new_sigma;
      dish->getCell(cpm->Sigma(x,y)).SetAdhesiveArea(adh_area);
    }}}
//
//   {int new_sigma[sizex][sizey];
//     for (int x=1;x<sizex-1;x++)
//     for (int y=1;y<sizey-1;y++) {
//     if (dish->getCell(cpm->Sigma(x,y)).getTau() ==0 && sigma[l][x][y]!=0){
//     	  sigma[l][x][y]= 0;}
//     else if (cpm->Sigma(x,y)>=1 && sigma[l][x][y]==0){
// 	sigma[l][x][y]=1;
//
// }}
//
// 	//Do Eden growth
// for (int x=1;x<sizex-1;x++)
// for (int y=1;y<sizey-1;y++) {
// new_sigma[x][y]=sigma[l][x][y];
// int k;
//
// if (sigma[l][x][y]==1) {
//   // take a random neighbour
//   int xyp=(int)(8*RANDOM()+1);
//   int xp = nx[xyp]+x;
//   int yp = ny[xyp]+y;
//   int kp;
//
//   //Check if both sites are part of the same cell
//   if (dish->getCell(cpm->Sigma(x,y)).getTau()==dish->getCell(cpm->Sigma(xp,yp)).getTau()){
//     //  NB removing this border test yields interesting effects :-)
//     // You get a ragged border, which you may like!
//     if ((kp=sigma[l][xp][yp])!=-1){
//       if (kp>1){
//         //Make site part of adhesion complex if next to adhesion complex
//         // Probabililty depends on number of 'old' neighbours
//         int old_neighbours=0;
//         for (int i1=-1;i1<=1;i1++)
//           for (int i2=-1;i2<=1;i2++){
//             if (sigma[l][x+i1][y+i2]>1)
//               old_neighbours+=1;}
//
//         double random_double=rand()/double(RAND_MAX);
//         if (random_double<par.eden_p){//old_neighbours){
//           new_sigma[x][y]=2;}}
//
//       else{
//         new_sigma[x][y]=1;
//     }}
//
//     else{
//       //cout<< x <<", " << y << " border"<< endl;
//       new_sigma[x][y]=1;}
//   }
//   //spontaneous formation of new adhesion
//   double rand_spon = rand()/double(RAND_MAX);
//   if (rand_spon < par.spontaneous_p){
//     new_sigma[x][y]=2;}
//
// }
//
// else if ((k=sigma[l][x][y])>1){//cpm->Sigma(x,y)>0){
//   if (k<par.max_matrix-1){
//     //cout << "1 " << new_sigma[x][y] << endl;
//     new_sigma[x][y]=k+value;}
//     //cout << "2 " << new_sigma[x][y] << endl;
//
//   int young_neighbours=0;
//   for (int i1=-1;i1<=1;i1++)
//     for (int i2=-1;i2<=1;i2++){
//       if (sigma[l][x+i1][y+i2]==1)
//         young_neighbours+=1;}
//
//   if (young_neighbours>0){	//cout<< x <<", " << y << " in cell old"<< endl;
//     double rand_double=rand()/double(RAND_MAX);
//     //cout << rand_double << endl;
//     if (rand_double<par.decay_p){
//     //cout<< x <<", " << y << " rejuvenate"<< endl;
//       new_sigma[x][y]=1;}
//     //else{
//     //cout<< x <<", " << y << " stay the same"<< endl;
//     //	new_sigma[x][y]= sigma[l][x][y]+1;}
// }}
// }
//
//     // copy sigma to new_sigma, but do not touch the border!
// 	  {  for (int x=1;x<sizex-1;x++) {
//       for (int y=1;y<sizey-1;y++) {
// 	//cout << x <<", " << y << "apply new sigmas" << endl;
// 	sigma[l][x][y]=new_sigma[x][y];
//       }
//     }
//   }}
//
//
//
// }


// int PDE::MapColour3(double val, int l) {
//
//   return (((int)((val/((val)+1.))*100))%100)+155;
// }

int PDE::MapColour(double val) {

  return (((int)((val/((val)+1.))*100))%100)+155;
}


int PDE::MapColour3(double val, int l) {
	int step=0;
	if (l==2){
	step = (240)/par.max_Act;
  return (int)(256-val*step-1);}
	else if (l==3 && val>1){
	step = (256)/par.max_matrix;
  return (int)(500+val*step);}
	else
	return 0;

}

// int PDE::MapColour3(double val, int l) {
// 	int step = (240)/par.max_Act;
//   return (int)(256-val*step-1);
// }
//
// int PDE::MapColour4(double val, int l){
// 	int step = (256)/par.max_Act;
//   if (val>par.max_Act) {
//     cout << "max_matrix value exceeded" << endl;
//   }
//   return (int)(256-val*step);
//
// }

int main(int argc, char *argv[]) {


  try {

#ifdef QTGRAPHICS
    QApplication a(argc, argv);
#endif
    // Read parameters
    par.Read(argv[1]);

    Seed(par.rseed);

    //QMainWindow mainwindow w;
#ifdef QTGRAPHICS

    QtGraphics g(par.sizex*2,par.sizey*2);
		// cout<< "After  QtGraphics g(par.sizex*2,par.sizey*2);"<< endl;
    a.setMainWidget( &g );
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
