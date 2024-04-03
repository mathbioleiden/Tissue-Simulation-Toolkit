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

/** \class Dish
  @brief The virtual Petri dish.
  Hosts the cells with states and the CA-plane.
*/

#ifndef CRITTER_H_
#define CRITTER_H_
#include "ca.hpp"
#include "cell.hpp"
#include "graph.hpp"
#include "inputoutput.hpp"
#include "mcds_io.h"
#include "pde.hpp"
#include "random.hpp"
#include <vector>

namespace ColourMode {
enum { State, CellType, Sigma, Auxilliary };
}

class Dish {
  friend class Info;

public:
  Dish();
  /** @brief Init defines the initial state of the virtual
    cell culture.

    Define Init() in your main file describing the simulation set up,
    within the block INIT { }. See for examples vessel.cpp and
    sorting.cpp.
  */
  void Init(void);

  void ConstructorBody(void);

  virtual ~Dish();
  /** @brief Plot the Dish to graphics window g.

  Simply calls CPM->Plot.
  */
  void Plot(Graphics *g);

  //! @brief Erase all cells
  void Erase(void);

  //! Returns the number of completed Monte Carlo Steps.
  int Time(void) const;

  //! Returns the number of cells in the dish, excluding apoptosed cells.
  int CountCells(void) const;

  /** @brief Stretched induced cell growth and division.

  See Hogeweg (2000), Journal of Theoretical Biology.

  Find stretched cells, and increase their target area.
  Find enlarged cells, and divide them.*/
  void CellGrowthAndDivision(void);

  //! @brief. Returns the summed area of all cells in the dish
  int Area(void) const;

  //! @brief Returns the summed of all cells target area in the dish
  int TargetArea(void) const;

  //! @brief Returns the horizontal size of the dish.
  int SizeX(void);

  //! @brief Returns the horizontal size of the dish.
  int SizeY(void);

  //! @brief Returns a reference to cell number "c"
  inline Cell &getCell(int c) { return cell[c]; }

  PDE *PDEfield;
  CellularPotts *CPM;
  IO *io;

  // Was used for gradient measurements, not functional now.
  void ClearGrads(void);

  void MeasureChemConcentrations(void);

  /**
   * @brief Export a cell configuration to an .xml format annotated
   * by the MultiCellDS format
   * @param fname Filename
   * Warning: This function is currently broken.
   */
  void ExportMultiCellDS(std::string const &fname);
  /**
   * @brief Import a cell configuration from an .xml format annotated
   * by the MultiCellDS format
   * @param fname Filename
   * Warning: This function is currently broken.
   */
  void ImportMultiCellDS(std::string const &fname);

protected:
  //! Assign a the cell to the current Dish
  void SetCellOwner(Cell &which_cell);

private:
  /**
   * @brief Returns wheter or not a cell is isolated,
   * @param c Cell object.
   * @param neighbours Neighbours of the cell.
   */
  bool CellIsolated(const Cell &c, int **neighbours) const;
  /**
   * @brief Import a cell annoted in .xml format annoted by
   * MulticellDS
   * Warning: This function is currently broken.
  */ 
  void MCDS_import_cell(MCDS_io *mcds, int cell_id);
    /**
   * @brief Export a cell annoted in .xml format annoted by
   * MulticellDS
   * Warning: This function is currently broken.
  */
  void MCDS_export_cell(MCDS_io *mcds, Cell *cell);

  bool sizechange = false;

public:
  //! The cells in the Petri dish; accessible to derived classes
  std::vector<Cell> cell;
};

#define INIT void Dish::Init(void)

#endif
