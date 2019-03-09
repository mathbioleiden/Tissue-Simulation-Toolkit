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

/*! \class Graphics 

\brief API for Graphics windows. 

No implementation here. Implemented by X11Graphics and QtGraphics.

*/
#ifndef _GRAPH_H_
#define _GRAPH_H_
#include <iostream>
// Base class for Graphics interface. No implementation

class Graphics {

 public:
  //  Graphics(int xfield, int yfield, const char *movie_file=0);
  virtual ~Graphics(void) {};
  
  //! \brief BeginScene() must be called before calling drawing functions.
  virtual void BeginScene(void) {
  };
  //! \brief EndScene() must be called to flush the drawing buffer and display the scene.
  virtual void EndScene(void) {
  };
  /*! \brief Plot a point in the Graphics window.

  \param color: Color index, as defined in colormap file "default.ctb", which should be in the same directory as the executable.
  \param x,y: Coordinate of point, in Graphics coordinates (typically twice as large as the cellular automata coordinates). 
  */
  virtual void Point( int color, int x, int y)=0;
  
  /*! \brief Draws a line (obviously... :-)
    
  \param x1, y1: First coordinate pair.
  \param x2, y2: Second coordinate pair.
  \param color: Color of the line, as given in the colormap file "default.ctb".
  */
  virtual void Line(int x1, int y1,int x2,int y2,int colour )=0;
  
  /*! \brief Probes the Window for user interaction, with mouse or keyboard.
    
  This function should return immediately, and return 0 if there was no user interaction.
  
  \param *X, *Y: Pointer where the clicked coordinate will be stored.
 
  */
  virtual int GetXYCoo(int *X,int *Y)=0;// {return 0;}
  
  //! \brief Returns the width of the Graphics window, in pixels.
  virtual int XField(void) const {return 0;}
  
  //! \brief Returns the height of the Graphics window, in pixels.
  virtual int YField(void) const {return 0;}
  
  /*! \brief Writes the Image to a file.

  File format is inferred from file extension. Currently only PNG is
  supported by the X-Windows implementation; the Qt-implentation
  supports all formats supported by Qt. 
  
  \param fname: File name with standard image file extension (e.g. png).
  \param quality: Quality of JPEG images, defaults to -1 (no value provided).
  */
  virtual void Write(char *fname, int quality=-1)=0;

  /*! \brief Implement this member function in your simulation code.
    
  Include all actions that should be carried out during a simulation
  step, including PDE and CPM simulation steps. See the included examples (vessel.cpp, sorting.cpp) for more information. 
  */
  virtual void TimeStep(void) {};
  
  /*! \brief Plots a field of values given by **f, using color coding
    given by colormap file.

  Only implemented in X11Graphics. No checks. Usage not recommended.

  \param f: Double pointer to array of integers, giving color indices
  using standard colormap ('default.ctb').
  \param mag: magnification factor.
  */
  virtual void Field(const int **f, int mag=1) {
    throw "Graphics::Field not implemented. Try X11 graphics.\n";
  }
  
};


#endif

