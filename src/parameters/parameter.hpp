#ifndef _PARAMETER_HPP_
#define _PARAMETER_HPP_

#ifdef _MOCK_PARAMETER_HPP_
#include _MOCK_PARAMETER_HPP_
#else

#include <ostream>
#include <string>
#include <vector>

/** Collection of all TST parameters
 *
 * The individual parameters are public member variables of this class.
 * See src/parameters/parameters.hpp for the definitions.
 */
class Parameter {
public:
  /** Create a Parameter object
   *
   * All parameters will be initialised to their defaults.
   */
  Parameter();

  /** Read parameters from a text file
   *
   * @param filename Name of the file to read
   */
  void Read(std::string const &filename);

  /** Write parameters to a stream
   *
   * @param stream Stream to write to, e.g. std::cout or a std::ofstream.
   */
  void Write(std::ostream &stream) const;

  /** Validate parameters
   *
   * This evaluates the constraints and throws std::invalid_argument if
   * any of them are not met.
   */
  void Validate() const;

  // Generate member variables

#define SECTION(TEXT)
#define PARAMETER(TYPE, NAME, DEFAULT, DESC) TYPE NAME;
#define CONSTRAINT(EXPR, MESSAGE)
#include "parameters.hpp"
#undef CONSTRAINT
#undef PARAMETER
#undef SECTION

private:
  /** Write a single parameter to a stream
   *
   * @param stream Stream to write to
   * @param name Name of the parameter
   * @param value Its value
   */
  template <typename Value>
  void WritePar(std::ostream &stream, std::string const &name,
                Value const &value) const;

  /** Write a comment to a stream
   *
   * @param text The text to write
   */
  void WriteComment(std::ostream &stream, std::string const &text) const;
};

#include "parameter.tpp"

#endif
#endif
