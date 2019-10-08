#ifndef CUSTOM_SIMPL_HPP
#define CUSTOM_SIMPL_HPP

#include <iostream>
#include <common-simpl.hpp>

namespace common
{
  class custom_simpl: public custom_base_simpl 
  {
  public:
    
    custom_simpl ();

    void pre(const ::common::custom& x);

    virtual void serialize_any () ;

    virtual void _pre();
    virtual bool any_next();
    virtual void _serialize_content ();
    virtual void any(std::string &ns, std::string &name);

  private:
    xml_schema::string_simpl* text_;
    custom::custom_data_const_iterator i_;
  };

  
}
#endif
