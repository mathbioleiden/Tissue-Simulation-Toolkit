#include "parameter_file.hpp"

#include <cctype>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

std::string trim(std::string const &s) {
  std::size_t i = 0, j = s.length();
  while (i < s.length() && (std::isspace(s[i]) || std::iscntrl(s[i])))
    ++i;

  while (j > 0 && (std::isspace(s[j - 1]) || std::iscntrl(s[j - 1])))
    --j;

  return s.substr(i, j - i);
}

} // namespace

ParameterFile::ParameterFile(std::string const &filename) {
  std::ifstream in_file(filename);
  if (!in_file.good())
    throw std::runtime_error("Could not open " + filename +
                             " for reading parameters");

  int lineno = 0;
  while (in_file.good()) {
    std::string line;
    std::getline(in_file, line);
    ++lineno;

    line = trim(line);

    if (line.empty())
      continue;

    if (line[0] == '#')
      continue;

    std::size_t mid = line.find("=");
    if (mid == line.npos)
      throw std::runtime_error("Error in " + filename + " on line " +
                               std::to_string(lineno) + ":\n    " + line +
                               "\nNo '=' found, and this line is not a comment"
                               " either (use # to start a comment)");

    std::string name = trim(line.substr(0, mid));
    std::string value = trim(line.substr(mid + 1, line.npos));

    entries_[name] = value;
  }
}

bool ParameterFile::has(std::string const &name) const {
  return entries_.count(name) > 0;
}

template <> bool ParameterFile::get<bool>(std::string const &name) const {
  auto const &value = entries_.at(name);
  if (value == "false")
    return false;
  if (value == "true")
    return true;
  throw std::invalid_argument("When reading parameter " + name + ":" + " \"" +
                              value +
                              "\" is not a valid boolean value. Please use"
                              " \"true\" or \"false\"");
}

template <> double ParameterFile::get<double>(std::string const &name) const {
  auto const &svalue = entries_.at(name);
  std::size_t idx;
  double value = std::stod(svalue, &idx);
  if (idx != svalue.length())
    throw std::invalid_argument(
        "When reading parameter " + name + ":" +
        " Extra characters found after double value: " + svalue);
  return value;
}

template <> int ParameterFile::get<int>(std::string const &name) const {
  auto const &svalue = entries_.at(name);
  std::size_t idx;
  int value = std::stoi(svalue, &idx);
  if (idx != svalue.length())
    throw std::invalid_argument(
        "When reading parameter " + name + ":" +
        " Extra characters found after int value: " + svalue);
  return value;
}

template <>
std::string ParameterFile::get<std::string>(std::string const &name) const {
  return entries_.at(name);
}

template <>
std::vector<double>
ParameterFile::get<std::vector<double>>(std::string const &name) const {
  std::string svalue = entries_.at(name);
  std::size_t idx = 0u;
  std::vector<double> result;

  try {
    result.emplace_back(std::stod(svalue, &idx));
  } catch (std::invalid_argument const &e) {
    throw std::invalid_argument(
        "When reading parameter " + name + ":" +
        " Expected a comma-separated list of doubles but got " + svalue);
  }
  svalue = trim(svalue.substr(idx, svalue.npos));

  while (!svalue.empty()) {
    if (svalue[0] != ',')
      throw std::invalid_argument("When reading parameter " + name + ":" +
                                  " Expected a comma but found " + svalue);

    svalue = trim(svalue.substr(1, svalue.npos));

    try {
      result.emplace_back(std::stod(svalue, &idx));
    } catch (std::invalid_argument const &e) {
      throw std::invalid_argument("When reading parameter " + name +
                                  ": Expected a double value but" + " got " +
                                  svalue);
    }

    svalue = trim(svalue.substr(idx, svalue.npos));
  }
  return result;
}
