#pragma once
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
//#ifndef _CELL_HH_
//#define _CELL_HH_

#include "cell_direction.hpp"
#include "parameter.hpp"
// #define EMPTY -1
#include <iostream>
#include <math.h>
#include "vec2.hpp"

extern Parameter par;
class Dish;

class Cell
{
    friend class Dish;
    friend class CellularPotts;
    friend class Info;
    friend class IO;
    friend void DivideCells(std::vector<bool> which_cells,
                            std::vector<Cell> &cells, int **sigma);

public:
    Vec2<double> polarity; 
    Vec2<double> previous_center_of_mass; 
    double lambda_act;
    /*! \brief Constructor to insert a cell into Dish "who"
    Used to add a new Cell to the dish: new Cell(dish,
    celtype).
    */
    Cell(const Dish &who, int settau = 1)
    {
        ConstructorBody(settau);
    }

    Cell(void) { ConstructorBody(1); }

    ~Cell(void);

    //! Default copy constructor.
    Cell(const Cell &src)
    {
        // make an exact copy (for internal use)
        sigma = src.sigma;
        amount++;
        area = src.area;
        target_area = src.target_area;
        adhesive_area = src.adhesive_area;
        ref_adhesive_area = src.ref_adhesive_area;
        perimeter = src.perimeter;
        target_perimeter = src.target_perimeter;
        target_length = src.target_length;
        growth_threshold = src.growth_threshold;
        mother = src.mother;
        daughter = src.daughter;
        times_divided = src.times_divided;
        date_of_birth = src.date_of_birth;
        colour_of_birth = src.colour_of_birth;
        tau = src.tau;
        alive = src.alive;
        v[0] = src.v[0];
        v[1] = src.v[1];
        n_copies = src.n_copies;
        owner = src.owner;

        chem = new double[par.n_chem];
        for (int ch = 0; ch < par.n_chem; ch++)
            chem[ch] = src.chem[ch];

        colour = src.colour;
        fit_ellipse = src.fit_ellipse;
    }

    /*! \brief Add a new cell to the dish.

       Call it as: new Cell(parent, true); mother will be modified for
       ancestry administration!

       \param settau
       Cell type of daughter cell.
    */
    void CellBirth(Cell &mother);

    /*! \brief Assignment operator.

    Called if one cell is assigned to another. Remember to change both
    assignment operator and copy constructor when adding new attributes
    to Cell.
    */
    inline Cell &operator=(const Cell &src)
    {
        colour = src.colour;
        alive = src.alive;
        sigma = src.sigma;
        area = src.area;
        tau = src.tau;
        target_area = src.target_area;
        v[0] = src.v[0];
        v[1] = src.v[1];
        n_copies = src.n_copies;

        border = src.border;

        target_length = src.target_length;
        amount++;
        owner = src.owner;

        chem = new double[par.n_chem];
        for (int ch = 0; ch < par.n_chem; ch++)
            chem[ch] = src.chem[ch];

        perimeter = src.perimeter;
        target_perimeter = src.target_perimeter;
        return *this;
    }

    /*! \brief Returns false if Cell has apoptosed (vanished). */
    inline bool AliveP(void) const { return alive; }

  //! Returns the cell colour.
  inline int Colour(void) const {
    /* if (par.dynamicJ)
      return colour;
      else */
    return colour;
  };

    //! Set cell type of this Cell.
    inline void setTau(int settau) { tau = settau; }

    /*! \brief Set the adhesive area of a cell, used for act model.
     * \param new_area: New area of the cell
     */
    inline int SetAdhesiveArea(int new_area)
    {
        return adhesive_area = new_area;
    }

    //! \brief Get the adhesive area of a cell, used for act model.
    inline int GetAdhesiveArea() { return adhesive_area; }

    //! Return the cell type of this Cell.
    inline int getTau(void) { return tau; }

    //! Return the x-coordinate of the geometric cell center.
    inline double getCenterX(void) { return fit_ellipse.center().x; }
    //! Return the y-coordinate of the geometric cell center.
    inline double getCenterY(void) { return fit_ellipse.center().y; }

    //! Set color of this cell to new_colour, irrespective of type.
    inline int SetColour(const int new_colour) { return colour = new_colour; }

    /* \brief Returns the energy between this cell and cell2.

    Called from CellularPotts::DeltaH.
    **/
    int EnergyDifference(const Cell &cell2) const;

    //! Return Cell's actual area.
    inline int Area() const { return fit_ellipse.area(); }

    //! Return Cell's target area.
    inline int TargetArea() const { return target_area; }

    // ! Return Cell's perimeter
    inline int Perimeter() { return perimeter; }

    // ! Return Cell's target perimeter
    inline int TargetPerimeter() { return target_perimeter; }
    // ! Set Cell's target perimeter
    inline int SetTargetPerimeter(const int new_perimeter)
    {
        return target_perimeter = new_perimeter;
    }
    // ! Set Cell's perimeter
    inline int SetPerimeter(const int new_perimeter)
    {
        return perimeter = new_perimeter;
    }

    inline double TargetLength() const { return target_length; }

    //! Set the Cell's target length
    inline double SetTargetLength(double l) { return target_length = l; }

    // return the current length
    inline double Length(void) { return fit_ellipse.length(); }

    /*! \brief Clears the table of J's.

    This is only important for a
    feature called "DynamicJ's", where J-values depend on internal states
    of the cells (such as a genetic network; see e.g. Hogeweg et
    al. 2000). The current version of TST does not include such functionality.
    */
    static void ClearJ(void);

    /*! \brief Returns the maximum cell identity number in the Dish.
      This would normally be the number of cells in the Dish, although
     the number includes apoptosed cells.
    */
    static inline int MaxSigma() { return maxsigma; }

    //! Returns the cell's cell identity number.
    inline int Sigma() const { return sigma; }

    //! Sets the target area of the cell.
    inline int SetTargetArea(const int new_area)
    {
        return target_area = new_area;
    }

    //! Sends the current cell into apoptosis
    inline void Apoptose() { alive = false; }

    //! Decrement the cell's target area by one unit.
    inline int IncrementTargetArea() { return ++target_area; }
    //! Increment the cell's target area by one unit.
    inline int DecrementTargetArea() { return --target_area; }

    //! Cell lineage tracking: get the cell's parent
    inline int Mother(void) const { return mother; }

    //! Cell lineage tracking: get the cell's daughter
    inline int Daughter(void) const { return daughter; }

    //! Returns a counter keeping track of the number of divisions
    inline int TimesDivided(void) const { return times_divided; }

    //! Returns Monte Carlo Step (MCS) when this cell originated.
    inline int DateOfBirth(void) const { return date_of_birth; }

    //! Returns the cell type at the time of birth.
    inline int ColourOfBirth(void) const { return colour_of_birth; }

    //! Returns the bond energy J between this cell and cell c2.
    inline int GetJ(const Cell &c2) const { return J[sigma][c2.sigma]; }

    //! Sets bond energy J between cell type t1 and t2 to val
    inline static int SetJ(int t1, int t2, int val)
    {
        return J[t2][t1] = J[t1][t2] = val;
    }

    // Deal with gradient measurements:

    //! Set the current gradient of the cell to g. Currently not in use.
    inline double *SetGrad(double *g)
    {
        grad[0] = g[0];
        grad[1] = g[1];
        return grad;
    }

    //! Returns the cell's measured gradient. Currently not in use.
    inline const double *GetGrad(void) const { return grad; }

    //! Returns the cell's measured gradient. Currently not in use.
    inline double GradX() const { return grad[0]; }

    //! Returns the cell's measured gradient. Currently not in use.
    inline double GradY() const { return grad[1]; }

    //! Currently not in use (remove?)
    inline double *AddToGrad(double *g)
    {
        grad[0] += g[0];
        grad[1] += g[1];
        return grad;
    }

    //! Currently not in use (remove?)
    inline void ClearGrad(void)
    {
        grad[0] = 0.;
        grad[1] = 0.;
    }

    /*! After introducing a new Cell (e.g. with GrowInCell)
      call this function to set the moments and areas right.
    */
    void MeasureCellSize(Cell &c);

    //! Increments the cell's actual adhesive area by 1 unit.
    inline int IncrementAdhesiveArea(int increment)
    {
        return adhesive_area = adhesive_area + increment;
    }

    //! Decrement the cell's actual adhesive area by 1 unit.
    inline int DecrementAdhesiveArea(int decrement)
    {
        return adhesive_area = adhesive_area - decrement;
    }

public:
    /*! \brief Read a table of static Js.
      First line: number of types (including medium)
      Next lines: diagonal matrix, starting with 1 element (0 0)
      ending with n elements */
    static void ReadStaticJTable(std::string const &fname);

    // used internally by dish in "CellGrowthAndDivision"
    inline int GrowthThreshold(void) const { return growth_threshold; }

    // used internally by class CellularPotts
    inline void CleanMoments(void)
    {
        fit_ellipse.clear();
        target_area = 0;
    }
    // used internally by class CellularPotts
    inline double AddSiteToMoments(int x, int y)
    {
        fit_ellipse.add_site({x, y});
    }

    // used internally by class CellularPotts
    inline double RemoveSiteFromMoments(int x, int y)
    {
        fit_ellipse.remove_site({x, y});
    }

    // return the new length that the cell would have
    // if site (x,y) were added.
    // used internally by CellularPotts
    inline double GetNewLengthIfXYWereAdded(int x, int y)
    {
        fit_ellipse.add_site({x, y});
        auto length = fit_ellipse.length();
        fit_ellipse.remove_site({x, y});
        return length;
    }

    // return the new length that the cell would have
    // if site (x,y) were removed
    // used internally by CellularPotts
    inline double GetNewLengthIfXYWereRemoved(int x, int y)
    {
        fit_ellipse.remove_site({x, y});
        auto length = fit_ellipse.length();
        fit_ellipse.add_site({x, y});
        return length;
    }

    inline void setSigma(int nsigma) { sigma = nsigma; }

private:
    //! Increments the cell's actual area by 1 unit.
    inline int IncrementArea() { return ++area; }

    //! Decrements the cell's actual area by 1 unit.
    inline int DecrementArea() { return --area; }

    //! Sets the adhesive area of the cell.
    inline int SetReferenceAdhesiveArea(const int new_area)
    {
        return ref_adhesive_area = new_area;
    }

    //! Increments the cell's actual perimeter by 1 unit.
    inline int IncrementPerimeter() { return ++perimeter; }

    //! Decrements the cell's actual perimeter by 1 unit.
    inline int DecrementPerimeter() { return ++perimeter; }

    inline int IncrementTargetPerimeter() { return ++target_perimeter; }

    inline int DecrementTargetPerimeter() { return --target_perimeter; }

    /*! \brief Sets target area to actual area, to remove "pressure".

    This is useful when reading an initial condition from an image.
    */
    inline int SetAreaToTarget(void) { return area = target_area; }

    //! Called whenever a cell is constructed, from constructor
    void ConstructorBody(int settau = 1);
    // returns the maximum cell type index
    // (depends on Jtable)
    static int MaxTau(void) { return maxtau; }
public:
    /**
     * @brief Retrieve the midpoint of the cell as vector.
     * @return Vector with position of the cell.
     */
    Vec2<double> CenterVector() const;

    /**
     * @brief Fit an ellipse to the cell, and retrieve the minor axis of said
     * ellipse
     * @return Unit vector in the direction of minor axis of the cell.
     */
    Vec2<double> MinorAxisVector();

    /**
     * @brief Fit an ellipse to the cell, and retrieve the major axis of said
     * ellipse
     * @return Unit vector in the direction of major axis of the cell.
     */
    Vec2<double> MajorAxisVector();

    /**
     * @brief Fit an ellipse to the cell, and retrieve the size of the major
     * axis of said ellipse. (Same function as Length)
     * @return Size of majoraxis.
     */
    double MajorAxis();

    /**
     * @brief Fit an ellipse to the cell, and retrieve the size of the minor
     * axis of said ellipse. (Same function as Length)
     * @return Size of minoraxis.
     */
    double MinorAxis();

    inline void GetCentroid(double *cx, double *cy)
    {
        auto pos = fit_ellipse.center();
        *cx = pos.x;
        *cy = pos.y;
    }

protected:
    FitEllipse fit_ellipse;
    int colour;
    bool alive;
    int sigma; // cell identity, 0 if medium
    int tau;   // Cell type, when dynamicJ's are not used

    // Two dimensional (square) array of ints, containing the J's.
    double target_length;

    // Dynamically increased when cells are added to the system
    // unless a static Jtable is used (currently this is the default situation)
    static int **J;
    static int maxtau;

    // Amount: the number of Cell instantations, INCLUDING copies
    // For internal use only.
    // Reading amount is NOT the way to get the number of cells!!
    static int amount;
    static int capacity;
    static int maxsigma; // the last cell identity number given out

    // indices of mother and daughter
    // (Note: no pointers, cells may be relocated)
    int mother;
    int daughter;
    int times_divided;
    int date_of_birth;
    int colour_of_birth;

    int area;
    int target_area;
    int adhesive_area;
    int ref_adhesive_area;
    int growth_threshold;

    int perimeter;        // amount of cell's membrane
    int target_perimeter; // cell's target membrane length

    double v[2];
    int n_copies; // number of expansions of this cell
    // gradient of a chemical (to be extended to the total number chemicals)
    double grad[2];
    double *chem;
    // Raw moments of the cells
    // Are used to calculate minor and major axes
    // and center of mass
    // are locally adjusted, so axes are easily
    // and quickly calculated!
    // N.B: N is area!

    double border;

    const Dish *owner; // pointer to owner of cell
};

//#endif
