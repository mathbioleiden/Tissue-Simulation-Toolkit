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
#include <math.h>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include "crash.hpp"
#include "parameter.hpp"
#include "ca.hpp"
#include "pde.hpp"
#include "conrec.hpp"

#define CL_HPP_TARGET_OPENCL_VERSION 220
#include <CL/opencl.hpp>

/* STATIC DATA MEMBER INITIALISATION */
const int PDE::nx[9] = {0, 1, 1, 1, 0,-1,-1,-1, 0 };
const int PDE::ny[9] = {0, 1, 0,-1,-1,-1, 0, 1, 1 };

extern Parameter par;

/** PRIVATE **/

PDE::PDE(const int l, const int sx, const int sy) {
  sigma=0;
  thetime=0;
  sizex=sx;
  sizey=sy;
  layers=l;
  
  sigma=AllocateSigma(l,sx,sy);
  alt_sigma=AllocateSigma(l,sx,sy);
}


PDE::PDE(void) {

  sigma=0;
  alt_sigma=0;
  sizex=0; sizey=0; layers=0;
  thetime=0;
  if (par.useopencl){this->SetupOpenCL();}
}

// destructor (virtual)
PDE::~PDE(void) {
  if (sigma) {
    free(sigma[0][0]);
    free(sigma[0]);
    free(sigma);
    sigma=0;
  }
  if (alt_sigma) {
    free(alt_sigma[0][0]);
    free(alt_sigma[0]);
    free(alt_sigma);
    alt_sigma=0;
  }
}

PDEFIELD_TYPE ***PDE::AllocateSigma(const int layers, const int sx, const int sy) {
  PDEFIELD_TYPE ***mem;
  sizex=sx; sizey=sy;
  mem=(PDEFIELD_TYPE ***)malloc(layers*sizeof(PDEFIELD_TYPE **));
  if (mem==NULL) {
    MemoryWarning();
  }
  mem[0]=(PDEFIELD_TYPE **)malloc(layers*sizex*sizeof(PDEFIELD_TYPE *));
  if (mem[0]==NULL) { 
    MemoryWarning();
  }
  for (int i=1;i<layers;i++) {
    mem[i]=mem[i-1]+sizex;
  }  
  mem[0][0]=(PDEFIELD_TYPE *)malloc(layers*sizex*sizey*sizeof(PDEFIELD_TYPE));
  if (mem[0][0]==NULL) {
    MemoryWarning();
  }
  for (int i=1;i<layers*sizex;i++) {
    mem[0][i]=mem[0][i-1]+sizey;
  }
  /* Clear PDE plane */
  for (int i=0;i<layers*sizex*sizey;i++) {
    mem[0][0][i]=0.; 
  }
  return mem;
}

void PDE::Plot(Graphics *g,const int l) {
  // l=layer: default layer is 0
  for (int x=0;x<sizex;x++) {
    for (int y=0;y<sizey;y++) {
      // Make the pixel four times as large
      // to fit with the CPM plane
      g->Point(MapColour(sigma[l][x][y]),2*x,2*y);
      g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y);
      g->Point(MapColour(sigma[l][x][y]),2*x,2*y+1);
      g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y+1);
    }
  }
}

// Plot the value of the PDE only in the medium of the CPM
void PDE::Plot(Graphics *g, CellularPotts *cpm, const int l) {
  // suspend=true suspends calling of DrawScene
  for (int x=0;x<sizex;x++) {
    for (int y=0;y<sizey;y++) { 
      if (cpm->Sigma(x,y)==0) {
	// Make the pixel four times as large
	// to fit with the CPM plane
	g->Point(MapColour(sigma[l][x][y]),2*x,2*y);
	g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y);
	g->Point(MapColour(sigma[l][x][y]),2*x,2*y+1);
	g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y+1);
      }
    }
  }
}

void PDE::ContourPlot(Graphics *g, int l, int colour) {
  // calls "conrec" routine by Paul Bourke, as downloaded from
  // http://astronomy.swin.edu.au/~pbourke/projection/conrec

  // number of contouring levels
  int nc = 10;

  // A one dimensional array z(0:nc-1) that saves as a list of the contour levels in increasing order.   
  double *z=(double *)malloc(nc*sizeof(double));
  double min=Min(l), max=Max(l);
  double step=(max-min)/nc;
  for (int i=0;i<nc;i++) {
    z[i]=(i+1)*step;
  }
  double *x=(double *)malloc(sizex*sizeof(double));
  for (int i=0;i<sizex;i++) {
    x[i]=i;
  }
  double *y=(double *)malloc(sizey*sizeof(double));
  for (int i=0;i<sizey;i++) {
    y[i]=i;
  }
  conrec(sigma[l],0,sizex-1,0,sizey-1,x,y,nc,z,g,colour);
  
  free(x);
  free(y);
  free(z);
}

/*
void PDE::PlotInCells (Graphics *g, CellularPotts *cpm, const int l) {
 for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++) {
      // Make the pixel four times as large
      // to fit with the CPM plane
      	if( cpm->Sigma(x,y)>0){

          if (par.lambda_Act>0){
               g->Point(MapColour3(cpm->actPixels[{x,y}],l),2*x,2*y);
               g->Point(MapColour3(cpm->actPixels[{x,y}],l),2*x+1,2*y);
               g->Point(MapColour3(cpm->actPixels[{x,y}],l),2*x,2*y+1);
               g->Point(MapColour3(cpm->actPixels[{x,y}],l),2*x+1,2*y+1);}
         else {
           		g->Point(255,2*x,2*y);
           		g->Point(255,2*x+1,2*y);
           		g->Point(255,2*x,2*y+1);
           		g->Point(255,2*x+1,2*y+1);}
        if (par.lambda_matrix>0){
            if (cpm->matrix[x][y]>0){
            		g->PointAlpha(100,2*x,2*y);
            		g->PointAlpha(100,2*x+1,2*y);
            		g->PointAlpha(100,2*x,2*y+1);
            		g->PointAlpha(100,2*x+1,2*y+1);}
              }}

    else {if (cpm->Sigma(x,y)==-2){
      g->Point(10,2*x,2*y);
      g->Point(10,2*x+1,2*y);
      g->Point(10,2*x,2*y+1);
      g->Point(10,2*x+1,2*y+1);
    }
    if (cpm->Sigma(x,y)==-3){
      g->Point(256,2*x,2*y);
      g->Point(256,2*x+1,2*y);
      g->Point(256,2*x,2*y+1);
      g->Point(256,2*x+1,2*y+1);
    }
  }
	}
}
*/

void PDE::SetupOpenCL(){
  openclsetup = true;
  //Basic OpenCL Setup
  std::vector<cl::Platform> all_platforms;
  cl::Platform::get(&all_platforms);
  if(all_platforms.size()==0){
    std::cout<<" No platforms found. Check OpenCL installation!\n";
    exit(1);
  }
  cl::Platform default_platform=all_platforms[0];
  std::cout << "Using platform: "<< default_platform.getInfo<CL_PLATFORM_NAME>()<<"\n";  

  std::vector<cl::Device> all_devices;
  default_platform.getDevices(CL_DEVICE_TYPE_ALL, &all_devices);
  if(all_devices.size()==0){
    std::cout<<" No devices found. Check OpenCL installation!\n";
    exit(1);
  }

  default_device=all_devices[0];
  std::cout<< "Using device: "<<default_device.getInfo<CL_DEVICE_NAME>()<<"\n";  
  context = cl::Context({default_device});
  cl::Program::Sources sources;

  //Use file pdeCLcore.cl as Kernel
  std::ifstream inFile;
  inFile.open("pdecore.cl"); 
  std::stringstream strStream;
  strStream << inFile.rdbuf(); 
  std::string kernel_code  = strStream.str();
  //std::cout << kernel_code << "\n";

  sources.push_back({kernel_code.c_str(),kernel_code.length()});
  program =  cl::Program(context,sources);
  if(program.build({default_device})!=CL_SUCCESS){
    std::cout<<" Error building: "<<program.getBuildInfo<CL_PROGRAM_BUILD_LOG>(default_device)<<"\n";
    exit(1);
  }
  
  //Secretion and diffusion variables
  PDEFIELD_TYPE dt = (PDEFIELD_TYPE) par.dt;
  PDEFIELD_TYPE dx2 = (PDEFIELD_TYPE) par.dx*par.dx;
  PDEFIELD_TYPE decay_rate = (PDEFIELD_TYPE) * par.decay_rate;
  PDEFIELD_TYPE secr_rate = (PDEFIELD_TYPE) * par.secr_rate;
  int btype; 
  
  if(par.periodic_boundaries){
    btype=2;
  }
  else{
    btype = 3;
  }

  //Allocate memory on the GPU
  queue = cl::CommandQueue(context,default_device);
  buffer_sigmacell = cl::Buffer(context, CL_MEM_READ_WRITE, sizeof(int)*sizex*sizey); 
  buffer_sigmapdeA = cl::Buffer(context, CL_MEM_READ_WRITE, sizeof(PDEFIELD_TYPE)*sizex*sizey*layers);
  buffer_sigmapdeB = cl::Buffer(context, CL_MEM_READ_WRITE, sizeof(PDEFIELD_TYPE)*sizex*sizey*layers); 
  buffer_diff_coeff = cl::Buffer(context, CL_MEM_READ_WRITE, sizeof(PDEFIELD_TYPE)*layers);


  //Making kernel and setting arguments
  kernel_SecreteAndDiffuse = cl::Kernel(program,"SecreteAndDiffuse");      

  kernel_SecreteAndDiffuse.setArg(0, buffer_sigmacell);
  kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeA);
  kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeB);
  kernel_SecreteAndDiffuse.setArg(3, sizeof(int), &sizex);
  kernel_SecreteAndDiffuse.setArg(4, sizeof(int), &sizey);
  kernel_SecreteAndDiffuse.setArg(5, sizeof(int), &layers);
  kernel_SecreteAndDiffuse.setArg(6, sizeof(PDEFIELD_TYPE), &decay_rate);
  kernel_SecreteAndDiffuse.setArg(7, sizeof(PDEFIELD_TYPE), &dt);
  kernel_SecreteAndDiffuse.setArg(8, sizeof(PDEFIELD_TYPE), &dx2);
  kernel_SecreteAndDiffuse.setArg(9, buffer_diff_coeff);
  kernel_SecreteAndDiffuse.setArg(10,sizeof(PDEFIELD_TYPE), &secr_rate);
  kernel_SecreteAndDiffuse.setArg(11, sizeof(int),  &btype);

  PDEFIELD_TYPE diff_coeff[layers];

  for (int index = 0; index < layers; index++){
    diff_coeff[index] = (PDEFIELD_TYPE) par.diff_coeff[index];
  }

  queue.enqueueWriteBuffer(buffer_diff_coeff,
    CL_TRUE, 0, sizeof(PDEFIELD_TYPE)*layers, diff_coeff);
}


void PDE::SecreteAndDiffuseCL(CellularPotts *cpm, int repeat){
    if (!openclsetup  ){this->SetupOpenCL();}
    //A B scheme used to keep arrays on GPU
    int AB = 1;
    int errorcode = 0;

    //Write the cellSigma array to GPU for secretion
    queue.enqueueWriteBuffer(buffer_sigmacell,
    CL_TRUE, 0, sizeof(int)*sizex*sizey, cpm->getSigma()[0]);

    //Writing pdefield sigma is only necessary if modified outside of kernel
    //queue.enqueueWriteBuffer(buffer_sigmapdeA,  CL_TRUE, 0, sizeof(PDEFIELD_TYPE)*sizex*sizey*layers, sigma[0][0]);


    //Main loop executing kernel and switching between A and B arrays
    for (int index = 0; index < repeat; index ++){
      if (AB == 1) AB = 0;
      else AB = 1;
      kernel_SecreteAndDiffuse.setArg(12, sizeof(int),  &AB);
      if(AB == 0){
        kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeA);
        kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeB);
      }
      else{
        kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeB);
        kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeA);
      }
      errorcode = queue.enqueueNDRangeKernel(kernel_SecreteAndDiffuse,
                  cl::NullRange, cl::NDRange(sizex*sizey*layers), cl::NullRange);
      errorcode = queue.finish();
      if (errorcode != 0){
        printf("Error during secretion and diffusion");
        exit(0);}
      }


    //Reading from correct array containing the output
    if (AB == 0)
    queue.enqueueReadBuffer(buffer_sigmapdeB,CL_TRUE,0,
                            sizeof(PDEFIELD_TYPE)*sizex*sizey*layers, sigma[0][0]);
    else
    queue.enqueueReadBuffer(buffer_sigmapdeA,CL_TRUE,0,
                            sizeof(PDEFIELD_TYPE)*sizex*sizey*layers, sigma[0][0]);

    if (errorcode != CL_SUCCESS){
      cout << "error:" << errorcode << endl;
    }
    thetime += par.dt;

}


// public
void PDE::Diffuse(int repeat) {
  
  // Just diffuse everywhere (cells are transparent), using finite difference
  // (We're ignoring the problem of how to cope with moving cell
  // boundaries right now)
  
  const PDEFIELD_TYPE dt=par.dt;
  const PDEFIELD_TYPE dx2=par.dx*par.dx;

  for (int r=0;r<repeat;r++) {
    //NoFluxBoundaries();
    if (par.periodic_boundaries) {
      PeriodicBoundaries();
    } else {
      AbsorbingBoundaries();
      //NoFluxBoundaries();
    }
    for (int l=0;l<layers;l++) {
      for (int x=1;x<sizex-1;x++)
	for (int y=1;y<sizey-1;y++) {
	  PDEFIELD_TYPE sum=0.;
	  sum+=sigma[l][x+1][y];
	  sum+=sigma[l][x-1][y];
	  sum+=sigma[l][x][y+1];
	  sum+=sigma[l][x][y-1];
	  sum-=4*sigma[l][x][y];
	  alt_sigma[l][x][y]=sigma[l][x][y]+sum*dt*par.diff_coeff[l]/dx2;
      }
    }
    PDEFIELD_TYPE ***tmp;
    tmp=sigma;
    sigma=alt_sigma;
    alt_sigma=tmp;
  
    thetime+=dt;
  }
}

double PDE::GetChemAmount(const int layer) {
  // Sum the total amount of chemical in the lattice
  // in layer l
  // (This is useful to check particle conservation)
  double sum=0.;
  if (layer==-1) { // default argument: sum all chemical species
    for (int l=0;l<layers;l++) {
      for (int x=1;x<sizex-1;x++) {
	for (int y=1;y<sizey-1;y++) {
	  sum+=sigma[l][x][y];
	}
      }
    }
  } else {
    for (int x=1;x<sizex-1;x++)
      for (int y=1;y<sizey-1;y++) {
	sum+=sigma[layer][x][y];
      }
  } 
  return sum;
}

// private
void PDE::NoFluxBoundaries(void) {
  // all gradients at the edges become zero, 
  // so nothing flows out
  // Note that four corners points are not defined (0.)
  // but they aren't used in the calculations
  for (int l=0;l<layers;l++) {
    for (int x=0;x<sizex;x++) {
      sigma[l][x][0]=sigma[l][x][1];
      sigma[l][x][sizey-1]=sigma[l][x][sizey-2];
    }
    for (int y=0;y<sizey;y++) {
      sigma[l][0][y]=sigma[l][1][y];
      sigma[l][sizex-1][y]=sigma[l][sizex-2][y];
    }
  }
}


// private
void PDE::AbsorbingBoundaries(void) {
  // all boundaries are sinks, 
  for (int l=0;l<layers;l++) {
    for (int x=0;x<sizex;x++) {
      sigma[l][x][0]=0.;
      sigma[l][x][sizey-1]=0.;
    }
    for (int y=0;y<sizey;y++) {
      sigma[l][0][y]=0.;
      sigma[l][sizex-1][y]=0.;
    }
  }
}

// private
void PDE::PeriodicBoundaries(void) {
  // periodic...
  for (int l=0;l<layers;l++) {
    for (int x=0;x<sizex;x++) {
      sigma[l][x][0]=sigma[l][x][sizey-2];
      sigma[l][x][sizey-1]=sigma[l][x][1];
    }
    for (int y=0;y<sizey;y++) {
      sigma[l][0][y]=sigma[l][sizex-2][y];
      sigma[l][sizex-1][y]=sigma[l][1][y];
    }
  }
}

void PDE::GradC(int layer, int first_grad_layer) {
  // calculate the first and second order gradients and put
  // them in the next chemical fields
  if (par.n_chem<5) {
    throw("PDE::GradC: Not enough chemical fields");
  }

  // GradX
  for (int y=0;y<sizey;y++) {
    for (int x=1;x<sizex-1;x++) {
      sigma[first_grad_layer][x][y]=(sigma[layer][x+1][y]-sigma[layer][x-1][y])/2.;
    } 
  }
  // GradY
  for (int x=0;x<sizex;x++) {
    for (int y=1;y<sizey-1;y++) {
      sigma[first_grad_layer+1][x][y]=(sigma[layer][x][y+1]-sigma[layer][x][y-1])/2.;
    } 
  }
  // GradXX
  for (int y=0;y<sizey;y++) {
    for (int x=1;x<sizex-1;x++) {
      sigma[first_grad_layer+2][x][y]=sigma[layer][x+1][y]-sigma[layer][x-1][y]-2*sigma[layer][x][y];
    } 
  }

  // GradYY
  for (int x=0;x<sizex;x++) {
    for (int y=1;y<sizey-1;y++) {
      sigma[first_grad_layer+3][x][y]=sigma[layer][x][y-1]-sigma[layer][x][y+1]-2*sigma[layer][x][y];
    } 
  }
}

void PDE::PlotVectorField(Graphics &g, int stride, int linelength, int first_grad_layer) {
  // Plot vector field assuming it's in layer 1 and 2
  for (int x=1;x<sizex-1;x+=stride) {
    for (int y=1;y<sizey-1;y+=stride) {
      
      // calculate line
      int x1,y1,x2,y2;
      
      x1=(int)(x-linelength*sigma[first_grad_layer][x][y]);
      y1=(int)(y-linelength*sigma[first_grad_layer+1][x][y]);
      x2=(int)(x+linelength*sigma[first_grad_layer][x][y]);
      y2=(int)(y+linelength*sigma[first_grad_layer+1][x][y]);
      if (x1<0) x1=0;
      if (x1>sizex-1) x1=sizex-1;
      if (y1<0) y1=0;
      if (y1>sizey-1) y1=sizey-1;
      if (x2<0) x2=0;
      if (x2>sizex-1) x2=sizex-1;
      if (y2<0) y2=0;
      if (y2>sizey-1) y2=sizey-1;

      // And draw it :-)
      // perhaps I can add arrowheads later to make it even nicer :-)
      g.Line(2*x1,2*y1,2*x2,2*y2,1);
    }
  }
}


void PDE::SetSpeciesName(int l, const char *name) {
    species_names[l]=string(name);
}


void PDE::InitLinearYGradient(int spec, double conc_top, double conc_bottom) {
    for (int y=0;y<sizey;y++) {
      double val=(double)conc_top+y*((double)(conc_bottom-conc_top)/(double)sizey);
    for (int x=0;x<sizex;x++) {
      sigma[spec][x][y]=val;
    }
    cerr << y << " " << val << endl;
  }
}