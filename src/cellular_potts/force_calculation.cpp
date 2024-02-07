#include "force_calculation.hpp"

template<typename T>
T mag(Vec2<T> v){
    return std::sqrt( v.dot(v) );
}

Force getAngularHarmonicForceOnA(ParPos A, ParPos B, ParPos C, double k, double theta0){
    auto v = A-B;
    auto w = C-B;    

    auto v_mag = mag(v);
    auto w_mag = mag(w);
    
    auto vhat = (1/v_mag) * v;
    auto what = (1/w_mag) * w;
    
    auto angle = std::acos(vhat.dot(what));
    
    auto size_of_force = k * ( theta0 - angle );

    return size_of_force * Force(-vhat.y, vhat.x);
}


Force getAngularHarmonicForceOnB(ParPos A, ParPos B, ParPos C, double k, double theta0){
    auto v = A-B;
    auto w = C-B;    

    auto v_mag = mag(v);
    auto w_mag = mag(w);
    
    auto vhat = (1/v_mag) * v;
    auto what = (1/w_mag) * w;
    
    auto angle = std::acos(v.dot(w));
    
    auto size_of_force = (k/2.0) * ( angle - theta0 );

    Force on_a = size_of_force * Force(-v.y, v.x);
    Force on_c = size_of_force * Force(-w.y, w.x);
    
    Force on_b = (-1.0) * (on_a + on_c);
    return on_b;
}

Force getLinearHarmonicForceOnB(ParPos A, ParPos B, double k, double r0){
    auto r = mag(B - A);

    auto size_of_force = k * (r0 - r) ;

    return size_of_force * (1/r) * (B-A);
}