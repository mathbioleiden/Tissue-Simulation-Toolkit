#include "dish.hpp"
#include "graph.hpp"

class Plotter {
public:
  Plotter(Dish *dish_pointer, Graphics *graphics_pointer);
  void Plot();

  void SetPDEDensityLayer(int layer);
  void SetPDEContourLayer(int layer);

private:
  void plotCPMCellTypes();
  void plotPDEDensity();
  void plotCPMLines();
  void plotPDEContourLines();

  Dish *dish;
  Graphics *graphics;

  int pde_density_layer = 0;
  int pde_contour_layer = 0;

#ifdef GLGRAPHICS
  GLGraphics *glgraphics;
#endif
#ifdef QTGLGRAPHICS
  QtGLGraphics *glgraphics;
#endif
  int *sigma_col;
};
