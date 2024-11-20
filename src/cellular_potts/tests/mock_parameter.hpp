#include <string>
class MockParameter {
    public:
        double lambda_Act;
        double max_Act;
        std::string polarity_kernel = "constant";
        double polarity_kernel_exp_rate;
    
};

MockParameter par;

using Parameter = MockParameter;