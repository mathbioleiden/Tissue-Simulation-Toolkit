#include <iostream>
#include "parameter.hpp"
#include "graph.hpp"
#include "dish.hpp"
#include "plotter.hpp"
#include "cell.hpp"   

#include "ca.hpp"
#include "pde.hpp"


Plotter::Plotter(Dish * dish_pointer , Graphics * graphics_pointer) {
  extern Parameter par;
  dish = dish_pointer;
  graphics = graphics_pointer;
#ifdef GLGRAPHICS  
  glgraphics = (GLGraphics *) graphics;
#endif
  sigma_col = new int[par.sizex*par.sizey];
}

#ifdef GLGRAPHICS

void Plotter::plotPDEDensity() {
  glgraphics->DensityPlot(dish->PDEfield->getSigma()[0][0], 
		  par.sizex, par.sizey, 
		  0, 0, 0.3);
}

void Plotter::plotCPMLines() {
  glgraphics->cpmLinePlot(dish->CPM->getSigma()[0], 
		  par.sizex, 
		  par.sizey, 
		  0, 0, 0);
}

void Plotter::plotPDEContourLines() {
  glgraphics->contourPlot(dish->PDEfield->getSigma()[0][0], 
                  par.sizex, par.sizey, 
                  0, 1.0, 0.0);
}

void Plotter::plotCPMCellTypes(){
  dish->CPM->fillCellColArr(sigma_col);
  glgraphics->intPlot(sigma_col, par.sizex, par.sizey);
}

#else

void Plotter::plotPDEDensity() {
  for (int x = 0; x < par.sizex; x++) {
    for (int y = 0; y < par.sizey; y++) {
      dish->PDEfield->plotPos(x, y, graphics, 0);
    }
  }
}

void Plotter::plotCPMLines() {
  for (int x = 0; x < par.sizex; x++) {
    for (int y = 0; y < par.sizey; y++) {
      dish->CPM->linePlotPos(x, y, graphics);
    }
  }
}

void Plotter::plotPDEContourLines() {
  dish->PDEfield->ContourPlot(graphics, 0, 7);
}

void Plotter::plotCPMCellTypes(){
   for (int x = 0; x < par.sizex; x++) {
    for (int y = 0; y < par.sizey; y++) {
      dish->CPM->plotPos(x, y, graphics);
    }
  }
}

#endif
