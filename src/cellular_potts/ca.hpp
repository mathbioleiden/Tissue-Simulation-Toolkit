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

// mainpage.hpp contains no C++ code, it is for the main page of the
// documentation
#include "mainpage.hpp"

/*! Implementation of the Glazier & Graner cellular Potts model **/
#ifndef _CA_HH_
#define _CA_HH_

#ifdef _MOCK_CA_HPP_
#include _MOCK_CA_HPP_
#else

#include <vector>
#include <stdio.h>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <array>
#include <random>
#include <cstddef>
#include <functional>

#include "pde.hpp"
#include "cell.hpp"
#include "adhesion_mover.hpp"
#include "cell_ecm_interactions.hpp"

using namespace std;

namespace std
{
  template<typename T, size_t N>
  struct hash <const array<T, N> >
  {
    typedef const array<T, N> argument_type;
    typedef size_t result_type;
    result_type operator()(const argument_type& a) const
    {
      hash<T> hasher;
      result_type h = 1;
      for (result_type i = 0; i < N; ++i)
      {
          h = h * hasher(a[i]);
      }
      return h;
    }
  };
  template<typename T, size_t N>
  struct hash <array<T, N> >
  {
    typedef array<T, N> argument_type;
    typedef size_t result_type;
    result_type operator()(const argument_type& a) const
    {
      hash<T> hasher;
      result_type h = 1;
      for (result_type i = 0; i < N; ++i)
      {
          h = h * hasher(a[i]);
      }
      return h;
    }
  };
}

class Dish;

class Dir {
  /* To store a celldirection matrix */
  friend class CellularPotts;
public:
  Dir() {
    aa1=0.; aa2=0.;
    bb1=0.; bb2=0.;
    lb1=0.; lb2=0.;
  }
  double  aa1,aa2;
  double  bb1,bb2;
  double  lb1,lb2;
};


class CellularPotts {

  friend class Info;
  friend class Morphometry;
    
public:
  int GetMatrixLevel(int x, int y);
  int GetActLevel(int x, int y);
  std::unordered_set<std::array<int,2>> alivePixels;
  std::unordered_map<std::array<int,2>,int> actPixels;
  int **matrix;

  //! \brief Constructs a CA field. This should be done in "Dish".
  CellularPotts(std::vector<Cell> *cells, const int sizex=200,
		const int sizey=200);
  // empty constructor
  // (necessary for derivation)
  CellularPotts(void);

  void InitializeEdgeList(void); //Set the initial edgelist which are eligible to change

  // Keyword virtual means, that derived classed (cppvmCellularPotts) can override
  // this function and carry out the memory allocation in their preferred way
  // Every time AllocateSigma is called in the base class methods
  // the function belonging the actual type will be called
  virtual void AllocateSigma(int sx, int sy);
  
  virtual void InitializeMatrix(Dish &beast);

  // destructor must also be virtual
  virtual ~CellularPotts();

  /*! \brief Plots the dish to the screen or to a movie and searches the
   neighbours. 

   These distinct tasks have been lumped together in the
   same method because both for drawing the black lines between the
   cells and for searching the neighbours the cell borders have to be
   determined. */
  int **SearchNandPlot(Graphics *g=0, bool get_neighbours=true);
  
  //! Plot the dish to Graphics window g
  inline void Plot(Graphics *g) {
    SearchNandPlot(g, false);
  }
  
  //! Special plotting for Ising model
  void PlotIsing(Graphics *g, int mag);
  
  void SearchNandPlotClear(Graphics *g=0);
  int **SearchNeighboursMatrix();

  //Functions needed for the perimeter constraint

  int GetNewPerimeterIfXYWereAdded(int sxyp,int x, int y);

  int GetNewPerimeterIfXYWereRemoved(int sxy,int x, int y);

  void SetTargetPerimeter(int tau, int value);

  void SetLambdaPerimeter(int tau, int value);

  //! Searches the cells' neighbors without plotting
  inline int **SearchNeighbours(void) {
    return SearchNandPlot(0, true);
  }

  //! Return the total area occupied by the cells
  inline int Mass(void) {
    int mass=0;
    for (int i=0;i<sizex*sizey;i++) {
      if (sigma[0][i]>0) mass++;
    }
    return mass;
  }
    
  void SetBoundingBox(void);

  /*! Plot the cells according to their cell identity, not their type.
  The black lines are omitted.
  */
    
  void PlotSigma(Graphics *g, int mag=2);
  void WriteData(void);

  /*! A simple method to count all sigma's and write the output to an ostream */
  void CountSigma(std::ostream &os);
  
  //! Divide all cells.
  void DivideCells(void) {
    std::vector<bool> tmp;
    DivideCells(tmp);
  }
  
  /*! Divide all cells marked "true" in which_cells.
  \param which_cells is a vector<bool> with the same number of
  elements as the number of cells. It is a mask indicating which
  cells should be divided; each cell marked true will be divided.
    
   If which_cells is empty, this method divides all cells.
  */
  void DivideCells(std::vector<bool> which_cells);
  
  /*! Implements the core CPM algorithm. Carries out one MCS.
    \return Total energy change during MCS.
  */
  int AmoebaeMove(PDE *PDEfield=0, bool anneal = false);
 
  
  int Act_AmoebaeMove(PDE *PDEfield);
 

  /*! Implements the core CPM algorithm with Kawasaki dynamics. Carries out one MCS.
   \return Total energy change during MCS.
   */
  int KawasakiMove(PDE *PDEfield=0);
  
  /*! Implements Metropolis dynamics for the Ising model. Carries out one MCS.
   \return Total energy change during MCS.
   */
  int IsingMove(PDE *PDEfield=0);
  
   /*! Implements standard large q-Potts model. Carries out one MCS.
    \return Total energy change during MCS.
    */
  int PottsMove(PDE *PDEfield=0);
  
  /*! Implements standard large q-Potts model via Neighbor copies.  Carries out one MCS.
   \return Total energy change during MCS.
   */
  int PottsNeighborMove(PDE *PDEfield);
  
  /*! Returns changes made to the adhesions since the last reset.
   * \return The accumulated changes
   */
  CellECMInteractions GetCellECMInteractions() const;

  /*! Clears recorded changes to the adhesions.
   */
  void ResetCellECMInteractions();

  /*! Set ECM boundary state, overwriting the current state.
   */
  void SetECMBoundaryState(ECMBoundaryState const & ecm_boundary_state);

  /*! \brief Read initial cell shape from XPM file.
    Reads the initial cell shape from an 
    include xpm picture called "ZYGXPM(ZYGOTE)",
    and it allocates enough cells for it to the Dish */
  void ReadZygotePicture(void);

  // Used internally to assign a Cell object to each "blob"
  // "blobs" should already have different indices.
  //
  // (i.e. to start from a binary image you'd probably first want
  // to apply a blob counting algorithm
  
  void ConstructInitCells(Dish &beast);
  //void ConstructInitCells(Dish &beast, int tau, int TArea,int TPerimeter);
  //void ConstructInitCells(Dish &beast, int tau, int TArea,int TPerimeter, int AdArea);

  //! Returns the number of completed Monte Carlo steps.
  inline int Time() const {
    return thetime;
  }

  // not currently used? In Critter implementation (see Hogeweg
  // 2000) this was used to have cells divide at double their original area.
  inline int ZygoteArea() const {
    return zygote_area;
  }

  //! \brief Return the horizontal size of the CA plane.
  inline int SizeX() const {
    return sizex;
  }

  //! \brief Return the vertical size of the CA plane.
  inline int SizeY() const {
    return sizey;
  }
  
  /*! \brief Return the value of lattice site (x,y).

  i.e. This will return the index of the cell which occupies site (x,y). */
  inline int Sigma(const int x, const int y) const {
    return sigma[x][y];
  }
  
  // Was used to make it possible to enlarge the Graphics window in
  // X11 and replace the contents interactively. Not currently supported.
  void Replace(Graphics *g);

  /*! In this method the principal axes of the cells are computed using
   the method described in "Biometry", box 15.5 
   \return a pointer to a "new[]"ed array containing the directions.
   The memory has to be freed afterwards using the delete[] operator
  */
  Dir *FindCellDirections(void) const;

  /*! \brief Initialize the CA plane with n circular cells fitting in
    a cellsize^2 square.*/
  int ThrowInCells(int n, int cellsize);

  /*! \brief Initialize the CA plane with n cells using an Eden growth algorithm.

  \param n: Number of cells.
  \param cellsize: Number of Eden growth iterations.
  \param subfield: Defines a centered frame of size (size/subfield)^2 in which all cell will be positioned. 
  \return Index of last cell inserted.
  */
  int GrowInCells(int n_cells, int cellsize, double subfield=1., int posx=-1, int posy=-1);
  int GrowInCells(int n_cells, int cell_size, int sx, int sy, int offset_x, int offset_y);
  void RandomSpins(double prob);
    
  int SquareCell(int sig, int cx, int cy, int size);

  
  //! \brief Adds a new Cell and returns a reference to it.
  inline Cell &AddCell(Dish &beast) {
    cell->push_back(Cell(beast));
    return cell->back();
  }
  /*! \brief Display the division planes returned by FindCellDirections.
  \param g: Graphics window
  \param celldir: cell axes as returned by FindCellDirections.
  */
  void ShowDirections(Graphics &g, const Dir *celldir) const;
  
  //! \brief Returns the mean area of the cells. 
  double MeanCellArea(void) const;
  
  /*! \brief Returns the cell density.

  Cell density is defined as the area occupied by cells divided by the size of the field.
  */
  double CellDensity(void) const; 
  
  //! \brief Set target lengths of all cells to the value given in parameter file.
  void ResetTargetLengths(void);
 
  int spins_converted;
  
  /*! \brief Give each cell a random cell type.
  The number of cell types is defined by the J parameter file. (See
  Jtable in parameter file).
  */
  void SetRandomTypes(void);

  /*! Cells grow until twice their original target_length, then
    divide, with rate "growth_rate"
  */
  void GrowAndDivideCells(int growth_rate);
  
  inline Cell &getCell(int c) {
    return (*cell)[c];
  }

  /*! Draw convex hull around all cells.
    \return The area of the convex hull in lattice sites.
  */
  double DrawConvexHull(Graphics *g, int color=1);
  
  /*! Calculate compactness (summed_area/hull_area) of all cells.
    This is a good measure for the density.
    \return Compactness.
  */
  double Compactness(void);  
  void RandomSigma(int n_cells);
  
  void MeasureCellSizes(void);
  void MeasureCellPerimeters();  

  void anneal(int steps);
  int ** get_annealed_sigma(int steps);

  //Return Sigma Array for use on GPU
  inline int** getSigma(){
    return sigma;
  }

  bool plotPos(int x, int y, Graphics * graphics);
  void linePlotPos(int x, int y, Graphics * graphics);
  
  inline void fillCellColArr(int * arr){
    for (int dex = 0; dex < par.sizex*par.sizey; dex++){
      int pos = sigma[0][dex];
      if (pos != 0) {
        arr[dex] = (*cell)[pos].Colour();
      }
      else {
        arr[dex] = 0;
      }
    }
  };

private:
  void IndexShuffle(void);
  /** Calculate the work required to make a copy.
   *
   * @param x x coordinate of target pixel
   * @param y y coordinate of target pixel
   * @param xp x coordinate of source pixel
   * @param yp y coordinate of source pixel
   * @param adh_disp Optional out parameter that receives displacements of
   *        adhesions if the copy is taken. Must not be null if adhesions are
   *        enabled.
   * @param PDEfield Optional concentrations to use for chemotaxis
   */
  int DeltaH(
          int x, int y, int xp, int yp, PDE *PDEfield=0,
          AdhesionDisplacements * adh_disp = nullptr);
  int Act_DeltaH(int x,int y, int xp, int yp, PDE *PDEfield=0);

  int KawasakiDeltaH(int x,int y, int xp, int yp, PDE *PDEfield=0);
  int IsingDeltaH(int x,int y, PDE *PDEfield=0);
  int PottsDeltaH(int x,int y, int new_state);
    
  bool Probability(int DH);
  void ConvertSpin(int x,int y,int xp,int yp);
  void ExchangeSpin(int x,int y,int xp,int yp);
    
  void SprayMedium(void);
  int CopyvProb(int DH,  double stiff, bool anneal);
  void FreezeAmoebae(void);
  void AddEdgeToEdgelist(int edge);
  void RemoveEdgeFromEdgelist(int edge);
  int CounterEdge(int edge);
  void MeasureCellSize(Cell &c);
  void CopyProb(double T);
  bool ConnectivityPreservedP(int x, int y);
  bool ConnectivityPreservedPCluster(int x, int y);

  // little debugging function to print the site and its neighbourhood
  inline void PrintSite(int x,int y) {
	  std::cerr << "--------\n";
	  std::cerr << "[" << sigma[x-1][y-1] << " " << sigma[x][y-1] << " " << sigma[x+1][y-1] << "]\n";
	  std::cerr << "[" << sigma[x-1][y] << " " << sigma[x][y] << " " << sigma[x+1][y] << "]\n";
	  std::cerr << "[" << sigma[x-1][y+1] << " " << sigma[x][y+1] << " " << sigma[x+1][y+1] << "]\n";
  }

protected:
	void BaseInitialisation(std::vector<Cell> *cell);

protected:
  int **sigma;
  int sizex;
  int sizey;

private:
  bool frozen;
  static const int nx[21], ny[21];
  static const int nbh_level[4];
  int *edgelist;
  int *orderedgelist;
  int sizeedgelist;
  static int shuffleindex[9];
  std::vector<Cell> *cell;
  int zygote_area;
  int thetime;
  int n_nb;
  AdhesionMover adhesion_mover;
};

#endif
#endif

