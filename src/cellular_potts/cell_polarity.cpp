#include "cell_polarity.hpp"
#include "parameter.hpp"
#include <functional>

extern Parameter par;

void CellPolarity::add_com(Vec2<double> center)
{
    com_history.push_back(center);
    // std::cout << "com " << center << ' ' << com_history.size() << '\n';
    if (com_history.size() > maximum_history)
    {
        com_history.pop_front();
    }
}

namespace {
    Vec2<double> integrate_history(const std::deque<Vec2<double>> &com_history,
                                   std::function<double(int)> kernel
    ){
        Vec2<double> output = {0.0, 0.0};
        for (int i = 0; i < com_history.size() - 1; i++)
        {
            Vec2<double> x = com_history[i+1];
            Vec2<double> y = com_history[i];
            auto scaler = kernel(com_history.size()-i-2);
            output = output + scaler * (x-y);
        }
        auto output_length = output.length();
        if (output_length == 0.0){
            return {0.0, 0.0};
        }
        output =(1.0 / output_length) * output;
        return output;
    }

}

Vec2<double> CellPolarity::get()
{
    if (polarity_on == false)
        return {0.0, 0.0};

    if (fixed)
        return fixed_direction;
    int n = com_history.size();
    if (n < 2) {
        previous_polarity ={0.0,0.0};
        return {0.0, 0.0};
    }
    std::function<double(int)> kernel = [&](int time) {return 1.0;};
    if (par.polarity_kernel == "exp") {
        double rate = par.polarity_kernel_exp_rate;
        kernel = [rate](int time) {
            return std::exp(-rate * time);
        };
    }

    auto output = integrate_history(com_history, kernel);
    previous_polarity = output;
    return output;
}

void CellPolarity::PolarityOff() {
    polarity_on = false;
}
void CellPolarity::PolarityOn() {
    polarity_on = true;
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

Vec2<double> CellPolarity::get_previous(){
    return previous_polarity;
}