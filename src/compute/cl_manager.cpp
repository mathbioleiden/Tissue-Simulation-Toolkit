#include "cl_manager.hpp"
#include "parameter.hpp"
#include <fstream>
#include <iostream>
#include <sstream>

CLManager clm = CLManager();

int CLManager::make_context() {
  extern Parameter par;
  int platform = 0;
  std::vector<cl::Platform> all_platforms;
  cl::Platform::get(&all_platforms);
  int num_plat = all_platforms.size();
  if (num_plat == 0) {
    std::cout << " No platforms found. Check OpenCL installation!" << std::endl;
    return 0;
  }
  std::cout << "num_plat" << num_plat << std::endl;
  if (par.opencl_pref_platform < num_plat) {
    platform = par.opencl_pref_platform;
  } else {
    std::cout << "Could not select platform: [" << par.opencl_pref_platform
              << "]" << std::endl;
  }
  cl::Platform default_platform = all_platforms[platform];
  std::cout << "Using platform: [" << platform << "] "
            << default_platform.getInfo<CL_PLATFORM_NAME>() << std::endl;

  std::vector<cl::Device> all_devices;
  default_platform.getDevices(CL_DEVICE_TYPE_ALL, &all_devices);
  if (all_devices.size() == 0) {
    std::cout << " No devices found. Check OpenCL installation!" << std::endl;
    return 0;
  }

  device = all_devices[0];
  std::cout << "Using device: " << device.getInfo<CL_DEVICE_NAME>()
            << std::endl;
  context = cl::Context({device});
  queue = cl::CommandQueue(context, device);
  return 1;
}

cl::Program CLManager::make_program(std::string filename, std::string head) {
  if (!context_prepared)
    make_context();
  cl::Program::Sources sources;
  std::ifstream inFile;
  inFile.open(filename);
  std::stringstream strStream;
  strStream << head;
  strStream << inFile.rdbuf();
  std::string kernel_code = strStream.str();
  sources.push_back({kernel_code.c_str(), kernel_code.length()});
  cl::Program program = cl::Program(context, sources);
  if (program.build({device}) != CL_SUCCESS) {
    std::cout << " Error building: "
              << program.getBuildInfo<CL_PROGRAM_BUILD_LOG>(device) << "\n";
    return (cl::Program)0;
  }
  return program;
}
