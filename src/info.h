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

/*! \class Info
  \brief Enables interactive querying of the simulation.
  
  Only using key presses, to be defined in Info::Menu().

  Right-click menu in future Qt-linked versions?
*/

class Graphics;
class Dish;
//class ostream;

class Info {

public:
  
  /*! \brief Constructs and Info class dish with specified graphics window.

  \param dish: The virtual Petri dish to query.
  \param graphics: The Graphics window displaying the dish.
  \param out: (optional) Stream into which info is written. Default: console.
  */
  Info(Dish &dish, Graphics &graphics, std::ostream &out=std::cout);
  
  /*! \brief Reads out key presses in the Graphics window and interprets them.
    
  If you want to define extra interactive queries, redefine this method.

  If you want a nice GUI menu, reimplement this method.
  */
  void Menu(void);
  
  /*! \brief Writes center of mass of cell "cell_id" to stream out.
   */
  void WriteCOM(int cell_id, std::ostream &out=std::cout);

  /*! \brief Waits until the user clicks a cell and returns a reference to it.
   */
  Cell &ClickCell(Graphics *g);
  
private:
  Info(void);


private:
  Graphics *graphics;
  Dish *dish;
  std::ostream *os;
};
