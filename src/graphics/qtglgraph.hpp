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

#ifndef _QTGLGRAPH_H_
#define _QTGLGRAPH_H_

#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>
#include <QOpenGLVertexArrayObject>
#include <QtOpenGL>

#include "graph.hpp"

struct color {
  float r;
  float g;
  float b;
  float a;
};

struct point {
  float x;
  float y;
  float z;
};

struct rect {
  point p1;
};

struct line {
  point p1;
  point p2;
};

class QtGLGraphics : public QWindow,
                     protected QOpenGLFunctions,
                     public Graphics {

  Q_OBJECT

public:
  QtGLGraphics(int xfield, int yfield, const char *movie_file = 0);
  QtGLGraphics(const char *name, int xfield, int yfield);

  void initialise();

  virtual void BeginScene(void);
  virtual void EndScene(void);

  virtual void Point(int colour, int i, int j);
  virtual void Line(float x1, float y1, float x2, float y2, int colour);

  virtual void PointAlpha(int alpha, int i, int j);
  virtual void Rectangle(int color, int x, int y);
  virtual void Arrow(int x1, int y1, int x2, int y2, int colour);

  void DensityPlot(float *data, int xsize, int ysize, float r, float g,
                   float b);
  void intPlot(int *data, int xsize, int ysize);
  void cpmLinePlot(int *data, int xsize, int ysize, float r, float g, float b);
  void contourPlot(float *data, int xsize, int ysize, float r, float g,
                   float b);

  virtual int GetXYCoo(int *X, int *Y);

  virtual int XField(void) const { return width; }
  virtual int YField(void) const { return height; }

  virtual void Write(char *fname, int quality = -1);
  virtual void ClearImage(void);

  virtual void Resize(int xfield, int yfield);

  virtual void resizeEvent(QResizeEvent *event);

  virtual void set_Paused() { paused = true; }
  virtual void set_unPaused() { paused = false; }

  virtual void TimeStep();

  void SimulationDone();

  void Draw();

public slots:
  void TimeStepWrap();

  // protected:
  // bool event(QEvent *event) override;
  // void exposeEvent(QExposeEvent *event) override;

private:
  QOpenGLContext *m_context = nullptr;
  QOpenGLPaintDevice *m_device = nullptr;
  QOpenGLExtraFunctions *gl_extra;
  QTimer *timer;

  int mouse_x;
  int mouse_y;

  int init_size_x;
  int init_size_y;

  int width;
  int height;

  int key;

  float uniform_size[3];
  float window_size[2];

  QOpenGLVertexArrayObject vertexarray;

  GLuint vertexbuffer;
  GLuint colbuffer;
  GLuint floatbuffer;
  GLuint floattexture;
  GLuint intbuffer;
  GLuint inttexture;
  GLuint coltablebuffer;

  QOpenGLShaderProgram basic_program;
  QOpenGLShaderProgram squares_program;
  QOpenGLShaderProgram densityplot_program;
  QOpenGLShaderProgram intplot_program;
  QOpenGLShaderProgram cpmlineplot_program;
  QOpenGLShaderProgram contourplot_program;

  GLint posAttrib = 1;
  GLint uni_size = 2;
  GLint colAttrib = 3;
  GLint floatDataAttrib = 5;
  GLint windowSizeAttrib = 6;
  GLint intDataAttrib = 7;
  GLint colTableAttrib = 8;
  GLint lineWidthAttrib = 9;

  int rect_pos = 0;
  rect *rects = 0;
  int rect_col_pos = 0;
  color *rect_cols = 0;
  int line_pos = 0;
  line *lines = 0;
  int line_col_pos = 0;
  color *line_cols = 0;
  int point_pos = 0;
  point *points = 0;
  color *point_cols = 0;

  color colors[300];
  // QColor colors[300];
  int col_num;
  bool paused = false;
  double mag;

  void ReadColorTable();
  void SetupBuffers();
  int LinkProgram(GLint program);

  void DrawRects();
  void DrawLines();
  void DrawPoints();

  GLuint LoadShader(std::string filename, GLenum shader_type);
  int SetupShaders();
};

extern QtGLGraphics *graphics_object;

#define TIMESTEP void QtGLGraphics::TimeStep(void)

#endif
