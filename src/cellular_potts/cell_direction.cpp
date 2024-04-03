#include "cell_direction.hpp"
#include <cmath>
namespace
{
    /**
     * Struct used internally by FitEllipse to fit an ellipse to given
     * moments.
     *
     * This is how the major and minor axis are calculated:
     * It is known that the inertia tensor of a 2d ellipse with axis a
     * and b is given by:
     *                     /                   \
     *                    |  1/4 a^2            |
     *    I_ellipse = M * |                     |
     *                    |            1/4 b^2  |
     *                     \                   /
     * with M = pi * a * b.
     * Given a shape made out of points (x_1,y_1),...,(x_n,y_n) its moment of
     * inertia tensor is defined as
     *  I =
     *   /                                                   \
     *  | sum_i (ybar_i)^2           -sum_i (xbar_i)*(ybar_i) |
     *  |                                                     |
     *  | -sum_i (xbar_i)*(ybar_i)   sum_i (xbar_i)^2         |
     *   \                                                   /
     *  with xbar_i = x_i - xbar and ybar_i = y_i - ybar where
     *  xbar = 1/n * sum_i x_i and ybar = 1/n * sum_i y_i.
     *
     * This method computes I (by rewriting the definition of I to only include
     * raw moments), and computes the eigenvalue of it. The largest eigenvalue
     * is then put equal to area * (1/4 a^2) and solved for the major axis. The
     * minor axis is solved in the same way except that the smallest eigenvalue
     * is used.
     *
     * TODO: This tensor gets constructed for every function call to
     * FitEllipse::length(), FitEllipse::minor_axis(), etc. However, the tensor
     * stays valid until a call is made to FitEllipse::add_site or
     * FitEllipse::remove_site. A possible speedup could be making a private
     * InertiaTensor which gets recomputed only if one of the aforementioned
     * methods was called.
     */
    struct InertiaTensor
    {
        InertiaTensor(double sum_x, double sum_y, double sum_xx, double sum_yy,
                      double sum_xy, double area)
        {
            xx = sum_yy - (1 / area) * sum_y * sum_y;
            yy = sum_xx - (1 / area) * sum_x * sum_x;
            xy = -(sum_xy - (1 / area) * sum_y * sum_x);
        }

        double xx;
        double yy;
        double xy;

        double largest_eigenvalue()
        {
            return 0.5 * (xx + yy) +
                   0.5 * (std::sqrt((xx + yy) * (xx + yy) - 4 * xx * yy +
                                    4 * xy * xy));
        }
        double smallest_eigenvalue()
        {
            return 0.5 * (xx + yy) -
                   0.5 * (std::sqrt((xx + yy) * (xx + yy) - 4 * xx * yy +
                                    4 * xy * xy));
        }
    };
    /**
     * \brief Find a non-zero unit vector in the kernel of a degenerate
     * symmetric matrix.
     *
     * \warning There is no check if the matrix is indeed degenerate!
     * \return A unit vector in ker([A,B],[B,C]).
     */
    Vec2<double> solve_symmetric_degenerate_matrix(double A, double B, double C)
    {
        const double eps = 0.00001;
        // If B is super close to one of the coordinate axis return just the
        // coordinate axis.
        if (std::abs(B) < eps)
        {
            if (std::abs(A) < eps)
                return {1.0, 0.0};
            return {0.0, 1.0};
        }

        double minusCoverB = -C / B;
        double scale = 1.0 / std::sqrt(minusCoverB * minusCoverB + 1.0);
        Vec2<double> result = scale * Vec2<double>(minusCoverB, 1.0);
        return result;
    }
}

Vec2<double> FitEllipse::major_axis() const
{
    InertiaTensor I(sum_x_, sum_y_, sum_xx_, sum_yy_, sum_xy_, area_);
    // Because the inertia is the lowest at the highest side of the ellipse.
    auto lambda = I.smallest_eigenvalue();
    // Matrix [A,B], [B, C] made by substracting largest eigenvalue from I.
    return solve_symmetric_degenerate_matrix(I.xx - lambda, I.xy,
                                             I.yy - lambda);
}

Vec2<double> FitEllipse::minor_axis() const
{
    InertiaTensor I(sum_x_, sum_y_, sum_xx_, sum_yy_, sum_xy_, area_);
    // Because the inertia is the higest at the small side of the ellipse.
    auto lambda = I.largest_eigenvalue();
    return solve_symmetric_degenerate_matrix(I.xx - lambda, I.xy,
                                             I.yy - lambda);
}

double FitEllipse::length() const
{
    InertiaTensor I(sum_x_, sum_y_, sum_xx_, sum_yy_, sum_xy_, area_);
    return std::sqrt(4 * I.largest_eigenvalue() / (1.0 * area_));
}

double FitEllipse::major() const { return length(); }

double FitEllipse::minor() const
{
    InertiaTensor I(sum_x_, sum_y_, sum_xx_, sum_yy_, sum_xy_, area_);
    return std::sqrt(4 * I.smallest_eigenvalue() / (1.0 * area_));
}

void FitEllipse::add_site(PixelPos pos)
{
    sum_x_ += pos.x;
    sum_y_ += pos.y;
    sum_xy_ += pos.x * pos.y;
    sum_xx_ += pos.x * pos.x;
    sum_yy_ += pos.y * pos.y;
    area_ += 1;
}

void FitEllipse::remove_site(PixelPos pos)
{
    sum_x_ -= pos.x;
    sum_y_ -= pos.y;
    sum_xy_ -= pos.x * pos.y;
    sum_xx_ -= pos.x * pos.x;
    sum_yy_ -= pos.y * pos.y;
    area_ -= 1;
}

Vec2<double> FitEllipse::center() const
{
    double center_x = (sum_x_ * 1.0) / (area_ * 1.0);
    double center_y = (sum_y_ * 1.0) / (area_ * 1.0);
    return {center_x, center_y};
}

void FitEllipse::clear()
{
    sum_x_ = 0;
    sum_y_ = 0;
    sum_xy_ = 0;
    sum_xx_ = 0;
    sum_yy_ = 0;
    area_ = 0;
    length_ = 0;
}
