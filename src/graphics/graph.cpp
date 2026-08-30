#include <iostream>

#include "graph.hpp"
#include "parameter.hpp"
#include "random.hpp"

#if defined(QTGRAPHICS) || defined(QTGLGRAPHICS)
#include <QtGlobal>
#endif

void start_graphics(int argc, char **argv) {
  extern Parameter par;
  int window_size_x = par.sizex * 2;
  int window_size_y = par.sizey * 2;

#if defined(QTGRAPHICS) || defined(QTGLGRAPHICS)
  // Select a headless Qt platform automatically for non-graphical runs,
  // while respecting an explicit user choice.
  if (!par.graphics && !qEnvironmentVariableIsSet("QT_QPA_PLATFORM"))
    qputenv("QT_QPA_PLATFORM", "minimal");
#endif

#ifdef QTGRAPHICS
  QApplication a(argc, argv);
  QtGraphics g(window_size_x, window_size_y);
  a.connect(&g, SIGNAL(SimulationDone(void)), SLOT(quit(void)));
  g.show();
  a.exec();
#endif

#ifdef GLGRAPHICS
  extern GLGraphics *graphics_object;
  glutInit(&argc, argv);
  graphics_object = new GLGraphics(window_size_x, window_size_y);
  glutMainLoop();
#endif

#ifdef QTGLGRAPHICS
  QGuiApplication app(argc, argv);
  QtGLGraphics graphics(window_size_x, window_size_y);
  graphics.show();
  app.exec();
#endif

#ifdef X11GRAPHICS
  X11Graphics g(window_size_x, window_size_y);
  int t;
  for (t = 0; t < par.mcs; t++) {
    g.TimeStep();
  }
#endif
}
