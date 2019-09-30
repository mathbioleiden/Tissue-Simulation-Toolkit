############################################################
#
# Makefile for creating libMultiCellDS
#
############################################################

############################################################
#
# Create header, inline, and code files
#
############################################################

XSDE_command := /home/samuel/codes/XML/xsde-3.2.0-1+dep/xsde/xsde/xsde
XSDE_include_path := libMCDS/xsde/libxsde
XSDE_include_path_val := libMCDS/xsde_val/libxsde


Archive_file_location := $(XSDE_include_path)/xsde
Archive_file_location_val := $(XSDE_include_path_val)/xsde
XSDE_generated_files_list := mcds_files.txt
XSDE_generated_files_list_val := mcds_files_val.txt
XSDE_serialize_generated_files_list := mcds_files_serialize.txt


export CC := /opt/local/bin/g++-mp-5
#export CXX := g++ 
export COMPILE_CFLAGS := -O3 -m64 -std=c++11
export COMPILE_COMMAND := $(CXX) $(COMPILE_CFLAGS) 
export LINK_COMMAND := $(CXX)

OUTPUT_DIR := libMCDS/mcds_api
OUTPUT_DIR_VAL := libMCDS/mcds_api_val
OUTPUT_DIR_SERIALIZE := libMCDS/mcds_api_serialize

export CFLAGS := -I $(XSDE_include_path) -I $(OUTPUT_DIR) 
# -I $(XSDE_config_path) 
export CFLAGS_VAL := -I $(XSDE_include_path_val) -I $(OUTPUT_DIR_VAL)

export archive_name := libmcds.a

XSD_files := MultiCellDS.xsd cell_cycle.xsd common.xsd metadata.xsd microenvironment.xsd  phenotype.xsd phenotype_common.xsd pkpd.xsd phenotype_base.xsd basement_membrane.xsd phenotype_dataset.xsd state.xsd cell.xsd mesh.xsd vascular.xsd cell_line.xsd  variables.xsd

XSDE_filetypes := --generate-forward --generate-inline 
XSDE_functions := --generate-clone --generate-detach
XSDE_XDR := --generate-insertion XDR  --generate-extraction XDR
XSDE_generates := --generate-polymorphic --generate-parser --generate-serializer --generate-aggregate $(XSDE_filetypes) $(XSDE_functions)
XSDE_serialize_generates := --generate-polymorphic --generate-inline
XSDE_base_suffixes := --hxx-suffix .hpp --cxx-suffix .cpp --ixx-suffix .ipp
XSDE_suffixes := $(XSDE_base_suffixes) --fwd-suffix -fwd.hpp
XSDE_fileinfo := --file-list $(XSDE_generated_files_list) --output-dir $(OUTPUT_DIR)
XSDE_fileinfo_val := --file-list $(XSDE_generated_files_list_val) --output-dir $(OUTPUT_DIR_VAL)
XSDE_fileinfo_serialize := --file-list $(XSDE_serialize_generated_files_list) --output-dir $(OUTPUT_DIR_SERIALIZE)
XSDE_polymorphism := --polymorphic-type type --polymorphic-type node 
#XSDE_custom := --custom-type custom=f/std::string --custom-parser custom=/../custom-pimpl.hpp --custom-serializer custom=/../custom-simpl.hpp
XSDE_custom := --custom-data custom --custom-parser custom=custom_base_pimpl/custom-pimpl.hpp --custom-serializer custom=custom_base_simpl/custom-simpl.hpp
#XSDE_custom := --custom-type custom=v/string  --custom-parser custom=/../custom-pimpl.hpp --custom-serializer custom=/../custom-simpl.hpp
#--custom-parser custom --custom-serializer custom
#--custom-parser custom --custom-serializer custom=string
#v/::xsde::cxx::hybrid::pod_sequence<::std::double>/
#\
#--custom-parser custom=custom_base_pimpl/custom-pimpl.hpp \
#--custom-serializer custom=custom_base_simpl/custom-simpl.hpp
# --custom-type custom=v//::std::string
#--polymorphic-type units_string --polymorphic-type custom --polymorphic-schema mesh.xsd

XSDE_serialize_custom := --type-map custom.map


bindings: $(XSD_files)
	$(XSDE_command) cxx-hybrid $(XSDE_generates) $(XSDE_suffixes) $(XSDE_fileinfo) $(XSDE_polymorphism) $(XSDE_custom) --root-element MultiCellDS --suppress-serializer-val  $(XSD_files)

bindings_val: $(XSD_files)
	$(XSDE_command) cxx-hybrid $(XSDE_generates) $(XSDE_suffixes) $(XSDE_fileinfo_val) $(XSDE_polymorphism) $(XSDE_custom) --root-element MultiCellDS $(XSD_files)

bindings_serialize: ${XSD_files}
	$(XSDE_command) cxx-serializer $(XSDE_serialize_generates) $(XSDE_base_suffixes) $(XSDE_fileinfo_serialize) $(XSDE_serialize_custom) --root-element MultiCellDS $(XSD_files)

export xsde_cpp_files := $(shell grep .cpp ${XSDE_generated_files_list} | xargs)
export xsde_cpp_files_val := $(shell grep .cpp ${XSDE_generated_files_list_val} | xargs)
#xsde_o_files := $(shell grep .cpp ${XSDE_generated_files_list} | sed s/.cpp/.o/ | xargs)
export xsde_o_files := $(xsde_cpp_files:.cpp=.o)
export xsde_o_files_val := $(xsde_cpp_files_val:.cpp=.o)
python_files := $(shell grep $(XSD_files) | sed s/.xsd/.py/ | xargs)


objects: $(xsde_cpp_files)
	$(MAKE) -C $(OUTPUT_DIR)

objects_val: $(xsde_cpp_files_val)
	$(MAKE) -C $(OUTPUT_DIR_VAL)

hello: hello_multicellds.cpp 
	$(COMPILE_COMMAND) -c hello_multicellds.cpp $(CFLAGS) 
#-I $(XSDE_include_path) -I $(OUTPUT_DIR) -I $(XSDE_config_path)
	$(LINK_COMMAND) hello_multicellds.o $(OUTPUT_DIR)/$(archive_name) -L$(Archive_file_location) -l xsde -std=c++11 -o mcds_hello

python_generator := pyxbgen
python_location := libMCDS/python/

python:
	$(python_generator) -u $(XSD_files) -m MultiCellDS --binding-root $(python_location)

.PHONY: clean clean_python clean_val

clean_python:
	rm $(python_location)/*.py
#	rm $(python_files)

clean:
	rm $(xsde_o_files)

clean_val:
	rm $(xsde_o_files_val)
