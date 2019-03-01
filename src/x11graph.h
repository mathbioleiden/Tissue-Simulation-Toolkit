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

/*! \class X11Graphics

\brief X-Windows implementation of Graphics interface. 

For API see documentation of base class Graphics.

Has a number extra features: see below.
*/


#ifndef _XGRAPH_H_
#define _XGRAPH_H_

#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <X11/keysym.h>
#include <X11/cursorfont.h>
#include "graph.h"

// Shared memory extensions

#ifdef USE_XSHM
#include <sys/ipc.h>
#include <sys/shm.h>
#include <X11/extensions/XShm.h>
#endif

//


#define OUTFILE "beestje.mov"
#define CFILE "sticky.ctb"

#define VERBOSE 1
#define RESIZE -20
#define MOTION -21


typedef struct li {
  
  int x1;
  int y1;
  int x2;
  int y2;

} LineType;

typedef struct co {
  long x;
  long y;
} Coordinate;


class X11Graphics : public Graphics {

public:
  X11Graphics(int xfield, int yfield, const char *movie_file=0);
  virtual ~X11Graphics(void);
  virtual void BeginScene(void);
  virtual void EndScene(void);

  //! \brief Flushes scene to window. Normally called by EndScene().
  inline void Flush(void) {
    XFlush(display);
  }

  virtual void Point( int color, int x, int y);
  virtual void Line ( int x1, int y1,int x2,int y2,int colour );
  void Field (const int **r, int mag=1);

  virtual int GetXYCoo(int *X,int *Y);
  
  /*! \brief Changes the title bar of the Graphics window.

  \param message: Text to display in title bar.
  */
  char *ChangeTitle (const char *message);

  
  //! \brief Recovers the title prior to the last call of ChangeTitle().
  void RecoverTitle(void);
  
  /*! \brief Returns the upper left and lower right coordinates of the area occupied by cells. 
    
  \return Bounding box as a LineType structure {int x1,int y1,int x2,int y2}.
  
  Warning: Assumes the window only displays cells (i.e. no PDE fields
  etc.). If you need this, better implement it as a member function of
  class CellularPotts.
  */
  LineType CropSize(void);
  
  /*! \brief This member function was part of functionality that
    enables interactive resizing of the Window and CPM field, and
    followed by interactive replacement of the Dish's contents. The
    current version of CPM does not contain such functionality.
  */

Coordinate ReplaceBeast(Coordinate old_size,Coordinate new_size); 

virtual inline int XField(void) const {return xfield;} 

virtual inline int YField(void) const {return yfield;} 

virtual void Write(char *fname, int quality=-1); 

/*! \brief Clears all pixels in the Image. 
  
*/
inline void ClearImage(void) {

    for (int x=0;x<xfield;x++) {
	for (int y=0;y<yfield;y++) {
	  Point(0,x,y);
	}
    }
  }
  virtual void TimeStep(void); 
private:
  void InitGraphics(int xfield, int yfield);
  void CloseGraphics();
  void InitStore(void);
  int DetectControl();
  void StoreCompPict(void);
  void SendScene();
  void receiveScene(int machineindex, int beastindex, int ndish);
  void receiveScene1(int machineindex, int beastindex, int ndish);
  void KillCell(struct creature *beast);
  int ResizeField(struct creature *beast);
  void ReceiveScene(int machineindex, int beastindex, int ndish);
  void ReceiveScene1(int machineindex, int beastindex, int ndish);
  void ReadColorTable(XColor *colors);
  void MakeColorMap();
  int XExposep();
  int GetHeight(Window w);
  // Data members
  int LineClearP(char direction, int pos, int cropcol=0);
  void Resize(void);
  
private:

#ifdef USE_XSHM
  int shm=0;
  XShmSegmentInfo shminfo;
#endif
  unsigned char *film;
  long count;
  int xfield,yfield;
  int dosendscene;
  /* int divided=0; */

  int hsize,vsize;
  char *title;
  Display *display;
  char *server;
  Window window;
  XImage *image;
  GC windowGC;
  XEvent event;
  XSizeHints hint;
  XWindowAttributes attributes;
  XSetWindowAttributes setattributes;
  int screen;
  int colourclass,color_screen;
  int depth;
  Visual *visual;
  unsigned long white, black, foreground, background;
  XColor *colors;
  Colormap new_colormap;
  char *image_data;
  unsigned char *movie_data;
  char *movie_file_name;
  bool compressed_movie_p;
  FILE *movie_fp;
  
  bool store;

  char *old_window_name;

  int pseudoCol8;
  XVisualInfo visual_info;
  XVisualInfo *visual_list;


};
#define TIMESTEP void X11Graphics::TimeStep(void)
#endif
