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
#include <float.h>
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>


#include "cl_manager.hpp"
#include "graph.hpp"
#include "pdetype.h"

class CellularPotts;
class Dish;
class PDE {

  friend class Info;

public:
  /** \brief Constructor for PDE object containing arbitrary number of planes.
  * \param layers: Number of PDE planes
  * \param sizex: horizontal size of PDE planes
  * \param sizey: vertical size of PDE planes
  */
  PDE(const int layers, const int sizex, const int sizey);

  // destructor must also be virtual
  virtual ~PDE();

  /** \brief Plots one layer of the PDE plane to a Graphics window.
  * \param g: Graphics window.
  * \param layer: The PDE plane to be plotted. Default layer 0.
  */
  void Plot(Graphics *g, const int layer = 0);
  /** \brief Plots one layer of the PDE to a Graphics window, but not over the
    cells. 
    * \param g: Graphics window. 
    * \param cpm: CellularPotts object
    containing the cells. 
    * \param layer: The PDE plane to be plotted. Default
    layer 0.
  */
  void Plot(Graphics *g, CellularPotts *cpm, const int layer = 0);

  /** \brief Plots the PDE field using contour lines.

  * \param g: Graphics window.
  * \param layer: The PDE plane to be plotted. Default layer 0.
  * \param colour: Color to use for the contour lines, as defined in the
  "default.ctb" color map file, which should be in the same directory as the
  executable. Default color 1 (black in the default color map).
  */
  void ContourPlot(Graphics *g, int layer = 0, int colour = 1);

  //! \brief Returns the horizontal size of the PDE planes.
  inline int SizeX() const { return sizex; }

  //! \brief Returns the vertical size of the PDE planes.
  inline int SizeY() const { return sizey; }

  //! \brief Returns the number of PDE layers in the PDE object
  inline int Layers() const { return layers; }

  /*! \brief Set the of name of a layer 
  * \param name Name of the species
  * \param l Layer of the species
  */
  void SetSpeciesName(int l, const char *name);

  /** \brief Returns the value of grid point x,y of PDE plane "layer".

  Warning, no range checking done.

  * \param layer: the PDE plane to probe.
  * \param x, y: grid point to probe.
  */
  inline PDEFIELD_TYPE get_PDEvars(const int layer, const int x,
                                   const int y) const {
    return PDEvars[layer][x][y];
  }

  /** \brief Sets grid point x,y of PDE plane "layer" to value "value".
  * \param layer: PDE plane.
  * \param x, y: grid point
  * \param value: new contents
  */
  inline void setValue(const int layer, const int x, const int y,
                       const PDEFIELD_TYPE value) {
    PDEvars[layer][x][y] = value;
  }

  /** \brief Adds a number to a PDE grid point.
  * \param layer: PDE plane.
  * \param x, y: grid point
  * \param value: value to add
  */
  inline void addtoValue(const int layer, const int x, const int y,
                         const PDEFIELD_TYPE value) {
    PDEvars[layer][x][y] += value;
  }

  /** \brief Gets the maximum value of PDE layer l.
  * \param l: layer
  * \return Maximum value in layer l.
  */
  inline PDEFIELD_TYPE Max(int l) {
    PDEFIELD_TYPE max = PDEvars[l][0][0];
    int loop = sizex * sizey;
    for (int i = 1; i < loop; i++)
      if (PDEvars[l][0][i] > max) {
        max = PDEvars[l][0][i];
      }
    return max;
  }
  /** \brief Returns the minimum value of PDE layer l.
  * \param l: layer
  * \return Minimum value in layer l.
  */
  inline PDEFIELD_TYPE Min(int l) {
    PDEFIELD_TYPE min = PDEvars[l][0][0];
    int loop = sizex * sizey;
    for (int i = 1; i < loop; i++)
      if (PDEvars[l][0][i] < min) {
        min = PDEvars[l][0][i];
      }
    return min;
  }

  /** \brief Carry out $n$ diffusion steps for all PDE planes.
  We use a forward Euler method here. Can be replaced for better algorithm.
  Function for the Act model. The whole field is initialised, usually with 0
  */
  void InitialiseAgeLayer(int l, double value, CellularPotts *cpm);

  /* Function for the Act model. All the lattice sites within cells are "aged"
   *  by decreasing their values, usually with 1.
   */
  void AgeLayer(int l, double value, CellularPotts *cpm, Dish *dish);

  /* Function for the Act model. Plots the values of the activity into the
   * cells.
   */
  void PlotInCells(Graphics *g, CellularPotts *cpm, const int l = 0);
  // lymphocyte matrix interaction function

  void MILayerCA(int l, double value, CellularPotts *cpm, Dish *dish);

  /** \brief Implementation of no-flux boundaries.

  Called internally (optionally) by Diffuse(). */
  void NoFluxBoundaries(void);

  /** \brief Implementation of absorbing boundaries.

  Called internally (optionally) by Diffuse(). */
  void AbsorbingBoundaries(void);

  /** \brief Implementation of periodic boundaries.
  Called internally (optionally) by Diffuse(). */
  void PeriodicBoundaries(void);

  /** \brief Intialisation of diffusion coefficients
  \param cpm: CellularPotts plane the PDE plane interacts with
  The initial diffusion coefficients may be space dependent on
  the cpm configuration
  */
  void InitialiseDiffusionCoefficients(CellularPotts *cpm);

  /** \brief Intialisation of PDE variables
  \param cpm: CellularPotts plane the PDE plane interacts with
  Initial conditions conditions for the PDE should be given here.
  */
  void InitialisePDE(CellularPotts *cpm);

  /** \brief Derivatives of PDE variables.
  \param cpm: CellularPotts plane the PDE plane interacts with
  You should implement this member function as part of your main
  simulation code. See for an example vessel.cpp.
  * \return Derivatives at pixel (x,y)
  */
  void DerivativesPDE(CellularPotts *cpm, PDEFIELD_TYPE *derivs, int x, int y);

  /** \brief Do a single forward Euler step to solve the ODE
  * \param repeat: Number of steps.
  We solve with a simple forward Euler solver. Ths can be replaced with
  alternative ODE solvers.
  */
  void ForwardEulerStep(int repeat, CellularPotts *cpm);

  /** \brief Carry out $n$ diffusion steps for all PDE planes.

  We use a forward Euler method here. Can be replaced for better algorithm.

  * * \param repeat: Number of steps.

  Time step dt, space step dx, diffusion coefficient diff_coeff and
  boundary conditions (bool periodic_boundary) are set as global
  parameters in a parameter file using class Parameter.

  */
  void Diffuse(int repeat);

  /** \brief Do a single reaction diffusion step based on the
  given PDE derivatives
  */
  void ReactionDiffusion(CellularPotts *cpm);

  /** \brief Reaction and interaction of CPM plane with PDE planes.
   * \param cpm: CellularPotts plane the PDE plane interacts with
   You should implement this member function as part of your main
   simulation code. See for an example vessel.cpp. This method
   is slightly faster than the general PDE solver.
   */
  void Secrete(CellularPotts *cpm);

  // Secrete and diffuse functions accelerated using OpenCL
  void SecreteAndDiffuseCL(CellularPotts *cpm, int repeat);

  /** \brief Returns cumulative "simulated" time,
    i.e. number of time steps * dt. */
  inline double TheTime(void) const { return thetime; }

  /** \brief Returns summed amount of chemical in PDE plane "layer".
  * \param layer: The PDE plane of which to sum the chemicals. layer=-1 (default)
  returns the summed amount of chemical in all planes.
  */
  double GetChemAmount(const int layer = -1);

  /**   Calculates the first and second order gradients, i.e. gradx,
    grady, gradxx, gradxy and gradyy and puts them in the next
    three chemical fields. Not currently used and might need some
    redoing. Make sure you have allocated sufficient fields (this
    method generates five planes).

    * \param layer: PDE plane of which to calculate the gradients
    (default 0) 
    * \param first_grad_layer: first plane of five in which
    to write the results (default 1).
  */
  void GradC(int layer = 0, int first_grad_layer = 1);

  /**   Plots a field of the first order gradients, i.e. gradx and
    grady; assumes you have called GradC before.
    Not currently used and might need some
    redoing.
    * \param g: Graphics window
    * \param stride: Number of grid points between vectors (drawn as lines,
    currently. 
    * \param linelength: Length of vector lines, in pixels. 
    * \param
    first_grad_layer: first plane of two which contain the calculated gradients
    (default 1).

  */
  void PlotVectorField(Graphics &g, int stride, int linelength,
                       int first_grad_layer = 1);
  /** \brief Initialise a linear gradient of the PDE variables in the Y
    direction 
  *  \param spec The layer that will be initialised 
  * \param conc_top Concentration at the top of the matrix
  * \param conc_bottom Concentration atthe bottom of the matrix
  */
  void InitLinearYGradient(int spec, double conc_top, double conc_bottom);

  /** \brief Plots the PDE variables of a pixel
  * \param x x-coordinate
  * \param y y-coordinate
  * \param graphics Graphics interface
  * \param layer Layer that will be displayed
  */
  bool plotPos(int x, int y, Graphics *graphics, int layer);

  inline PDEFIELD_TYPE ***getPDEvars() { return PDEvars; }

  // CUDA functions

  /**
  * @brief Allocate memory required for the CUDA reaction-diffusion solver.
  *
  * To use this CUDA solver, the following steps must be taken.
  * - Make sure you have an Nvidia GPU
  * - Install CUDA 12.x or higher (contains required cuSparse version for
  *   cusparseDgtsvInterleavedBatch and cusparseSgtsvInterleavedBatch)
  * - Implement your derivatives function in __device__ void DerivativesPDE in
  *   pde.cu 
  * - Enable CUDA by changing the USECUDA flag in Tissue_Similation_Toolkit.pri 
  * - Recompile your code base by performing 'make clean' and 'make' 
  * - Specify the desired number of cores and threads per core
  *   in the parameter file 
  * - Enable CUDA by using 'usecuda = true' in the
  *   parameter file
  */
  void InitialiseCuda();
  /** \brief Intialise the PDE variables

  * The variables will be used to solve the reaction diffusion equation
  * \param cpm Initialisation may depend on the CPM configuration
  * \param celltypes Initalisation may depend on the celltypes
  This initialisation is used for both the CPU and CUDA solver
  */
  void InitialisePDEvars(CellularPotts *cpm, int *celltypes);

  /** \brief Do a single reaction diffusion step on CUDA of size dt
    A reaction-diffusion step of time dt is performed on CUDA. The reaction part
    is solved with the Forward Euler method on CUDA. The diffusion is solved
    with the alternating directions implicit (ADI) method. Communication between
    host and device is only necessary before and after the reaction-diffusion
    step. The PDEvars vector is updated accordingly. PDEvars need to be
    initialised with InitialisePDEvars. The derivatives must be described in
    __device__ void DerivativesPDE in pde.cu, rather than the PDE derivatives
    function from pde.hpp A single reaction-diffusion step is structured as
    follows:
    1. Perform an Forward Euler steps of size dt/2 in increments of ddt
    2. Perform a horizontal ADI sweep of size dt/2
    3. Perform an Forward Euler steps of size dt/2 in increments of ddt
    4. Perform a horizontal ADI sweep of size dt/2
    * \param cpm The current CPM configuration
    * \param repeats Number of reaction-diffusion steps that are performed
  */
  void cuPDEsteps(CellularPotts *cpm, int repeats);
  /** \brief Perform a single ODE step
    Currently this is done with a forward Euler solver, but other solvers may be
    implemented in a straight forward way.
  */
  void cuODEstep(void);
  /** \brief Perform the horizontal alternating directions implicit method step
    This uses an interleaved format for solving which is taken care of by the
    initialisation functions
  */
  void cuHorizontalADIstep(void);
  /** \brief Perform the vertical alternating directions implicit method step
    This uses an interleaved format for solving which is taken care of by the
    initialisation functions
  */
  void cuVerticalADIstep(void);

protected:
  /** \brief First 3D array containing the PDE variables.
  *  PDEvars contains the values of the PDEvars prior to an ODE step
  */
  PDEFIELD_TYPE ***PDEvars;

  // Used as temporary memory in the diffusion step
  // (addresses will be swapped for every time step, so
  // never directly use them!!! Access is guaranteed to be correct
  // through user interface)

  /** \brief Second 3D array containing the PDE variables.
  * PDEvars contains the values of the PDEvars prior to a diffusion step
  */
  PDEFIELD_TYPE ***alt_PDEvars;

  /** \brief 3D array solving containing the spatial dependent diffusion
  coefficients PDEvars contains the values of the PDEvars prior to a diffusion
  step
  */
  PDEFIELD_TYPE ***DiffCoeffs;

  int sizex;
  int sizey;
  int layers;

  // Protected member functions
  /** \brief Used in Plot. Takes a color and turns it into a grey value.
  * \param val: Value from PDE plane.
  Implement this function in you main simulation code. See e.g. vessel.cpp.
  */
  virtual int MapColour(double val);

  // virtual int MapColour3(double val, int l);

  //! empty constructor (necessary for derivation)
  PDE(void);

  /** \brief Allocates a PDE plane (internal use).
  For internal use, can be reimplemented in derived class to change
  method of memory allocation.
  */
  virtual PDEFIELD_TYPE ***AllocatePDEvars(const int layers, const int sx,
                                           const int sy);

  // CUDA variables
  // Variables with d_ are only accesible on the GPU and memory is allocated in
  // InitialiseCuda
  PDEFIELD_TYPE *d_PDEvars;
  PDEFIELD_TYPE *d_alt_PDEvars;
  PDEFIELD_TYPE *d_diffusioncoefficient;
  PDEFIELD_TYPE *d_secr_rate;
  PDEFIELD_TYPE *d_decay_rate;
  int **celltype;
  int *d_celltype;
  int **sigmafield;
  int *d_sigmafield;
  PDEFIELD_TYPE *lowerH, *upperH, *diagH, *BH, *lowerV, *upperV, *diagV, *BV;

private:
  PDEFIELD_TYPE z[10];

  static const int nx[9], ny[9];
  double thetime;
  PDEFIELD_TYPE dt;
  PDEFIELD_TYPE ddt;
  PDEFIELD_TYPE dx2;

  inline double Z(double k, int steps);

  std::vector<std::string> species_names;

  /** \brief Initialise the OpenCL implementation of reaction diffusion solving
    This solver is no longer supported. Use at your own risk. We recommend the
    CUDA solver if you have access to an Nvidia GPU.
  */
  void SetupOpenCL();
  // OpenCL variables
  bool openclsetup = false;
  cl::Program program;
  cl::Kernel kernel_SecreteAndDiffuse;
  bool first_round = true;
};

#endif
