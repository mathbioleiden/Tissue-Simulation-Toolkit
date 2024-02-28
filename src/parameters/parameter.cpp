#include "parameter.hpp"
#include "parameter_file.hpp"

#include <iomanip>
#include <vector>

Parameter par;

Parameter::Parameter() {
#define SECTION(TEXT)
#define PARAMETER(TYPE, NAME, DEFAULT, DESC) NAME = DEFAULT;
#define CONSTRAINT(EXPR, MESSAGE)
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION
}

void Parameter::Read(std::string const &filename) {
  ParameterFile file(filename);

#define SECTION(TEXT)
#define PARAMETER(TYPE, NAME, DEFAULT, DESC)                                   \
  if (file.has(#NAME))                                                         \
    NAME = file.get<TYPE>(#NAME);
#define CONSTRAINT(EXPR, MESSAGE)
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION
  Validate();
}

void Parameter::Write(std::ostream &stream) const {
#define SECTION(TEXT) WriteComment(stream, TEXT);
#define PARAMETER(TYPE, NAME, DEFAULT, DESC) WritePar(stream, #NAME, NAME);
#define CONSTRAINT(EXPR, MESSAGE)
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION
  stream.flush();
}

void Parameter::Validate() const {
#define SECTION(TEXT)
#define PARAMETER(TYPE, NAME, DEFAULT, DESC)
#define CONSTRAINT(EXPR, MESSAGE)                                              \
  if (!(EXPR))                                                                 \
    throw std::invalid_argument(MESSAGE);
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION
}

void Parameter::WriteComment(std::ostream &stream,
                             std::string const &text) const {
  stream << "\n";
  stream << "# " << text << "\n";
}

template <>
void Parameter::WritePar<>(std::ostream &stream, std::string const &name,
                           bool const &value) const {
  std::ios::fmtflags state(stream.flags());
  stream.setf(std::ios::boolalpha);
  stream << name << " = " << value << "\n";
  stream.flags(state);
}

template <>
void Parameter::WritePar<>(std::ostream &stream, std::string const &name,
                           double const &value) const {
  std::ios::fmtflags state(stream.flags());
  stream.precision(17);
  stream << name << " = " << value << "\n";
  stream.flags(state);
}

template <>
void Parameter::WritePar(std::ostream &stream, std::string const &name,
                         std::vector<double> const &value) const {
  stream << name << " = ";
  if (value.size() > 0u)
    stream << value[0];
  for (std::size_t i = 1u; i < value.size(); ++i)
    stream << ", " << value[i];
  stream << "\n";
}