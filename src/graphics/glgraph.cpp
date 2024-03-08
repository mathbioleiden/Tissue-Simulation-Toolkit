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
#include <GL/glew.h>
#include <GL/glut.h>
#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <thread>

#include "graph.hpp"
#include "parameter.hpp"

GLGraphics *graphics_object = 0;

void static_display_func() {
  extern GLGraphics *graphics_object;
  graphics_object->TimeStepWrap();
}

void static_idle_func() { glutPostRedisplay(); }

void static_resize_func(int w, int h) {
  extern GLGraphics *graphics_object;
  graphics_object->Resize(w, h);
}

void GLGraphics::SetupBuffers() {
  glGenVertexArrays(1, &VertexArrayID);
  glBindVertexArray(VertexArrayID);

  glGenBuffers(1, &vertexbuffer);
  glEnableVertexAttribArray(posAttrib);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 0, (void *)0);

  glGenBuffers(1, &colbuffer);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glEnableVertexAttribArray(colAttrib);
  glVertexAttribPointer(colAttrib, 4, GL_FLOAT, GL_FALSE, 0, 0);

  glGenBuffers(1, &floatbuffer);
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, floatbuffer);
  glBindBufferBase(GL_SHADER_STORAGE_BUFFER, floatDataAttrib, floatbuffer);

  glGenBuffers(1, &intbuffer);
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, intbuffer);
  glBindBufferBase(GL_SHADER_STORAGE_BUFFER, intDataAttrib, intbuffer);

  glGenBuffers(1, &coltablebuffer);
  glBindBuffer(GL_UNIFORM_BUFFER, coltablebuffer);
  glBindBufferBase(GL_UNIFORM_BUFFER, colTableAttrib, coltablebuffer);
}

void GLGraphics::Draw() {
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

void GLGraphics::DrawRects() {
  glUseProgram(squares_program);
  glUniform3fv(uni_size, 1, uniform_size);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(rect) * rect_pos, rects,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(color) * rect_col_pos, rect_cols,
               GL_DYNAMIC_DRAW);
  glDrawArrays(GL_POINTS, 0, rect_col_pos);
}

void GLGraphics::DrawLines() {
  glUseProgram(basic_program);
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

void GLGraphics::DrawPoints() {
  glUseProgram(basic_program);
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

void GLGraphics::DensityPlot(float *data, int xsize, int ysize, float r,
                             float g, float b) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {r, g, b, 1, r, g, b, 1, r, g, b, 1,
                  r, g, b, 1, r, g, b, 1, r, g, b, 1};

  glUseProgram(densityplot_program);
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, floatbuffer);
  glBufferData(GL_SHADER_STORAGE_BUFFER, sizeof(float) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);

  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void GLGraphics::intPlot(int *data, int xsize, int ysize) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

  glUseProgram(intplot_program);
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);
  glBindBuffer(GL_UNIFORM_BUFFER, coltablebuffer);
  glBufferData(GL_UNIFORM_BUFFER, sizeof(colors), colors, GL_DYNAMIC_DRAW);
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, intbuffer);
  glBufferData(GL_SHADER_STORAGE_BUFFER, sizeof(int) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);

  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void GLGraphics::cpmLinePlot(int *data, int xsize, int ysize, float r, float g,
                             float b) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {r, g, b, 1, r, g, b, 1, r, g, b, 1,
                  r, g, b, 1, r, g, b, 1, r, g, b, 1};
  glUseProgram(cpmlineplot_program);
  glUniform1f(lineWidthAttrib, 0.3);
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, intbuffer);
  glBufferData(GL_SHADER_STORAGE_BUFFER, sizeof(int) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);

  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void GLGraphics::contourPlot(float *data, int xsize, int ysize, float r,
                             float g, float b) {
  float z = 0;
  float single_rect[] = {-1, 1,  z, 1, 1, z, -1, -1, z,
                         -1, -1, z, 1, 1, z, 1,  -1, z};
  float cols[] = {r, g, b, 1, r, g, b, 1, r, g, b, 1,
                  r, g, b, 1, r, g, b, 1, r, g, b, 1};

  glUseProgram(contourplot_program);
  glUniform2fv(windowSizeAttrib, 1, window_size);
  glUniform3fv(uni_size, 1, uniform_size);
  glUniform1f(lineWidthAttrib, 0.2);
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, floatbuffer);
  glBufferData(GL_SHADER_STORAGE_BUFFER, sizeof(float) * xsize * ysize, data,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(single_rect), single_rect,
               GL_DYNAMIC_DRAW);
  glBindBuffer(GL_ARRAY_BUFFER, colbuffer);
  glBufferData(GL_ARRAY_BUFFER, sizeof(cols), cols, GL_DYNAMIC_DRAW);

  glDrawArrays(GL_TRIANGLES, 0, 6);
}

void GLGraphics::make_context() {
  glutInitWindowSize(width, height);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
  glutCreateWindow("Tissue Simulation Toolkit");
  GLenum err = glewInit();
  if (err != GLEW_OK) {
    std::cout << "Failed to initialise OpenGL" << std::endl;
    exit(1);
  }
  if (!glewIsSupported("GL_VERSION_2_0")) {
    std::cout << "OpenGL 2.0 or higher is necessary" << std::endl;
    ;
    exit(1);
  }
  glEnable(GL_COLOR_MATERIAL);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
}

GLGraphics::GLGraphics(int xfield, int yfield, const char *movie_file) {
  width = xfield;
  height = yfield;
  init_size_x = xfield;
  init_size_y = yfield;
  mag = 4.;

  if (movie_file) {
    std::cout << "Movie writing is not implemented" << std::endl;
  }
  make_context();

  glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

  glutReshapeFunc(static_resize_func);
  glutIdleFunc(static_idle_func);
  glutDisplayFunc(static_display_func);

  Resize(xfield, yfield);
  ReadColorTable();
  SetupShaders();
  SetupBuffers();
}

void GLGraphics::Start() { glutMainLoop(); }

GLGraphics::~GLGraphics() {
  if (rects != 0) {
    delete[] rects;
    delete[] rect_cols;
    delete[] lines;
    delete[] line_cols;
    delete[] points;
    delete[] point_cols;
  }
}

void GLGraphics::Point(int color, int x, int y) {
  points[point_pos].x = (float)x;
  points[point_pos].y = (float)y;
  points[point_pos].z = 0.0;
  point_cols[point_pos] = colors[color];
  point_pos++;
}

void GLGraphics::PointAlpha(int alpha, int x, int y) {
  points[point_pos].x = x;
  points[point_pos].y = y;
  points[point_pos].y = 0;

  point_cols[point_pos] = colors[0];
  point_cols[point_pos].a = alpha;
  point_pos++;
}

void GLGraphics::Rectangle(int color, int x, int y) {
  rects[rect_pos].p1.x = (float)x;
  rects[rect_pos].p1.y = (float)y;
  rects[rect_pos].p1.z = 0;

  rect_pos++;
  if (color > col_num)
    color = 0;
  rect_cols[rect_col_pos] = colors[color];
  rect_col_pos++;
}

void GLGraphics::BeginScene(void) {
  rect_pos = 0;
  line_pos = 0;
  point_pos = 0;
  glViewport(0, 0, init_size_x * mag, init_size_y * mag);
}

void GLGraphics::EndScene(void) {
  Draw();
  glutSwapBuffers();
}

void GLGraphics::Line(float x1, float y1, float x2, float y2, int color) {
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

void GLGraphics::ReadColorTable() {
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
}

void GLGraphics::Arrow(int x1, int y1, int x2, int y2, int colour) {
  std::cout << "Arrows not implemented" << std::endl;
}

void GLGraphics::Resize(int xfield, int yfield) {
  extern Parameter par;
  width = xfield;
  height = yfield;

  if (xfield > yfield) {
    mag = (double)yfield / (double)init_size_y;
  } else {
    mag = (double)xfield / (double)init_size_x;
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
}

void GLGraphics::ClearImage() { glClear(GL_COLOR_BUFFER_BIT); }

void GLGraphics::TimeStepWrap(void) {
  static int t = 0;
  TimeStep();
  if (!paused)
    t++;
  extern Parameter par;
  if (t == par.mcs) {
    exit(0);
  }
}

int GLGraphics::GetXYCoo(int *X, int *Y) {
  *X = 0;
  *Y = 0;
  return 0;
}

GLuint GLGraphics::LoadShader(std::string filename, GLenum shader_type) {
  std::ifstream infile;
  infile.open(filename);
  std::stringstream source_stream;
  source_stream << infile.rdbuf();
  infile.close();
  std::string source = source_stream.str();
  const char *source_c = source.c_str();
  int size = source.size();
  GLuint shader = glCreateShader(shader_type);
  glShaderSourceARB(shader, 1, &source_c, &size);
  glCompileShaderARB(shader);
  GLint compiled;
  glGetObjectParameterivARB(shader, GL_COMPILE_STATUS, &compiled);
  if (!compiled) {
    std::cout << "Shader compile failed." << std::endl;
    GLint blen = 0;
    GLsizei slen = 0;
    glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &blen);
    if (blen > 1) {
      GLchar *compiler_log = (GLchar *)malloc(blen);
      glGetInfoLogARB(shader, blen, &slen, compiler_log);
      std::cout << "compiler_log:" << std::endl << compiler_log << std::endl;
      ;
      free(compiler_log);
    }
    return 0;
  }
  return shader;
}

int GLGraphics::LinkProgram(GLint program) {
  glLinkProgram(program);
  GLint linked;
  glGetProgramiv(program, GL_LINK_STATUS, &linked);
  if (!linked) {
    std::cout << "Failed to link program" << std::endl;
    GLint blen = 0;
    GLsizei slen = 0;
    glGetProgramiv(program, GL_INFO_LOG_LENGTH, &blen);
    if (blen > 1) {
      GLchar *linker_log = (GLchar *)malloc(blen);
      glGetInfoLogARB(program, blen, &slen, linker_log);
      std::cout << "linker_log:" << std::endl << linker_log << std::endl;
      ;
      free(linker_log);
    }
    return 0;
  }
  return 1;
}

int GLGraphics::SetupShaders() {
  GLuint basic_vert_shader =
      LoadShader("../src/graphics/shaders/basic.vert", GL_VERTEX_SHADER);
  if (!basic_vert_shader)
    exit(1);
  GLuint scaled_vert_shader =
      LoadShader("../src/graphics/shaders/scaled.vert", GL_VERTEX_SHADER);
  if (!scaled_vert_shader)
    exit(1);
  GLuint geom_shader =
      LoadShader("../src/graphics/shaders/squares.geom", GL_GEOMETRY_SHADER);
  if (!geom_shader)
    exit(1);
  GLuint frag_shader =
      LoadShader("../src/graphics/shaders/basic.frag", GL_FRAGMENT_SHADER);
  if (!frag_shader)
    exit(1);
  GLuint densityplot_shader = LoadShader(
      "../src/graphics/shaders/densityplot.frag", GL_FRAGMENT_SHADER);
  if (!densityplot_shader)
    exit(1);
  GLuint intplot_shader =
      LoadShader("../src/graphics/shaders/intplot.frag", GL_FRAGMENT_SHADER);
  if (!intplot_shader)
    exit(1);
  GLuint cpm_lineplot_shader = LoadShader(
      "../src/graphics/shaders/cpmlineplot.frag", GL_FRAGMENT_SHADER);
  if (!cpm_lineplot_shader)
    exit(1);
  GLuint contourplot_shader = LoadShader(
      "../src/graphics/shaders/contourplot.frag", GL_FRAGMENT_SHADER);
  if (!contourplot_shader)
    exit(1);

  basic_program = glCreateProgram();
  glAttachShader(basic_program, scaled_vert_shader);
  glAttachShader(basic_program, frag_shader);
  if (!LinkProgram(basic_program))
    std::cout << "Failed to link basic_program" << std::endl;

  squares_program = glCreateProgram();
  glAttachShader(squares_program, scaled_vert_shader);
  glAttachShader(squares_program, geom_shader);
  glAttachShader(squares_program, frag_shader);
  if (!LinkProgram(squares_program))
    std::cout << "Failed to link squares_program" << std::endl;

  densityplot_program = glCreateProgram();
  glAttachShader(densityplot_program, basic_vert_shader);
  glAttachShader(densityplot_program, densityplot_shader);
  if (!LinkProgram(densityplot_program))
    std::cout << "Failed to link densityplot_program" << std::endl;

  intplot_program = glCreateProgram();
  glAttachShader(intplot_program, basic_vert_shader);
  glAttachShader(intplot_program, intplot_shader);
  if (!LinkProgram(intplot_program))
    std::cout << "Failed to link intplot_program" << std::endl;

  cpmlineplot_program = glCreateProgram();
  glAttachShader(cpmlineplot_program, basic_vert_shader);
  glAttachShader(cpmlineplot_program, cpm_lineplot_shader);
  if (!LinkProgram(cpmlineplot_program))
    std::cout << "Failed to link cpmlineplot_program" << std::endl;

  contourplot_program = glCreateProgram();
  glAttachShader(contourplot_program, basic_vert_shader);
  glAttachShader(contourplot_program, contourplot_shader);
  if (!LinkProgram(contourplot_program))
    std::cout << "Failed to link contourplot_program" << std::endl;

  return 1;
}

void GLGraphics::Write(char *fname, int quality) {
  //  unsigned char * pixels = new unsigned char[width*height*4];
  //  glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE, pixels);
  //
  //  string name(fname);
  //  if (name.find("png")==string::npos) {
  //    throw("GLGraphics::Write: Sorry, only PNG writing is implemented");
  //  }
  //
  //  std::cerr << "Writing a PNG picture\n";
  //
  //  FILE *fp;
  //  fp = fopen(fname,"wb");
  //  if (fp==0) {
  //    perror(fname);
  //    throw("X11Graphics::Write: File error\n");
  //  }
  //  png_structp png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING,
  //						(png_voidp)NULL,
  //						(png_error_ptr)NULL,
  //						(png_error_ptr)NULL);
  //  png_infop info_ptr = png_create_info_struct (png_ptr);
  //  png_init_io(png_ptr, fp);
  //  png_set_IHDR(png_ptr, info_ptr, width, height,
  //	       8, PNG_COLOR_TYPE_RGB, PNG_INTERLACE_NONE,
  //	       PNG_COMPRESSION_TYPE_BASE, PNG_FILTER_TYPE_BASE);
  //  png_write_info(png_ptr,info_ptr);
  //
  //  png_write_rows(pixels, pixels + width*height*4, 1);
  //  }
  //  png_write_end(png_ptr, info_ptr);
  //  png_destroy_write_struct(&png_ptr,(png_infopp)NULL);
  //  free(png_image);
  //  fclose(fp);
}
