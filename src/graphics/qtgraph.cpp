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
#include <QImageWriter>
#include <QMouseEvent>
#include <QPaintEvent>
#include <QPalette>
#include <QPicture>
#include <qapplication.h>
#include <qlabel.h>
#include <qpainter.h>
#include <qwidget.h>
#ifndef Q_OS_DARWIN
#include <malloc.h>
#endif
#include "parameter.hpp"
#include "qtgraph.hpp"
#include <QResizeEvent>
#include <iostream>
#include <qimage.h>
#include <qpixmap.h>
#include <qtimer.h>

using namespace std;
QtGraphics::QtGraphics(int xfield, int yfield, const char *movie_file) {
  mag = 1.;
  if (movie_file) {
    throw("QtGraphics in qtgraph.cc: Sorry, movie writing not (yet) "
          "implemented\n");
  }
  Resize(xfield, yfield);

  // Save what has been drawn to the QPicture
  // object to a file, called file.pic. When
  // you have run this program, a file with this
  // name will be created (in the directory which
  // this program is located in).
  //   pic.save( "file.png" );

  // Allocate colors
  pens = new QPen[256];

  ReadColorTable(pens);

  // Set background color of widget (i.e. the color outside the Pixmap that
  // will be shown after resizing the window)
  QPalette pal = palette();
  pal.setColor(backgroundRole(), pens[0].color());
  setPalette(pal);

  timer = new QTimer(this);
  connect(timer, SIGNAL(timeout()), SLOT(TimeStepWrap()));
  timer->start(0);

  mouse_button = Qt::NoButton;
  pixmap = new QPixmap(xfield, yfield);
  picture = new QPainter();
  key = -1;
}

QtGraphics::~QtGraphics() {
  // cout << "DESTROY WIDGET\n";
  delete picture;
  // delete paint2;
  delete pixmap;
}

void QtGraphics::Point(int colour, int i, int j) {
  picture->setPen(pens[colour]);
  picture->drawPoint(i, j);
}

void QtGraphics::PointAlpha(int alpha, int i, int j) {
  picture->setPen(QPen(QColor(0, 0, 0, alpha)));
  picture->drawPoint(i, j);
}

void QtGraphics::Rectangle(int colour, int i, int j) {

  if (colour > col_num)
    return;
  picture->fillRect(QRect(i * 2, j * 2, 2, 2), pens[colour].color());
}

void QtGraphics::BeginScene(void) {
  picture->begin(pixmap);
  // picture->scale(mag);
}

void QtGraphics::EndScene(void) {
  picture->end();
  update();
}

void QtGraphics::Line(float x1, float y1, float x2, float y2, int colour) {
  picture->setPen(pens[colour]);
  picture->drawLine(x1 * 2, y1 * 2, x2 * 2, y2 * 2);
}

void QtGraphics::ReadColorTable(QPen *pens) {
  extern Parameter par;
  FILE *fpc;
  if ((fpc = fopen(par.colortable.c_str(), "r")) == NULL) {
    char *message = new char[2000];
    if (message == 0) {
      throw "Memory panic in QtGraphics::ReadColorTable\n";
    }
    sprintf(message, "QtGraphics::ReadColorTable: Colormap '%s' not found.",
            par.colortable.c_str());
    throw(message);
  }
  int r, g, b, a;
  int i;
  int res = EOF;
  col_num = 0;
  while (fscanf(fpc, "%d", &i) != EOF || res == EOF) {
    res = fscanf(fpc, "%d %d %d %d\n", &r, &g, &b, &a);
    QPen p(QColor(r, g, b, a));
    pens[i] = p;
    col_num++;
  }
  fclose(fpc);
}

void QtGraphics::Arrow(int x1, int y1, int x2, int y2, int colour) {
  picture->setPen(pens[colour]);
  picture->drawLine(x1, y1, x2, y2);
  int b1 = (int)2 * sqrt(2) * (x1 - x2 - y1 + y2) /
           ((sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))));
  int b2 = (int)2 * sqrt(2) * (x1 - x2 + y1 - y2) /
           ((sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))));
  int c1 = (int)2 * sqrt(2) * (x1 - x2 + y1 - y2) /
           ((sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))));
  int c2 = (int)2 * sqrt(2) * (-x1 + x2 + y1 - y2) /
           ((sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))));
  picture->drawLine(x2, y2, x2 + b1, y2 + b2);
  picture->drawLine(x2, y2, x2 + c1, y2 + c2);
}

void QtGraphics::Resize(int xfield, int yfield) {
  resize(xfield * mag, yfield * mag);
  init_size_x = xfield;
  init_size_y = yfield;

  if (xfield > yfield) {
    mag = (double)yfield / (double)init_size_y;
  } else {
    mag = (double)xfield / (double)init_size_x;
  }
  pixmap = new QPixmap(xfield, yfield);
}

// Of course, we also want to see the image
// on screen. This is taken care of by the
void QtGraphics::paintEvent(QPaintEvent *) {
  QPainter win(this);
  win.scale(mag, mag);
  win.drawPixmap(QPoint(0, 0), *pixmap);
}

void QtGraphics::mousePressEvent(QMouseEvent *e) {
  mouse_x = e->pos().x();
  mouse_y = e->pos().y();
  mouse_button = e->button();
}

void QtGraphics::mouseReleaseEvent(QMouseEvent *) {
  mouse_button = Qt::NoButton;
}

void QtGraphics::keyPressEvent(QKeyEvent *e) { key = e->key(); }

void QtGraphics::keyReleaseEvent(QKeyEvent *e) { key = -1; }

void QtGraphics::TimeStepWrap(void) {
  static int t = 0;
  TimeStep();
  if (!paused)
    t++;
  // check number of timesteps
  extern Parameter par;
  if (t == par.mcs) {
    emit SimulationDone();
  }
}

int QtGraphics::GetXYCoo(int *X, int *Y) {
  *X = mouse_x;
  *Y = mouse_y;
  if (mouse_button != Qt::NoButton) {
    switch (mouse_button) {
    case Qt::LeftButton:
      return 1;
      break;
    case Qt::MiddleButton:
      return 2;
      break;
    case Qt::RightButton:
      return 3;
      break;
    default:
      return 0;
      break;
    }
  }
  if (key != Qt::Key_No) {
    return key;
  }
  return 0;
}

void QtGraphics::Write(char *fname, int quality) {
  if (fname == 0) {
    throw("QtGraphics::Write: empty filename!\n");
  }
  // replay the picture on image
  // and write it to fname
  QString imname(fname);

  // Get file extension to infer desired image format
  QString extension_str = imname.section('.', -1).toUpper();
  const char *extension = extension_str.toLocal8Bit().constData();
  // cerr << "Extension is: " << extension << "\n";
  if (pixmap->save(imname, extension, quality)) {
    cerr << "Image " << imname.toLocal8Bit().constData()
         << " was succesfully written.\n";
  } else {
    cerr << "Image " << imname.toLocal8Bit().constData()
         << " could not be written.\n";
    QList<QByteArray> fmt = QImageWriter::supportedImageFormats();
    cerr << "Please choose one of the following formats: ";
    for (QList<QByteArray>::ConstIterator f = fmt.begin(); f != fmt.end();
         f++) {
      cerr << f->constData() << " ";
    }
    cerr << "\n";
  }
}

void QtGraphics::resizeEvent(QResizeEvent *event) {
  qreal new_width = event->size().width();
  qreal new_height = event->size().height();
  if (new_width > new_height) {
    mag = (double)new_height / (double)init_size_y;
  } else {
    mag = (double)new_width / (double)init_size_x;
  }
}
