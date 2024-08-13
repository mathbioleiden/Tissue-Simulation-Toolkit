#include "cell_polarity.hpp"

void CellPolarity::add_com(Vec2<double> center)
{
    com_history.push_back(center);
    if (com_history.size() > maximum_history)
    {
        com_history.pop_front();
    }
}

Vec2<double> CellPolarity::get() const
{
    if (fixed)
        return fixed_direction;
    int n = com_history.size();
    if (n < 2)
        return {0.0, 0.0};

    Vec2<double> output = {0.0, 0.0};
    for (int i = 0; i < com_history.size() - 1; i++)
    {
        output = output + (com_history[i + 1] - com_history[i]);
    }
    auto output_length = output.length();
    if (output_length == 0.0)
        return {0.0, 0.0};
    return (1.0 / output_length) * output;
}

void CellPolarity::fix(Vec2<double> direction) {
    if (direction.x == 0.0 and direction.y == 0.0){
        fixed = false;
    }
    else{
        fixed = true;
        fixed_direction = direction;  
    }
}

void CellPolarity::set_maximum_history(int max_history) {
    maximum_history = max_history;
    // com_history.resize(max_history);
}