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
#ifndef _QTGRAPH_H_
#define _QTGRAPH_H_
#include <QWidget>
#include <qlabel.h>
#include <qpainter.h>
//#include <q3picture.h>
// #include <qpixmap.h>
#include <QPicture>
#include <QPixmap>
//Added by qt3to4:
#include <QMouseEvent>
#include <QPaintEvent>
#include <QResizeEvent>
#include "graph.h"



class QtGraphics : public QWidget, public Graphics {

  Q_OBJECT

    public:
  QtGraphics(int xfield, int yfield, const char *movie_file=0);
  QtGraphics(QWidget *parent, const char *name, int xfield, int yfield, const char *movie_file=0) : QWidget(parent, 0) {
    QtGraphics(xfield, yfield, movie_file);
      // set name here somewhere
  }
  
  virtual ~QtGraphics(void);
  virtual void BeginScene(void);
  virtual void EndScene(void);
  /*inline void Flush(void) {
    XFlush(display);
    } */
  virtual void Point( int colour, int i, int j);
  virtual void Line ( int x1, int y1,int x2,int y2,int colour );
  /*void Field (const int **r, int mag=1);
    void PlotNumber(int number, int x, int y);*/
  
  virtual int GetXYCoo(int *X,int *Y);
  /*char *ChangeTitle (const char *message);
  void RecoverTitle(void);*/
  //LineType CropSize(void);
  //Coordinate ReplaceBeast(Coordinate old_size,Coordinate new_size);
  virtual int XField(void) const {return width();}
  virtual int YField(void) const {return height();}

  virtual void Write(char *fname, int quality=-1);
  inline void ClearImage(void) {

    pixmap->fill(pens[0].color());
  }
  
  virtual void TimeStep(void);
	virtual void resizeEvent( QResizeEvent *event);
  public slots:
    void TimeStepWrap(void);

  signals:
    void SimulationDone(void);

 private:
  void paintEvent( QPaintEvent* );
  void mousePressEvent( QMouseEvent *e);
  void mouseReleaseEvent( QMouseEvent *e);
  QPainter *picture;
  QLabel *label;
  QPicture pic;
  QPen *pens;
  QTimer *timer;
  QPixmap *pixmap;
  QLabel *image;

  int mouse_x;
  int mouse_y;
	
	int init_size_x;
	int init_size_y;
	
	double mag;
  Qt::MouseButton mouse_button;

  // private methods
  void ReadColorTable(QPen *pens);
  QTimer *t;
  
  
  
};

#include <qapplication.h>
//#include <qsignal.h>

#define TIMESTEP void QtGraphics::TimeStep(void)
#endif
