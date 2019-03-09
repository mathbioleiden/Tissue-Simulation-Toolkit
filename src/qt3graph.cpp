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
#include <qapplication.h>
#include <qwidget.h>
#include <qlabel.h>
#include <qpainter.h>
#include <qpicture.h>
#include <malloc.h>
#include <iostream>
#include <qtimer.h>
#include <qpixmap.h>
#include <qimage.h>
#include <qstrlist.h>
#include "qtgraph.h"
#include "parameter.h"


using namespace std;
QtGraphics::QtGraphics(int xfield, int yfield, const char *movie_file)
{
  if (movie_file) {
    throw("QtGraphics in qtgraph.cc: Sorry, movie writing not (yet) implemented\n");
  }
  resize( xfield, yfield );
  
 
  //Instead of painting in the window,
  //we choose to output to the QPicture
  //object:
  //paint->begin( &pic );
  //We draw a rectangle. Not to the screen,
  //but to the QPicture object:
  //paint->drawRect( 20, 20, 160, 160 );
  //paint->end();
  
  //Save what has been drawn to the QPicture
  //object to a file, called file.pic. When
  //you have run this program, a file with this
  //name will be created (in the directory which
  //this program is located in).
  //  pic.save( "file.png" );
  
  // Allocate colors
  pens = new QPen[256];

  
  ReadColorTable(pens);
 
  timer = new QTimer( this );
  connect( timer, SIGNAL(timeout()), SLOT(TimeStepWrap()) );
  timer->start( 0 );
  
  paint=new QPainter();
  paint2=new QPainter();
  mouse_button=NoButton;
  pixmap=new QPixmap(width(),height(),-1,QPixmap::BestOptim);
  pixmap->fill();
 
}

QtGraphics::~QtGraphics() {
  delete paint;
  delete paint2;
  delete pixmap;
}

void QtGraphics::Point(int colour, int i, int j) {

  paint->setPen( pens[colour] );
  paint->drawPoint( i, j);

}

void QtGraphics::BeginScene(void) {

  paint->begin(pixmap);

}

void QtGraphics::EndScene(void) {
  
  paint->end();
  paintEvent(0);

}

void QtGraphics::Line( int x1, int y1,int x2,int y2,int colour ) {
  paint->setPen( pens[colour] );
  paint->drawLine( x1, y1, x2, y2);
}


void QtGraphics::ReadColorTable(QPen *pens)
{
  
  char name[50];
  sprintf(name,"default.ctb");
   
  FILE *fpc;
  if ((fpc = fopen(name,"r")) == NULL) {
     
    char *message=new char[2000];
    if (message==0) {
      throw "Memory panic in QtGraphics::ReadColorTable\n";
    }
     
    sprintf(message,"QtGraphics::ReadColorTable: Colormap '%s' not found.",name);
     
    throw(message);
     
  }
   
  int r,g,b;
  int i;
  while (fscanf(fpc,"%d",&i) != EOF) {
    fscanf(fpc,"%d %d %d\n",&r,&g,&b);
    QPen p(QColor(r,g,b));
    pens[i]=p;
  }
   
  fclose(fpc);

}

//Of course, we also want to see the image
//on screen. This is taken care of by the
//paintEvent() function:
void QtGraphics::paintEvent( QPaintEvent* )
{
  bitBlt(this, 0, 0, pixmap);
    
}

void QtGraphics::mousePressEvent( QMouseEvent *e) {
  mouse_x=e->x();
  mouse_y=e->y();
  mouse_button=e->button();
}

void QtGraphics::mouseReleaseEvent( QMouseEvent *) {
  mouse_button=NoButton;
}

void QtGraphics::TimeStepWrap(void) {
  
  //  paint->begin(pixmap);
  static int t=0;
  TimeStep();
  t++;
  // check number of timesteps
  extern Parameter par;
  if (t==par.mcs) {
    emit SimulationDone();
  }
  //paint->end();
}

int QtGraphics::GetXYCoo(int *X, int *Y)
{
  *X = mouse_x;
  *Y = mouse_y;
  switch (mouse_button) {
  
  case LeftButton:
    return 1;
    break;
  case MidButton:
    return 2;
    break;
  case RightButton:
    return 3;
    break;
  default:
    return 0;
    break;
  }
  return 0;
}

void QtGraphics::Write(char *fname, int quality) {
  
  if (fname==0) {

    throw("QtGraphics::Write: empty filename!\n");
  }
  
  cerr << "Entering Write\n";
  //timer->stop();
  // QPixmap is a paint device
  //QPixmap image(width(),height());
  //image.fill();

  // replay the picture on image
  //paint->end(); // Write might be called from within a TimeStep event
  // and write it to fname
  QString imname(fname);
  
  // Get file extension to infer desired image format
  QString extension = imname.section( '.', -1).upper();
  
  cerr << "Extension is: " << extension << "\n";
  if (pixmap->save(imname,extension,quality)) {
    cerr << "Image " << imname << " was succesfully written.\n";
  } else {
    cerr << "Image " << imname << " could not be written.\n";
    QStrList fmt = QImage::outputFormats();
    cerr << "Please choose one of the following formats: ";
    for (const char* f = fmt.first(); f; f = fmt.next()) {
      cerr << f << " ";
    }
    cerr << "\n";
  } 
}
  

