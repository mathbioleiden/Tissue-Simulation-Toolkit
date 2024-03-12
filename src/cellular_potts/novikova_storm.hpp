#pragma once
#include "vector"

namespace NS
{
    struct Parameter
    {
        Parameter(double Nt, double phi_s, double phi_c, double d0,
                  double gamma, double dt, double T, double N0, double fstar)
            : Nt(Nt), phi_s(phi_s), phi_c(phi_c), d0(d0), gamma(gamma), dt(dt),
              T(T), N0(N0), fstar(fstar)
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
    };

    double integrate(double force, double size, NS::Parameter par);

    std::vector<double> integrate(std::vector<double> forces,
                                  std::vector<double> sizes, NS::Parameter par);

} // namespace NS
