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

// mainpage.h contains no C++ code, it is for the main page of the
// documentation
#include "mainpage.h"

/*! Implementation of the Glazier & Graner cellular Potts model **/
#ifndef _CA_HH_
#define _CA_HH_
#include <vector>
#include <stdio.h>
#include "graph.h"
#include "pde.h"
//#include "dish.h"
#include "cell.h"

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
  //! \brief Constructs a CA field. This should be done in "Dish".
  CellularPotts(std::vector<Cell> *cells, const int sizex=200, 
		const int sizey=200 );
  // empty constructor
  // (necessary for derivation)
  CellularPotts(void);

	void InitializeEdgeList(void); //Set the initial edgelist which are eligible to change

  // Keyword virtual means, that derived classed (cppvmCellularPotts) can override
  // this function and carry out the memory allocation in their preferred way
  // Every time AllocateSigma is called in the base class methods
  // the function belonging the actual type will be called
  virtual void AllocateSigma(int sx, int sy);
  
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

  /*! Plot the cells according to their cell identity, not their type.
    
  The black lines are omitted.
  */
  void PlotSigma(Graphics *g, int mag=2);

  
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
    int AmoebaeMove(PDE *PDEfield=0);
  
    /*! \brief Read initial cell shape from XPM file.
      Reads the initial cell shape from an 
      include xpm picture called "ZYGXPM(ZYGOTE)",
      and it allocates enough cells for it to the Dish */
    void ReadZygotePicture(void);

    
    // int BlobCounting(void); (not implemented?)
    
    // Used internally to assign a Cell object to each "blob"
    // "blobs" should already have different indices.
    //
    // (i.e. to start from a binary image you'd probably first want
    // to apply a blob counting algorithm
    void ConstructInitCells(Dish &beast);
    
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
  int GrowInCells(int n_cells, int cellsize, double subfield=1.);
  int GrowInCells(int n_cells, int cell_size, int sx, int sy, int offset_x, int offset_y);
  
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
  double Compactness(double *res_compactness = 0, 
		     double *res_area = 0, 
		     double *res_cell_area = 0);
  
private:
  void IndexShuffle(void);
  int DeltaH(int x,int y, int xp, int yp, PDE *PDEfield=0);
  bool Probability(int DH);
  void ConvertSpin(int x,int y,int xp,int yp);
  void SprayMedium(void);
  int CopyvProb(int DH,  double stiff);
  void FreezeAmoebae(void);
	void AddEdgeToEdgelist(int edge);
	void RemoveEdgeFromEdgelist(int edge);
	int CounterEdge(int edge);
  void MeasureCellSizes(void);
  void MeasureCellSize(Cell &c);
  void CopyProb(double T);
  bool ConnectivityPreservedP(int x, int y);

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
	int *edgelist;
	int *orderedgelist;
	int sizeedgelist;
  static const int nx[21], ny[21];
  static const int nbh_level[4];
  static int shuffleindex[9];
  std::vector<Cell> *cell;
  int zygote_area;
  int thetime;
  int n_nb;
};


#endif
