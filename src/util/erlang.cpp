#include "erlang.hpp"
#include "random.hpp"
#include <cmath>
#include <random>

namespace
{
    /*
     * The erlang distribution is just the gamma distribution
     */
    double erlang_gamma(int k, double lambda)
    {
        int seed = RANDOM() * 10000;
        std::default_random_engine engine(seed);
        std::gamma_distribution<double> distribution(static_cast<double>(k),
                                                     1.0 / lambda);
        return distribution(engine);
    }

    /*
     * Different method, from Wikipedia
     */
    double erlang_from_tst(int k, double lambda)
    {
        double sum = 0;
        for (int i = 0; i < k; i++)
            sum += std::log(RANDOM());
        return -sum / lambda;
    }
}

double erlang(int k, double lambda) { return erlang_from_tst(k, lambda); }