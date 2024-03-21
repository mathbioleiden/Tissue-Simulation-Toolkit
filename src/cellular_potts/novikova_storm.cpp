#include "novikova_storm.hpp"
#include <cmath>
#include <stdexcept>

#include <iostream>

double NS::integrate(double force, double size, NS::Parameter par)
{
    int timesteps(std::ceil(par.T / par.dt));
    for (int i = 0; i < timesteps; i++)
    {
        double phi = par.fstar * (force / size);

        double growth = par.gamma * (par.Nt - size);
        double decay_rate(0.0);
        try
        {
            decay_rate = par.d0 * (std::exp(phi - par.phi_s) +
                                   std::exp(par.phi_c - phi));
        }
        catch (const std::exception &exc)
        {
            std::cout << "Warning " << exc.what() << "\n";
            growth = 0.0;
            decay_rate = 0.0;
        }
        double decay = size * decay_rate;
        size += par.dt * (growth - decay);

        if (size > par.Nt) 
            size = par.Nt;
        if (size < par.N0)
            size = par.N0;
    }
    return size;
}

std::vector<double> NS::integrate(std::vector<double> forces,
                                  std::vector<double> sizes, NS::Parameter par)
{
    if (forces.size() != sizes.size())
        throw std::invalid_argument("Forces and sizes are not of the "
                                    "same size");
    for (int i = 0; i < forces.size(); i++)
    {
        auto force = forces[i];
        auto size = sizes[i];
        sizes[i] = NS::integrate(force, size, par);
    }
    return sizes;
}
