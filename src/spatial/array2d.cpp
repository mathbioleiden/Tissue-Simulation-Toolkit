#include "array2d.hpp"

/// Takes care of the mapping of coordinates based on type of boundary
Vec2<int> map_coordinate_torus(Vec2<int> coordinate, int sizex, int sizey) {
  while (coordinate.x < 0)
    coordinate.x += sizex;
  while (coordinate.x > sizex)
    coordinate.x -= sizex;
  while (coordinate.y < 0)
    coordinate.y += sizey;
  while (coordinate.y > sizey)
    coordinate.y -= sizey;
  return coordinate;
}

template <typename DataType>
Array2d<DataType>::Array2d(int sizex, int sizey)
    : Array2d<DataType>(sizex, sizey, 1, BoundaryType::wall) {}

template <typename DataType>
Array2d<DataType>::Array2d(int sizex, int sizey, int layers)
    : Array2d<DataType>(sizex, sizey, layers, BoundaryType::wall) {}

template <typename DataType>
Array2d<DataType>::Array2d(int sizex, int sizey, BoundaryType boundary_type)
    : Array2d<DataType>(sizex, sizey, 1, boundary_type) {}

template <typename DataType>
Array2d<DataType>::Array2d(int sizex, int sizey, int layers,
                           BoundaryType boundary_type)
    : sizex_(sizex), sizey_(sizey), layers_(layers),
      boundary_type_(boundary_type), data_(sizex * sizey * layers) {}

template <typename DataType>
void Array2d<DataType>::initialise(int sizex, int sizey, int layers,
                                   BoundaryType boundary_type) {
  sizex_ = sizex;
  sizey_ = sizey;
  layers_ = layers;
  boundary_type_ = boundary_type;
  data_.clear();
  for (int i = 0; i < sizex_ * sizey_ * layers_; i++)
    data_.push_back(DataType());
}

template <typename DataType>
DataType Array2d<DataType>::get(Vec2<int> coordinate) const {
  return get(coordinate, 0);
}

template <typename DataType>
DataType Array2d<DataType>::get(Vec2<int> coordinate, int layer) const {

  if (layer < 0 or layer >= layers_) {
    throw std::out_of_range("Layer argument is out of range.");
  }
  if ((boundary_type_ == BoundaryType::wall) &&
      (coordinate.x < 0 || coordinate.x > sizex_ || coordinate.y < 0 ||
       coordinate.y > sizey_))
    return -1;
  auto mapped_coordinate = map_coordinate_torus(coordinate, sizex_, sizey_);
  return data_[mapped_coordinate.y + mapped_coordinate.x * sizey_ +
               layer * sizex_ * sizey_];
}

template <typename DataType>
void Array2d<DataType>::set(Vec2<int> coordinate, DataType value) {
  set(coordinate, 0, value);
}

template <typename DataType> DataType *Array2d<DataType>::get_data() {
  return data_.data();
}

template <typename DataType>
void Array2d<DataType>::set(Vec2<int> coordinate, int layer, DataType value) {
  if (layer < 0 or layer >= layers_) {
    throw std::out_of_range("Layer argument is out of range.");
  }
  if ((boundary_type_ == BoundaryType::wall) &&
      (coordinate.x < 0 || coordinate.x > sizex_ || coordinate.y < 0 ||
       coordinate.y > sizey_))
    throw std::out_of_range("Setting outside of array");
  auto mapped_coordinate = map_coordinate_torus(coordinate, sizex_, sizey_);
  data_[mapped_coordinate.y + mapped_coordinate.x * sizey_ +
        layer * sizex_ * sizey_] = value;
}

template class Array2d<int>;
template class Array2d<double>;
template class Array2d<float>;