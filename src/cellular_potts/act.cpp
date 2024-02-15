#include <act.hpp>
#include <cmath>
#include <iostream>
#include <parameter.hpp>
#include <vector>
extern Parameter par;

using namespace ACT;
namespace
{
    double GeoMetricMean(ActField const &act_field, int **sigma, PixelPos pos)
    {
        // NO BOUNDS CHECK for sigma!!!
        int mainspin = sigma[pos.x][pos.y];
        double output = 1.0;
        int count = 0;
        for (int i = -1; i <= 1; i++)
            for (int j = -1; j <= 1; j++)
            {
                PixelPos neighbour_pos(i, j);
                neighbour_pos += pos;
                if (sigma[neighbour_pos.x][neighbour_pos.y] == mainspin)
                {
                    double value = act_field.Value(neighbour_pos);
                    if (value > 0.0)
                    {
                        count++;
                        output *= value;
                    }
                }
            }
        if (count == 0.0)
            return 0.0;
        return std::pow(output, 1.0 / count);
    }
}

double ActField::Value(PixelPos pos) const
{
    auto it = value_.find(pos);
    if (it != value_.end())
    {
        return it->second;
    }
    return 0.0;
}

void ActField::SetValue(PixelPos pos, double value) { value_[pos] = value; }

void ActField::Decrease()
{
    auto it = value_.begin();
    while (it != value_.end())
    {
        it->second -= 1.0;
        if (it->second <= 0.0)
        {
            it = value_.erase(it);
        }
        else
        {
            it++;
        }
    }
}

double ACT::DeltaH(ActField const &act_field, int **sigma, PixelPos from,
                   PixelPos to)
{
    double GM_source = GeoMetricMean(act_field, sigma, from);
    double GM_target = GeoMetricMean(act_field, sigma, to);
    return (par.lambda_Act / par.max_Act) * (GM_source - GM_target);
}

void ACT::commit_move(ActField &act_field, int **sigma, PixelPos from,
                      PixelPos to)
{
    if (sigma[to.x][to.y] > 0)
        act_field.SetValue(to, par.max_Act);
}