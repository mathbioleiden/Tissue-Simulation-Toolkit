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
//#include <q3picture.h>
#include <QPicture>
#include <QPalette>
//Added by qt3to4:
#include <QMouseEvent>
#include <QPaintEvent>
#include <QImageWriter>
#ifndef Q_OS_DARWIN
#include <malloc.h>
#endif
#include <iostream>
#include <qtimer.h>
#include <qpixmap.h>
#include <qimage.h>
//#include <q3strlist.h>
#include <QResizeEvent>
#include "qtgraph.h"
#include "parameter.h"

using namespace std;
QtGraphics::QtGraphics(int xfield, int yfield, const char *movie_file)
{
	mag = 1.;
	if (movie_file) {
    throw("QtGraphics in qtgraph.cc: Sorry, movie writing not (yet) implemented\n");
  }
  resize( xfield * mag, yfield  * mag);
	init_size_x = xfield;
	init_size_y = yfield;

  //Instead of painting in the window,
  //we choose to output to the QPicture
  //object:
  //picture->begin( &pic );
  //We draw a rectangle. Not to the screen,
  //but to the QPicture object:
  //picture->drawRect( 20, 20, 160, 160 );
  //picture->end();
  
  //Save what has been drawn to the QPicture
  //object to a file, called file.pic. When
  //you have run this program, a file with this
  //name will be created (in the directory which
  //this program is located in).
  //  pic.save( "file.png" );
  
  // Allocate colors
  pens = new QPen[256];
	
  
  ReadColorTable(pens);
 
	// Set background color of widget (i.e. the color outside the Pixmap that
	// will be shown after resizing the window)
	QPalette pal = palette();
	pal.setColor(backgroundRole(), pens[0].color());
	setPalette(pal);
	
  timer = new QTimer( this );
  connect( timer, SIGNAL(timeout()), SLOT(TimeStepWrap()) );
  timer->start( 0 );
  

  mouse_button=Qt::NoButton;
  // changed by RM for porting to Win Qt4
	pixmap=new QPixmap(xfield,yfield);
  //pixmap->fill(pens[0].color());
	//ClearImage();
	picture=new QPainter();
}

QtGraphics::~QtGraphics() {
  delete picture;
  //delete paint2;
  delete pixmap;
}

void QtGraphics::Point(int colour, int i, int j) {

  picture->setPen( pens[colour] );
  picture->drawPoint( i, j);

}

void QtGraphics::BeginScene(void) {

  picture->begin(pixmap);
	//picture->scale(mag);
}

void QtGraphics::EndScene(void) {
  
  picture->end();
  update();
}

void QtGraphics::Line( int x1, int y1,int x2,int y2,int colour ) {
  picture->setPen( pens[colour] );
  picture->drawLine( x1, y1, x2, y2);
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
void QtGraphics::paintEvent( QPaintEvent* )
{
//  bitBlt(this, 0, 0, pixmap);
	QPainter win(this);
	win.scale(mag,mag);
	win.drawPixmap(QPoint(0,0),*pixmap);  
  //painter.drawPixmap(QRect(0,0,
}

void QtGraphics::mousePressEvent( QMouseEvent *e) {
  mouse_x=e->x();
  mouse_y=e->y();
  mouse_button=e->button();
}

void QtGraphics::mouseReleaseEvent( QMouseEvent *) {
  mouse_button=Qt::NoButton;
}

void QtGraphics::TimeStepWrap(void) {
  
  //  picture->begin(pixmap);
  static int t=0;
  TimeStep();
  t++;
  // check number of timesteps
  extern Parameter par;
  if (t==par.mcs) {
    emit SimulationDone();
  }
  //picture->end();
}

int QtGraphics::GetXYCoo(int *X, int *Y)
{
  *X = mouse_x;
  *Y = mouse_y;
  switch (mouse_button) {
  
  case Qt::LeftButton:
    return 1;
    break;
  case Qt::MidButton:
    return 2;
    break;
  case Qt::RightButton:
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
  
    // replay the picture on image
    // and write it to fname
  QString imname(fname);
  
  // Get file extension to infer desired image format
  QString extension_str = imname.section( '.', -1).toUpper();
    const char *extension = extension_str.toLocal8Bit().constData();
  //cerr << "Extension is: " << extension << "\n";
  if (pixmap->save(imname,extension,quality)) {
    cerr << "Image " << imname.toLocal8Bit().constData() << " was succesfully written.\n";
  } else {
    cerr << "Image " << imname.toLocal8Bit().constData() << " could not be written.\n";
    QList< QByteArray > fmt = QImageWriter::supportedImageFormats();
    cerr << "Please choose one of the following formats: ";
      for (QList< QByteArray >::ConstIterator f=fmt.begin(); f!=fmt.end(); f++) {
      cerr << f->constData() << " ";
    }
    cerr << "\n";
  } 
}
  
void QtGraphics::resizeEvent(QResizeEvent *event) {
	qreal old_width=event->oldSize().width();
	qreal old_heigth=event->oldSize().height();	
	qreal new_width=event->size().width(); 
	qreal new_height=event->size().height();
	
	if (new_width > new_height) {
		mag = (double)new_height / (double)init_size_y;
	} else {
		mag = (double)new_width / (double)init_size_x;
	}
	
	
}
