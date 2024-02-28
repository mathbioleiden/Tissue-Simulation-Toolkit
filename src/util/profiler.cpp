#include "profiler.hpp"
#include <iomanip>

#ifdef PROFILING_ENABLED
Profiler profiler = Profiler();
#endif

int Profiler::new_timer(std::string name) {
  timer new_timer;
  new_timer.name = name;
  new_timer.count = 0;
  int dex = index;
  index++;
  timers.push_back(new_timer);
  return dex;
}

int Profiler::start_new_timer(std::string name) {
  int timer = new_timer(name);
  start_timer(timer);
  return timer;
}

void Profiler::start_timer(int timer) {
  timers[timer].start = std::chrono::system_clock::now();
}

void Profiler::stop_timer(int timer) {
  timers[timer].stop = std::chrono::system_clock::now();
  timers[timer].delta = timers[timer].stop - timers[timer].start;
  timers[timer].sum += timers[timer].delta;
  timers[timer].count++;
  timers[timer].avg = timers[timer].sum / timers[timer].count;
}

timer Profiler::get_timer(int timer) { return timers[timer]; }

void Profiler::print_timer(int timer) {
  std::cout << std::left << std::setw(20) << timers[timer].name
            << "  last: " << std::setw(13) << timers[timer].delta.count()
            << "     sum: " << std::setw(13) << timers[timer].sum.count()
            << "     avg: " << std::setw(13) << timers[timer].avg.count()
            << std::endl;
}

void Profiler::stop_print(int timer) {
  stop_timer(timer);
  print_timer(timer);
}

void Profiler::print_all() {
  for (int i = 0; i < index; i++) {
    print_timer(i);
  }
  std::cout << std::endl;
}
