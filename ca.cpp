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

#include <stdio.h>
#include <math.h>
#include <cstdlib>
#include <cstring>
#include <algorithm> // for std::find
#include <iterator> // for std::begin, std::end
#include <unordered_set>
#include <unordered_map>
#include "sticky.h"
#include "random.h"
#include "ca.h"
#include "parameter.h"
#include "dish.h"
#include "sqr.h"
#include "crash.h"
#include "hull.h"
#include <tuple>
#include <boost/functional/hash.hpp>
#include <boost/array.hpp>
#include <algorithm>
// #include "pickset.hpp"

template <typename T> int sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

#define ZYGFILE(Z) <Z.xpm>
#define XPM(Z) Z ## _xpm
#define ZYGXPM(Z) XPM(Z)

/* define default zygote */
/* NOTE: ZYGOTE is normally defined in Makefile!!!!!! */
#ifndef ZYGOTE
#define ZYGOTE one
#include "1.xpm"
#else
#include ZYGFILE(ZYGOTE)
#endif

/* STATIC DATA MEMBER INITIALISATION */
double copyprob[BOLTZMANN];


const int CellularPotts::nx[25] = {0, 0, 1, 0,-1, 1, 1,-1,-1, 0, 2, 0, -2, 1, 2, 2, 1,-1,-2,-2,-1, 0, 3, 0,-3 };
const int CellularPotts::ny[25] = {0,-1, 0, 1, 0,-1, 1, 1,-1,-2, 0, 2,  0,-2,-1, 1, 2, 2, 1,-1,-2,-3, 0, 3, 0 };

const int CellularPotts::nbh_level[5] = { 0, 4, 8, 20, 24 };
int CellularPotts::shuffleindex[9]={0,1,2,3,4,5,6,7,8};

extern Parameter par;


/** PRIVATE **/

using namespace std;
void CellularPotts::BaseInitialisation(vector<Cell> *cells) {
  CopyProb(par.T);
  cell=cells;
  if (par.neighbours>=1 && par.neighbours<=4)
    n_nb=nbh_level[par.neighbours];
  else
    throw "Panic in CellularPotts: parameter neighbours invalid (choose [1-4]).";

}

CellularPotts::CellularPotts(vector<Cell> *cells,
			     const int sx, const int sy) {

  sigma=0;
  frozen=false;
  thetime=0;
  zygote_area=0;


  BaseInitialisation(cells);
  sizex=sx;
  sizey=sy;

  AllocateSigma(sx,sy);


  // fill borders with special border state
  for (int x=0;x<sizex;x++) {
    sigma[x][0]=-1;
    sigma[x][sizey-1]=-1;
  }
  for (int y=0;y<sizey;y++) {
    sigma[0][y]=-1;
    sigma[sizex-1][y]=-1;
  }

  for (int x=0;x<sizex;x++){
    for (int y=0;y<sizey;y++){
      if (par.checkerboard == true){
        int which_pillar=WhichPillar(x,y);
        if (which_pillar==0){
          sigma[x][y]=-2;}
        else if (which_pillar!=-2){
          sigma[x][y]=-3;}
      }
      else{
      if (IsPillar(x,y)){
        sigma[x][y]=-2;}
      }
    }
  }

  if (par.neighbours>=1 && par.neighbours<=4)
    n_nb=nbh_level[par.neighbours];
  else
    throw "Panic in CellularPotts: parameter neighbours invalid (choose [1-4])";
}

CellularPotts::CellularPotts(void) {

  sigma=0;
  sizex=0; sizey=0;
  frozen=false;
  thetime=0;
  zygote_area=0;

  CopyProb(par.T);

  // fill borders with special border state
  for (int x=0;x<sizex;x++) {
    sigma[x][0]=-1;
    sigma[x][sizey-1]=-1;
  }
  for (int y=0;y<sizey;y++) {
    sigma[0][y]=-1;
    sigma[sizex-1][y]=-1;
  }

  for (int x=0;x<sizex;x++){
    for (int y=0;y<sizey;y++){
      if (par.checkerboard==true){
        int which_pillar=WhichPillar(x,y);
        if (which_pillar==0){
          sigma[x][y]=-2;}
        else if (which_pillar==1){
          sigma[x][y]=-3;}
      }
      else{
      if (IsPillar(x,y)){
        sigma[x][y]=-2;}
      }
    }
  }

  if (par.neighbours>=1 && par.neighbours<=4)
    n_nb=nbh_level[par.neighbours];
  else
    throw "Panic in CellularPotts: parameter neighbours invalid (choose [1-4])";
}

// destructor (virtual)
CellularPotts::~CellularPotts(void) {
  if (sigma) {
    free(sigma[0]);
    free(sigma);
    sigma=0;
  }
}

void CellularPotts::AllocateSigma(int sx, int sy) {

  sizex=sx; sizey=sy;

  sigma=(int **)malloc(sizex*sizeof(int *));
  if (sigma==NULL)
    MemoryWarning();

  sigma[0]=(int *)malloc(sizex*sizey*sizeof(int));
  if (sigma[0]==NULL)
    MemoryWarning();


  {for (int i=1;i<sizex;i++)
    sigma[i]=sigma[i-1]+sizey;}

  /* Clear CA plane */
   {for (int i=0;i<sizex*sizey;i++)
     sigma[0][i]=0; }

}

void CellularPotts::InitializeMatrix(Dish &beast){
  // sizex; sizey=sy;

  matrix=(int **)malloc(sizex*sizeof(int *));
  if (matrix==NULL)
    MemoryWarning();

  matrix[0]=(int *)malloc(sizex*sizey*sizeof(int));
  if (matrix[0]==NULL)
    MemoryWarning();


  {for (int i=1;i<sizex;i++)
    matrix[i]=matrix[i-1]+sizey;}

  /* Clear CA plane */
   {for (int i=0;i<sizex*sizey;i++)
     matrix[0][i]=0; }

}

void CellularPotts::IndexShuffle() {

  int i;
  int temp;
  int index1,index2;

  for (i=0;i<9;i++) {

    index1=RandomNumber(8);
    index2=RandomNumber(8);

    temp=shuffleindex[index1];
    shuffleindex[index1]=shuffleindex[index2];
    shuffleindex[index2]=temp;

  }
}

void CellularPotts::InitializeEdgeList(void){
  // unordered_set<long long int> edgeSet;
	int neighbour;
	int x,y, xp, yp;
	int c, cp;
  int xstart =0;
  int xend=sizex-1;
  int ystart=0;
  int yend=sizey-1;

  bool init_single_cell_center=true;

  if (init_single_cell_center && sizex>200 && sizey>200){
    xstart=(sizex-1)/2-100;
    xend=(sizex-1)/2+100;
    ystart=(sizey-1)/2-100;
    yend=(sizey-1)/2+100;
  }

	for (x=xstart; x< xend; x++){
    for ( y=ystart; y<yend; y++){
      for (int nb=1; nb<=n_nb; nb++){
    		c = sigma[x][y];
    		xp = nx[nb]+x;
    		yp = ny[nb]+y;

		      if (par.periodic_boundaries) {

          // since we are asynchronic, we cannot just copy the borders once
          // every MCS

    			if (xp<=0)
    				xp=sizex-2+xp;
        	if (yp<=0)
    				yp=sizey-2+yp;
       	  if (xp>=sizex-1)
    				xp=xp-sizex+2;
       	  if (yp>=sizey-1)
    				yp=yp-sizey+2;

          cp=sigma[xp][yp];
          }
    		else if (xp<=0 || yp<=0 || xp>=sizex-1 || yp>=sizey-1)
    			cp=-1;
        else
    			cp=sigma[xp][yp];
    if (cp != c && cp != -1 && c!=-1 && sgn(cp)+sgn(c)>=0){
      edgeSetpair.insert({x,y,xp,yp});
      edgeSetVector.insert({x,y,xp,yp});
      // cout << edgeSetVector.subset_size() <<endl;
      // edgeSetVector.push_back({x,y,xp,yp});
      // edgeSetVector.insert_in_subset(edgeSetVector.subset_size());
      // cout << edgeSetVector.subset_size() << endl;
      edgeSetpair.insert({xp,yp,x,y});
      edgeSetVector.insert({xp,yp,x,y});
      // edgeSetVector.push_back({xp,yp,x,y});
      // edgeSetVector.insert_in_subset(edgeSetVector.subset_size());
      // edgeVector.push_back({x,y,xp,yp});
		}
	}
}}
}

double sat(double x) {

  return x/(par.saturation*x+1.);
  //return x;

}

int CellularPotts::DeltaH(int x,int y, int xp, int yp, PDE *PDEfield){
  int DH = 0;
  int i, sxy, sxyp;
  int neighsite;

  /* Compute energydifference *IF* the copying were to occur */
  int DH_adhesive_energy =0;
  int DH_polarised_adhesive_energy =0;
  sxy = sigma[x][y];
  sxyp = sigma[xp][yp];
  if (sxyp<=-1){sxyp=0;}//allow for medium to copy in from box border or pillars

  /* DH due to cell adhesion */
  //also compute changes in neighbours for alignment with newneighbours
  int xy_neighbour_changes[cell->size()]={0};
  int xyp_neighbour_changes[cell->size()]={0};
  for (i=1;i<=n_nb;i++) {
    int xp2,yp2;
    xp2=x+nx[i]; yp2=y+ny[i];
    if (par.periodic_boundaries) {

      // since we are asynchronic, we cannot just copy the borders once
      // every MCS

      if (xp2<=0)
	xp2=sizex-2+xp2;
      if (yp2<=0)
	yp2=sizey-2+yp2;
      if (xp2>=sizex-1)
	xp2=xp2-sizex+2;
      if (yp2>=sizey-1)
	yp2=yp2-sizey+2;

      neighsite=sigma[xp2][yp2];
    } else {

      if (xp2<=0 || yp2<=0
	  || xp2>=sizex-1 || yp2>=sizey-1)
	neighsite=-1;
      else
	neighsite=sigma[xp2][yp2];

    }

    if (neighsite==-1) { // border
      DH_adhesive_energy += (sxyp==0?0:par.border_energy)-
	(sxy==0?0:par.border_energy);
    }
    else { if (neighsite<=-2){//pillar
      if (neighsite==-2){
  DH_adhesive_energy += (sxyp>0?par.pillar_energy:0)-
(sxy>0?par.pillar_energy:0);
    }
    if (neighsite==-3 & par.checkerboard == true){
      DH_adhesive_energy += (sxyp>0?par.pillar_energy_odd:0)-
	(sxy>0?par.pillar_energy_odd:0);
    }}
    else{
      DH_adhesive_energy += (*cell)[sxyp].EnergyDifference((*cell)[neighsite])
	- (*cell)[sxy].EnergyDifference((*cell)[neighsite]);
    if (par.J_pol && par.max_Act){
      DH_polarised_adhesive_energy += PolarizedAdhesiveEnergy(par.max_Act,sxyp,GetActLevel(xp2,yp2), neighsite) -PolarizedAdhesiveEnergy(GetActLevel(x,y), sxy, GetActLevel(xp2,yp2), neighsite) ;}
  if (i<=4 | par.extended_neighbour_border){
    if (neighsite!=sxy)
    xy_neighbour_changes[neighsite]-=1;
    if (neighsite!=sxyp)
    xyp_neighbour_changes[neighsite]+=1;
  }}}
  }
  DH+=DH_adhesive_energy+DH_polarised_adhesive_energy;
  //
  // for (int i=1;i<=cell->size();i++){
  //   if (sxy==1)
  //   cout << sxy << " " << i << " " << NB[sxy][i] << " " << xy_neighbour_changes[i] << endl;
  //   // cout << sxyp << " " << i << " " << NB[sxyp][i] << " " << xyp_neighbour_changes[i] << endl;
  // }
//cout << "cell id" << (*cell)[sxy].Sigma();
//cout << ", matrix_adhesion = " << ComputeCellMatrixAdhesion( (*cell)[sxy], PDEfield) << "\n";
  // lambda is determined by chemical 0
  int DH_area=0;
  if (par.area_constraint_type == 0){
  //cerr << "[" << lambda << "]";
  if ( sxyp == MEDIUM ) {
    DH_area += (int)(par.lambda *  (1. - 2. *
			       (double) ( (*cell)[sxy].Area() - (*cell)[sxy].TargetArea()) ));
  }
  else if ( sxy == MEDIUM ) {
    DH_area += (int)((par.lambda * (1. + 2. *
			       (double) ( (*cell)[sxyp].Area() - (*cell)[sxyp].TargetArea()) )));
  }
  else
    DH_area += (int)(par.lambda * (2.+  2.  * (double)
			       (  (*cell)[sxyp].Area() - (*cell)[sxyp].TargetArea()
			       - (*cell)[sxy].Area() + (*cell)[sxy].TargetArea() )) );
}
  else if (par.area_constraint_type == 1){
	if (sxyp == MEDIUM ) {
		//cout << "Cell adhesive area " << (*cell)[sxy].ReferenceAdhesiveArea() << endl;
		int dh =(int)(par.lambda * (1. -2.*(double)((*cell)[sxy].Area())) +
    par.lambda_c*((double)((*cell)[sxy].ReferenceAdhesiveArea())/
    (((double)((*cell)[sxy].ReferenceAdhesiveArea()+
    (double)((*cell)[sxy].Area()-1)))*((double)((*cell)[sxy].ReferenceAdhesiveArea()+
    (*cell)[sxy].Area() )))));
		DH_area += dh;
		//cout << "retraction, DH adhesion " << dh << endl;
	}
	else if (sxy == MEDIUM ) {
		//cout << "Cell adhesive area " << (*cell)[sxyp].ReferenceAdhesiveArea() << endl;
		DH_area += (int)(par.lambda * (1. +2.*(double)((*cell)[sxyp].Area())) -
    par.lambda_c*((double)((*cell)[sxyp].ReferenceAdhesiveArea())/
    (((double)((*cell)[sxyp].ReferenceAdhesiveArea()+
    (double)((*cell)[sxyp].Area()+1)))*((double)((*cell)[sxyp].ReferenceAdhesiveArea()+
    (double)((*cell)[sxyp].Area()))))));
	}
	else
		DH_area += (int)(2.*par.lambda * (1. + (double)((*cell)[sxyp].Area()) -
    (double)((*cell)[sxy].Area())) - par.lambda_c*((double)((*cell)[sxyp].ReferenceAdhesiveArea())/
    (((double)((*cell)[sxyp].ReferenceAdhesiveArea()+(double)((*cell)[sxyp].Area()+1)))*
    ((double)((*cell)[sxyp].ReferenceAdhesiveArea()+(double)((*cell)[sxyp].Area())))) -
    (double)((*cell)[sxy].ReferenceAdhesiveArea())/(((double)((*cell)[sxy].ReferenceAdhesiveArea()+
    (double)((*cell)[sxy].Area()-1)))*((double)((*cell)[sxy].ReferenceAdhesiveArea()+
    (double)((*cell)[sxy].Area()))))    ));

}

  else if (par.area_constraint_type == 2){
	if (sxyp == MEDIUM ) {
		DH_area+= (int)(par.lambda * (1. -2.*(double)((*cell)[sxy].Area())) +
    par.lambda_c*((double)((*cell)[sxy].ReferenceAdhesiveArea()*GetMatrixLevel(x,y))/
    (((double)((*cell)[sxy].ReferenceAdhesiveArea()+(double)((*cell)[sxy].AdhesiveArea())-
    GetMatrixLevel(x,y)))*((double)((*cell)[sxy].ReferenceAdhesiveArea()+
    (*cell)[sxy].AdhesiveArea() )))));
	}
	else if (sxy == MEDIUM ) {
		DH_area+= (int)(par.lambda * (1. +2.*(double)((*cell)[sxyp].Area())) -
    par.lambda_c*((double)((*cell)[sxyp].ReferenceAdhesiveArea())/
    (((double)((*cell)[sxyp].ReferenceAdhesiveArea()+
    (double)((*cell)[sxyp].AdhesiveArea()+1)))*((double)((*cell)[sxyp].ReferenceAdhesiveArea()+
    (double)((*cell)[sxyp].AdhesiveArea()))))));
	}
	else
		DH_area+= (int)(2.*par.lambda * (1. + (double)((*cell)[sxyp].Area()) -
    (double)((*cell)[sxy].Area())) - par.lambda_c*((double)((*cell)[sxyp].ReferenceAdhesiveArea())/
    (((double)((*cell)[sxyp].ReferenceAdhesiveArea()+(double)((*cell)[sxyp].AdhesiveArea()+1)))*
    ((double)((*cell)[sxyp].ReferenceAdhesiveArea()+(double)((*cell)[sxyp].AdhesiveArea())))) -
    (double)((*cell)[sxy].ReferenceAdhesiveArea()*GetMatrixLevel(x,y))/
    (((double)((*cell)[sxy].ReferenceAdhesiveArea()+(double)((*cell)[sxy].AdhesiveArea()-
    GetMatrixLevel(x,y))))*((double)((*cell)[sxy].ReferenceAdhesiveArea()+
    (double)((*cell)[sxy].AdhesiveArea())))    )));
  }
DH+=DH_area;


		//!Perimeter constraint, only available when par.area_constraint_type==0, in other words,
		//when the target area constraint is in place
int DH_perimeter=0;
if (par.area_constraint_type == 0){
		if ( sxyp == MEDIUM) {

    DH_perimeter -= par.lambda_perimeter*( DSQR((*cell)[sxy].Perimeter()-(*cell)[sxy].TargetPerimeter())
		       - DSQR(GetNewPerimeterIfXYWereRemoved(sxy,x,y) -(*cell)[sxy].TargetPerimeter() ) );

  }
  else if ( sxy == MEDIUM ) {

    DH_perimeter -= par.lambda_perimeter* (  DSQR((*cell)[sxyp].Perimeter()-(*cell)[sxyp].TargetPerimeter())
			 -DSQR(GetNewPerimeterIfXYWereAdded(sxyp,x,y)-(*cell)[sxyp].TargetPerimeter() ) );

  }
  // they're both cells
  else {

			DH_perimeter -= par.lambda_perimeter*( (DSQR((*cell)[sxyp].Perimeter()-(*cell)[sxyp].TargetPerimeter())
		     -DSQR(GetNewPerimeterIfXYWereAdded(sxyp,x,y)-(*cell)[sxyp].TargetPerimeter())) );

			DH_perimeter -= par.lambda_perimeter*( DSQR((*cell)[sxy].Perimeter()-(*cell)[sxy].TargetPerimeter())
		      - DSQR(GetNewPerimeterIfXYWereRemoved(sxy,x,y) -(*cell)[sxy].TargetPerimeter())) ;
 }
}
DH +=DH_perimeter;
  /* Chemotaxis */
  int DDH=0;
  if (PDEfield && (par.vecadherinknockout || (sxyp==0 || sxy==0))) {

    // copying from (xp, yp) into (x,y)
    // If par.extensiononly == true, apply CompuCell's method, i.e.
    // only chemotactic extensions contribute to energy change
    if (!( par.extensiononly && sxyp==0)) {
      DDH=(int)(par.chemotaxis*(sat(PDEfield->Sigma(0,x,y))-sat(PDEfield->Sigma(0,xp,yp))));

      DH-=DDH;
    }
  }


  const double lambda2=par.lambda2;

  /* Length constraint */
  // sp is expanding cell, s is retracting cell

  int DH_length=0;
  if ( sxyp == MEDIUM ) {
    DH_length -= (int)(lambda2*( DSQR((*cell)[sxy].Length()-(*cell)[sxy].TargetLength())
		       - DSQR((*cell)[sxy].GetNewLengthIfXYWereRemoved(x,y) -
			      (*cell)[sxy].TargetLength()) ));

  }
  else if ( sxy == MEDIUM ) {
    DH_length -= (int)(lambda2*(DSQR((*cell)[sxyp].Length()-(*cell)[sxyp].TargetLength())
			 -DSQR((*cell)[sxyp].GetNewLengthIfXYWereAdded(x,y)-(*cell)[sxyp].TargetLength())));


  }
  else {
    DH_length -= (int)(lambda2*( (DSQR((*cell)[sxyp].Length()-(*cell)[sxyp].TargetLength())
		     -DSQR((*cell)[sxyp].GetNewLengthIfXYWereAdded(x,y)-(*cell)[sxyp].TargetLength())) +
		    ( DSQR((*cell)[sxy].Length()-(*cell)[sxy].TargetLength())
		      - DSQR((*cell)[sxy].GetNewLengthIfXYWereRemoved(x,y) -
			     (*cell)[sxy].TargetLength()) ) ));
  }
  DH +=DH_length;

  /************************The Act model****************/
 // let the cell extend with
 int DH_act=0;
	if (par.lambda_Act)// && NearbyAdhesionSite(x,y,10,PDEfield))
{
	 double Act_expanding=1, Act_retracting=1;
   int nxp =0,nret =0;


     	for (int i1=-1;i1<=1;i1++)
     		for (int i2=-1;i2<=1;i2++){

       		if (sigma[xp+i1][yp+i2]>=0 && sigma[xp+i1][yp+i2]== sigma[xp][yp] ){
       			Act_expanding *= GetActLevel(xp+i1, yp+i2);
       			nxp++;
       		}


       		if (sigma[x+i1][y+i2]>=0 && sigma[x+i1][y+i2] == sigma[x][y]){
       			Act_retracting *= GetActLevel(x+i1,y+i2);
						nret++;
       		}
       	}

     	// apply the smoothing
     	//Act_expanding*= pow( PDEfield->Sigma(2,xp,yp), w-1);
     	//Act_retracting*= pow(PDEfield->Sigma(2,x,y), w-1);
     	//nxp += w-1;
     	//nret += w-1;

     	Act_expanding= pow(Act_expanding, 1./nxp);
     	Act_retracting= pow(Act_retracting, 1./nret);


	if( (*cell)[sxyp].sigma>0){
      double strength = 1;
      double adhesion_fraction = (double)(*cell)[sxyp].AdhesiveArea()/(double)(*cell)[sxyp].area;
      double threshold=0.1;
      if (adhesion_fraction>threshold){
        strength = 2;
        }
      else{
        strength= 1+(1.0/threshold)*adhesion_fraction;
      }
            // cout << (*cell)[sxyp].AdhesiveArea() << " " <<(*cell)[sxyp].area <<" " << strength <<" "<< adhesion_fraction <<endl;
			DH_act-= (par.lambda_Act * strength)/par.max_Act * Act_expanding;
	}
  if( (*cell)[sxy].sigma>0){
    double strength =1;
    double threshold=0.1;
    double adhesion_fraction = (double)(*cell)[sxy].AdhesiveArea()/(double)(*cell)[sxy].area;
    if (adhesion_fraction>threshold){
      strength = 2;
    }
    else{
      strength= 1+(1.0/threshold)*adhesion_fraction;
    }
	   DH_act+= (par.lambda_Act * strength)/par.max_Act * Act_retracting;
		}
}
DH+=DH_act;


/************************The vector based persistence model****************/
// let the cell extend with
int DH_persistence=0;
if (par.lambda_persistence)
{
  if (sxyp>0){
 //
 int reference_x, reference_y;
 if (par.periodic_boundaries){
   reference_x = x+(int) (round((((double)(*cell)[sxyp].getSumX()/(double) (*cell)[sxyp].Area())-x)/ sizex) * sizex);
   reference_y = y+(int) (round((((double)(*cell)[sxyp].getSumY()/(double) (*cell)[sxyp].Area())-y)/ sizey) * sizey);
 }
 else{
   reference_x=x;
   reference_y=y;
 }
 double vx=(*cell)[sxyp].getVectorX();
 double vy=(*cell)[sxyp].getVectorY();
 double th=(*cell)[sxyp].getTheta();
 double x_displacement=(double)((*cell)[sxyp].getSumX()+reference_x)/(double)((*cell)[sxyp].Area()+1)-(double)(*cell)[sxyp].getSumX()/(double)(*cell)[sxyp].Area();
 double y_displacement=(double)((*cell)[sxyp].getSumY()+reference_y)/(double)((*cell)[sxyp].Area()+1)-(double)(*cell)[sxyp].getSumY()/(double)(*cell)[sxyp].Area();

 double norm_inner_product=(x_displacement*(*cell)[sxyp].getVectorX()+y_displacement*(*cell)[sxyp].getVectorY())/
(sqrt(pow((*cell)[sxyp].getVectorX(),2)+pow((*cell)[sxyp].getVectorY(),2))*sqrt(pow(x_displacement,2)+pow(y_displacement,2)));
 double alpha=std::acos(norm_inner_product);
 DH_persistence=(int)-par.lambda_persistence*std::cos(alpha);
 // cout << x_displacement <<"," << y_displacement <<","<<  vx <<"," << vy <<"," << th<< "," << norm_inner_product << ", " << DH_persistence << endl;
}}

 DH+=DH_persistence;

  /************************Act-based vector alignment****************/
 //  ///*schooling vector
 //  int DH_alignment=0;
 //  int A=0;
 //  int B=0;
 //  int C=0;
 //  int D=0;
 //  int E=0;
 //  int F=0;
 //  // cout << (thetime>100) << endl;
 //  if (par.lambda_Act && par.lambda_schooling && (thetime>100)){
 //  //Compute the relevant before and after inner products:
 //  //Compute contact surface of sxy and sxyp
 //
 //    int contact_sxy=0;
 //    int contact_sxy_change=0;
 //    std::vector<double> vxy(3);
 //    if (sxy>0){
 //    ComputeActVectorRemoveSite(x,y,(*cell)[sxy],PDEfield,vxy);}
 //    // cout << "after remove site vector calculation" << endl;
 //  int contact_sxyp=0;
 //  int contact_sxyp_change=0;
 //    std::vector<double> vxyp(3);
 //  if(sxyp>0){
 //  ComputeActVectorAddSite(x,y,(*cell)[sxyp],PDEfield,vxyp);}
 //  // cout << "after add site vector calculation" << endl;
 //  // for (int i=1;i<cell->size();++i){
 //  //   if (sxy>0){
 //  //   contact_sxy+=NB[sxy][i];
 //  //   if (i!=sxyp)
 //  //   contact_sxy_change+=NB[sxy][i]+xy_neighbour_changes[i];
 //  //   else
 //  //   contact_sxy_change+=NB[sxy][i]+xy_neighbour_changes[i]+xyp_neighbour_changes[sxy];}
 //  //   if (sxyp>0){
 //  //   contact_sxyp+=NB[sxyp][i];
 //  //   if (i!=sxy)
 //  //   contact_sxyp_change+=NB[sxyp][i]+xyp_neighbour_changes[i];
 //  //   else
 //  //   contact_sxyp_change+=NB[sxyp][i]+xyp_neighbour_changes[i]+xy_neighbour_changes[sxyp];}
 //  // }
 // // cout << "contacts established" << endl;
 //  // if (sxy>0 & contact_sxy<=0){
 //  // cout << "current cell has no contacts" << endl;
 //  // for (int i=1; i<cell->size();++i){
 //    // cout << NB[sxy][i] << " ";
 //  // }
 //  // cout << endl;
 //  // }
 //  // if (sxy>0 & contact_sxy_change<=0){
 //  // cout << "future cell "<< sxy <<" has no contacts by taking sigma" << sxyp<< " " << contact_sxy_change << endl;
 //  // for (i=0;i<=n_nb;i++) {
 //    // int xp2,yp2;
 //    // xp2=x+nx[i]; yp2=y+ny[i];
 //    // cout << nx[i] << " " << ny[i] << " " << sigma[xp2][yp2] << endl;}
 //    // cout << endl;
 //  // for (int i=1; i<cell->size();++i){
 //  //   cout << i << " " << NB[sxy][i] << " ";
 //  //   if (i==sxyp)
 //  //   cout << xy_neighbour_changes[i]+xyp_neighbour_changes[sxy] <<endl;
 //  //   else
 //  //   cout << xy_neighbour_changes[i] <<endl;
 //  // }
 //  // }
 //  for (int j=1; j<cell->size();++j){
 //  //   //Part A & C cell sxy
 //    double vxy_norm_x=vxy[0]/sqrt(vxy[0]*vxy[0]+vxy[1]*vxy[1]);//vxy[2])/sqrt((vxy[0]/vxy[2])*(vxy[0]/vxy[2])+(vxy[1]/vxy[2])*(vxy[1]/vxy[2]));
 //    double vxy_norm_y=vxy[1]/sqrt(vxy[0]*vxy[0]+vxy[1]*vxy[1]);
 //    double vxyp_norm_x=vxyp[0]/sqrt(vxyp[0]*vxyp[0]+vxyp[1]*vxyp[1]);
 //    double vxyp_norm_y=vxyp[1]/sqrt(vxyp[0]*vxyp[0]+vxyp[1]*vxyp[1]);
 //    double jxy_norm_x=((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())/sqrt(((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())*((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())+((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber())*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //    double jxy_norm_y=((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber())/sqrt(((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())*((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())+((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber())*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //    double sxy_norm_x=((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())/sqrt(((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())*((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())+((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber())*((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber()));
 //    double sxy_norm_y=((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber())/sqrt(((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())*((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())+((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber())*((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber()));
 //    double sxyp_norm_x=((*cell)[sxyp].getVectorActX()/(*cell)[sxyp].GetBorderNumber())/sqrt(((*cell)[sxyp].getVectorActX()/(*cell)[sxyp].GetBorderNumber())*((*cell)[sxyp].getVectorActX()/(*cell)[sxyp].GetBorderNumber())+((*cell)[sxyp].getVectorActY()/(*cell)[sxyp].GetBorderNumber())*((*cell)[sxyp].getVectorActY()/(*cell)[sxyp].GetBorderNumber()));
 //    double sxyp_norm_y=((*cell)[sxyp].getVectorActY()/(*cell)[sxyp].GetBorderNumber())/sqrt(((*cell)[sxyp].getVectorActX()/(*cell)[sxyp].GetBorderNumber())*((*cell)[sxyp].getVectorActX()/(*cell)[sxyp].GetBorderNumber())+((*cell)[sxyp].getVectorActY()/(*cell)[sxyp].GetBorderNumber())*((*cell)[sxyp].getVectorActY()/(*cell)[sxyp].GetBorderNumber()));
 //    if (sxy>0){
 //      if (j!=sxy){
 //        if (j!=sxyp){
 //          if (NB[sxy][j]+xy_neighbour_changes[j]>0){
 //            // A-=par.lambda_schooling*(((NB[sxy][j]+xy_neighbour_changes[j])/contact_sxy_change)*(vxy[0] * ((*cell)[j].getVectorActX())+vxy[1]*(*cell)[j].getVectorActY()));
 //            // A-=par.lambda_schooling * (NB[sxy][j]+xy_neighbour_changes[j])*(vxy[0] * ((*cell)[j].getVectorActX())+vxy[1]*(*cell)[j].getVectorActY());}
 //            // cout << vxy[0] << " " << vxy[2] << " " <<(*cell)[j].getVectorActX() << " " << (*cell)[j].GetBorderNumber() << endl;
 //            // cout << (vxy[0]/vxy[2]) * ((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())<< endl;
 //              // A-=par.lambda_schooling *((vxy[0]/vxy[2]) * ((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())+(vxy[1]/vxy[2])*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //            A-=par.lambda_schooling *((vxy_norm_x) * (jxy_norm_x)+(vxy_norm_y)*(jxy_norm_y));}
 //          if (NB[sxy][j]>0){
 //            //bereken voor bekende vector het inproduct, vermenigvuldig met contactoppervlak gedeeld door totale contactoppervlak
 //              // B+= par.lambda_schooling*((NB[sxy][j]/(double) contact_sxy)* ((*cell)[sxy].getVectorActX()*(*cell)[j].getVectorActX()+(*cell)[sxy].getVectorActY()*(*cell)[j].getVectorActY()));
 //              // B+= par.lambda_schooling* NB[sxy][j] * ((*cell)[sxy].getVectorActX()*(*cell)[j].getVectorActX()+(*cell)[sxy].getVectorActY()*(*cell)[j].getVectorActY());}}
 //              // B+= par.lambda_schooling * (((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())*((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())+
 //              // ((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber())*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //              B+= par.lambda_schooling * ((sxy_norm_x)*(jxy_norm_x)+
 //              (sxy_norm_y)*(jxy_norm_y));
 //            }}
 //        else{
 //          if (NB[sxy][j]+xy_neighbour_changes[j]+xyp_neighbour_changes[sxy]>0){
 //            // A-=par.lambda_schooling*(((NB[sxy][j]+xy_neighbour_changes[j]+xyp_neighbour_changes[sxy])/contact_sxy_change)*(vxy[0] * ((*cell)[j].getVectorActX())+vxy[1]*(*cell)[j].getVectorActY()))
 //            // A-=par.lambda_schooling*(NB[sxy][j]+xy_neighbour_changes[j]+xyp_neighbour_changes[sxy])*(vxy[0] * ((*cell)[j].getVectorActX())+vxy[1]*(*cell)[j].getVectorActY());}
 //            // C-=par.lambda_schooling*((vxy[0]/vxy[2]) * ((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())+(vxy[1]/vxy[2]) *((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //          C-=par.lambda_schooling*((vxy_norm_x) * (jxy_norm_x)+(vxy_norm_y) *(jxy_norm_y));}
 //          if (NB[sxy][j]>0){
 //            // B+=par.lambda_schooling* NB[sxy][j] * ((*cell)[sxy].getVectorActX()*(*cell)[j].getVectorActX()+(*cell)[sxy].getVectorActY()*(*cell)[j].getVectorActY());}
 //            // D+=par.lambda_schooling * (((*cell)[sxy].getVectorActX()/(*cell)[sxy].GetBorderNumber())*((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())
 //            // +((*cell)[sxy].getVectorActY()/(*cell)[sxy].GetBorderNumber())*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //            D+=par.lambda_schooling * ((sxy_norm_x)*(jxy_norm_x)
 //            +(sxy_norm_y)*(jxy_norm_y));}
 //        }}}
 //
 //    if (sxyp>0){
 //      if (j!=sxyp){
 //        if (j!=sxy){
 //          if (NB[sxyp][j]+xyp_neighbour_changes[j]>0){
 //            // C-=par.lambda_schooling*(((NB[sxyp][j]+xyp_neighbour_changes[j])/contact_sxyp_change)*(vxyp[0]*(*cell)[j].getVectorActX()+vxyp[1]*(*cell)[j].getVectorActY()));
 //            // C-=par.lambda_schooling* (NB[sxyp][j]+xyp_neighbour_changes[j])*(vxyp[0]*(*cell)[j].getVectorActX()+vxyp[1]*(*cell)[j].getVectorActY());}
 //            // E-=par.lambda_schooling * ((vxyp[0]/vxyp[2])*((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())+(vxyp[1]/vxyp[2])*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //          E-=par.lambda_schooling * ((vxyp_norm_x)*(jxy_norm_x)+(vxyp_norm_y)*(jxy_norm_y));}
 //          if (NB[sxyp][j]>0){
 //            // D+=par.lambda_schooling*((NB[sxyp][j]/(double) contact_sxyp)* ((*cell)[sxyp].getVectorActX()*(*cell)[j].getVectorActX()+(*cell)[sxyp].getVectorActY()*(*cell)[j].getVectorActY()));
 //            // D+=par.lambda_schooling* NB[sxyp][j] * ((*cell)[sxyp].getVectorActX()*(*cell)[j].getVectorActX()+(*cell)[sxyp].getVectorActY()*(*cell)[j].getVectorActY());}
 //            // F+=par.lambda_schooling * (((*cell)[sxyp].getVectorActX()/(*cell)[sxyp].GetBorderNumber())*((*cell)[j].getVectorActX()/(*cell)[j].GetBorderNumber())
 //            // +((*cell)[sxyp].getVectorActY()/(*cell)[sxyp].GetBorderNumber())*((*cell)[j].getVectorActY()/(*cell)[j].GetBorderNumber()));
 //            F+=par.lambda_schooling * ((sxyp_norm_x)*(jxy_norm_x)
 //            +(sxyp_norm_y)*(jxy_norm_y));}
 //          }}}
 //        }
 //    // if (sxyp>0 & sxy>0){
 //    //
 //    // }
 //
 //  }
 //  //
 //  DH_alignment=A+(C+E)+B+(D+F);
 //  DH+=DH_alignment;
 //   // cout << "Even after this" << endl;
 // // delete [] xy_neighbour_changes;
 // // delete [] xyp_neighbour_changes;
 //

  /************************The matrix interaction model****************/
 // let the cell extend with
/*	if (par.lambda_matrix)
{

	if (par.geometric_mean){
	 double  matrix_retracting=1;
   int nxp =0,nret =0;


     	for (int i1=-1;i1<=1;i1++)
     		for (int i2=-1;i2<=1;i2++){

       		if (sigma[x+i1][y+i2]>=0 && sigma[x+i1][y+i2] == sigma[x][y]){
       			matrix_retracting *= GetMatrixLevel(x+i1,y+i2);
						nret++;
       		}
       	}

     	// apply the smoothing
     	//Act_expanding*= pow( PDEfield->Sigma(2,xp,yp), w-1);
     	//Act_retracting*= pow(PDEfield->Sigma(2,x,y), w-1);
     	//nxp += w-1;
     	//nret += w-1;

     	matrix_retracting= pow(matrix_retracting, 1./nret);

  if( (*cell)[sxy].AliveP()){

	   DH+= par.lambda_matrix/par.max_matrix * matrix_retracting;

		}
}
	else {if( (*cell)[sxy].AliveP()){
	   DH+= par.lambda_matrix *pow( GetMatrixLevel(x,y)/par.max_matrix,par.single_site_power);}}


}
*/
/****** Matrix interaction retraction yield energy ****/
int DH_matrix_interaction=0;
	if ( sxyp == MEDIUM && par.lambda_matrix){// should be done for all retractions, I assume.
	DH_matrix_interaction+=par.lambda_matrix * (GetMatrixLevel(x,y));//(par.age_saturation + GetMatrixLevel(x,y));
	}
DH+=DH_matrix_interaction;

// cout << "Contact energies "<< DH_adhesive_energy << endl;
// cout << "Area " << DH_area << endl;
// cout << "Perimeter " << DH_perimeter << endl;
// cout << "Length " << DH_length << endl;
// cout << "Act " << DH_act << endl;
// cout << "Alignment " << DH_alignment << endl;
// cout << "Alignment A " <<  A<< endl;
// cout << "Alignment B" <<  B<< endl;
// cout << "Alignment C" <<  C<< endl;
// cout << "Alignment D" <<  D<< endl;
// cout << "Alignment E" <<  E<< endl;
// cout << "Alignment F" <<  F<< endl;
// cout << "Chemotaxis " << DDH << endl;
// cout << "Matrix interaction " << DH_matrix_interaction << endl;
// cout << endl;
  return DH;
}



bool CellularPotts::Probability(int DH)
{
  if ( DH > BOLTZMANN-1 )
    return false;
  else if ( DH < 0 || RANDOM() < copyprob[DH] )
    return true;
   return false;
}

void CellularPotts::ConvertSpin(int x,int y,int xp,int yp)
{
  int tmpcell;
  if ( (tmpcell=sigma[x][y]) ) { // if tmpcell is not MEDIUM

    (*cell)[tmpcell].DecrementArea();
    (*cell)[tmpcell].RemoveSiteFromMoments(x,y);
    (*cell)[tmpcell].SetPerimeter(GetNewPerimeterIfXYWereRemoved(tmpcell,x,y));

    if (!(*cell)[tmpcell].Area()) {
      (*cell)[tmpcell].Apoptose();
      cerr << "Cell " << tmpcell << " apoptosed\n";
    }
  }
  if ( (tmpcell=sigma[xp][yp])>0 ) {// if tmpcell is not MEDIUM
    (*cell)[tmpcell].IncrementArea();
    (*cell)[tmpcell].AddSiteToMoments(x,y);
		(*cell)[tmpcell].SetPerimeter(GetNewPerimeterIfXYWereAdded(tmpcell,x,y));

  }
  // for (int i=1;i<=4;i++) {
  //   int xp2,yp2;
  //   xp2=x+nx[i]; yp2=y+ny[i];
  //   if (par.periodic_boundaries) {
  //     if (xp2<=0)
  //       xp2=sizex-2+xp2;
  //     if (yp2<=0)
  //       yp2=sizey-2+yp2;
  //     if (xp2>=sizex-1)
  //       xp2=xp2-sizex+2;
  //     if (yp2>=sizey-1)
  //       yp2=yp2-sizey+2;}
  //   if (sigma[x][y]!=sigma[xp2][yp2]){
  //   NB[sigma[x][y]][sigma[xp2][yp2]]-=1;
  //   NB[sigma[xp2][yp2]][sigma[x][y]]-=1;}
  //   if (sigma[xp][yp]!=sigma[xp2][yp2]){
  //   NB[sigma[xp][yp]][sigma[xp2][yp2]]+=1;
  //   NB[sigma[xp2][yp2]][sigma[xp][yp]]+=1;}
  // }
  // if (par.extended_neighbour_border){
  //   for (int i=5;i<=8;i++) {
  //     int xp2,yp2;
  //     xp2=x+nx[i]; yp2=y+ny[i];
  //     if (par.periodic_boundaries) {
  //       if (xp2<=0)
  //         xp2=sizex-2+xp2;
  //       if (yp2<=0)
  //         yp2=sizey-2+yp2;
  //       if (xp2>=sizex-1)
  //         xp2=xp2-sizex+2;
  //       if (yp2>=sizey-1)
  //         yp2=yp2-sizey+2;}
  //   NB[sigma[x][y]][sigma[xp2][yp2]]-=1;
  //   NB[sigma[xp2][yp2]][sigma[x][y]]-=1;
  //   NB[sigma[xp][yp]][sigma[xp2][yp2]]+=1;
  //   NB[sigma[xp2][yp2]][sigma[xp][yp]]+=1;
  //  }
  //  }
  if (sigma[xp][yp]<=-2){//if pillar, let retract cell to medium
    sigma[x][y]=0;
  }
  else{
  sigma[x][y] = sigma[xp][yp];
}
}


/** PUBLIC **/
int CellularPotts::CopyvProb(int DH,  double stiff) {
  // cout << "inside copyvprob" << endl;
  double dd;
  int s;
  s=(int)stiff;
  if (DH<=-s) return 2;

  // if DH becomes extremely large, calculate probability on-the-fly
  if (DH+s > BOLTZMANN-1)
    dd=exp( -( (double)(DH+s)/par.T ));
  else{
  // cout <<"try to print copyprob[DH+s] because less or equal to " << BOLTZMANN-1 << endl;
  // cout << DH << endl;
  // cout << DH+s << endl;
  // cout << copyprob[DH+s] << endl;
    dd=copyprob[DH+s];}
  if (RANDOM()<dd) return 1; else return 0;
  // cout << "end copyvprob" << endl;
}

void CellularPotts::CopyProb(double T) {
  int i;
  for ( i = 0; i < BOLTZMANN; i++ )
    copyprob[i] = exp( -( (double)(i)/T ) );
}

void CellularPotts::FreezeAmoebae(void)
{
  if (frozen)
    frozen=FALSE;
  else
    frozen=TRUE;
}

#include <fstream>
//! Monte Carlo Step. Returns summed energy change
int CellularPotts::AmoebaeMove(PDE *PDEfield)
{
  double loop,p;
  //int updated=0;
  thetime++;
  int SumDH=0;

  if (frozen)
    return 0;

  int x,y;
  int xp,yp;
  int k,kp;

  int H_diss;
  int D_H;

	int xn, yn; //neighbour cells
  // loop = edgeSetpair.size() / n_nb;
  loop = edgeSetVector.size_map()/n_nb;
  // cout << edgeSetVector.size_map() << " "<< edgeSetVector.size_vector() << " " << edgeSetpair.size() << endl;
  for (int i = 0; i < loop; i++){
    int edgesize=edgeSetVector.size_map();
    if (edgesize==0){break;}
    else{
      // std::vector<std::array<int,4>> escopy(edgeSetpair.begin(), edgeSetpair.end());
      // int bucket_counter=0;
      // int b = 0;
      // while (b<edgeSetpair.size()){
      //   // cout << "test bucketing " << b <<  endl;
      //   if (edgeSetpair.bucket_size(bucket_counter)>0){
      //     int bb;
      //     for (bb = 0; bb<edgeSetpair.bucket_size(bucket_counter); bb++){
      //       // cout << "test bucketing " << b << " " << bb << endl;
      //       bucketpair[b+bb]={bucket_counter, bb};
      //       }
      //   b+=bb;
      //   }
      //   bucket_counter++;
      // }
      // // cout << bucketpair.size() << " " << edgeSetpair.size() << endl;
      // std::array<int,4> it = escopy[RandomNumber(edgeSetpair.size()-1)];
      // int rbucket= bp[0];
      // int rstep = bp[1];
      // std::unordered_set<std::array<int, 4>>::const_local_iterator it = edgeSetpair.begin(rbucket);
      // while (rstep>0){
      //     it++;
      //     rstep--;
      //     }
      int rindex=RandomNumber(edgesize-1);
      // int nbuckets = edgeSetpair.bucket_count();
      // int rbucket = RandomNumber(nbuckets-1);
      // while (edgeSetpair.bucket_size(rbucket)==0){
      //     if (rbucket<nbuckets-1){rbucket++;}
      //     else{rbucket=0;}}
      // std::unordered_set<std::array<int, 4>>::const_local_iterator it = edgeSetpair.begin(rbucket);
      // int rstep = RandomNumber(edgeSetpair.bucket_size(rbucket))-1;
      // while (rstep>0){
      //     it++;
      //     rstep--;
      //     }
      auto it = edgeSetVector[rindex];
      x=(*it).first[0];
      y=(*it).first[1];
      xp=(*it).first[2];
      yp=(*it).first[3];
      k=sigma[x][y];

      if (par.periodic_boundaries) {

         // since we are asynchronic, we cannot just copy the borders once
         // every MCS
         if (x<=0)
           x=sizex-2+x;
         if (y<=0)
           y=sizey-2+y;
         if (x>=sizex-1)
           x=x-sizex+2;
         if (y>=sizey-1)
           y=y-sizey+2;
        if (xp<=0)
          xp=sizex-2+xp;
        if (yp<=0)
          yp=sizey-2+yp;
        if (xp>=sizex-1)
          xp=xp-sizex+2;
        if (yp>=sizey-1)
          yp=yp-sizey+2;
      }

      kp=sigma[xp][yp];
      // Don't even think of copying the special border state into you! Do allow pillars to be copied from, but not into.
      if (k>=0 && kp!=-1) {
        // cout << "Check ConnectivityPreservedPCluster" << endl;
        if ( par.cluster_connectivity==false || ConnectivityPreservedPCluster(x,y)){
      	// connectivity dissipation:
      	H_diss=0;
      	if (!ConnectivityPreservedP(x,y)) H_diss=par.conn_diss;
        int D_H=DeltaH(x,y,xp,yp,PDEfield);
        if ((p=CopyvProb(D_H,H_diss))>0) {
      	  ConvertSpin ( x,y,xp,yp );

          for (int j = 1; j <= n_nb; j++){
    				xn = nx[j]+x;
    				yn = ny[j]+y;

    				if (par.periodic_boundaries) {
    					 	// since we are asynchronic, we cannot just copy the borders once
    					 	// every MCS
    					if (xn<=0)
    						xn=sizex-2+xn;
    					if(yn<=0)
    						yn=sizey-2+yn;
    					if (xn>=sizex-1)
    						xn=xn-sizex+2;
    				  if (yn>=sizey-1)
    						yn=yn-sizey+2;
    				}
    				if (xn>0 && yn>0 && xn<sizex-1 && yn<sizey-1){//if the neighbour site is within the lattice
              // std::unordered_set<std::array<int,4>>::const_iterator edge_in_set =(edgeSetpair.find({x,y,xn,yn}));

              // auto it_to = std::find(edgeVector.begin(), edgeVector.end(), {x,y,xn,yn});
              // int index_to = std::distance(edgeVector.begin(), it_to);
              // std::vector<std::array<int,4>>::iterator it_fro = std::find(edgeVector.begin(), edgeVector.end(), {xn,yn,x,y});
              // int index_fro = std::distance(edgeVector.begin(), it_fro);

    					// if (edge_in_set==edgeSetpair.end() && sigma[xn][yn] != sigma[x][y] && sigma[xn][yn]+sigma[x][y]!=-2){ //if we should add the edge to the edgelist, add it
              if (sigma[xn][yn] != sigma[x][y] && sgn(sigma[xn][yn])+sgn(sigma[x][y])>=0){ //if we should add the edge to the edgelist, add it
                // edgeSetpair.insert({x,y,xn,yn});
                // edgeSetpair.insert({xn,yn,x,y});
                edgeSetVector.insert({x,y,xn,yn});
                edgeSetVector.insert({xn,yn,x,y});
                // if (it_to==edgeVector.end()){
                //     edgeVector.push_back({x,y,xn,yn});
                // }
                // else if (it_fro==edgeVector.end()){
                //     edgeVector.push_back({xn,yn,x,y});
                // }

                loop += (double)2/n_nb;
    					}
    					// if (edge_in_set!=edgeSetpair.end() && (sigma[xn][yn] == sigma[x][y] || sigma[xn][yn]+sigma[x][y]==-2)){//if the sites have the same celltype and they have an edge, remove it
              if ((sigma[xn][yn] == sigma[x][y] || sgn(sigma[xn][yn])+sgn(sigma[x][y])<0)){
                // edgeSetpair.erase({x,y,xn,yn});
                // edgeSetpair.erase({xn,yn,x,y});
                edgeSetVector.erase({x,y,xn,yn});
                edgeSetVector.erase({xn,yn,x,y});
                // if (it_to!=edgeVector.end()){
                //     edgeVector.erase(it_to);
                // }
                // else if (it_fro!=edgeVector.end()){
                //     edgeVector.erase(it_fro);
                // }
    						loop -= (double)2/n_nb;
    					}
    				}
    			}

      	  SumDH+=D_H;
      		if (par.lambda_Act>0){
            // Update actin field
            if (sigma[x][y]>0){
            actPixels[{x,y}]=par.max_Act;
            std::unordered_set<std::array<int,2>>::const_iterator it =(alivePixels.find({x,y}));
            if (it==alivePixels.end()){
            alivePixels.insert({x,y});
            }
          }
          else{
            std::unordered_set<std::array<int,2>>::const_iterator it =(alivePixels.find({x,y}));
            if (it!=alivePixels.end()){
            alivePixels.erase({x,y});
            }
            std::unordered_map<std::array<int,2>, int>::const_iterator ap =(actPixels.find({x,y}));
            if (ap!=actPixels.end()){
              actPixels.erase({x,y});
            }
          }}
          //Update adhesive areas
          if (kp == 0){
            getCell(k).DecrementAdhesiveArea(GetMatrixLevel(x,y));
          }
          else if (k==0){
            // getCell(kp).IncrementAdhesiveArea(1);
          }
          else {
            getCell(k).DecrementAdhesiveArea(GetMatrixLevel(x,y));
            // getCell(kp).IncrementAdhesiveArea(1);
          }

      		if (par.lambda_matrix>0){
            // Update matrix interaction field
      			if (sigma[x][y]>0){
      			// matrixPixels[{x,y}]=0;
            matrix[x][y]=0;
            }
      			else {
      			// matrixPixels.erase({x,y});
            matrix[x][y]=0;
          }

          }

        }
    }
  }}}
  return SumDH;
}


/** A simple method to plot all sigma's in window
    without the black lines */
void CellularPotts::PlotSigma(Graphics *g, int mag) {

  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++) {
      for (int xm=0;xm<mag;xm++)
	for (int ym=0;ym<mag;ym++)
      g->Point( sigma[x][y], mag*x+xm, mag*y+ym);
  }

}

int **CellularPotts::SearchNandPlot(Graphics *g, bool get_neighbours)
{
  int i, j,q;
  int **neighbours=0;


  /* Allocate neighbour matrix */
  if (get_neighbours) {
    neighbours=(int **)malloc((cell->size()+1)*sizeof(int *));
    if (neighbours==NULL)
      MemoryWarning();

    neighbours[0]=(int *)malloc((cell->size()+1)*(cell->size()+1)*sizeof(int));
    if (neighbours[0]==NULL)
      MemoryWarning();

    for (i=1;i<(int)cell->size()+1;i++)
      neighbours[i]=neighbours[i-1]+(cell->size()+1);

    /* Clear this matrix */
    for (i=0;i<((int)cell->size()+1)*((int)cell->size()+1);i++)
      neighbours[0][i]=EMPTY;
  }

  for ( i = 0; i < sizex-1; i++ )
    for ( j = 0; j < sizey-1; j++ ) {


      int colour;
      if (sigma[i][j]<=0) {
	colour=0;
      } else {
	colour = (*cell)[sigma[i][j]].Colour();
	//colour = sigma[i][j];
      }

      if (g && sigma[i][j]>0)  /* if draw */
        g->Point( colour, 2*i, 2*j);

      if ( sigma[i][j] != sigma[i+1][j] )  /* if cellborder */ /* etc. etc. */
	{
	  if (g)
	    g->Point( 1, 2*i+1, 2*j );
	  if (get_neighbours) {
	    if (sigma[i][j]>0) {
	      for (q=0;q<(int)cell->size();q++)
		if (neighbours[sigma[i][j]][q]==EMPTY) {
		  neighbours[sigma[i][j]][q]=sigma[i+1][j];
		  break;
		}
		else
		  if (neighbours[sigma[i][j]][q]==sigma[i+1][j])
		    break;
	    }
	    if (sigma[i+1][j]>0) {
	      for (q=0;q<(int)cell->size();q++)
		if (neighbours[sigma[i+1][j]][q]==EMPTY) {
		  neighbours[sigma[i+1][j]][q]=sigma[i][j];
		  break;
		}
		else
		  if (neighbours[sigma[i+1][j]][q]==sigma[i][j])
		    break;
	    }
	  }
	}
      else
        if (g && sigma[i][j]>0)
          g->Point( colour, 2*i+1, 2*j );


      if ( sigma[i][j] != sigma[i][j+1] ) {

        if (g)
	  g->Point( 1, 2*i, 2*j+1 );

	if (get_neighbours) {
	  if (sigma[i][j]>0) {
	    for (q=0;q<(int)cell->size();q++)
	      if (neighbours[sigma[i][j]][q]==EMPTY) {
		neighbours[sigma[i][j]][q]=sigma[i][j+1];
		break;
	      }
	      else
		if (neighbours[sigma[i][j]][q]==sigma[i][j+1])
		  break;
	  }

	  if (sigma[i][j+1]>0) {

	    for (q=0;q<(int)cell->size();q++)
	      if (neighbours[sigma[i][j+1]][q]==EMPTY) {
		neighbours[sigma[i][j+1]][q]=sigma[i][j];
		break;
	      }
	      else
		if (neighbours[sigma[i][j+1]][q]==sigma[i][j])
		  break;
	  }
	}
      }
      else
        if (g && sigma[i][j]>0)
          g->Point( colour, 2*i, 2*j+1 );

      /* Cells that touch eachother's corners are NO neighbours */

      if (sigma[i][j]!=sigma[i+1][j+1]
	  || sigma[i+1][j]!=sigma[i][j+1] ) {
        if (g)
          g->Point( 1, 2*i+1, 2*j+1 );
      }
      else
        if (g && sigma[i][j]>0)
          g->Point( colour, 2*i+1, 2*j+1 );
    }

  if (get_neighbours)
    return neighbours;
  else
    return 0;

}

void **CellularPotts::SearchNandPlotClear(Graphics *g)
{
  int i, j,q;

  for ( i = 0; i < sizex-1; i++ )
    for ( j = 0; j < sizey-1; j++ ) {


      int colour;
      if (sigma[i][j]<=0) {
	colour=0;
      } else {
	colour = (*cell)[sigma[i][j]].Colour();
	//colour = sigma[i][j];
      }

      if ( sigma[i][j] != sigma[i+1][j] )  /* if cellborder */ /* etc. etc. */
	{
	  if (g)
	    g->Point( 1, 2*i+1, 2*j );
	}
      if ( sigma[i][j] != sigma[i][j+1] ) {

        if (g)
	  g->Point( 1, 2*i, 2*j+1 );
      }
      /* Cells that touch eachother's corners are NO neighbours */

      if (sigma[i][j]!=sigma[i+1][j+1]
	  || sigma[i+1][j]!=sigma[i][j+1] ) {
        if (g)
          g->Point( 1, 2*i+1, 2*j+1 );
      }
      // else
      //   if (g && sigma[i][j]>0)
      //     g->Point( colour, 2*i+1, 2*j+1 );
    }

}
void **CellularPotts::PlotVectors(Graphics *g){
  // cout << "plotting vectors" << endl;
  // cout << cell->size() << endl;
  for (int i=1;i<=cell->size()-1;i++){
    // cout << i << endl;
    // cout << (*cell)[i].area << endl;
    int x1,y1,x2,y2;
    if ((*cell)[i].area>0){
    x1=(int) (((double)(*cell)[i].sum_x)/(double)(*cell)[i].area) %sizex;
    y1=(int) (((double)(*cell)[i].sum_y)/(double)(*cell)[i].area) %sizey;
    if ((*cell)[i].GetBorderNumber()>0){
      if (x1>sizex or x1<0){
        cout << "x1 outside field" << endl;
      }
    x2=x1+(int)(10*(*cell)[i].getVectorActX()/sqrt((*cell)[i].getVectorActX()*(*cell)[i].getVectorActX()+(*cell)[i].getVectorActY()*(*cell)[i].getVectorActY()));
    y2=y1+(int)(10*(*cell)[i].getVectorActY()/sqrt((*cell)[i].getVectorActX()*(*cell)[i].getVectorActX()+(*cell)[i].getVectorActY()*(*cell)[i].getVectorActY()));
  }
    else{ x2=0;y2=0;
    }
    // cout << "add line" << endl;
    // cout << x1 << " "<< y1 << " " << x2 << " " << y2 << endl;
    g->Arrow(2*x1,2*y1,2*x2,2*y2,1);
    //g->Line(2*x1,2*y1,2*x2,2*y2,1);
    // cout << "line added" << endl;
  }

  }
}

int **CellularPotts::SearchNeighboursMatrix()
{
  int i, j;
  int** neighbours = new int*[cell->size()+1];
  for (int i = 0; i < (int)cell->size()+1; i++)
		neighbours[i] = new int[cell->size()+1];
  // int **neighbours=0;
// int **neighbours[cell->size()+1][cell->size()+1] = {{0}};

  // /* Allocate neighbour matrix */
  //   neighbours=(int **)malloc((cell->size()+1)*sizeof(int *));
  //   if (neighbours==NULL)
  //     MemoryWarning();
  //
  //   for (i=0;i<(int)cell->size()+1;i++){
  //     neighbours[i]=(int *)malloc((cell->size()+1)*(cell->size()+1)*sizeof(int));
  //   if (neighbours[i]==NULL)
  //     MemoryWarning();}
  //
  //   for (i=1;i<(int)cell->size()+1;i++)
  //     neighbours[i]=neighbours[i-1]+(cell->size()+1);
  //
  //   /* Clear this matrix */
  for (i=0;i<((int)cell->size()+1);i++)
   for (j=0;j<((int)cell->size()+1);j++)
    neighbours[i][j]=0;
  // }

  for ( i = 0; i < sizex-1; i++ )
    for ( j = 0; j < sizey-1; j++ ) {
    int iplus=i+1;
    int jplus=j+1;
    if (par.periodic_boundaries) {
    if (iplus<=0)
iplus=sizex-2+iplus;
    if (jplus<=0)
jplus=sizey-2+jplus;
    if (iplus>=sizex-1)
iplus=iplus-sizex+2;
    if (jplus>=sizey-1)
jplus=jplus-sizey+2;}

      if ( sigma[i][j] != sigma[i+1][j] )  /* if cellborder */ /* etc. etc. */
	{
	 	neighbours[sigma[i][j]][sigma[iplus][j]]+=1;
    neighbours[sigma[iplus][j]][sigma[i][j]]+=1;
		}

    if ( sigma[i][j] != sigma[i][j+1] ) {
    neighbours[sigma[i][j]][sigma[i][jplus]]+=1;
    neighbours[sigma[i][jplus]][sigma[i][j]]+=1;
	}

    if (par.extended_neighbour_border){ //if extended_neighbour_border is true, also count cells touching by a corner.

      if (sigma[i][j]!=sigma[i+1][j+1]){
      neighbours[sigma[i][j]][sigma[iplus][jplus]]+=1;
      }

	  if(sigma[i+1][j]!=sigma[i][j+1] ) {
    neighbours[sigma[iplus][j]][sigma[i][jplus]]+=1;
      }
    }}
    return neighbours;
}

int CellularPotts::GetNewPerimeterIfXYWereAdded(int sxyp,int x, int y) {

 /*int n_nb;

  if (par.neighbours>=1 && par.neighbours<=4)
    n_nb=nbh_level[par.neighbours];
 */
  int perim = (*cell)[sxyp].Perimeter();

   /* the cell with sigma sxyp wants to extend by adding lattice site (x, y).
  This means that the sxyp neighbours of (x,y) will not be borders anymore,so they can be
  subtracted from the perimeter of sxyp.
 */
   for (int i=1;i<=n_nb;i++) {

    int xp2,yp2;

    xp2=x+nx[i]; yp2=y+ny[i];

    if (par.periodic_boundaries) {

	    if (xp2<=0)
		    xp2=sizex-2+xp2;
	    if (yp2<=0)
		    yp2=sizey-2+yp2;
	    if (xp2>=sizex-1)
		    xp2=xp2-sizex+2;
	    if (yp2>=sizey-1)
		    yp2=yp2-sizey+2;
    }
    if (sigma[xp2][yp2] ==sxyp){
      perim--;
    }
    else{
    perim++;
    }

 }
return perim;
}

int CellularPotts::GetActLevel(int x, int y){
if (sigma[x][y]>0)
  return(actPixels[{x,y}]);
else
  return(0);}
// std::unordered_map<std::array<int,2>,int>::const_iterator it =(actPixels.find({x,y}));
// if (it!=actPixels.end()){
//   return(it->second);}
//   else{
//   return(0);
//   }
//  }
//matrixPixels Implementation
 // int CellularPotts::GetMatrixLevel(int x, int y){
 // std::unordered_map<std::array<int,2>,int>::const_iterator it =(matrixPixels.find({x,y}));
 // if (it!=matrixPixels.end()){
 //   return(it->second);}
 //   else{
 //   return(0);
 //   }
 //  }
 //matrix array implementation
  int CellularPotts::GetMatrixLevel(int x, int y){
  if (matrix[x][y]>0){
    return(matrix[x][y]);}
  else{
    return(0);
  }}

int CellularPotts:: GetNewPerimeterIfXYWereRemoved(int sxy, int x, int y) {

  /*int n_nb;

   if (par.neighbours>=1 && par.neighbours<=4)
    int n_nb=nbh_level[par.neighbours];
  */
   int perim = (*cell)[sxy].Perimeter();
    /* the cell with sigma sxy loses xy
 */
  for (int i=1;i<=n_nb;i++) {

    int xp2,yp2;
    xp2=x+nx[i]; yp2=y+ny[i];
    if (par.periodic_boundaries) {

	    if (xp2<=0)
		    xp2=sizex-2+xp2;
	    if (yp2<=0)
		    yp2=sizey-2+yp2;
	    if (xp2>=sizex-1)
		    xp2=xp2-sizex+2;
	    if (yp2>=sizey-1)
		    yp2=yp2-sizey+2;
    }
    if (sigma[xp2][yp2] ==sxy){
      perim++;
    }
    else{
    perim--;
    }

 }
  return perim;
 }
void CellularPotts::ReadZygotePicture(void) {



  int pix,cells,i,j,c,p,checkx,checky;
  char **pixelmap;
  char pixel[3];

  sscanf(ZYGXPM(ZYGOTE)[0],"%d %d %d %d",&checkx,&checky,&cells,&pix);

  if ((checkx>sizex)||(checky>sizey)) {
    std::cerr <<  "ReadZygote: The included xpm picture is smaller than the grid!\n";
    std::cerr << "\n Please adjust either the grid size or the picture size.\n";
    std::cerr << sizex << "," << sizey << "," << checkx << "," << checky << "\n";
    exit(1);
  }

  pixelmap=(char **)malloc(cells*sizeof(char *));
  if (pixelmap==NULL) MemoryWarning();

  pixelmap[0]=(char *)malloc(cells*3*sizeof(char));
  if (pixelmap[0]==NULL) MemoryWarning();

  for(i=1;i<cells;i++)
    pixelmap[i]=pixelmap[i-1]+3;

  for (i=0;i<cells;i++) {
    for (j=0;j<pix;j++)
      pixelmap[i][j]=ZYGXPM(ZYGOTE)[i+1][j];
    pixelmap[i][pix]='\0';
  }

  for (i=0;i<sizex*sizey;i++) sigma[0][i]=0;
  fprintf(stderr,"[%d %d]\n",checkx,checky);

  int offs_x, offs_y;
  offs_x=(sizex-checkx)/2;
  offs_y=(sizey-checky)/2;

  for (i=0;i<checkx;i++)
    for (j=0;j<checky;j++) {
      for (p=0;p<pix;p++)
        pixel[p]=ZYGXPM(ZYGOTE)[cells+1+j][i*pix+p];

      pixel[pix]='\0';

      for (c=0;c<cells;c++) {
	if (!(strcmp(pixelmap[c],pixel))) {
	  if ( (sigma[offs_x+i][offs_y+j]=c) ) {

	    // if c is _NOT_ medium (then c=0)
	    // assign pixel values from "sigmamax"
	    sigma[offs_x+i][offs_y+j]+=(Cell::MaxSigma()-1);
	  }
	}

      }
    }

  free(pixelmap[0]);
  free(pixelmap);
}


// void CellularPotts::ConstructInitCells (Dish &beast) {
//
//   // Get the maximum cell ID (mostly equal to the cell number)
//   int loop=sizex*sizey;
//   int cells=0;
//   for (int i=0;i<loop;i++) {
//     if (cells<sigma[0][i]) cells=sigma[0][i];
//   }
//
//   cerr << "[ cells = " << cells << "]\n";
//
//   // construct enough cells for the zygote.  "cells", contains the
//   // number of colours (excluding background).
//   {
//     for (int i=0; i<cells; i++) {
//       cell->push_back(Cell(beast));
//     }
//   }
//
//   // Set the area and target area of the cell
//   // makes use of the pointer to the Cell pointer of Dish
//   // which is a member of CellularPotts
//   //MeasureCellSizes();
//
//   // set zygote_area to mean cell area.
//   int mean_area=0;
//   for (vector<Cell>::iterator c=cell->begin();c!=cell->end();c++) {
// 		MeasureCellSize(*c);
//     mean_area+=c->Area();
//   }
//   if (cells!=0)
//     mean_area/=cells;
//
//   zygote_area=mean_area;
//
//   cout << "mean_area = " << mean_area << "\n";
//   // set all cell areas to the mean area
//   {
//     for (vector<Cell>::iterator c=cell->begin();c!=cell->end();c++) {
//       if (par.target_area) {
// 	c->SetTargetArea(par.target_area);
//       } else	 {
// 	c->SetTargetArea(mean_area);
//       }
//
//      if (par.target_perimeter) {
// 			 c->SetTargetPerimeter(par.target_perimeter);
//
// 		}
//
//
//     }
//   }
// }
//
// void CellularPotts::MeasureCellSizes(void) {
//
//   // Clean areas of all cells, including medium
//   for (vector<Cell>::iterator c=cell->begin();c!=cell->end();c++) {
// //     c->SetTargetArea(0);
// //     c->area = 0;
// 		MeasureCellSize(*c);
//   }
//
// //   // calculate the area of the cells
// //   for (int x=1;x<sizex-1;x++) {
// //     for (int y=1;y<sizey-1;y++) {
// //       if (sigma[x][y]) {
// // 	(*cell)[sigma[x][y]].IncrementTargetArea();
// // 	(*cell)[sigma[x][y]].IncrementArea();
// // 	(*cell)[sigma[x][y]].AddSiteToMoments(x,y);
// //
// //       }
// //     }
// //   }
// }

 void CellularPotts::ConstructInitCells (Dish &beast,int tau, int TArea,int TPerimeter) {

	vector<Cell>::iterator it;


	// Get the maximum cell ID (mostly equal to the cell number)
	int loop=sizex*sizey;
	int cells=0;
	int nr_existing_cells = cell->size()-1;
	for (int i=0;i<loop;i++) {
		if (cells<sigma[0][i]) cells=sigma[0][i];
	}

	//cerr << "[ cells = " << cells << "]\n";
	//cerr << "[ size cell vector = " << cell->size() << "]\n";
	// construct enough cells for the zygote.  "cells", contains the
	// number of colours (excluding background).
	{
		for (int i=0; i<(cells - nr_existing_cells); i++){
			Cell c1=Cell(beast, tau);
			//cout<< "Initial value granzyme "<< c1.GF()<< endl;
			MeasureCellSize(c1);
			//c1.setTau(tau);
			c1.SetTargetArea(TArea);
			c1.SetTargetPerimeter(TPerimeter);
      if (par.lambda_persistence){
      c1.SetTheta((RANDOM()-1)*2*3.141592653589793238462643383279502884L);
    }
			cell->push_back(c1);

		}
	}
// NB=SearchNeighboursMatrix();

// for (int i=0;i<=cell->size();i++){
//   for (int j=0;j<=cell->size();j++){
//     cout << NB[i][j] << " ";
//   }
//   cout << endl;
// }
}

 void CellularPotts::ConstructInitCells (Dish &beast,int tau, int TArea,int TPerimeter, int AdArea) {

	vector<Cell>::iterator it;


	// Get the maximum cell ID (mostly equal to the cell number)
	int loop=sizex*sizey;
	int cells=0;
	int nr_existing_cells = cell->size()-1;
	for (int i=0;i<loop;i++) {
		if (cells<sigma[0][i]) cells=sigma[0][i];
	}

	//cerr << "[ cells = " << cells << "]\n";
	//cerr << "[ size cell vector = " << cell->size() << "]\n";
	// construct enough cells for the zygote.  "cells", contains the
	// number of colours (excluding background).
	{
		for (int i=0; i<(cells - nr_existing_cells); i++){
			Cell c1=Cell(beast, tau);
			//cout<< "Initial value granzyme "<< c1.GF()<< endl;
			MeasureCellSize(c1);
			//c1.setTau(tau);
			c1.SetTargetArea(TArea);
			c1.SetTargetPerimeter(TPerimeter);
			c1.SetReferenceAdhesiveArea(AdArea);
      if (par.lambda_persistence){
      c1.SetTheta((RANDOM()-1)*2*3.141592653589793238462643383279502884L);
    }
			cell->push_back(c1);

		}
	}

// NB=SearchNeighboursMatrix();

}
  void CellularPotts::MeasureCellSize(Cell &c) {

c.CleanMoments();
cerr<< " Measuring cell " <<c.Sigma()<<endl;
// calculate the area of the cell
	for (int x=1;x<sizex-1;x++) {
		for (int y=1;y<sizey-1;y++) {

			if (sigma[x][y] == c.sigma) {
        //check if pixel in alivePixels, if not, then add
        std::unordered_set<std::array<int,2>>::const_iterator it =(alivePixels.find({x,y}));
        if (it==alivePixels.end()){
        alivePixels.insert({x,y});
        }

				c.IncrementTargetArea();
				c.IncrementArea();
				c.AddSiteToMomentsMeasureCell(x,y);
				//c.AddSiteToInfMoments(x,y);

				//cout<< "n_nb : "<<n_nb<< endl;
				for (int i=1;i<=n_nb;i++) {
					int xp2,yp2;
					xp2=x+nx[i]; yp2=y+ny[i];
					if (par.periodic_boundaries) {

						if (xp2<=0)
							xp2=sizex-2+xp2;
						if (yp2<=0)
							yp2=sizey-2+yp2;
						if (xp2>=sizex-1)
							xp2=xp2-sizex+2;
						if (yp2>=sizey-1)
							yp2=yp2-sizey+2;
					}
					// did we find a border?
					if (sigma[xp2][yp2]!=sigma[x][y]){
						//add to the perimeter of the cell
						c.IncrementTargetPerimeter();
						c.IncrementPerimeter();

						//cerr<< "Perimeter cell "<< c.Sigma()<<": "<< c.Perimeter()<<endl;
						//cerr<< "Target perimeter cell "<<c.TargetPerimeter()<<endl;

					}
				}

			}
		}
	}
		c.SetTargetArea(par.target_area);
		c.SetTargetPerimeter(par.target_perimeter);
// 		c.inf_sum_x = c.sum_x;
// 		c.inf_sum_y = c.sum_y;
			//c.meanX = c.sum_x/(double)c.area;
			//c.meanY = c.sum_y/(double)c.area;
//     c.old_meanX = c.meanX;
//     c.old_meanY = c.meanY;
//     c.meanX_inf = c.meanX;
//     c.meanY_inf = c.meanY;

  // set the actual area to the target area
//   {
//   for (vector<Cell>::iterator c=cell->begin();c!=cell->end();c++) {
//     c->SetAreaToTarget();
//
//
//   }
 // }
}

//
// void CellularPotts::ComputeActVector(Cell &c, PDE *PDEfield) {
// //center based computation
// // cerr<< " Measuring cell " <<c.Sigma()<<endl;
// double sumAct=0;
// double sumDist=0;
// double vx=0;
// double vy=0;
// // calculate the area of the cell
// for (int x=1;x<sizex-1;x++) {
//   for (int y=1;y<sizey-1;y++) {
//     if (sigma[x][y] == c.sigma) {
//       // if (sigma[x][y]== 1){
//       // cout << " x addition " << (double) ( (x+round((c.getCenterX()-x)/ this->SizeX()) * this->SizeX()) - c.getCenterX())  * (PDEfield->Sigma(2,x,y)/(double)par.max_Act) << endl;}
//       // double pixelDist=sqrt(pow((double)((x+round(((c.getCenterX())-x)/ this->SizeX()) * this->SizeX())-c.getCenterX()),2)+ pow((double)((y+round(((c.getCenterY())-y)/ this->SizeY()) * this->SizeY())-c.getCenterY()),2));
//       // if (pixelDist>0){
//       vx+=(double) ( (x+round((c.getCenterX()-x)/ this->SizeX()) * this->SizeX()) - c.getCenterX())  * PDEfield->Sigma(2,x,y)/((double) par.max_Act);//*pixelDist);
//       vy+=(double) ( (y+round((c.getCenterY()-y)/ this->SizeY()) * this->SizeY())- c.getCenterY())*(PDEfield->Sigma(2,x,y))/((double) par.max_Act)  ;//*pixelDist);
//       sumAct+=PDEfield->Sigma(2,x,y)/ (double) par.max_Act;
//       sumDist+=sqrt(pow((double)((x+round(((c.getCenterX())-x)/ this->SizeX()) * this->SizeX())-c.getCenterX()),2)+ pow((double)((y+round(((c.getCenterY())-y)/ this->SizeY()) * this->SizeY())-c.getCenterY()),2));
//     // }
//   }
// }}
// if (sumAct>0){
//   vx=vx/((sumDist/c.Area())*(sumAct));
//   // vx=vx/((sumAct)/(double) par.max_Act);
//   vy=vy/((sumDist/c.Area())*(sumAct));
//   // vy=vy/((sumAct)/(double) par.max_Act);
// }
// else {
//   vx=0;
//   vy=0;
// }
//
// c.SetVectorAct(vx,vy);
// c.SetBorderNumber(1);
//
// }

void CellularPotts::ComputeActVector(Cell &c, PDE *PDEfield) {
//border based vector

double border_x=0;
double border_y=0;
double border_number=0;
double vx=0;
double vy=0;

for (int x=1;x<sizex-1;x++) {
  for (int y=1;y<sizey-1;y++) {
    if (sigma[x][y] == c.sigma) {
      double border_pixel_x=0;
      double border_pixel_y=0;
      double missing_neighbours=0;
      for (int i=1;i<=12;i++) {
        int xp2,yp2;
        xp2=x+nx[i]; yp2=y+ny[i];
        if (par.periodic_boundaries) {
          if (xp2<=0)
      xp2=sizex-2+xp2;
          if (yp2<=0)
      yp2=sizey-2+yp2;
          if (xp2>=sizex-1)
      xp2=xp2-sizex+2;
          if (yp2>=sizey-1)
      yp2=yp2-sizey+2;
        }
        if ((not(xp2<=0 || yp2<=0
  	  || xp2>=sizex-1 || yp2>=sizey-1) and sigma[xp2][yp2]!=c.sigma) or (xp2<=0 || yp2<=0
	  || xp2>=sizex-1 || yp2>=sizey-1)){
          border_pixel_x+=nx[i]/(sqrt(pow(nx[i],2)+pow(ny[i],2)));
          border_pixel_y+=ny[i]/(sqrt(pow(nx[i],2)+pow(ny[i],2)));
          missing_neighbours+=1;
        }}
      if (missing_neighbours>0){
        border_x+= PDEfield->Sigma(2,x,y) * border_pixel_x/missing_neighbours;
        border_y+= PDEfield->Sigma(2,x,y) * border_pixel_y/missing_neighbours;
        border_number+=1;
      }}}}

if (border_number>0){
  vx=border_x;
  vy=border_y;
}
else {
  vx=0;
  vy=0;
}
if (isnan(vx) or isnan(vy)){
  cout << "ComputeActVector, nan encoutered" << endl;
  return;
}
c.SetVectorAct(vx,vy);
c.SetBorderNumber(border_number);
}

// void CellularPotts::ComputeActVectorAddSite(int new_x, int new_y, Cell &c, PDE *PDEfield, vector<double> &vector_act){
//   //center based vector
//   int sumAct=0;
//   sumAct+=par.max_Act;
//   new_x=(double)(new_x+round((c.getCenterX()-new_x)/ this->SizeX()) * this->SizeX());
//   new_y=(double)(new_y+round((c.getCenterY()-new_y)/ this->SizeY()) * this->SizeY());
//   double new_com_x=(c.getSumX()+new_x)/((double)c.Area()+1);
//   double new_com_y=(c.getSumY()+new_y)/((double)c.Area()+1);
//   double sumDist=0;
//   // double pixelDist=sqrt(pow((double)((new_x+round(((c.getCenterX())-new_x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((new_y+round(((c.getCenterY())-new_y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//   // double vx=0; double vy=0;
//   // if (pixelDist>0){
//     // cout << "add first" << endl;
//   double vx=(double) ( (new_x+round((c.getCenterX()-new_x)/ this->SizeX()) * this->SizeX()) - new_com_x);///pixelDist;
//   double vy=(double) ( (new_y+round((c.getCenterY()-new_y)/ this->SizeY()) * this->SizeY())- new_com_y);///pixelDist;
//   // cout << "after add first" << endl;
// // }
//   //double sumDist=sqrt(pow((double)((new_x+round(((c.getCenterX())-new_x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((new_y+round(((c.getCenterY())-new_y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//   // calculate the area of the cell
//   for (int x=1;x<sizex-1;x++) {
//     for (int y=1;y<sizey-1;y++) {
//       if (sigma[x][y] == c.sigma) {
//         // if (sigma[x][y]== 1){
//         // cout << " x addition " << (double) ( (x+round((c.getCenterX()-x)/ this->SizeX()) * this->SizeX()) - c.getCenterX())  * (PDEfield->Sigma(2,x,y)/(double)par.max_Act) << endl;}
//         // pixelDist=sqrt(pow((double)((x+round(((c.getCenterX())-x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((y+round(((c.getCenterY())-y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//         // if (pixelDist>0){
//           // cout << "add later" << endl;
//         vx+=(double) ( (x+round((c.getCenterX()-x)/ this->SizeX()) * this->SizeX()) - new_com_x)  * PDEfield->Sigma(2,x,y)/((double)par.max_Act);//*pixelDist);
//         vy+=(double) ( (y+round((c.getCenterY()-y)/ this->SizeY()) * this->SizeY())- new_com_y)* (PDEfield->Sigma(2,x,y))/((double)par.max_Act);//*pixelDist);
//         sumAct+=PDEfield->Sigma(2,x,y);
//         // cout << "after add alter" << endl;
//         sumDist+=sqrt(pow((double)((x+round(((c.getCenterX())-x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((y+round(((c.getCenterY())-y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//       // }
//     }
//   }}
//   if (sumAct>0){
//     // cout << "add normalizing"<< endl;
//     vx=vx/((sumDist/(c.Area()+1))*(sumAct/(double) par.max_Act));
//     // vx=vx/(sumAct/(double) par.max_Act);
//     vy=vy/((sumDist/(c.Area()+1))*(sumAct/(double) par.max_Act));
//     // vy=vy/(sumAct/(double) par.max_Act);
//     // cout << "add normalizing after" << endl;
//   }
//   else {
//     vx=0;
//     vy=0;
//   }
//   vector_act[0]=vx;
//   vector_act[1]=vy;
//  vector_act[2]=1;
//  // cout << "return vector" << endl;
// }

void CellularPotts::ComputeActVectorAddSite(int new_x, int new_y, Cell &c, PDE *PDEfield, vector<double> &vector_act){
  // cout << "assigning  help variables" << endl;
  double remove_from_border_x=0;
  double remove_from_border_y=0;
  double remove_from_border_number=0;
  double add_to_border_x=0;
  double add_to_border_y=0;
  double add_to_border_number=0;

  double nb_new_x=0;
  double nb_new_y=0;
  double missing_neighbours=0;

  for (int i=1;i<=12;i++) {
    // cout << "next neighbour" << endl;
    // cout <<" add_to_border_x" << add_to_border_x << endl;
    // cout <<" remove_from_border_x " << remove_from_border_x << endl;
    int xp2,yp2;
    xp2=new_x+nx[i]; yp2=new_y+ny[i];
    if (par.periodic_boundaries) {
      if (xp2<=0)
        xp2=sizex-2+xp2;
      if (yp2<=0)
        yp2=sizey-2+yp2;
      if (xp2>=sizex-1)
        xp2=xp2-sizex+2;
      if (yp2>=sizey-1)
        yp2=yp2-sizey+2;
    }
    // cout << " neighbour selected" << endl;
    // cout <<"xp2 " << xp2 << " yp2 "<< yp2 <<  endl;
    // cout << sigma[xp2][yp2] << endl;
    // cout << "do stuff with neighbour" << endl;
    if (not (xp2<=0 || yp2<=0
  || xp2>=sizex-1 || yp2>=sizey-1) and sigma[xp2][yp2]==c.sigma){
      // cout <<" part of cell" << endl;
      double nb_b_x=0;
      double nb_b_y=0;
      double missing_neighbours_b=0;
      // double empty_close_neighbours=0;
      int i_new=0;
      for (int j=1;j<=12;j++){
      int xp3,yp3;
      xp3=xp2+nx[j]; yp3=yp2+ny[j];
      if (par.periodic_boundaries) {
        if (xp3<=0)
          xp3=sizex-2+xp3;
        if (yp3<=0)
          yp3=sizey-2+yp3;
        if (xp3>=sizex-1)
          xp3=xp3-sizex+2;
        if (yp3>=sizey-1)
          yp3=yp3-sizey+2;
      }
      if ((xp3<=0 || yp3<=0
	  || xp3>=sizex-1 || yp3>=sizey-1) or sigma[xp3][yp3]!=c.sigma){
        nb_b_x+=nx[j]/(sqrt(pow(nx[j],2)+pow(ny[j],2)));
        nb_b_y+=ny[j]/(sqrt(pow(nx[j],2)+pow(ny[j],2)));
        missing_neighbours_b+=1;
        // if (j <=5)
        //   empty_close_neighbours+=1;
        if (xp3==new_x & yp3==new_y){
          i_new=j;
        }
      }}
      if (missing_neighbours_b>0){
      remove_from_border_x+=PDEfield->Sigma(2,xp2,yp2)*nb_b_x/missing_neighbours_b;
      remove_from_border_y+=PDEfield->Sigma(2,xp2,yp2)*nb_b_y/missing_neighbours_b;
      if (missing_neighbours_b==1){
        remove_from_border_number+=1;
      }
      else{
        // cout << "missing_neighbours_b "<< missing_neighbours_b << endl;
        add_to_border_x+=(nb_b_x-nx[i_new])* PDEfield->Sigma(2,xp2,yp2)/(missing_neighbours_b-1);
        add_to_border_x+=(nb_b_y-ny[i_new])* PDEfield->Sigma(2,xp2,yp2)/(missing_neighbours_b-1);
      }
    }

    }
    else{
      // cout << " outside cell" << endl;
      nb_new_x+=nx[i]/(sqrt(pow(nx[i],2)+pow(ny[i],2)));
      nb_new_y+=ny[i]/(sqrt(pow(nx[i],2)+pow(ny[i],2)));
      missing_neighbours+=1;
      // cout << "added to help variables" << endl;
    }}
  // cout <<"updating vector" << endl;
  // cout << add_to_border_x << endl;
  if (missing_neighbours>0){
  add_to_border_x+=nb_new_x*par.max_Act/missing_neighbours;
  add_to_border_y+=nb_new_y*par.max_Act/missing_neighbours;
  add_to_border_number+=1;}
  double vx=c.getVectorActX()-remove_from_border_x+add_to_border_x;
  double vy=c.getVectorActY()-remove_from_border_y+add_to_border_y;
  double border=c.GetBorderNumber()-remove_from_border_number+add_to_border_number;
  // cout << "add site" << remove_from_border_x << " " << add_to_border_x << " " << missing_neighbours << " " << nb_new_x << endl;
  if (isnan(vx) or isnan(vy)){
    cout << "ComputeActVectorAddSite, nan encountered" << endl;
    return;}
  vector_act[0]=vx;
  vector_act[1]=vy;
  vector_act[2]=border;
}

// void CellularPotts::ComputeActVectorRemoveSite(int new_x, int new_y, Cell &c, PDE *PDEfield, vector<double> &vector_act){
//   int sumAct=0;
//   // sumAct+=par.max_Act;
//
//   new_x=(double)(new_x+round((c.getCenterX()-new_x)/ this->SizeX()) * this->SizeX());
//   new_y=(double)(new_y+round((c.getCenterY()-new_y)/ this->SizeY()) * this->SizeY());
//   double new_com_x=(c.getSumX()-new_x)/((double)c.Area()-1);
//   double new_com_y=(c.getSumY()-new_y)/((double)c.Area()-1);
//   double vx=0;//(double) ( (new_x+round((c.getCenterX()-new_x)/ this->SizeX()) * this->SizeX()) - new_com_x)  * par.max_Act;
//   double vy=0;//(double) ( (new_y+round((c.getCenterY()-new_y)/ this->SizeY()) * this->SizeY())- new_com_y)* par.max_Act;
//   // double sumDist=0;
//   // double pixelDist;
//   double sumDist=sqrt(pow((double)((new_x+round(((c.getCenterX())-new_x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((new_y+round(((c.getCenterY())-new_y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//   // calculate the area of the cell
//   for (int x=1;x<sizex-1;x++) {
//     for (int y=1;y<sizey-1;y++) {
//       if (sigma[x][y] == c.sigma) {
//         if (x!=new_x && y!=new_y)
//         // if (sigma[x][y]== 1){
//         // cout << " x addition " << (double) ( (x+round((c.getCenterX()-x)/ this->SizeX()) * this->SizeX()) - c.getCenterX())  * (PDEfield->Sigma(2,x,y)/(double)par.max_Act) << endl;}
//         // double pixelDist=sqrt(pow((double)((x+round(((c.getCenterX())-x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((y+round(((c.getCenterY())-y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//         // if (pixelDist>0){
//         vx+=(double) ( (x+round((c.getCenterX()-x)/ this->SizeX()) * this->SizeX()) - new_com_x)  * PDEfield->Sigma(2,x,y)/((double)par.max_Act);//*pixelDist);
//         vy+=(double) ( (y+round((c.getCenterY()-y)/ this->SizeY()) * this->SizeY())- new_com_y)*(PDEfield->Sigma(2,x,y))/((double)par.max_Act);//*pixelDist);
//         sumAct+=PDEfield->Sigma(2,x,y);
//         sumDist+=sqrt(pow((double)((x+round(((c.getCenterX())-x)/ this->SizeX()) * this->SizeX())-new_com_x),2)+ pow((double)((y+round(((c.getCenterY())-y)/ this->SizeY()) * this->SizeY())-new_com_y),2));
//       // }
//     }
//   }}
//   if (sumAct>0){
//     vx=vx/((sumDist/(c.Area()-1))*(sumAct/(double) par.max_Act));
//     // vx=vx/((sumAct/(double) par.max_Act));//=
//     vy=vy/((sumDist/(c.Area()-1))*(sumAct/(double) par.max_Act));
//     // vy=vy/((sumAct/(double) par.max_Act));//
//   }
//   else {
//     vx=0;
//     vy=0;
//   }
//   vector_act[0]=vx;
//   vector_act[1]=vy;
//     vector_act[2]=1;
// }

void CellularPotts::ComputeActVectorRemoveSite(int new_x, int new_y, Cell &c, PDE *PDEfield, vector<double> &vector_act){
  double remove_from_border_x=0;
  double remove_from_border_y=0;
  double remove_from_border_number=0;
  double add_to_border_x=0;
  double add_to_border_y=0;
  double add_to_border_number=0;

  double nb_new_x=0;
  double nb_new_y=0;
  double missing_neighbours=0;

  for (int i=1;i<=12;i++) {
    // cout << "remove_from_border_x" << remove_from_border_x << endl;
    int xp2,yp2;
    xp2=new_x+nx[i]; yp2=new_y+ny[i];
    if (par.periodic_boundaries) {
      if (xp2<=0)
        xp2=sizex-2+xp2;
      if (yp2<=0)
        yp2=sizey-2+yp2;
      if (xp2>=sizex-1)
        xp2=xp2-sizex+2;
      if (yp2>=sizey-1)
        yp2=yp2-sizey+2;
    }
    if (not(xp2<=0 || yp2<=0
  || xp2>=sizex-1 || yp2>=sizey-1) and sigma[xp2][yp2]==c.sigma){
      double nb_b_x=0;
      double nb_b_y=0;
      double missing_neighbours_b=0;
      // double empty_close_neighbours=0;
      int i_new=0;
      for (int j=1;j<=12;j++){
      int xp3,yp3;
      xp3=xp2+nx[j]; yp3=yp2+ny[j];
      if (par.periodic_boundaries) {
        if (xp3<=0)
          xp3=sizex-2+xp3;
        if (yp3<=0)
          yp3=sizey-2+yp3;
        if (xp3>=sizex-1)
          xp3=xp3-sizex+2;
        if (yp3>=sizey-1)
          yp3=yp3-sizey+2;
      }
      if ((xp2<=0 || yp2<=0
	  || xp2>=sizex-1 || yp2>=sizey-1) or sigma[xp3][yp3]!=c.sigma){
        nb_b_x+=nx[j]/(sqrt(pow(nx[j],2)+pow(ny[j],2)));
        nb_b_y+=ny[j]/(sqrt(pow(nx[j],2)+pow(ny[j],2)));
        missing_neighbours_b+=1;
        // if (j<=5)
        //   empty_close_neighbours+=1;
        if (xp3==new_x & yp3==new_y){
          i_new=j;
        }
      }}
      if (missing_neighbours_b>=0){
        add_to_border_x+=(nb_b_x-nx[i_new])* PDEfield->Sigma(2,xp2,yp2)/(missing_neighbours_b+1);
        add_to_border_x+=(nb_b_y-ny[i_new])* PDEfield->Sigma(2,xp2,yp2)/(missing_neighbours_b+1);
      if (missing_neighbours_b==0){
        add_to_border_number+=1;
      }
      else{
        remove_from_border_x+=nb_b_x*PDEfield->Sigma(2,xp2,yp2)/missing_neighbours_b;
        remove_from_border_y+=nb_b_y*PDEfield->Sigma(2,xp2,yp2)/missing_neighbours_b;}
      }


    }
    else{
      nb_new_x+=nx[i]/(sqrt(pow(nx[i],2)+pow(ny[i],2)));
      nb_new_y+=ny[i]/(sqrt(pow(nx[i],2)+pow(ny[i],2)));
      missing_neighbours+=1;
    }}
  remove_from_border_x+=nb_new_x*PDEfield->Sigma(2,new_x,new_y)/missing_neighbours;
  remove_from_border_y+=nb_new_y*PDEfield->Sigma(2,new_x,new_y)/missing_neighbours;
  remove_from_border_number+=1;
  double vx=c.getVectorActX()-remove_from_border_x+add_to_border_x;
  double vy=c.getVectorActY()-remove_from_border_y+add_to_border_y;
  double border=c.GetBorderNumber()-remove_from_border_number+add_to_border_number;
  // cout << "remove site" << remove_from_border_x << " " << add_to_border_x << " " << missing_neighbours << " " << nb_new_x << endl;
  if (isnan(vx) or isnan(vy)){
    cout << "ComputeActVectorRemoveSite, nan encountered" << endl;
    return;}
  vector_act[0]=vx;
  vector_act[1]=vy;
  vector_act[2]=border;
}

// void CellularPotts::MeasureCellSize(Cell &c) {
//
//   c.CleanMoments();
//
//   // calculate the area of the cell
//   for (int x=1;x<sizex-1;x++) {
//     for (int y=1;y<sizey-1;y++) {
//       if (sigma[x][y] == c.sigma) {
// 	(*cell)[sigma[x][y]].IncrementTargetArea();
// 	(*cell)[sigma[x][y]].IncrementArea();
// 	(*cell)[sigma[x][y]].AddSiteToMoments(x,y);
//
//       }
//     }
//   }
//
// //   // set the actual area to the target area
// //   {
// //   for (vector<Cell>::iterator c=cell->begin();c!=cell->end();c++) {
// //     c->SetAreaToTarget();
//
// //   }
//
// }

Dir *CellularPotts::FindCellDirections(void) const
{

  double *sumx=0,*sumy=0;
  double *sumxx=0,*sumxy=0,*sumyy=0;
  double *n=0;

  double xmean=0,ymean=0,sxx=0,sxy=0,syy=0;
  double D,lb1=0,lb2=0;


  Dir *celldir;

  /* Allocation of sufficient memory space */
  if( (sumx= (double *)malloc(cell->size()*sizeof(double)))==NULL)
    MemoryWarning();
  else
    if( (sumy= (double *)malloc(cell->size()*sizeof(double)))==NULL)
      MemoryWarning();
    else
      if ((sumxx=(double *)malloc(cell->size()*sizeof(double)))==NULL)
	MemoryWarning();
      else
	if((sumxy=(double *)malloc(cell->size()*sizeof(double)))==NULL)
	  MemoryWarning();
	else
	  if((sumyy=(double *)malloc(cell->size()*sizeof(double)))==NULL)
	    MemoryWarning();
	  else
	    if((n=(double *)malloc(cell->size()*sizeof(double)))==NULL)
	      MemoryWarning();


  if ( !(celldir=new Dir[cell->size()]) )
    MemoryWarning();


  /* Initialization of the variables */

  for (int i=0;i<(int)cell->size();i++) {

    sumx[i]=0.;
    sumy[i]=0.;
    sumxx[i]=0.;
    sumxy[i]=0.;
    sumyy[i]=0.;
    n[i]=0L;

  }


  /* Find sumx, sumy, sumxx and sumxy for all cells */

  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++)
      if (sigma[x][y]>0) {
	sumx[0]+=(double)x;
	sumy[0]+=(double)y;
	sumxx[0]+=(double)x*x;
	sumxy[0]+=(double)x*y;
	sumyy[0]+=(double)y*y;

	n[0]++;

	sumx[sigma[x][y]]+=(double)x;
	sumy[sigma[x][y]]+=(double)y;

	sumxx[sigma[x][y]]+=(double)x*x;
	sumxy[sigma[x][y]]+=(double)x*y;
	sumyy[sigma[x][y]]+=(double)y*y;

	n[sigma[x][y]]++;

      }

  /* Compute the principal axes for all cells */

  {
    for (int i=0;i<(int)cell->size();i++) {

      if (n[i]>10) {

	xmean=((double)sumx[i])/((double)n[i]);
	ymean=((double)sumy[i])/((double)n[i]);

	sxx=(double)(sumxx[i])-((double)(sumx[i]*sumx[i]))/(double)n[i];
	sxx=sxx/(double)(n[i]-1);

	sxy=(double)(sumxy[i])-((double)(sumx[i]*sumy[i]))/(double)n[i];
	sxy=sxy/(double)(n[i]-1);

	syy=(double)(sumyy[i])-((double)(sumy[i]*sumy[i]))/(double)n[i];
	syy=syy/(double)(n[i]-1);

	D=sqrt( (sxx+syy)*(sxx+syy)-4.*(sxx*syy-sxy*sxy) );
	lb1=(sxx+syy+D)/2.;lb2=(sxx+syy-D)/2.;
	celldir[i].lb1=lb1; celldir[i].lb2=lb2;
      }
      if (sxy==0.0)
	celldir[i].bb1=1.;
      else
	celldir[i].bb1=sxy/(lb1-syy);

      if (fabs(celldir[i].bb1)<.00001) {
	if (celldir[i].bb1>0.)
	  celldir[i].bb1=.00001;
	else
	  celldir[i].bb1=-.00001;
      }

      celldir[i].aa1=ymean-xmean*celldir[i].bb1;
      celldir[i].bb2= (-1.)/celldir[i].bb1;

      celldir[i].aa2=ymean-celldir[i].bb2*xmean;
    }

  }

  /* bevrijd gealloceerd geheugen */
  free(sumx);
  free(sumy);
  free(sumxx);
  free(sumxy);
  free(sumyy);
  free(n);

  return celldir;

}

void CellularPotts::ShowDirections(Graphics &g, const Dir *celldir) const
{
  int i;

  if (cell->size()>1)
    for (i=1;i<(int)cell->size();i++)
      g.Line(0,(int)(2*celldir[i].aa1),sizex*2,(int)((celldir[i].aa1+celldir[i].bb1*sizey)*2),2);

}

void CellularPotts::DivideCells(vector<bool> which_cells)
{

  // for the cell directions
  Dir *celldir=0;

  /* Allocate space for divisionflags */
  int *divflags=(int *)malloc((cell->size()*2+5)*sizeof(int));

  /* Clear divisionflags */
  for (int i=0;i<(int)(cell->size()*2+5);i++)
    divflags[i]=0;


  if ( !(which_cells.size()==0 || which_cells.size()>=cell->size()) ) {
    throw "In CellularPotts::DivideCells, Too few elements in vector<int> which_cells.";
  }

  /* division */
  {for (int i=0;i<sizex;i++)
      for (int j=0;j<sizey;j++)
	if (sigma[i][j]>0) // i.e. not medium and not border state (-1)
	  {


	    // Pointer to mother. Warning: Renew pointer after a new
	    // cell is added (push_back). Then, the array *cell is relocated and
	    // the pointer will be lost...

	    Cell *motherp=&((*cell)[sigma[i][j]]);
	    Cell *daughterp;

	    /* Divide if NOT medium and if DIV bit set or divide_always is set */
	    // if which_cells is given, divide only if the cell
	    // is marked in which_cells.
	    if  ( !which_cells.size() || which_cells[motherp->sigma] )    {

	      if (!(divflags[ motherp->Sigma() ]) ) {

		// add daughter cell, copying states of mother
		daughterp=new Cell(*(motherp->owner));
		daughterp->CellBirth(*motherp);
		cell->push_back(*daughterp);

		// renew pointer to mother
		motherp=&((*cell)[sigma[i][j]]);

		divflags[ motherp->Sigma() ]=daughterp->Sigma();
		delete daughterp;

		// array may be relocated after "push_back"

		// renew daughter pointers
		daughterp=&(cell->back());

		/* administration on the onset of mitosis */

		/* Ancestry is taken care of in copy constructor of Cell
		   see cell.hh: Cell(const Cell &src, bool newcellP=false) : Cytoplasm(src) {} */

		/* inherit  polarity of mother */
		// All that needs to be copied is copied in the copy constructor
		// of Cell and in the default copy constr. of its base class Cytoplasm
		// note: also the celltype is inherited



	      } else {
		daughterp=&((*cell)[ divflags[motherp->Sigma()] ]);
	      }


	      /* Now the actual division takes place */

	      /* If celldirections where not yet computed: do it now */
	      if (!celldir)
		celldir=FindCellDirections();

	      /* if site is below the minor axis of the cell: sigma of new cell */
	      if (j>((int)(celldir[motherp->sigma].aa2+
			   celldir[motherp->sigma].bb2*(double)i))) {

		motherp->DecrementArea();
		motherp->DecrementTargetArea();
		motherp->RemoveSiteFromMoments(i,j);
		sigma[i][j]=daughterp->Sigma();
		daughterp->AddSiteToMoments(i,j);
		daughterp->IncrementArea();
		daughterp->IncrementTargetArea();

	      }


	    }

	  }
  }
  if (celldir)
    delete[] (celldir);

  if (divflags)
    free(divflags);
}


/**! Fill the plane with initial cells
 \return actual amount of cells (some are not draw due to overlap) */
int CellularPotts::ThrowInCells(int n,int cellsize) {

  //  int gapx=(sizex-nx*cellsize)/(nx+1);
  //int gapy=(sizey-ny*cellsize)/(ny+1);

  int cellnum=1;

  for (int i=0;i<n;i++) {

    // draw a circle at x0, y0
    int x0=RandomNumber(sizex);
    int y0=RandomNumber(sizey);

    bool overlap=false;

    // check overlap
    for (int x=0;x<cellsize;x++)
      for (int y=0;y<cellsize;y++)
	if ( (
	      ( (x-cellsize/2)*(x-cellsize/2)+(y-cellsize/2)*(y-cellsize/2) )<
	      ( (cellsize/2)*(cellsize/2))) &&
	     ( x0+x<sizex && y0+y<sizey ) )
	  if (sigma[x0+x][y0+y]) {
	    overlap=true;
	    break;
	  }

    if (!overlap) {
      for (int x=0;x<cellsize;x++)
	for (int y=0;y<cellsize;y++)
	  if ( (
		( (x-cellsize/2)*(x-cellsize/2)+(y-cellsize/2)*(y-cellsize/2) )<
		( (cellsize/2)*(cellsize/2))) &&
	       ( x0+x<sizex && y0+y<sizey ) )
	    sigma[x0+x][y0+y]=cellnum;

      cellnum++;
    }
  }
  cerr << "[ cellnum = " << cellnum << "]";

  // repair borders
  // fill borders with special border state
  for (int x=0;x<sizex-1;x++) {
    sigma[x][0]=-1;
    sigma[x][sizey-1]=-1;
  }
  for (int y=0;y<sizey-1;y++) {
    sigma[0][y]=-1;
    sigma[sizex-1][y]=-1;
  }

  {for (int x=1;x<sizex-2;x++) {
      sigma[x][1]=0;
      sigma[x][sizey-2]=0;
    }}
  {for (int y=1;y<sizey-2;y++) {
      sigma[1][y]=0;
      sigma[sizex-2][y]=0;
    }}
  return cellnum;
}


int CellularPotts::GrowInCells(int n_cells, int cell_size, double subfield) {


  int sx = (int)((sizex-2)/subfield);
  int sy = (int)((sizey-2)/subfield);

  int offset_x = (sizex-2-sx)/2;
  int offset_y = (sizey-2-sy)/2;

  if (n_cells==1) {
    return GrowInCells(1, cell_size, sizex/2, sizey/2, 0, 0);
  } else {
    return GrowInCells(n_cells, cell_size, sx, sy, offset_x, offset_y);
  }
}

int CellularPotts::GrowInCells(int n_cells, int cell_size, int sx, int sy, int offset_x, int offset_y) {

  // make initial cells using Eden Growth

  int **new_sigma=(int **)malloc(sizex*sizeof(int *));
  if (new_sigma==NULL)
    MemoryWarning();

  new_sigma[0]=(int *)malloc(sizex*sizey*sizeof(int));
  if (new_sigma[0]==NULL)
    MemoryWarning();

  for (int i=1;i<sizex;i++)
    new_sigma[i]=new_sigma[i-1]+sizey;

  /* Clear CA plane */
  { for (int i=0;i<sizex*sizey;i++)
     new_sigma[0][i]=0;
  }


  // scatter initial points, or place a cell in the middle
  // if only one cell is desired
  int cellnum=cell->size()-1;

  if (n_cells>1) {



    { for (int i=0;i<n_cells;i++) {

      sigma[RandomNumber(sx)+offset_x][RandomNumber(sy)+offset_y]=++cellnum;

    }}
  } else {
    sigma[sx][sy]=++cellnum;

  }

  // Do Eden growth for a number of time steps
  {for (int i=0;i<cell_size;i++) {
    for (int x=1;x<sizex-1;x++)
      for (int y=1;y<sizey-1;y++) {

	if (sigma[x][y]==0) {
	  // take a random neighbour
	  int xyp=(int)(8*RANDOM()+1);
	  int xp = nx[xyp]+x;
	  int yp = ny[xyp]+y;
	  int kp;
	  //  NB removing this border test yields interesting effects :-)
	  // You get a ragged border, which you may like!
    if (!IsPillar(xp,yp)){
	  if ((kp=sigma[xp][yp])!=-1)
	    if (kp>(cellnum-n_cells))
	      new_sigma[x][y]=kp;
	    else
	      new_sigma[x][y]=0;
	  else
	    new_sigma[x][y]=0;

	}} else {
	  new_sigma[x][y]=sigma[x][y];
	}
      }

    // copy sigma to new_sigma, but do not touch the border!
	  {  for (int x=1;x<sizex-1;x++) {
      for (int y=1;y<sizey-1;y++) {
        if (!IsPillar(x,y))
	sigma[x][y]=new_sigma[x][y];
      }
    }
  }}}
  free(new_sigma[0]);
  free(new_sigma);

  return cellnum;
}


// Predicate returns true when connectivity is locally preserved
// if the value of the central site would be changed
bool CellularPotts::ConnectivityPreservedP(int x, int y) {

  // Use local nx and ny in a cyclic order (starts at upper left corner)
  // first site is repeated, for easier looping
  const int cyc_nx[10] = {-1, -1, 0, 1, 1, 1, 0, -1, -1, -1 };
  const int cyc_ny[10] = {0, -1,-1,-1, 0, 1, 1,  1,  0, -1 };

  int sxy=sigma[x][y]; // the central site
  if (sxy==0) return true;

  int n_borders=0; // to count the amount of sites in state sxy bordering a site !=sxy

  static int stack[8]; // stack to count number of different surrounding cells
  int stackp=-1;
  bool one_of_neighbors_medium=false;

  for (int i=1;i<=8;i++) {
    int xcn=x+cyc_nx[i];
    int ycn=y+cyc_ny[i];
    int xncn=x+cyc_nx[i+1];
    int yncn=y+cyc_ny[i+1];

    if (par.periodic_boundaries) {
      if (xcn<=0)
        xcn=sizex-2+xcn;
      if (ycn<=0)
        ycn=sizey-2+ycn;
      if (xcn>=sizex-1)
        xcn =xcn-sizex+2;
      if (ycn>=sizey-1)
        ycn=ycn-sizey+2;
      if (xncn<=0)
        xncn=sizex-2+xncn;
      if (yncn<=0)
        yncn=sizey-2+yncn;
      if (xncn>=sizex-1)
        xncn =xncn-sizex+2;
      if (yncn>=sizey-1)
        yncn=yncn-sizey+2;
    }

    int s_nb=sigma[xcn][ycn];
    int s_next_nb=sigma[xncn][yncn];

    if ((s_nb==sxy || s_next_nb==sxy) && (s_nb!=s_next_nb)) {

      // check whether s_nb is adjacent to non-identical site,
      // count it
      n_borders++;
    }
    int j;
    bool on_stack_p=false;

    // we need the next heuristic to prevent stalling at
    // cell-cell borders
    // do not enforce constraint at two cell interface(no medium)
    if (s_nb) {
      for (j=stackp;j>=0;j--) {
	if (s_nb==stack[j]) {
	  on_stack_p=true;
	  break;
	}
      }
      if (!on_stack_p) {
	if (stackp>6) {
	  cerr << "Stack overflow, stackp=" << stackp << "\n";
	}
	stack[++stackp]=s_nb;
      }
    } else {
      one_of_neighbors_medium=true;
    }
  }

  // number of different neighbours is stackp+1;
  if (n_borders>2 && ( (stackp+1)>2 || one_of_neighbors_medium) ) {
    return false;
  }
  else
    return true;

}



// Predicate returns true when cluster connectivity is locally preserved
// if the value of the central site would be changed
bool CellularPotts::ConnectivityPreservedPCluster(int x, int y) {

  // Use local nx and ny in a cyclic order (starts at upper left corner)
  // first site is repeated, for easier looping
  const int cyc_nx[10] = {-1, -1, 0, 1, 1, 1, 0, -1, -1, -1 };
  const int cyc_ny[10] = {0, -1,-1,-1, 0, 1, 1,  1,  0, -1 };

  int sxy=sigma[x][y]; // the central site
  if (sxy==0) return true;

  int n_borders=0; // to count the amount of sites in state sxy bordering a site !=sxy

  static int stack[8]; // stack to count number of different surrounding cells
  int stackp=-1;
  bool one_of_neighbors_medium=false;

  for (int i=1;i<=8;i++) {
    int xcn=x+cyc_nx[i];
    int ycn=y+cyc_ny[i];
    int xncn=x+cyc_nx[i+1];
    int yncn=y+cyc_ny[i+1];

        if (par.periodic_boundaries) {

    if (xcn<=0)
xcn=sizex-2+xcn;
    if (ycn<=0)
ycn=sizey-2+ycn;
    if (xcn>=sizex-1)
xcn =xcn-sizex+2;
    if (ycn>=sizey-1)
ycn=ycn-sizey+2;
if (xncn<=0)
xncn=sizex-2+xncn;
if (yncn<=0)
yncn=sizey-2+yncn;
if (xncn>=sizex-1)
xncn =xncn-sizex+2;
if (yncn>=sizey-1)
yncn=yncn-sizey+2;}

    int s_nb=sigma[xcn][ycn];
    int s_next_nb=sigma[xncn][yncn];

    if ((s_nb>0 || s_next_nb>0) && (s_nb==0 ||s_next_nb ==0)) {

      // check whether s_nb is adjacent to non-identical site,
      // count it
      n_borders++;
    }
    int j;
    bool on_stack_p=false;
    // cout << "i="<<i <<" s_nb="<< s_nb << " stack p" << stackp << " j initialized as " << j<< endl;
    // we need the next heuristic to prevent stalling at
    // cell-cell borders
    // do not enforce constraint at two cell interface(no medium)
    if (s_nb) {
      // cout << "j starts as " << j << endl;
      for (j=stackp;j>=0;j--) {
        // cout << "j=" <<j <<" stack[j]= " << stack[j] << endl;
      	if (s_nb==stack[j]) {
      	  on_stack_p=true;
      	  break;
	      }
      }
      if (!on_stack_p) {
  	     if (stackp>6) {
  	        cerr << "Stack overflow, stackp=" << stackp << "\n";
  	     }
  	     stack[++stackp]=s_nb;
      }
    }
    else {
      one_of_neighbors_medium=true;
    }
  }

  // number of different neighbours is stackp+1;
  if (n_borders>2 && ( (stackp+1)>2 || one_of_neighbors_medium) ) {
    return false;
  }
  else
    return true;

}







bool CellularPotts::NearbyAdhesionSite(int x, int y, int r, PDE *PDEfield) {
	// central site
	int sxy=sigma[x][y];
	bool nearbyadhesion=false;
	for (int i=0;i<=r;i++) {
	for (int j=0;j<=r-i;j++){
		for (int s1=0; s1<=1; s1++) {
		for (int s2=0; s2<=1; s2++) {
			int nx = i*pow(-1,s1)+x;
			int ny = j*pow(-1,s2)+y;
      if (nx>0 && nx<sizex && ny>0 && ny<sizey){
			int nsxy= sigma[nx][ny];
			//cout << i<< ", " << j << " ," << s1 << ", " << s2 << ", " << nsxy << ", " << GetMatrixLevel(nx,ny)<< endl;
			if (sxy==nsxy){
				if (GetMatrixLevel(nx,ny)>=2){
					nearbyadhesion=true;

					//goto stop;
}
}}}}}}
  //stop:
	return nearbyadhesion;
    }


double CellularPotts::CellDensity(void) const {

  // return the density of cells
  int sum=0;
  for (int i=0;i<sizex*sizey;i++) {
    if (sigma[0][i]) {
      sum++;
    }
  }
  return (double)sum/(double)(sizex*sizey);

}
//
// int CellularPotts::ComputeCellMatrixAdhesion( int sxy){//}, PDE *PDEfield) {
// 	int age_sum = 0;
// 	// for (int x=1;x<sizex-1;x++) {
// 	// for (int y=1;y<sizey-1;y++) {
// 	// 		if (Sigma(x,y) == sxy) {
// 	// 			age_sum=age_sum +PDEfield->Sigma(3,x,y);}}}
// 	// return(age_sum);
//
//   for (const auto elem: matrixPixels){
//     int x=elem.first[0];
//     int y =elem.first[1];
//     if(Sigma(x,y)==sxy){
//       age_sum+= elem.second;
//     }}
//   return(age_sum);
// }

int CellularPotts::ComputeCellMatrixAdhesion( int sxy){//}, PDE *PDEfield) {
	int age_sum = 0;
	for (int x=1;x<sizex-1;x++) {
	for (int y=1;y<sizey-1;y++) {
			if (Sigma(x,y) == sxy) {
				age_sum+=matrix[x][y];}}}
	return(age_sum);

  // for (const auto elem: matrixPixels){
  //   int x=elem.first[0];
  //   int y =elem.first[1];
  //   if(Sigma(x,y)==sxy){
  //     age_sum+= elem.second;
  //   }}
  // return(age_sum);
}

double CellularPotts::MeanCellArea(void) const {

  int sum_area=0, n=0;
  double sum_length=0.;
  vector<Cell>::iterator c=cell->begin(); ++c;

  for (;
	c!=cell->end();
	c++) {

    sum_area+=c->Area();
    sum_length+=c->Length();
    n++;
  }

  cerr << "Mean cell length is " << sum_length/((double)n) << endl;
  return (double)sum_area/(double)n;
}

void CellularPotts::ResetTargetLengths(void)  {
   vector<Cell>::iterator c=cell->begin(); ++c;

   for (;
        c!=cell->end();
        c++) {

     c->SetTargetLength(par.target_length);

}

}

void CellularPotts::SetTargetPerimeter(int tau, int value){

 vector<Cell>::iterator c=cell->begin(); ++c;

  for (;c!=cell->end();c++) {
	  if (c->getTau()==tau && c->AliveP())
			c->SetTargetPerimeter(value);

	}
}

// void CellularPotts::SetLambdaPerimeter(int tau, int value){
//
//  vector<Cell>::iterator c=cell->begin(); ++c;
//
//   for (;c!=cell->end();c++) {
// 		if (c->getTau()==tau)
// 			c->SetLambdaPerimeter(value);
//
// 	}
// }

void CellularPotts::SetRandomTypes(void) {

  // each cell gets a random type 1..maxtau

  vector<Cell>::iterator c=cell->begin(); ++c;

  for (;
       c!=cell->end();
       c++) {

    int celltype = RandomNumber(Cell::maxtau);
    c->setTau(celltype);

  }

}
int CellularPotts::PolarizedAdhesiveEnergy(int actlevelxy, int sxy, int actlevelxyp2, int sxyp2)
{
  if (sxy==sxyp2)
    return 0;
  if (sxy==0 or sxyp2==0)
    return 0;

  return -par.J_pol*actlevelxy*actlevelxyp2/pow(par.max_Act,2);

}


void CellularPotts::GrowAndDivideCells(int growth_rate) {

  vector<Cell>::iterator c=cell->begin(); ++c;
  vector<bool> which_cells(cell->size());

  for (;
       c!=cell->end();
       c++) {

    // only tumor cells grow and divide
    if (c->getTau()==2) {

      c->SetTargetArea(c->TargetArea()+growth_rate);

      if (c->Area()>par.target_area) {
	which_cells[c->Sigma()]=true;
      } else {
	which_cells[c->Sigma()]=false;
      }

      if (c->chem[1]<0.9) { //arbitrary oxygen threshold for the moment
	c->setTau(3);
      }
    } else {
      which_cells[c->Sigma()]=false;
    }

  }

  DivideCells(which_cells);

}

double CellularPotts::DrawConvexHull(Graphics *g, int color) {

  // Draw the convex hull of the cells
  // using Andrew's Monotone Chain Algorithm (see hull.cpp)

  // Step 1. Prepare data for 2D hull code

  // count number of points to determine size of array
  int np=0;
  for (int x=1;x<sizex-1;x++)
    for (int y=1;y<sizey-1;y++) {
      if (sigma[x][y]) {
	np++;
      }
    }

  Point *p=new Point[np];

  int pc=0;
  for (int x=1;x<sizex-1;x++)
    for (int y=1;y<sizey-1;y++) {
      if (sigma[x][y]) {
	p[pc++]=Point(x,y);
      }
    }

  // Step 2: call 2D Hull code
  Point *hull=new Point[np];
  int nph=chainHull_2D(p,np,hull);

  // Step 3: draw it
  for (int i=0;i<nph-1;i++) {
    g->Line(2*hull[i].x,2*hull[i].y,2*hull[i+1].x,2*hull[i+1].y, color);
  }


  // Step 4: calculate area of convex hull
  double hull_area=0.;
  for (int i=0;i<nph-1;i++) {
    hull_area+=hull[i].x*hull[i+1].y-hull[i+1].x*hull[i].y;
  }
  hull_area/=2.;

  //cerr << "Area = " << hull_area << "\n";

  delete[] p;
  delete[] hull;

  return hull_area;

}

double CellularPotts::Compactness(double *res_compactness, double *res_area, double *res_cell_area) {

  // Calculate compactness using the convex hull of the cells
  // We use Andrew's Monotone Chain Algorithm (see hull.cpp)

  // Step 1. Prepare data for 2D hull code

  // count number of points to determine size of array
  int np=0;
  for (int x=1;x<sizex-1;x++)
    for (int y=1;y<sizey-1;y++) {
      if (sigma[x][y]) {
	np++;
      }
    }

  Point *p=new Point[np];

  int pc=0;
  for (int x=1;x<sizex-1;x++)
    for (int y=1;y<sizey-1;y++) {
      if (sigma[x][y]) {
	p[pc++]=Point(x,y);
      }
    }

  // Step 2: call 2D Hull code
  Point *hull=new Point[np];
  int nph=chainHull_2D(p,np,hull);

  //// Step 3: draw it
  //for (int i=0;i<nph-1;i++) {
  //  g->Line(2*hull[i].x,2*hull[i].y,2*hull[i+1].x,2*hull[i+1].y, color);
  //}


  // Step 3: calculate area of convex hull
  double hull_area=0.;
  for (int i=0;i<nph-1;i++) {
    hull_area+=hull[i].x*hull[i+1].y-hull[i+1].x*hull[i].y;
  }
  hull_area/=2.;

  // Step 4: calculate total cell area
  double cell_area=0;

  vector<Cell>::const_iterator c;

  for ( (c=cell->begin(),c++);
       c!=cell->end();
       c++) {
    cell_area+=c->Area();
  }

  delete[] p;
  delete[] hull;


  // put intermediate results into optional pointers
  if (res_compactness) {
    *res_compactness = cell_area/hull_area;
  }
  if (res_area) {
    *res_area = hull_area;
  }
  if (res_cell_area) {
    *res_cell_area = cell_area;
  }

  // return compactness
  return cell_area/hull_area;

}

bool CellularPotts::AnyPillar(){
  for (int x= 0; x < sizex; ++x)
{
    for (int y = 0; y <sizey; ++y)
      if (sigma[x][y]<-1)
        return(true);
}
return(false);
}


bool CellularPotts::IsPillar(int x, int y){
  // if ((x<100 || x>200)  && (y<100 || y>200))
  //   return(true);
  // else
  //   return(false);

  if (par.pillar_radius<=0)
    return(false);
  //check if there is a gradient
  if (par.pillar_r>0){
    // if((double)x-sizex/2.0>(2.1*par.pillar_radius-par.pillar_distance)/(1-std::exp(-par.pillar_r))+par.pillar_distance/2.0-par.pillar_radius &&
    // (double)x-sizex/2.0<(par.pillar_distance-2.1*par.pillar_radius)/(1-std::exp(-par.pillar_r))+par.pillar_distance/2.0+par.pillar_radius){
    double d_min=2*par.pillar_radius+6;
    double d_max=2*par.pillar_distance-d_min;

    double n=std::log(((double)x-(double)sizex/2.0-par.pillar_distance/2)*(1-std::exp(-par.pillar_r))/par.pillar_distance+1)/par.pillar_r;
    double n_low=std::floor(n);
    double n_high=std::ceil(n);
    double m_l=((double)y-sizey/2.0)/(par.pillar_distance*std::exp(par.pillar_r*n_low))-1/2;
    double m_h=((double)y-sizey/2.0)/(par.pillar_distance*std::exp(par.pillar_r*n_high))-1/2;
    double n_min=(1/par.pillar_r)*std::log((2*par.pillar_radius+6)/par.pillar_distance);
    double n_max=(1/par.pillar_r)*std::log(2.0-(2*par.pillar_radius+6)/par.pillar_distance);
    double n_min_star=std::ceil(n_min);
    double n_max_star=std::floor(n_max);
    double x_n_min_star=par.pillar_distance*(std::exp(par.pillar_r*n_min_star)-1)/(1-std::exp(-par.pillar_r))+par.pillar_distance/2.0;
    double x_n_max_star=par.pillar_distance*(std::exp(par.pillar_r*n_max_star)-1)/(1-std::exp(-par.pillar_r))+par.pillar_distance/2.0;

        //The part with gradient first
    if((n_low>=n_min || (n_high==n_min_star && fabs((double)x-(double)sizex/2.0-x_n_min_star)<par.pillar_radius))  &&
(n_high<=n_max || (n_low==n_max_star && fabs((double)x-(double)sizex/2.0-x_n_max_star)<par.pillar_radius))) {
//n_low>=n_min && n_low<n_max &&
    if ( std::sqrt(std::pow((std::exp(par.pillar_r*n_low)-1)*par.pillar_distance/(1-std::exp(-1*par.pillar_r))+par.pillar_distance/2.0-(double)x+(double)sizex/2.0,2)
    +std::pow(par.pillar_distance*(std::floor(m_l)+1.0/2.0)*std::exp(n_low*par.pillar_r)-y+(double)sizey/2.0,2))<par.pillar_radius)
      return(true);
      //n_low>=n_min && n_low<n_max &&
    else if (std::sqrt(std::pow((std::exp(par.pillar_r*n_low)-1)*par.pillar_distance/(1-std::exp(-1*par.pillar_r))+par.pillar_distance/2.0-x+sizex/2.0,2)
    +std::pow(par.pillar_distance*(std::ceil(m_l)+1.0/2.0)*std::exp(n_low*par.pillar_r)-y+sizey/2.0,2))<par.pillar_radius)
      return(true);
      //n_high<n_max &&
    else if (std::sqrt(std::pow((std::exp(par.pillar_r*n_high)-1)*par.pillar_distance/(1-std::exp(-1*par.pillar_r))+par.pillar_distance/2.0-x+sizex/2.0,2)
    +std::pow(par.pillar_distance*(std::floor(m_h)+1.0/2.0)*std::exp(n_high*par.pillar_r)-y+sizey/2.0,2))<par.pillar_radius)
      return(true);
      //n_high<n_max &&
    else if (std::sqrt(std::pow((std::exp(par.pillar_r*n_high)-1)*par.pillar_distance/(1-std::exp(-1*par.pillar_r))+par.pillar_distance/2.0-x+sizex/2.0,2)
    +std::pow(par.pillar_distance*(std::ceil(m_h)+1.0/2.0)*std::exp(n_high*par.pillar_r)-y+sizey/2.0,2))<par.pillar_radius)
      return(true);
    // else
    //   return(false);
}
// //Transition region around n_min
// if(n_low<n_min && n_high>=n_min){}
//
// //Transition region around n_max
// if(n_low<=n_max && n_high>n_max){}

// now the leftover parts on the sides with regular grid
   else {
  //   if (n_low<=n_min ||
  // n_high>=n_max ){
  // //   if (n_low<=n_min || (n_low<n_min && n_high>=n_min) &&
  // // n_high>=n_max || (n_low<=n_max && n_high>n_max)){
      double pillar_distance=par.pillar_distance;
      double shift=0;
      if (n_low<n_min){
        pillar_distance=d_min;
        shift=x_n_min_star-d_min/2.0;
        //par.pillar_distance/2.0+(2.1*par.pillar_radius-par.pillar_distance)/(1-std::exp(-par.pillar_r));
      }
      if (n_high>n_max){
        pillar_distance=d_max;
        shift=x_n_max_star+d_max/2.0;
        //par.pillar_distance/2.0+par.pillar_distance/2.0+(par.pillar_distance-2.1*par.pillar_radius)/(1-std::exp(-par.pillar_r));
      }
      double new_n=((double)x-shift-sizex/2.0-pillar_distance/2.0)/(double)pillar_distance;
      double m=((double)y-sizey/2.0-pillar_distance/2.0)/(double)pillar_distance;
      double new_n_low=std::floor(new_n);
      double new_n_high=std::ceil(new_n);
      double m_low=std::floor(m);
      double m_high=std::ceil(m);
      // cout << "n "<< n<<" m " << m<< endl;
      // cout <<"x-wise " << abs(pillar_distance*(n_low+1.0/2.0)-x) << endl;
      // cout << "y-wise " <<  abs(pillar_distance*(m_low+1.0/2.0)-y) << endl;
      if (sqrt(pow(pillar_distance*(new_n_low+1.0/2.0)+sizex/2.0-x+shift,2)+pow(pillar_distance*(m_low+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius){
        // if (not(n_high>=n_max && n_low<n_max) && n<n_low+0.1){
          return(true);}
        // }
      else if ( sqrt(pow(pillar_distance*(new_n_low+1.0/2.0)+sizex/2.0-x+shift,2)+pow(pillar_distance*(m_high+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius){
            // if (not(n_high>=n_max && n_low<n_max)){
          return(true);}
        // }
      else if (sqrt(pow(pillar_distance*(new_n_high+1.0/2.0)+sizex/2.0-x+shift,2)+pow(pillar_distance*(m_low+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius){
                    // if (not(n_low<=n_min && n_high>n_min)){
          return(true);}
        // }
      else if (sqrt(pow(pillar_distance*(new_n_high+1.0/2.0)+sizex/2.0-x+shift,2)+pow(pillar_distance*(m_high+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius){
                            // if (not(n_low<=n_min && n_high>n_min)){
          return(true);}
        // }
      else
        return(false);
    }



      // return(false);

    // if (n_low>=n_min && abs(par.pillar_distance*(std::exp(par.pillar_r*n_low)-1/(1-std::exp(-1)) +par.pillar_distance/2-x))<par.pillar_radius){
    //   if (abs(par.pillar_distance*(std::floor(m_l)+1/2)*std::exp(par.pillar_r*n_low)-y)<par.pillar_radius) {
    //     return(true);
    //   }
    //   else if (abs(par.pillar_distance*(std::ceil(m_l)+1/2)*std::exp(par.pillar_r*n_low)-y)<par.pillar_radius){
    //     return(true);
    //   }
    // }
    // else if (n_high<n_max && abs(par.pillar_distance*(std::exp(par.pillar_r*n_high)-1/(1-std::exp(-1)) +par.pillar_distance/2-x))<par.pillar_radius){
    //   if (abs(par.pillar_distance*(std::floor(m_h)+1/2)*std::exp(par.pillar_r*n_high)-y)<par.pillar_radius) {
    //     return(true);
    //   }
    //   else if (abs(par.pillar_distance*(std::ceil(m_h)+1/2)*std::exp(par.pillar_r*n_high)-y)<par.pillar_radius){
    //     return(true);
    //   // }
    // }
    // }
    // else
    //   return(false);
}
  //Exception for r==0
  // if ((double)x-sizex/2.0<=d_min || (double)x-sizex/2.0>=d_max)
  // {}

  //if no gradient, draw regular grid
  else{
    double n=((double)x-sizex/2.0-par.pillar_distance/2.0)/(double)par.pillar_distance;
    double m=((double)y-sizey/2.0-par.pillar_distance/2.0)/(double)par.pillar_distance;
    double n_low=std::floor(n);
    double n_high=std::ceil(n);
    double m_low=std::floor(m);
    double m_high=std::ceil(m);
    // cout << "n "<< n<<" m " << m<< endl;
    // cout <<"x-wise " << abs(par.pillar_distance*(n_low+1.0/2.0)-x) << endl;
    // cout << "y-wise " <<  abs(par.pillar_distance*(m_low+1.0/2.0)-y) << endl;
    if (sqrt(pow(par.pillar_distance*(n_low+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_low+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
        return(true);
    else if (sqrt(pow(par.pillar_distance*(n_low+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_high+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
        return(true);
    else if (sqrt(pow(par.pillar_distance*(n_high+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_low+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
        return(true);
    else if (sqrt(pow(par.pillar_distance*(n_high+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_high+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
        return(true);
    else
      return(false);
  }
}


int CellularPotts::WhichPillar(int x, int y){
//returns which pillar for regular checkerboard patterned grid
  double n=((double)x-sizex/2.0-par.pillar_distance/2.0)/(double)par.pillar_distance;
  double m=((double)y-sizey/2.0-par.pillar_distance/2.0)/(double)par.pillar_distance;
  double n_low=std::floor(n);
  double n_high=std::ceil(n);
  double m_low=std::floor(m);
  double m_high=std::ceil(m);
  // cout << "n "<< n<<" m " << m<< endl;
  // cout <<"x-wise " << abs(par.pillar_distance*(n_low+1.0/2.0)-x) << endl;
  // cout << "y-wise " <<  abs(par.pillar_distance*(m_low+1.0/2.0)-y) << endl;
  if (sqrt(pow(par.pillar_distance*(n_low+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_low+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
      return((((int)n_low+(int)m_low))%2);
  else if (sqrt(pow(par.pillar_distance*(n_low+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_high+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
      return((((int)n_low+(int)m_high))%2);
  else if (sqrt(pow(par.pillar_distance*(n_high+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_low+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
      return(((int)n_high+(int)m_low)%2);
  else if (sqrt(pow(par.pillar_distance*(n_high+1.0/2.0)+sizex/2.0-x,2)+pow(par.pillar_distance*(m_high+1.0/2.0)+sizey/2.0-y,2))<par.pillar_radius)
      return((((int)n_high+(int)m_high))%2);
  else
    return(-2);
}
