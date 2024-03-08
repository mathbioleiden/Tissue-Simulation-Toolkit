#include "dish.hpp"
#include "graph.hpp"

class Plotter {
  public:
    Plotter(Dish * dish_pointer, Graphics * graphics_pointer);
    void Plot();
  private:
    void plotCPMCellTypes();
    void plotPDEDensity();
    void plotCPMLines();
    void plotPDEContourLines();
    void plotActModel();

    Dish * dish;
    Graphics * graphics;

#ifdef GLGRAPHICS
  GLGraphics *glgraphics;
#endif
#ifdef QTGLGRAPHICS
  QtGLGraphics *glgraphics;
#endif
  int *sigma_col;
};
