#include "dish.hpp"
#include "graph.hpp"
#include "glgraph.hpp"

class Plotter {
  public:
    Plotter(Dish * dish_pointer, Graphics * graphics_pointer);
    void Plot();
  private:
    void plotCPMCellTypes();
    void plotPDEDensity();
    void plotCPMLines();
    void plotPDEContourLines();

    Dish * dish;
    Graphics * graphics;
    GLGraphics * glgraphics;

    int * sigma_col;
};
