#include "custom-simpl.hpp"
#include "common.hpp"
#include "common-simpl.hpp"
#include "MultiCellDS.hpp"
#include <iterator>
#include <string>

namespace common
{
  
  custom_simpl::custom_simpl () : text_(0)
    {
    }

  void custom_simpl::
  serialize_any ()
  {
    auto end = custom_base_simpl_state_.custom_->custom_data ().end ();
    text_->pre(*((std::string *)*i_));
    xml_schema::serializer_base* s = text_;
    xml_schema::serializer_context& ctx = _context ();
    if(text_ != 0) {
      s->_pre_impl (ctx);
      s->_serialize_content ();
      s->_post_impl ();
    }
    i_++;
  }

  void custom_simpl::
  _pre()
  {
    // Initialize the body iterator.
    //
    i_  = custom_base_simpl_state_.custom_->custom_data ().begin ();
  }

  void custom_simpl::pre(const ::common::custom& x)
  {
    this->custom_base_simpl_state_.custom_ = &x;
  }

  
  bool custom_simpl:: any_next()
  {
    custom::custom_data_const_iterator end (
	    custom_base_simpl_state_.custom_->custom_data ().end ());
    return i_ != end;

    }
  void custom_simpl:: any (std::string &ns, std::string &name) {
  }

  void custom_simpl::
  _serialize_content ()
  {
    while (this->any_next ())
    {
      ::std::string ns, name;
      this->any (ns, name);
      if(name.empty()) {
	this->_characters(((std::string *)*i_)->c_str());
	i_++;
      }
      else {
	if (ns.empty ())
	  this->_start_element (name.c_str ());
	else
	  this->_start_element (ns.c_str (), name.c_str ());
	this->serialize_any ();
	this->_end_element ();
      }
    }
  }

}
