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
#include <fstream>
#include <iostream>

#include "parameter.hpp"
#include "qtglgraph.hpp"

QtGLGraphics::QtGLGraphics(int xfield, int yfield, const char *movie_file) {
  setSurfaceType(QWindow::OpenGLSurface);
  create();
  QSurfaceFormat format;
  format.setSamples(16);
  setFormat(format);

  width = xfield;
  height = yfield;
  init_size_x = xfield;
  init_size_y = yfield;
  if (movie_file) {
    std::cout << "Movie writing is not implemented" << std::endl;
  }

  timer = new QTimer(this);
  connect(timer, SIGNAL(timeout()), SLOT(TimeStepWrap()));
  initialise();
  resize(xfield, yfield);
}

void QtGLGraphics::initialise() {
  m_context = new QOpenGLContext(this);
  m_context->setFormat(requestedFormat());
  m_context->create();

  m_context->makeCurrent(this);
  initialiseOpenGLFunctions();
  gl_extra = new QOpenGLExtraFunctions(m_context);

  glClearColor(1, 1, 1, 1);

  int shadercode = SetupShaders();
  if (shadercode) {
    std::cout << "Failed to compile shaders." << std::endl;
    std::cout << "Failed at number: " << shadercode << std::endl;
    exit(1);
  }
  glEnable(GL_COLOR_MATERIAL);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

  SetupBuffers();
  ReadColorTable();
  timer->start();
}

void QtGLGraphics::SetupBuffers() {
  vertexarray.create();
  vertexarray.bind();

  glGenBuffers(1, &vertexbuffer);
  glEnableVertexAttribArray(posAttrib);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 0, (void *)0);

  glGenBuffers(1, &colbuffer);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glEnableVertexAttribArray(colAttrib);
  glVertexAttribPointer(colAttrib, 4, GL_FLOAT, GL_FALSE, 0, 0);

  glGenBuffers(1, &floatbuffer);
  glGenTextures(1, &floattexture);

  glGenBuffers(1, &intbuffer);
  glGenTextures(1, &inttexture);

  glGenBuffers(1, &coltablebuffer);
  glBindBuffer(GL_UNIFORM_BUFFER, coltablebuffer);
  gl_extra->glBindBufferBase(GL_UNIFORM_BUFFER, colTableAttrib, coltablebuffer);
}

void QtGLGraphics::Draw() {
  if (rect_pos > 0)
    DrawRects();
  rect_pos = 0;
  rect_col_pos = 0;
  if (point_pos > 0)
    DrawPoints();
  point_pos = 0;
  if (line_pos > 0)
    DrawLines();
  line_pos = 0;
  line_col_pos = 0;
}

void QtGLGraphics::DrawRects() {
  squares_program.bind();
  glUniform3fv(uni_size, 1, uniform_size);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(rect) * rect_pos, rects,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(color) * rect_col_pos, rect_cols,
               GL_DYNAMIC_DRAW);
  glDrawArrays(GL_POINTS, 0, rect_col_pos);
}

void QtGLGraphics::DrawLines() {
  basic_program.bind();
  glUniform3fv(uni_size, 1, uniform_size);
  glLineWidth(mag / 1.5);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(line) * line_pos, lines,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(color) * line_col_pos, line_cols,
               GL_DYNAMIC_DRAW);
  glDrawArrays(GL_LINES, 0, line_pos * 2);
}

void QtGLGraphics::DrawPoints() {
  basic_program.bind();
  glPointSize(mag);
  glUniform3fv(uni_size, 1, uniform_size);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(point) * point_pos, points,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(color) * point_pos, point_cols,
               GL_DYNAMIC_DRAW);
  glDrawArrays(GL_POINTS, 0, point_pos);
}

void QtGLGraphics::DensityPlot(float *data, int xsize, int ysize, float r,
                               float g, float b) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {r, g, b, 1, r, g, b, 1, r, g, b, 1,
                  r, g, b, 1, r, g, b, 1, r, g, b, 1};
  densityplot_program.bind();
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);

  glBindBuffer(GL_TEXTURE_BUFFER, floatbuffer);
  glBufferData(GL_TEXTURE_BUFFER, sizeof(float) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_BUFFER, floattexture);
  gl_extra->glTexBuffer(GL_TEXTURE_BUFFER, GL_R32F, floatbuffer);
  glUniform1i(floatDataAttrib, 0);

  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);
  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void QtGLGraphics::intPlot(int *data, int xsize, int ysize) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  intplot_program.bind();
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);

  glBindBuffer(GL_TEXTURE_BUFFER, intbuffer);
  glBufferData(GL_TEXTURE_BUFFER, sizeof(int) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_BUFFER, inttexture);
  gl_extra->glTexBuffer(GL_TEXTURE_BUFFER, GL_R32I, intbuffer);
  glUniform1i(intDataAttrib, 0);

  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);
  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void QtGLGraphics::cpmLinePlot(int *data, int xsize, int ysize, float r,
                               float g, float b) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {r, g, b, 1, r, g, b, 1, r, g, b, 1,
                  r, g, b, 1, r, g, b, 1, r, g, b, 1};
  cpmlineplot_program.bind();
  glUniform1f(lineWidthAttrib, 0.3);
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);

  glBindBuffer(GL_TEXTURE_BUFFER, intbuffer);
  glBufferData(GL_TEXTURE_BUFFER, sizeof(int) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_BUFFER, inttexture);
  gl_extra->glTexBuffer(GL_TEXTURE_BUFFER, GL_R32I, intbuffer);
  glUniform1i(intDataAttrib, 0);

  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);
  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void QtGLGraphics::contourPlot(float *data, int xsize, int ysize, float r,
                               float g, float b) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {r, g, b, 1, r, g, b, 1, r, g, b, 1,
                  r, g, b, 1, r, g, b, 1, r, g, b, 1};
  contourplot_program.bind();
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);
  glUniform1f(lineWidthAttrib, 0.2);

  glBindBuffer(GL_TEXTURE_BUFFER, floatbuffer);
  glBufferData(GL_TEXTURE_BUFFER, sizeof(float) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glActiveTexture(GL_TEXTURE0);
  glBindTexture(GL_TEXTURE_BUFFER, floattexture);
  gl_extra->glTexBuffer(GL_TEXTURE_BUFFER, GL_R32F, floatbuffer);
  glUniform1i(floatDataAttrib, 0);

  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);
  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void QtGLGraphics::Point(int color, int x, int y) {
  points[point_pos].x = (float)x;
  points[point_pos].y = (float)y;
  points[point_pos].z = 0.0;
  point_cols[point_pos] = colors[color];
  point_pos++;
}

void QtGLGraphics::PointAlpha(int alpha, int x, int y) {
  points[point_pos].x = x;
  points[point_pos].y = y;
  points[point_pos].y = 0;

  point_cols[point_pos] = colors[0];
  point_cols[point_pos].a = alpha;
  point_pos++;
}

void QtGLGraphics::Rectangle(int color, int x, int y) {
  rects[rect_pos].p1.x = (float)x;
  rects[rect_pos].p1.y = (float)y;
  rects[rect_pos].p1.z = 0;

  rect_pos++;
  if (color > col_num)
    color = 0;
  rect_cols[rect_col_pos] = colors[color];
  rect_col_pos++;
}

void QtGLGraphics::BeginScene(void) {
  rect_pos = 0;
  line_pos = 0;
  point_pos = 0;
}

void QtGLGraphics::EndScene(void) {
  Draw();
  m_context->swapBuffers(this);
}

void QtGLGraphics::Line(float x1, float y1, float x2, float y2, int color) {
  lines[line_pos].p1.x = x1;
  lines[line_pos].p1.y = y1;
  lines[line_pos].p1.z = 0;
  lines[line_pos].p2.x = x2;
  lines[line_pos].p2.y = y2;
  lines[line_pos].p2.z = 0;

  line_pos++;

  line_cols[line_col_pos] = colors[color];
  line_col_pos++;
  line_cols[line_col_pos] = colors[color];
  line_col_pos++;
}

void QtGLGraphics::ReadColorTable() {
  extern Parameter par;
  FILE *fpc;
  if ((fpc = fopen(par.colortable, "r")) == NULL) {
    char *message = new char[2000];
    if (message == 0) {
      throw "Memory panic in GLGraphics::ReadColorTable\n";
    }
    sprintf(message, "GLGraphics::ReadColorTable: Colormap '%s' not found.",
            par.colortable);
    throw(message);
  }
  int r, g, b, a;
  int i;
  int res = EOF;
  col_num = 0;
  while (fscanf(fpc, "%d", &i) != EOF || res == EOF) {
    res = fscanf(fpc, "%d %d %d %d\n", &r, &g, &b, &a);
    colors[i].r = (float)r / 255.0f;
    colors[i].g = (float)g / 255.0f;
    colors[i].b = (float)b / 255.0f;
    colors[i].a = (float)a / 255.0f;
    col_num++;
  }
  fclose(fpc);
  glBindBuffer(GL_UNIFORM_BUFFER, coltablebuffer);
  glBufferData(GL_UNIFORM_BUFFER, sizeof(colors), colors, GL_DYNAMIC_DRAW);
}

void QtGLGraphics::Arrow(int x1, int y1, int x2, int y2, int colour) {
  std::cout << "Arrows not implemented" << std::endl;
}

void QtGLGraphics::Resize(int w, int h) {
  extern Parameter par;
  if (w > h) {
    mag = (double)h / (double)init_size_y;
  } else {
    mag = (double)w / (double)init_size_x;
  }

  int size = par.sizex * par.sizey;
  if (rects != 0) {
    delete[] rects;
    delete[] rect_cols;
    delete[] lines;
    delete[] line_cols;
    delete[] points;
    delete[] point_cols;
  }

  rects = new rect[size * 2];
  rect_cols = new color[size * 4];
  lines = new line[size * 4];
  line_cols = new color[size * 8];
  points = new point[size * 10];
  point_cols = new color[size * 10];
  uniform_size[0] = par.sizex;
  uniform_size[1] = par.sizey;
  uniform_size[2] = 1;

  window_size[0] = init_size_x * mag;
  window_size[1] = init_size_y * mag;

  glViewport(0, 0, init_size_x * mag, init_size_y * mag);
}

void QtGLGraphics::ClearImage() { glClear(GL_COLOR_BUFFER_BIT); }

void QtGLGraphics::TimeStepWrap(void) {
  extern Parameter par;
  static int t = 0;
  TimeStep();
  if (!paused)
    t++;
  if (t == par.mcs) {
    exit(0);
  }
}

int QtGLGraphics::GetXYCoo(int *X, int *Y) {
  *X = 0;
  *Y = 0;
  return 0;
}

int QtGLGraphics::SetupShaders() {
  QOpenGLShader basic_vert_shader(QOpenGLShader::Vertex);
  if (!basic_vert_shader.compileSourceFile(
          "../src/graphics/shaders/basic.vert"))
    return 1;

  QOpenGLShader scaled_vert_shader(QOpenGLShader::Vertex);
  if (!scaled_vert_shader.compileSourceFile(
          "../src/graphics/shaders/scaled.vert"))
    return 2;

  QOpenGLShader geom_shader(QOpenGLShader::Geometry);
  if (!geom_shader.compileSourceFile("../src/graphics/shaders/squares.geom"))
    return 3;

  QOpenGLShader frag_shader(QOpenGLShader::Fragment);
  if (!frag_shader.compileSourceFile("../src/graphics/shaders/basic.frag"))
    return 4;

  QOpenGLShader densityplot_shader(QOpenGLShader::Fragment);
  if (!densityplot_shader.compileSourceFile(
          "../src/graphics/shaders/densityplot.frag"))
    return 5;

  QOpenGLShader intplot_shader(QOpenGLShader::Fragment);
  if (!intplot_shader.compileSourceFile("../src/graphics/shaders/intplot.frag"))
    return 6;

  QOpenGLShader cpm_lineplot_shader(QOpenGLShader::Fragment);
  if (!cpm_lineplot_shader.compileSourceFile(
          "../src/graphics/shaders/cpmlineplot.frag"))
    return 7;

  QOpenGLShader contourplot_shader(QOpenGLShader::Fragment);
  if (!contourplot_shader.compileSourceFile(
          "../src/graphics/shaders/contourplot.frag"))
    return 8;

  basic_program.addShader(&scaled_vert_shader);
  basic_program.addShader(&frag_shader);
  if (!basic_program.link())
    return 9;

  squares_program.addShader(&scaled_vert_shader);
  squares_program.addShader(&geom_shader);
  squares_program.addShader(&frag_shader);
  if (!squares_program.link())
    return 10;

  densityplot_program.addShader(&basic_vert_shader);
  densityplot_program.addShader(&densityplot_shader);
  if (!densityplot_program.link())
    return 11;

  intplot_program.addShader(&basic_vert_shader);
  intplot_program.addShader(&intplot_shader);
  if (!intplot_program.link())
    return 12;

  cpmlineplot_program.addShader(&basic_vert_shader);
  cpmlineplot_program.addShader(&cpm_lineplot_shader);
  if (!cpmlineplot_program.link())
    return 13;

  contourplot_program.addShader(&basic_vert_shader);
  contourplot_program.addShader(&contourplot_shader);
  if (!cpmlineplot_program.link())
    return 14;
  return 0;
}

void QtGLGraphics::resizeEvent(QResizeEvent *event) {
  qreal new_width = event->size().width();
  qreal new_height = event->size().height();
  qreal ratio = devicePixelRatio();
  Resize(new_width * ratio, new_height * ratio);
}

void QtGLGraphics::Write(char *fname, int quality) {
  std::cout << "Image writing not implemented!" << std::endl;
}
