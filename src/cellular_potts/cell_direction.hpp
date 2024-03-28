#pragma once;
#include "vec2.hpp"

struct Dir
{
    Dir()
    {
        aa1 = 0.;
        aa2 = 0.;
        bb1 = 0.;
        bb2 = 0.;
        lb1 = 0.;
        lb2 = 0.;
    }
    double aa1, aa2;
    double bb1, bb2;
    double lb1, lb2;
};

/// Class used to effectivly keep track of a fitted ellipse to a changing shape.
class FitEllipse
{
public:
    FitEllipse()
        : sum_x_(), sum_y_(), sum_xy_(), sum_xx_(), sum_yy_(), area_(),
          length_()
    {
    }

    /**
     * \brief Returns a unit vector that lies on the major axis of the fitted ellips.
     * \return Unit vector with positive y coordinate
    */
    Vec2<double> major_axis() const;

    /**
     * \brief Returns a unit vector that lies on the minor axis of the fitted ellips.
     * \return Unit vector with positive y coordinate.
    */
    Vec2<double> minor_axis() const;

    /**
     * @brief Computes the size of the major axis of the fitted ellipse.
     * @return Size of the major axis.
     */
    double major() const; 

    /**
     * @brief Computes the size of the minor axis of the fitted ellipse.
     * @return Size of the minor axis.
     */
    double minor() const;

    /**
     * @brief Computes the length the fitted ellipse (alias for FitEllipse::major)
     * @return Length of the shape.
     */
    double length() const;

    /**
     * @brief Add a site to the shape.
    */
    void add_site(PixelPos);

    /**
     * @brief Removes a site of the shape.
    */
    void remove_site(PixelPos);
    
    /**
     * @brief Clears the moments of stored chape.
    */
    void clear();
    
    /**
     * @brief Returns the center of mass of the shape.
     * @return A vector with the x and y coordinates of the shape.
     */
    Vec2<double> center() const;

private:
    int sum_x_;
    int sum_y_;
    int sum_xy_;
    int sum_xx_;
    int sum_yy_;
    int area_;
    int length_;
};
