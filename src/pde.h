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

#ifndef _PDE_HH_
#define _PDE_HH_
#include <stdio.h>
#include <float.h>
#include "graph.h"

class CellularPotts;
class PDE {

  friend class Info;

 public:

  /*! \brief Constructor for PDE object containing arbitrary number of planes.
    
  \param layers: Number of PDE planes
  \param sizex: horizontal size of PDE planes
  \param sizey: vertical size of PDE planes

  */
  PDE(const int layers, const int sizex, 
      const int sizey);
      
    
  // destructor must also be virtual
  virtual ~PDE();

  /*! \brief Plots one layer of the PDE plane to a Graphics window.
    
  \param g: Graphics window.
  \param layer: The PDE plane to be plotted. Default layer 0.
  */
  void Plot(Graphics *g, const int layer=0);
  
  /*! \brief Plots one layer of the PDE to a Graphics window, but not over the cells.
    \param g: Graphics window.
    \param cpm: CellularPotts object containing the cells.
    \param layer: The PDE plane to be plotted. Default layer 0.
  */
  void Plot(Graphics *g, CellularPotts *cpm, const int layer=0);
  
  /*! \brief Plots the PDE field using contour lines.
    
  \param g: Graphics window.
  \param layer: The PDE plane to be plotted. Default layer 0.
  \param colour: Color to use for the contour lines, as defined in the "default.ctb" color map file, which should be in the same directory as the executable. Default color 1 (black in the default color map).
  */
  void ContourPlot(Graphics *g, int layer=0, int colour=1);
    
  //! \brief Returns the horizontal size of the PDE planes.
  inline int SizeX() const {
    return sizex;
  }
  
  //! \brief Returns the vertical size of the PDE planes.
  inline int SizeY() const {
    return sizey;
  }
  
  //! \brief Returns the number of PDE layers in the PDE object
  inline int Layers() const {
    return layers;
  }

  /*! \brief Returns the value of grid point x,y of PDE plane "layer".
    
  Warning, no range checking done.
  
  \param layer: the PDE plane to probe.
  \param x, y: grid point to probe.
  */
  inline double Sigma(const int layer, const int x, const int y) const {
    return sigma[layer][x][y];
  }
  
  /*! \brief Sets grid point x,y of PDE plane "layer" to value "value".

  \param layer: PDE plane.
  \param x, y: grid point
  \param value: new contents
  
  */
  inline void setValue(const int layer, const int x, const int y, const double value) {
    sigma[layer][x][y]=value;
  }
  
  /*! \brief Adds a number to a PDE grid point.
    
  \param layer: PDE plane.
  \param x, y: grid point
  \param value: value to add
  */
  inline void addtoValue(const int layer, const int x, const int y, const double value) {
    sigma[layer][x][y]+=value;
  }

  /*! \brief Gets the maximum value of PDE layer l.
    
  \param l: layer
  \return Maximum value in layer l.
  */
  inline double Max(int l) {
    double max=sigma[l][0][0];
    int loop=sizex*sizey;
    for (int i=1;i<loop;i++)
      if (sigma[l][0][i]>max) {
	max=sigma[l][0][i];
      }
    return max;
  }
  /*! \brief Returns the minimum value of PDE layer l.
    
  \param l: layer
  \return Minimum value in layer l.
  */
  inline double Min(int l) {
    double min=sigma[l][0][0];
    int loop=sizex*sizey;
    for (int i=1;i<loop;i++)
      if (sigma[l][0][i]<min) {
	min=sigma[l][0][i];
      }
    return min;
  }
  
  /*! \brief Carry out $n$ diffusion steps for all PDE planes.
    
  We use a forward Euler method here. Can be replaced for better algorithm.
  
  \param repeat: Number of steps.

  Time step dt, space step dx, diffusion coefficient diff_coeff and
  boundary conditions (bool periodic_boundary) are set as global
  parameters in a parameter file using class Parameter.

  */
  void Diffuse(int repeat);

  /*! \brief Implementation of no-flux boundaries.
    
  Called internally (optionally) by Diffuse(). */
  void NoFluxBoundaries(void);
  
  /*! \brief Implementation of absorbing boundaries.
    
  Called internally (optionally) by Diffuse(). */
  void AbsorbingBoundaries(void);

  /*! \brief Implementation of periodic boundaries.
    
  Called internally (optionally) by Diffuse(). */
  void PeriodicBoundaries(void);

  /*! \brief Reaction and interaction of CPM plane with PDE planes.
    
  \param cpm: CellularPotts plane the PDE plane interacts with
  
  You should implement this member function as part of your main
  simulation code. See for an example vessel.cpp.

  */
  void Secrete(CellularPotts *cpm);

  /*! \brief Returns cumulative "simulated" time,
    i.e. number of time steps * dt. */
  inline double TheTime(void) const {
    return thetime;
  }
  
  /*! \brief Returns summed amount of chemical in PDE plane "layer".

  \param layer: The PDE plane of which to sum the chemicals. layer=-1 (default) returns the summed amount of chemical in all planes.

  */
  double GetChemAmount(const int layer=-1);

  /*!   Calculates the first and second order gradients, i.e. gradx,
    grady, gradxx, gradxy and gradyy and puts them in the next
    three chemical fields. Not currently used and might need some
    redoing. Make sure you have allocated sufficient fields (this
    method generates five planes).

    \param layer: PDE plane of which to calculate the gradients
    (default 0) \param first_grad_layer: first plane of five in which
    to write the results (default 1).
  */
  void GradC(int layer=0, int first_grad_layer=1); 

  /*!   Plots a field of the first order gradients, i.e. gradx and
    grady; assumes you have called GradC before.
    Not currently used and might need some
    redoing. 

    \param g: Graphics window
    \param stride: Number of grid points between vectors (drawn as lines, currently.
    \param linelength: Length of vector lines, in pixels.
    \param first_grad_layer: first plane of two which contain the
    calculated gradients (default 1).
       
       
  */
  void PlotVectorField(Graphics &g, int stride, int linelength, int first_grad_layer=1);

 protected:

  double ***sigma;
  
  // Used as temporary memory in the diffusion step
  // (addresses will be swapped for every time step, so
  // never directly use them!!! Access is guaranteed to be correct
  // through user interface)

  double ***alt_sigma;
 
  int sizex;
  int sizey;
  int layers;
 
 
  // Protected member functions

  /*! \brief Used in Plot. Takes a color and turns it into a grey value.
    
  \param val: Value from PDE plane.
  
  Implement this function in you main simulation code. See e.g. vessel.cpp.
  */
  virtual int MapColour(double val);

  //! empty constructor (necessary for derivation)
  PDE(void);
  
  /*! \brief Allocates a PDE plane (internal use). 

  For internal use, can be reimplemented in derived class to change
  method of memory allocation.
  */   
  virtual double ***AllocateSigma(const int layers, const int sx, const int sy);
 
 private:
  static const int nx[9], ny[9];
  double thetime;

};


#endif
