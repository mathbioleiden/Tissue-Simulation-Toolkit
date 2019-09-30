#ifndef CUSTOM_PIMPL_HPP
#define CUSTOM_PIMPL_HPP

namespace common
{

  class custom_pimpl: public custom_pskel //::xml_schema::string_pimpl
  {
  public:
    common::custom* post_custom()
    {
    }
  };

  //class custom_pimpl: public custom_pskel
  //{
  //};
}
#endif
