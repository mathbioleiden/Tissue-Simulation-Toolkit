#pragma once
#include "vec2.hpp"
#include <vector>

enum class BoundaryType { wall, periodic };

/** A 2D array class template
 *
 * This array takes care of storing values in a grid. Behind the scenes it
 * stores the data in a single vector which is needed for CUDA computations.
 * When the data is accesed via the interface, the boundary type dictates the
 * behaviour.
 */
template <typename DataType> class Array2d {
public:
  /**
   * @brief Default constructor, creates a 1x1 grid of 1 layer.
   */
  Array2d() = default;

  /**
   * @brief Constructor of an array with one layer and wall boundaries
   * @param sizex The maximum of the first coordinate.
   * @param sizey The maximum of the second coordinate.
   */
  Array2d(int sizex, int sizey);

  /**
   * @brief Constructor of an array with wall boundaries
   * @param sizex The maximum of the first coordinate.
   * @param sizey The maximum of the second coordinate.
   * @param layers The amount of layers
   */
  Array2d(int sizex, int sizey, int layers);

  /**
   * @brief Constructor of an array with one layer.
   * @param sizex The maximum of the first coordinate.
   * @param sizey The maximum of the second coordinate.
   * @param boundary_type The type of boundary used.
   */
  Array2d(int sizex, int sizey, BoundaryType boundary_type);
  /**
   * @brief Constructor of an array
   * @param sizex The maximum of the first coordinate.
   * @param sizey The maximum of the second coordinate.
   * @param layers The amount of layers
   * @param boundary_type The type of boundary used.
   */
  Array2d(int sizex, int sizey, int layers, BoundaryType boundary_type);

  /**
   * @brief (Re-)initalizes data. Clears array and constructs a new one.
   */
  void initialise(int sizex, int sizey, int layers, BoundaryType boundary_type);

  /** Getter for data of layer 0
   *
   * @param coordinate The position for which the data is requested.
   */
  DataType get(Vec2<int> coordinate) const;

  /** Getter for data at a layer
   *
   * @param coordinate The position for which the data is requested.
   * @param layer The layer which is queried.
   */
  DataType get(Vec2<int> coordinate, int layer) const;

  /** Sets value at layer 0 of given coordinate
   *
   * @param coordinate The position at which the data is stored.
   * @param value The value that is stored.
   */
  void set(Vec2<int> coordinate, DataType value);

  /** Sets value at given layer for given coordinate
   *
   * @param coordinate The position at which the data is stored.
   * @param layer The layer at which the data is stored.
   * @param value The value that is stored.
   */
  void set(Vec2<int> coordinate, int layer, DataType value);

  /**
   * @brief Used to get the underlying pointer to the continuous data;
   * @return Pointer to the data
   */
  DataType *get_data();

private:
  int sizex_;
  int sizey_;
  int layers_;
  BoundaryType boundary_type_;
  std::vector<DataType> data_;
};
