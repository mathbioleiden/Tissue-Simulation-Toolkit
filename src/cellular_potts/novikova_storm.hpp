#pragma once
#include <vector>

namespace NS
{
    struct Parameter
    {
        Parameter(double Nt, double phi_s, double phi_c, double d0,
                  double gamma, double dt, double T, double N0, double fstar, double d_FA)
            : Nt(Nt), phi_s(phi_s), phi_c(phi_c), d0(d0), gamma(gamma), dt(dt),
              T(T), N0(N0), fstar(fstar), d_FA(d_FA)
        {
        }

        double Nt;
        double phi_s;
        double phi_c;
        double d0;
        double gamma;
        double dt;
        double T;
        double N0;
        double fstar;

        double d_FA;
    };

    /**
     * @brief Compute the size of a FA given it changing values
     * @param force Tension on this FA
     * @param size CUrrent size of the FA
     * @param act_level Number between 0 and 1 describing the current actin levels
     * @param par Parameters used
     * @return New FA size
     */
    double integrate(double force, double size, double act_level, NS::Parameter par);

    std::vector<double> integrate(std::vector<double> forces,
                                  std::vector<double> sizes, NS::Parameter par);

} // namespace NS
