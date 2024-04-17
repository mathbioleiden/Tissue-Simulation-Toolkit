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

/** Implementation of the Glazier & Graner cellular Potts model **/
#ifndef _CA_HH_
#define _CA_HH_

#ifdef _MOCK_CA_HPP_
#include _MOCK_CA_HPP_
#else

#include <array>
#include <cstddef>
#include <functional>
#include <random>
#include <stdio.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "pde.hpp"
#include "cell.hpp"
#include "adhesion_mover.hpp"
#include "cell_ecm_interactions.hpp"
#include "extension_history.hpp"
#include "act.hpp"
#include "grid.hpp"

using namespace std;

namespace std
{
    template <typename T, size_t N> struct hash<const array<T, N>>
    {
        typedef const array<T, N> argument_type;
        typedef size_t result_type;
        result_type operator()(const argument_type &a) const
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
    template <typename T, size_t N> struct hash<array<T, N>>
    {
        typedef array<T, N> argument_type;
        typedef size_t result_type;
        result_type operator()(const argument_type &a) const
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
} // namespace std

class Dish;

class Dir
{
    /* To store a celldirection matrix */
    friend class CellularPotts;

public:
    Dir()
    {
        aa1 = 0.;
        aa2 = 0.;
        bb1 = 0.;
        bb2 = 0.;
        lb1 = 0.;
        lb2 = 0.;
    }
    double aa1, aa2;
    double bb1, bb2;
    double lb1, lb2;
};

class CellularPotts
{

    friend class Info;
    friend class Plotter;
    friend class Morphometry;

public:
    inline int getNbhx(int i) { return nx[i]; }

    inline int getNbhy(int i) { return ny[i]; }

    /** @brief Obtain the level of matrix
     * \return Matrix concentration concentration
     */
    int GetMatrixLevel(int x, int y);

    /** @brief Obtain the level of act
     * \return Act concentration
     */
    int GetActLevel(int x, int y);
    std::unordered_set<std::array<int, 2>> alivePixels;
    std::unordered_map<std::array<int, 2>, int> actPixels;
    int **matrix;

    //! @brief Constructs a CA field. This should be done in "Dish".
    CellularPotts(std::vector<Cell> *cells, const int sizex = 200,
                  const int sizey = 200);
    // empty constructor
    // (necessary for derivation)
    CellularPotts(void);

    /** @brief Initialises the edgelist at the beginning of a simulation

    * The edgelist keeps track of pairs of lattice points that are eligible to
    change the CPM configuration. This function initialises the edgelist at the
    start.
    */
    void InitialiseEdgeList(void);

    /** @brief Allocates data for the sigma array

     Keyword virtual means, that derived classed (cppvmCellularPotts) can
     override this function and carry out the memory allocation in their
     preferred way Every time AllocateSigma is called in the base class methods
     the function belonging the actual type will be called
    */
    virtual void AllocateSigma(int sx, int sy);

    /** @brief Allocates data for the matrix array*/
    virtual void AllocateMatrix(Dish &beast);

    // destructor must also be virtual
    virtual ~CellularPotts();

    /** @brief Plots the dish to the screen or to a movie and searches the
     neighbours.

     These distinct tasks have been lumped together in the
     same method because both for drawing the black lines between the
     cells and for searching the neighbours the cell borders have to be
     determined.

     * \return neighbourhood array
     */

    int **SearchNandPlot(Graphics *g = 0, bool get_neighbours = true);

    //! Plot the dish to Graphics window g
    inline void Plot(Graphics *g) { SearchNandPlot(g, false); }

    /**  @brief Special plotting for Ising model

    Only plot lines between the two states.
    */
    void PlotIsing(Graphics *g, int mag);

    /** @brief Plot the neighbours between cells*/
    void SearchNandPlotClear(Graphics *g = 0);

    /** @brief Obtain the neighbour matrix of cells
     * \return Neighbourhood array
     */
    int **SearchNeighboursMatrix();

    // Functions needed for the perimeter constraint

    /** @brief Get perimeter if new pixel is added
     * \return New perimeter
     */
    int GetNewPerimeterIfXYWereAdded(int sxyp, int x, int y);

    /** @brief Get perimeter if pixel is removed
     * \return New perimeter
     */
    int GetNewPerimeterIfXYWereRemoved(int sxy, int x, int y);

    /** @brief Set the target perimeter
     */
    void SetTargetPerimeter(int tau, int value);

    /** @brief Set the strength of the perimeter constraint
     */
    void SetLambdaPerimeter(int tau, int value);

    //! Searches the cells' neighbours without plotting
    inline int **SearchNeighbours(void) { return SearchNandPlot(0, true); }

    //! Return the total area occupied by the cells
    inline int Mass(void)
    {
        int mass = 0;
        for (int i = 0; i < sizex * sizey; i++)
        {
            if (sigma[0][i] > 0)
                mass++;
        }
        return mass;
    }

    /** @brief Find a bounding box that contains all cells.

    Currently has no output
    */
    void FindBoundingBox(void);

    /** @brief Plot the cells according to their cell identity, not their type.

    The black lines are omitted.
    */
    void PlotSigma(Graphics *g, int mag = 2);

    /** @brief Divide all cells.
    Divide along cell elongation axis */
    void DivideCells(vector<Cell> &cells)
    {
        std::vector<bool> which_cells(cells.size());
        for (int i = 1; i < cells.size(); i++)
            which_cells[i] = true;
        DivideCells(which_cells, cells);
    }

    /** Divide all cells marked "true" in which_cells.
    \param which_cells is a vector<bool> with the same number of
    elements as the number of cells. It is a mask indicating which
    cells should be divided; each cell marked true will be divided.

     If which_cells is empty, this method divides all cells.
    */
    void DivideCells(std::vector<bool> which_cells, vector<Cell> &cells);

    /** Implements the core CPM algorithm. Carries out one MCS.
     * \return Total energy change during MCS.
     */
    int AmoebaeMove(PDE *PDEfield = 0, bool anneal = false);

    /** @brief Implements the core CPM algorithm including Act dynamics.

      Carries out one
      MCS with the edge lsit algorithmAMo.
    * \return Total energy change during MCS.
    */
    int Act_AmoebaeMove(PDE *PDEfield);

    /** @brief Implements the core CPM algorithm with Kawasaki dynamics.

      Carries out one MCS.
     * \return Total energy change during MCS.
     */
    int KawasakiMove(PDE *PDEfield = 0);

    /** @brief

      Implements Metropolis dynamics for the Ising model. Carries out one MCS.
     * \return Total energy change during MCS.
     */
    int IsingMove(PDE *PDEfield = 0);

    /** @brief

      Implements standard large q-Potts model. Carries out one MCS.
     * \return Total energy change during MCS.
     */
    int PottsMove(PDE *PDEfield = 0);

    /** @brief

      Implements standard large q-Potts model via Neighbour copies.  Carries out
       one MCS.
     *\return Total energy change during MCS.
     */
    int PottsNeighbourMove(PDE *PDEfield);

    /** Returns changes made to the adhesions since the last reset.
     * \return The accumulated changes
     */
    CellECMInteractions GetCellECMInteractions() const;

    /** Clears recorded changes to the adhesions.
     */
    void ResetCellECMInteractions();

    /** Set ECM boundary state, overwriting the current state.
     */
    void SetECMBoundaryState(ECMBoundaryState const &ecm_boundary_state);

    /** @brief Read initial cell shape from XPM file.

      Reads the initial cell shape from an
      include xpm picture called "ZYGXPM(ZYGOTE)",
      and it allocates enough cells for it to the Dish */
    void ReadZygotePicture(void);
    // Used internally to assign a Cell object to each "blob"
    // "blobs" should already have different indices.
    //
    // (i.e. to start from a binary image you'd probably first want
    // to apply a blob counting algorithm

    /** @brief Construct initial cells
      Construct the cells from the sigma-field
    */
    void ConstructInitCells(Dish &beast);
    // void ConstructInitCells(Dish &beast, int tau, int TArea,int TPerimeter);
    // void ConstructInitCells(Dish &beast, int tau, int TArea,int TPerimeter,
    // int AdArea);

    //! Returns the number of completed Monte Carlo steps.
    inline int Time() const { return thetime; }

    //! @brief Return the horizontal size of the CA plane.
    inline int SizeX() const { return sizex; }

    //! @brief Return the vertical size of the CA plane.
    inline int SizeY() const { return sizey; }

    /** @brief Return the value of lattice site (x,y).

    i.e. This will return the index of the cell which occupies site (x,y). */
    inline int Sigma(const int x, const int y) const { return sigma[x][y]; }

    /** In this method the principal axes of the cells are computed using
     the method described in "Biometry", box 15.5
     * \return a pointer to a "new[]"ed array containing the directions.
     The memory has to be freed afterwards using the delete[] operator
    */
    Dir *FindCellDirections(void) const;

    /** @brief Initialise the CA plane with n circular cells fitting in
      a cellsize^2 square.*/
    int ThrowInCells(int n, int cellsize);

    /** @brief Initialise the subfield in which eden growth takes place.
    \param n: Number of cells.
    \param cellsize: Number of Eden growth iterations.
    \param subfield: Defines a centered frame of size (size/subfield)^2 in which
    all cell will be positioned.
    * \return Index of last cell inserted.
    */
    int GrowInCells(int n_cells, int cellsize, double subfield = 1.,
                    int posx = -1, int posy = -1);

    /** @brief Initialise the CA plane with n cells using an Eden growth
    algorithm.
    * \param n: Number of cells.
    * \param cell_size: Number of Eden growth
    iterations. \param sx: x-size of subfield.
    * \param sy: y-size of subfield.
    * \param offset_x: x location for subfield.
    * \param offset_y: y location for subfield.
    * \return Index of last cell inserted.
    */
    int GrowInCells(int n_cells, int cell_size, int sx, int sy, int offset_x,
                    int offset_y);

    /** @brief Initialise cpm field with a random sigma of 0 or 1 of every pixel

    * \param prob: This fraction of pixels will be a medium pixel
    */
    void RandomSpins(double prob);

    /** @brief Initialise a square cell
     * \param sig: sigma value of the cell
     * \param cx: x-coordinate of the cell
     * \param cy: y-coordinate of the cell
     * \param size: length of the square cells
     */
    int SquareCell(int sig, int cx, int cy, int size);

    //! @brief Adds a new Cell and returns a reference to it.
    inline Cell &AddCell(Dish &beast)
    {
        cell->push_back(Cell(beast));
        return cell->back();
    }
    /** @brief Display the division planes returned by FindCellDirections.

    \param g: Graphics window
    \param celldir: cell axes as returned by FindCellDirections.
    */
    void ShowDirections(Graphics &g, const Dir *celldir) const;

    //! @brief Returns the mean area of the cells.
    double MeanCellArea(void) const;

    /** @brief Returns the cell density.

    Cell density is defined as the area occupied by cells divided by the size of
    the field.
    */
    double CellDensity(void) const;

    /** @brief Set target lengths of all cells to the value given in parameter
    file.*/
    void ResetTargetLengths(void);

    int spins_converted;

    /** @brief Give each cell a random cell type.

    The number of cell types is defined by the J parameter file. (See
    Jtable in parameter file).
    */
    void SetRandomTypes(void);

    /** Cells grow until twice their original target_length, then
      divide, with rate "growth_rate"
    */
    void GrowAndDivideCells(int growth_rate, std::vector<Cell> &cells);

    /** @brief Returns cell with sigma c.
     */
    inline Cell &getCell(int c) const { return (*cell)[c]; }

    inline vector<Cell> *getCellArray() const { return cell; }

    /** Draw convex hull around all cells.
     * \return The area of the convex hull in lattice sites.
     */
    double DrawConvexHull(Graphics *g, int color = 1);

    /** Calculate compactness (summed_area/hull_area) of all cells.
      This is a good measure for the density.
      Function allows a bounding box.
     * \return Compactness.
    */
    double Compactness(void);

    /** @brief Assign random sigma to every lattice point

    *  \par n_cells: total number of cells
    */
    void RandomSigma(int n_cells);

    /** @brief Measure the initial cell sizes.

    * Measure cell sizes of all initial size and assign them to the cells
    */
    void MeasureCellSizes(void);

    /** @brief Measure the initial cell perimeters

    *  Measure cell perimeters of all initial size and assign them to the cells
    */
    void MeasureCellPerimeters();

    /** @brief Run amoebaemove while only accepting negative delta H
     */
    void anneal(int steps);
    /** @brief Find the sigma field after annealing steps

    * \param steps: Number of annealing MCS
    * \return sigma-field after annealing
    */
    int **get_annealed_sigma(int steps);

    /**  Return Sigma Array
     */
    inline int **getSigma() const { return sigma; }

    /** @brief plot the sigma at (x,y)

    * \return True if cell belongs to medium
    */
    bool plotPos(int x, int y, Graphics *graphics);
    /** @brief plot cell outlines
     */
    void linePlotPos(int x, int y, Graphics *graphics);

    inline void fillCellColArr(int *arr)
    {
        for (int dex = 0; dex < par.sizex * par.sizey; dex++)
        {
            int pos = sigma[0][dex];
            if (pos != 0)
            {
                arr[dex] = (*cell)[pos].Colour();
            }
            else
            {
                arr[dex] = 0;
            }
        }
    };

  vector<AdhesionWithEnvironment> getAdhesions();
private:
    /** @brief Standard deltaH with are constraint, length constraint and
     * chemotaxis
     */
    int DeltaH(int x, int y, int xp, int yp, PDE *PDEfield,
               AdhesionDisplacements *adh_disp);

    /** @brief DeltaH, including act dynamics
     */
    int Act_DeltaH(int x, int y, int xp, int yp, PDE *PDEfield = 0);

    /** @brief Compute deltaH for Kawasaki dynamics
     */
    int KawasakiDeltaH(int x, int y, int xp, int yp, PDE *PDEfield = 0);

    /** @brief Compute deltaH for Ising dynamics
     */
    int IsingDeltaH(int x, int y, PDE *PDEfield = 0);

    /** @brief Compute deltaH for Potts dynamics
     */
    int PottsDeltaH(int x, int y, int new_state);

    /** @brief Change the spin at site (x,y) to the spin at (xp,yp)
     */
    void ConvertSpin(int x, int y, int xp, int yp);

    /** @brief Exhange the spins at (x,y) and (xp,yp)
     */
    void ExchangeSpin(int x, int y, int xp, int yp);

    void SprayMedium(void);

    /** @brief Compute if a copy attempt should get accepted
     */
    int CopyvProb(int DH, double stiff, bool anneal);

    /** @brief Freeze the CPM configuration
     */
    void FreezeAmoebae(void);

    /** @brief Add a new edge to the edge list
     */
    void AddEdgeToEdgelist(int edge);

    /** @brief Remove an edge from the edge list
     */
    void RemoveEdgeFromEdgelist(int edge);

    /** @brief Find the edge in the other direction for the edge list
     */
    int CounterEdge(int edge);

    /** @brief Find the cell size of cell c
     */
    void MeasureCellSize(Cell &c);

    /** @brief Compute large deltaH 'on-the-fly'
     */
    void CopyProb(double T);

    /** @brief Check if the cell is locally connected at (x,y).

    From Durand, M., & Guesnet, E. (2016). An efficient Cellular Potts Model
    algorithm that forbids cell fragmentation. Computer Physics Communications,
    208, 54-63. Checks if cell sigma is locally connected at lattice point (x,y)
    if using LocalConnectedness(x,y,sigma[x][y]) and
    LocalConnectedness(x,y,sigma[xp][yp] both are true This prevents cell
    fragementation, as well as holes within a cell.
    * \return Local connectedness of cell s at site (x,y)
    */
    bool LocalConnectedness(int x, int y, int s);

    /** @brief Checks if connectivity is preserved if (x,y) would be changed
     */
    bool ConnectivityPreservedP(int x, int y);
    /** @brief Checks if a cluster of cell would remain conencted if (x,y) would
     * be changed
     */
    bool ConnectivityPreservedPCluster(int x, int y);

    /** Plot a cell and its neighbours
     */
    inline void PrintSite(int x, int y)
    {
        std::cerr << "--------\n";
        std::cerr << "[" << sigma[x - 1][y - 1] << " " << sigma[x][y - 1] << " "
                  << sigma[x + 1][y - 1] << "]\n";
        std::cerr << "[" << sigma[x - 1][y] << " " << sigma[x][y] << " "
                  << sigma[x + 1][y] << "]\n";
        std::cerr << "[" << sigma[x - 1][y + 1] << " " << sigma[x][y + 1] << " "
                  << sigma[x + 1][y + 1] << "]\n";
    }

protected:
    /** @brief Initialise CPM class
     */
    void BaseInitialisation(std::vector<Cell> *cell);

protected:
  int **sigma;
  int sizex;
  int sizey;
public:
  ExtensionHistory history;
  void MoveAdhesions();
  void setGrid(const Grid &grid);
  ACT::ActField& getActField() {
    return act_field;
  }

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
  ACT::ActField act_field;
};

#endif
#endif
