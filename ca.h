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
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include "graph.h"
#include "pde.h"
//#include "dish.h"
#include "cell.h"
// #include <boost/container_hash/hash.hpp>
#include <array>
#include <boost/array.hpp>
// #include "pickset.hpp"
// #include <tr1/unordered_set>
// #include <tr1/array>

// #include <vector>
#include <random>
#include <cstddef>
#include <functional>
// #include <unordered_set>

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

template <class T>
class Edges
{
public:
   const std::unordered_map<std::array<int, 4>,int>::iterator & operator[](unsigned index) const { return edgevector[index]; }
   std::unordered_map<std::array<int, 4>,int>::iterator & operator[](unsigned index) { return edgevector[index]; }

   void insert(std::array<int,4> edge)
   {
        int n = edgevector.size();
       auto insertion = edgemap.insert({edge, n});
       if (insertion.second){
         edgevector.push_back(insertion.first);
       }
       else{
         // cout << "edge already in set while trying to add" << endl;
       }
   }
   void erase(std::array<int,4> edge)
   {
     // cout << "trying to erase, length = " << edgemap.size() <<endl;
     try {
       int index = edgemap.at(edge);
       // std::unordered_map<std::array<int,4>,int>::iterator last_it = edgevector
       std::swap(edgevector[index],edgevector.back());
       edgevector[index]->second = index;
       edgevector.pop_back();
       edgemap.erase(edge);
        // cout << "trying to erase, length = " << edgemap.size() <<endl;
     }
     catch (const std::out_of_range& oor) {
       // cout << "edge not present while trying to delete" << endl;
     }
   }
   unsigned size_map() const
   {
       return edgemap.size();
   }
   unsigned size_vector() const
   {
     return edgevector.size();
   }

private:
   std::unordered_map<std::array<int,4>,int> edgemap;
   std::vector<std::unordered_map<std::array<int, 4>,int>::iterator> edgevector;
};
// template <typename T, typename H = std::hash<T> >
// struct Hasher
// {
//     std::size_t operator()( T* const pt) const
//     {
//         return H()(*pt);
//     }
// };
//
// template <class T, typename H = std::hash<T>>
// struct EqualTo
// {
//     bool operator() ( T* x,  T* y) const
//     {
//         return Hasher<T, H>()(x) == Hasher<T, H>()(x);
//     }
// };
//
// template <typename T, typename H = std::hash<T> >
// struct PickSet
// {
//     unsigned size() const{
//       return _unorderedSet.size();
//     }
//
//     void rebuildAndReserve()
//     {
//         _unorderedSet.clear();
//         _unorderedSet.reserve(_vector.capacity());
//         for ( T& t : _vector) _unorderedSet.insert(&t);
//     }
//
//     void insert(T& t)
//     {
//         if (_unorderedSet.find(&t) == _unorderedSet.end())
//         {
//             _vector.push_back(t);
//
//             if (_unorderedSet.find(&(*(_vector.cbegin()))) != _unorderedSet.end())
//             {
//                 _unorderedSet.insert(&(*(_vector.crbegin())));
//             }
//             else
//             {
//                 rebuildAndReserve();
//             }
//         }
//     }
//
//     void erase( T& t)
//     {
//         auto fit = _unorderedSet.find(&t);
//
//         if (fit != _unorderedSet.end())
//         {
//             if (*fit != &(*(_vector.crbegin())))
//             {
//                 *(const_cast<T*>(*fit)) = *(_vector.rbegin());
//             }
//             _vector.pop_back();
//         }
//     }
//
//     T& pickRandom() const
//     {
//         return _vector[_distribution(_generator) % _vector.size()];
//     }
//
//     std::unordered_set< T*, Hasher<T, H>, EqualTo<T, H> > _unorderedSet;
//     std::vector<T> _vector;
//
//     static std::default_random_engine _generator;
//     static std::uniform_int_distribution<std::size_t> _distribution;
// };
//
// template <typename T, typename H>
// std::default_random_engine PickSet<T, H>::_generator = std::default_random_engine();
//
// template <typename T, typename H>
// std::uniform_int_distribution<std::size_t> PickSet<T, H>::_distribution = std::uniform_int_distribution<std::size_t>();

// template <class T>
// class SubsetVector
// {
// private:
//    struct Entry
//    {
//        T element;
//        int index_in_subset = -1;
//    };
// public:
//    explicit SubsetVector(unsigned size = 0) : m_entries(size)
//    {
//        m_subset_indices.reserve(size);
//    }
//
//    void push_back(const T & element)
//    {
//        m_entries.push_back(Entry{element, -1});
//    }
//    const T & operator[](unsigned index) const { return m_entries[index].element; }
//    T & operator[](unsigned index) { return m_entries[index].element; }
//
//    void insert_in_subset(unsigned index)
//    {
//        if (m_entries[index].index_in_subset < 0) {
//            m_entries[index].index_in_subset = m_subset_indices.size();
//            m_subset_indices.push_back(index);
//        }
//    }
//    void erase_from_subset(unsigned index)
//    {
//        if (m_entries[index].index_in_subset >= 0) {
//            auto subset_index = m_entries[index].index_in_subset;
//            auto & entry_to_fix = m_entries[m_subset_indices.back()];
//            std::swap(m_subset_indices[subset_index], m_subset_indices.back());
//            entry_to_fix.index_in_subset = subset_index;
//            m_subset_indices.pop_back();
//            m_entries[index].index_in_subset = -1;
//        }
//    }
//    unsigned subset_size() const
//    {
//        return m_subset_indices.size();
//    }
//    T & subset_at(unsigned subset_index)
//    {
//        auto index = m_subset_indices.at(subset_index);
//        return m_entries.at(index).element;
//    }
//    const T & subset_at(unsigned subset_index) const
//    {
//        auto index = m_subset_indices.at(subset_index);
//        return m_entries.at(index).element;
//    }
//
// private:
//    std::vector<Entry> m_entries;
//    std::vector<unsigned> m_subset_indices;
// };




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

// class NB {
//   friend class CellularPotts;
//   public
//
//   NB() {
//
//   }
// }

class CellularPotts {

  friend class Info;
  friend class Morphometry;

public:

  std::unordered_set<std::array<int,2>> alivePixels;
  std::unordered_map<std::array<int,2>,int> actPixels;
  std::unordered_map<std::array<int,2>,int> matrixPixels;
  bool AnyPillar();
  bool IsPillar(int x, int y);
  int WhichPillar(int x, int y);

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

  // destructor must also be virtual
  virtual ~CellularPotts();

  /*! \brief Plots the dish to the screen or to a movie and searches the
   neighbours.

   These distinct tasks have been lumped together in the
   same method because both for drawing the black lines between the
   cells and for searching the neighbours the cell borders have to be
   determined. */
  int **SearchNandPlot(Graphics *g=0, bool get_neighbours=true);
  void **SearchNandPlotClear(Graphics *g=0);
  void **PlotVectors(Graphics *g=0);
  int **SearchNeighboursMatrix();

  inline int **GetNeighbourMatrix(void){
    return NB;
  }

 //Functions needed for the perimeter constraint

	int GetNewPerimeterIfXYWereAdded(int sxyp,int x, int y);

  int GetNewPerimeterIfXYWereRemoved(int sxy,int x, int y);

	void SetTargetPerimeter(int tau, int value);

	void SetLambdaPerimeter(int tau, int value);

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
    //void ConstructInitCells(Dish &beast);

		void ConstructInitCells(Dish &beast, int tau, int TArea,int TPerimeter);
		void ConstructInitCells(Dish &beast, int tau, int TArea,int TPerimeter, int AdArea);

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
  void ComputeActVector(Cell &c, PDE *PDEfield);
  void ComputeActVectorAddSite(int new_x, int new_y, Cell &c, PDE *PDEfield, vector<double> &vector_act);
  void ComputeActVectorRemoveSite(int new_x, int new_y, Cell &c, PDE *PDEfield, vector<double> &vector_act);
  void ChangeThetas(Dish *beast);
  int PolarizedAdhesiveEnergy(int actlevelsxy, int sxy, int actlevelsxyp, int sxyp2);

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


  //! \brief Returns the summed age of matrix interactions of specific cell.
  int ComputeCellMatrixAdhesion( int sxy, PDE *PDEfield);

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
  int GetActLevel(int x, int y);
  void MeasureCellSizes(void);
  void MeasureCellSize(Cell &c);
  void CopyProb(double T);


  bool ConnectivityPreservedP(int x, int y);
  bool ConnectivityPreservedPCluster(int x, int y);
  bool NearbyAdhesionSite(int x, int y, int r, PDE *PDEfield);

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
  int **NB;



private:
  bool frozen;
  std::unordered_set<std::array<int, 4>> edgeSetpair;
  Edges<std::unordered_set<std::array<int, 4>,std::vector<std::unordered_map<std::array<int, 4>,int>::iterator>>> edgeSetVector;
  // std::vector<boost::array<int, 4> > edgeVector;
  static const int nx[25], ny[25];
  static const int nbh_level[5];
  static int shuffleindex[9];
  std::vector<Cell> *cell;
  int zygote_area;
  int thetime;
  int n_nb;
};


#endif
