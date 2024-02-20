
#include "parameter.hpp"
#include "grid.hpp"

extern Parameter par;

Grid::Grid() {
    auto boundary_type = BoundaryType::periodic;
    if (!par.periodic_boundaries) 
        boundary_type = BoundaryType::wall;

    spinfield_.initalize(
        par.sizex,
        par.sizey,
        1,
        boundary_type
    );
}

Spin Grid::get(PixelPos coordinate) {
    return spinfield_.get(coordinate);
}

void Grid::set(PixelPos coordinate, Spin value){
    spinfield_.set(coordinate, value);
}

Neighbors Grid::neighbors(PixelPos coordinate){
    return Neighbors(coordinate);
}

