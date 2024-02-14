#include "novikova_storm.hpp"
#include <cmath>

#include <iostream>

double NS::integrate(double force, double size, NS::Parameter par)
{
    int timesteps(std::ceil(par.T / par.dt));
    std:: cout <<
        "ns_Nt               = " << par.Nt  <<      "\n"
        "ns_phi_s,           = " << par.phi_s <<    "\n"
        "ns_phi_c,           = " << par.phi_c <<    "\n"
        "ns_d0,              = " << par.d0  <<      "\n"
        "ns_gamma,           = " << par.gamma <<    "\n"
        "ns_dt,              = " << par.dt <<       "\n"
        "ns_T,               = " << par.T <<       "\n"
        "adhesion_integrin_N0= " << par.N0 <<       "\n"
        "ns_f_star           = " << par.fstar << '\n';
    for (int i = 0; i < timesteps; i++)
    {
        std::cout << "phi =   " << par.fstar << '*'<<  force << '/' << size << '=';
        double phi = par.fstar * (force / size);
        std::cout << phi << '\n';

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
        std::cout << "decay , growth = " << decay << ',' << growth << '\n';

        if (size > par.Nt) {
            size = par.Nt;
            std::cout << "set size to " << par.Nt << '\n';
        }
        else if (size < par.N0)
            size = par.N0;
        std::cout << "size = "  << size << "\n";
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
