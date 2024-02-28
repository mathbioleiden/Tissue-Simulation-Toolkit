#ifndef _PARAMETER_FILE_HPP_
#define _PARAMETER_FILE_HPP_

#include <string>
#include <unordered_map>

/** Reads a file with parameters and makes them available on demand */
class ParameterFile {
public:
  /** Read and parse a parameter file
   *
   * \param filename Path of the file to open
   */
  ParameterFile(std::string const &filename);

  /** Check if a parameter with the given name is present
   *
   * \param name Name of the parameter to check for
   */
  bool has(std::string const &name) const;

  /** Get the value of the given parameter
   *
   * \tparam T Type of the parameter to get
   * \param name Name of the parameter to get
   * \throws std::out_of_range If the parameter was not found
   */
  template <typename T> T get(std::string const &name) const;

private:
  std::unordered_map<std::string, std::string> entries_;
};

#endif
