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


#include <fstream>
#include <iostream>
#include <sstream> 
#include <stdio.h>
#include <math.h>
#include <cstdlib>
#include "crash.h"
#include "parameter.h"
#include "ca.h"
#include "pde.h"
#include "conrec.h"

#include <MultiCellDS.hpp>
#include <MultiCellDS-pimpl.hpp>
#include <MultiCellDS-simpl.hpp>

#include <CL/cl.hpp>


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

double ***PDE::AllocateSigma(const int layers, const int sx, const int sy) {
  
  double ***mem;
  sizex=sx; sizey=sy;
  
  mem=(double ***)malloc(layers*sizeof(double **));
  
  if (mem==NULL)
    MemoryWarning();
  
  mem[0]=(double **)malloc(layers*sizex*sizeof(double *));
  if (mem[0]==NULL)  
      MemoryWarning();
  
  {  for (int i=1;i<layers;i++) 
    mem[i]=mem[i-1]+sizex;}
  
  mem[0][0]=(double *)malloc(layers*sizex*sizey*sizeof(double));
  if (mem[0][0]==NULL)  
    MemoryWarning();

  {for (int i=1;i<layers*sizex;i++) 
    mem[0][i]=mem[0][i-1]+sizey;}

  
  /* Clear PDE plane */
  { for (int i=0;i<layers*sizex*sizey;i++) 
    mem[0][0][i]=0.; }

   return mem;
}

void PDE::Plot(Graphics *g,const int l) {
  // l=layer: default layer is 0
  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++) {
      // Make the pixel four times as large
      // to fit with the CPM plane
      g->Point(MapColour(sigma[l][x][y]),2*x,2*y);
      g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y);
      g->Point(MapColour(sigma[l][x][y]),2*x,2*y+1);
      g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y+1);
    } 
  
}

// Plot the value of the PDE only in the medium of the CPM
void PDE::Plot(Graphics *g, CellularPotts *cpm, const int l) {
  
  // suspend=true suspends calling of DrawScene
  for (int x=0;x<sizex;x++)
    for (int y=0;y<sizey;y++) 
      if (cpm->Sigma(x,y)==0) {
	// Make the pixel four times as large
	// to fit with the CPM plane
	g->Point(MapColour(sigma[l][x][y]),2*x,2*y);
	g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y);
	g->Point(MapColour(sigma[l][x][y]),2*x,2*y+1);
	g->Point(MapColour(sigma[l][x][y]),2*x+1,2*y+1);
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
  {for (int i=0;i<nc;i++)
    z[i]=(i+1)*step;}
  
  double *x=(double *)malloc(sizex*sizeof(double));
  {for (int i=0;i<sizex;i++)
    x[i]=i;}
  
  double *y=(double *)malloc(sizey*sizeof(double));
  {for (int i=0;i<sizey;i++)
    y[i]=i;}
  
  conrec(sigma[l],0,sizex-1,0,sizey-1,x,y,nc,z,g,colour);
  
  free(x);
  free(y);
  free(z);
  
  
 
}



void PDE::SecreteAndDiffuse(CellularPotts *cpm, int repeat){
  //Secrete
  for (int re = 0; re < repeat; re++){
  const double dt=par.dt;
  const double dx2=par.dx*par.dx;
  
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
  //Diffuse
  if (par.gradient) {
          NoFluxBoundaries();
          for (int i=0;i<sizex;i++) {
              sigma[0][i][0]=0.;
              sigma[0][i][sizey-1]=1.;
          }
      } else {

    if (par.periodic_boundaries) {
      PeriodicBoundaries();
    } else {
      AbsorbingBoundaries();
      //NoFluxBoundaries();
    }
      }
    for (int l=0;l<layers;l++) {
      for (int x=1;x<sizex-1;x++)
        for (int y=1;y<sizey-1;y++) {

          double sum=0.;
          sum+=sigma[l][x+1][y];
          sum+=sigma[l][x-1][y];
          sum+=sigma[l][x][y+1];
          sum+=sigma[l][x][y-1];

          sum-=4*sigma[l][x][y];
          alt_sigma[l][x][y]=sigma[l][x][y]+sum*dt*par.diff_coeff[l]/dx2;

        }
    }
    double ***tmp;
    tmp=sigma;
    sigma=alt_sigma;
    alt_sigma=tmp;

    thetime+=dt;
    }  
}


void PDE::SetupOpenCL(){
  openclsetup = true;
//get all platforms (drivers)
  std::vector<cl::Platform> all_platforms;
  cl::Platform::get(&all_platforms);
  if(all_platforms.size()==0){
      std::cout<<" No platforms found. Check OpenCL installation!\n";
      exit(1);
  }
  cl::Platform default_platform=all_platforms[0];
  std::cout << "Using platform: "<< default_platform.getInfo<CL_PLATFORM_NAME>()<<"\n";  

  //get default device of the default platform
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
 


  std::ifstream inFile;
  inFile.open("pdeCLcore.c"); //open the input file

  std::stringstream strStream;
  strStream << inFile.rdbuf(); //read the file
  std::string kernel_code  = strStream.str(); //str holds the content of the file
  std::cout << kernel_code << "\n";

  sources.push_back({kernel_code.c_str(),kernel_code.length()});
  program =  cl::Program(context,sources);
  if(program.build({default_device})!=CL_SUCCESS){
        std::cout<<" Error building: "<<program.getBuildInfo<CL_PROGRAM_BUILD_LOG>(default_device)<<"\n";
        exit(1);
    }
}


void PDE::SecreteAndDiffuseCL(CellularPotts *cpm, int repeat){
   if (!openclsetup  ){this->SetupOpenCL();}
   const double dt=par.dt;
   const double dx2=par.dx*par.dx;
   int step = 0;
   int AB = 1;   
  //for (int index = 0; index < repeat; index ++){
    int errorcode = 0;
    cl::CommandQueue queue = cl::CommandQueue(context,default_device);
    cl::Buffer buffer_sigmacell   (context, CL_MEM_READ_WRITE, sizeof(int)*sizex*sizey); 
    cl::Buffer buffer_sigmapdeA  (context, CL_MEM_READ_WRITE, sizeof(double)*sizex*sizey*layers);
    cl::Buffer buffer_sigmapdeB (context, CL_MEM_READ_WRITE, sizeof(double)*sizex*sizey*layers);
    int test[] = {1,2,3};
   /* 
    for (int x=0;x<sizex;x++){
      for (int y = 0; y<sizey; y++){
      sigma[0][x][y] = (double) y;
      cout << sigma[0][x][y] << " ";
      }
     }*/
    queue.enqueueWriteBuffer(buffer_sigmacell,   CL_TRUE, 0, sizeof(int)*sizex*sizey, cpm->getSigma()[0]);
    queue.enqueueWriteBuffer(buffer_sigmapdeA,  CL_TRUE, 0, sizeof(double)*sizex*sizey*layers, sigma[0][0]);

    cl::Kernel kernel_SecreteAndDiffuse(program,"SecreteAndDiffuse");    
    
     
    kernel_SecreteAndDiffuse.setArg(0, buffer_sigmacell);
   // kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeA);
   // kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeB);
    kernel_SecreteAndDiffuse.setArg(3, sizeof(int), &sizex);
    kernel_SecreteAndDiffuse.setArg(4, sizeof(int), &sizey);
    kernel_SecreteAndDiffuse.setArg(5, sizeof(int), &layers);
    kernel_SecreteAndDiffuse.setArg(6, sizeof(double), par.decay_rate);
    kernel_SecreteAndDiffuse.setArg(7, sizeof(double), &dt);
    kernel_SecreteAndDiffuse.setArg(8, sizeof(double), &dx2);
    kernel_SecreteAndDiffuse.setArg(9, sizeof(double), par.diff_coeff);
    kernel_SecreteAndDiffuse.setArg(10,sizeof(double), par.secr_rate);

    
  // Step 1 Secrete
    errorcode = kernel_SecreteAndDiffuse.setArg(11, sizeof(int),  &step);
    for (int index = 0; index < repeat; index ++){
    if (AB == 1) AB = 0;
    else AB = 1; 
    //kernel_SecreteAndDiffuse.setArg(12, sizeof(int),  &AB);
    if(AB == 0){ 
    kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeA);
    kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeB); 
    }
    else{
    kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeB);
    kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeA);
    }
    errorcode = queue.enqueueNDRangeKernel(kernel_SecreteAndDiffuse, cl::NullRange, cl::NDRange(sizex*sizey*layers), cl::NullRange);   
    errorcode = queue.finish();
    if (errorcode != 0){printf("OH SHIT ERROR IN SECRETE SHIT FUCK OMG"); exit(0);}

    }

    //Step 2 diffuse
    step = 1;
    kernel_SecreteAndDiffuse.setArg(11, sizeof(int),  &step);

    if (AB == 1) AB = 0;
    else AB = 1;

    for (int index = 0; index < repeat; index ++){
    if (AB == 1) AB = 0;
    else AB = 1;
    if(AB == 0){
    kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeA);
    kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeB);
    }
    else{
    kernel_SecreteAndDiffuse.setArg(1, buffer_sigmapdeB);
    kernel_SecreteAndDiffuse.setArg(2, buffer_sigmapdeA);
    }
    errorcode = queue.enqueueNDRangeKernel(kernel_SecreteAndDiffuse, cl::NullRange, cl::NDRange(sizex*sizey*layers), cl::NullRange);
    errorcode = queue.finish();
    if (errorcode != 0){printf("OH SHIT ERROR IN DIFFUSE SHIT FUCK OMG");}
    }
    
    if (AB == 0) queue.enqueueReadBuffer(buffer_sigmapdeB,CL_TRUE,0,sizeof(double)*sizex*sizey*layers, sigma[0][0]);
    else queue.enqueueReadBuffer(buffer_sigmapdeA,CL_TRUE,0,sizeof(double)*sizex*sizey*layers, sigma[0][0]);
   
    if (errorcode != CL_SUCCESS){
      cout << "error:" << errorcode << endl;
    }
    
    thetime += dt;
    /*for (int x=0;x<sizex;x++){
      for (int y = 0; y<sizey; y++){
      cout << sigma[0][x][y] << " ";
      }
    cout << "\n";
  /
    }
   }*/

}



// public
void PDE::Diffuse(int repeat) {
  
  // Just diffuse everywhere (cells are transparent), using finite difference
  // (We're ignoring the problem of how to cope with moving cell
  // boundaries right now)
  
  const double dt=par.dt;
  const double dx2=par.dx*par.dx;

  for (int r=0;r<repeat;r++) {
    
      
    //NoFluxBoundaries();
      if (par.gradient) {
          NoFluxBoundaries();
          for (int i=0;i<sizex;i++) {
              sigma[0][i][0]=0.;
              sigma[0][i][sizey-1]=1.;
          }
      } else {
      
    if (par.periodic_boundaries) {
      PeriodicBoundaries();
    } else {
      AbsorbingBoundaries();
      //NoFluxBoundaries();
    }
      }
    for (int l=0;l<layers;l++) {
      for (int x=1;x<sizex-1;x++)
	for (int y=1;y<sizey-1;y++) {
	  
	  double sum=0.;
	  sum+=sigma[l][x+1][y];
	  sum+=sigma[l][x-1][y];
	  sum+=sigma[l][x][y+1];
	  sum+=sigma[l][x][y-1];
      
	  sum-=4*sigma[l][x][y];
	  alt_sigma[l][x][y]=sigma[l][x][y]+sum*dt*par.diff_coeff[l]/dx2;

	}
    }
    double ***tmp;
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
      for (int x=1;x<sizex-1;x++)
	for (int y=1;y<sizey-1;y++) {
	  
	  sum+=sigma[l][x][y];
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


mesh::mesh *PDE::CreateMultiCellDSMesh(void) {
    
    mesh::mesh *mesh = new mesh::mesh;
    
    common::units_double_list *xcoo = new common::units_double_list;
    common::units_double_list *ycoo = new common::units_double_list;
    common::units_double_list *zcoo = new common::units_double_list;
    xcoo->units("micron");
    ycoo->units("micron");
    zcoo->units("micron");
    
    
    for (int x=0;x<SizeX();x++) {
        xcoo->push_back(round((double)x*par.dx*1e+6));
    }
    
    for (int y=0;y<SizeY();y++) {
        ycoo->push_back(round((double)y*par.dx*1e+6));
    }
    
    zcoo->push_back(round((double)0*par.dx*1e+6));
    
    mesh->x_coordinates(xcoo);
    mesh->y_coordinates(ycoo);
    mesh->z_coordinates(zcoo);
    
    return mesh;
}


void PDE::AddToMultiCellDS(MultiCellDS *mcds) {
    
    microenvironment::microenvironment *me=new microenvironment::microenvironment;
    mesh::mesh *mesh = CreateMultiCellDSMesh();
   
    microenvironment::domain *dom = new microenvironment::domain;
    dom->mesh(mesh);
    
    variables::data *data = new variables::data;
    variables::list_of_variables *lov = new variables::list_of_variables;

    for (int j=0;j<layers;j++) {
        // Add data to domain
        variables::data_vector *dv = new variables::data_vector;
        for (int i=0;i<sizex*sizey;i++) {
            dv->push_back(sigma[0][0][i]);
        }
        data->type(common::data_storage_formats::xml);
        data->data_vector().push_back(dv);
        
        variables::variable *var = new variables::variable;
        var->name("VEGF");
        
        lov->variable().push_back(var);
    }
    dom->data(data);
    
    
 
    // should become part of field definition on user's end:
   
    dom->variables(lov);
    me->domain().push_back(dom);
    mcds->microenvironment(me);

}

int PDE::ReadFromMultiCellDS(MultiCellDS *mcds) {
    
    
    if (mcds) {
        
        // get grid size & check
        
        int read_lay=0;
        // loop over all domains
        for (microenvironment::microenvironment::domain_iterator d = mcds->microenvironment().domain().begin();
             d != mcds->microenvironment().domain().end();
             d++) {
            
            int sx=d->mesh().x_coordinates().size();
            int sy=d->mesh().y_coordinates().size();
            int sz=d->mesh().z_coordinates().size();
            
            if (sx!=sizex || sy!=sizey) {
                cerr << "PDE::ReadFromMultiCellDS: Mesh size of field (" << sx << " x " << sy << ") does not match mesh size of CPM model (" << sizex << " x " << sizey << ")" << endl;
                exit(1);
            } /*else {
                 cerr << "PDE::ReadFromMultiCellDS - Success: Mesh size of field (" << sx << " x " << sy << ") matches mesh size of CPM model (" << sizex << " x " << sizey << ")" << endl;
            }*/
            // OKAY - ready to read
            int pos=0;
            if (read_lay>=layers) {
                cerr << "PDE::ReadFromMultiCellDS error: insufficient PDE layers declared for MultiCellDS File" << endl;
                exit(1);
            }
            for (variables::data::data_vector_iterator dv=d->data().data_vector().begin();
                 dv !=d->data().data_vector().end();
                 dv++) {
                
                for (variables::data_vector::const_iterator i=dv->begin();
                    i !=dv->end();
                    i++) {
                    sigma[read_lay][0][pos++]=*i;
                }
                read_lay++;
            }
            
        }
    } else {
        return 1; // error: no MCDS
    }
    
        /*microenvironment::microenvironment *me=new microenvironment::microenvironment;
         mesh::mesh *mesh = CreateMultiCellDSMesh();
         
         microenvironment::domain *dom = new microenvironment::domain;
         dom->mesh(mesh);
         
         variables::data *data = new variables::data;
         for (int j=0;j<layers;j++) {
         // Add data to domain
         variables::data_vector *dv = new variables::data_vector;
         for (int i=0;i<sizex*sizey;i++) {
         dv->push_back(sigma[0][0][i]);
         }
         data->type(common::data_storage_formats::xml);
         data->data_vector().push_back(dv);
         }
         dom->data(data);
         
         variables::list_of_variables *lov = new variables::list_of_variables;
         variables::variable *var = new variables::variable;
         
         // should become part of field definition on user's end:
         var->name("VEGF");
         
         lov->variable().push_back(var);
         dom->variables(lov);
         me->domain().push_back(dom);
         mcds->microenvironment(me);*/
        
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

