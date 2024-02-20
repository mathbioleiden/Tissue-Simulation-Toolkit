#include <iostream>
#include <chrono>
#include <vector>

//#define PROFILING_ENABLED

#ifdef PROFILING_ENABLED
#define PROFILE(a,b) static int a = profiler.new_timer(#a); profiler.start_timer(a); b profiler.stop_timer(a);
#else
#define PROFILE(a,b) b
#endif


struct timer {
  std::string name;
  std::chrono::time_point<std::chrono::system_clock> start;
  std::chrono::time_point<std::chrono::system_clock> stop;
  std::chrono::duration<double> delta;
  std::chrono::duration<double> sum;
  std::chrono::duration<double> avg;
  int count;
};


class Profiler {
  public:
    int start_new_timer(std::string name);
    int new_timer(std::string name);
    void start_timer(int timer);
    void stop_timer(int timer);
    void stop_print(int timer);
    timer get_timer(int timer);
    void print_timer(int timer);
    void print_all();

  private:
    std::vector<timer> timers;
    int index;
};


extern Profiler profiler;
 
