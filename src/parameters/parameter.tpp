template <typename Value>
void Parameter::WritePar(std::ostream &stream, std::string const &name,
                         Value const &value) const {
  stream << name << " = " << value << "\n";
}

template <>
void Parameter::WritePar<>(std::ostream &stream, std::string const &name,
                           bool const &value) const;

template <>
void Parameter::WritePar<>(std::ostream &stream, std::string const &name,
                           double const &value) const;

template <>
void Parameter::WritePar<>(std::ostream &stream, std::string const &name,
                           std::vector<double> const &value) const;
