############################################################
#
# Makefile for creating Read_DCIS
#
############################################################

#CXX := /opt/local/bin/g++-mp-5
CXX := g++ 
COMPILE_CFLAGS := -O3 -s -mfpmath=both  -m64 -std=c++11
COMPILE_COMMAND := $(CXX) $(COMPILE_CFLAGS) 
LINK_COMMAND := $(CXX)
mcds_api := mcds_api_val
libMultiCellDS_DIR := ../$(mcds_api)
XSDE_DIR := ../xsde_val/libxsde/

#-I ../mcds_api_test -I xsde_val/libxsde/ ../mcds_api_test/mcds_api.a -L xsde_val/libxsde/xsde/ -l xsde -o Read_Chaste -std=c++11

pugixml.o: pugixml.cpp
	$(COMPILE_COMMAND) -c pugixml.cpp

Read_DCIS.o: Read_DCIS.cpp
	$(COMPILE_COMMAND) -c Read_DCIS.cpp -I $(libMultiCellDS_DIR) -I $(XSDE_DIR)

all: pugixml.o Read_DCIS.o
	$(LINK_COMMAND) -o Read_DCIS pugixml.o Read_DCIS.o -L $(XSDE_DIR)/xsde/ $(libMultiCellDS_DIR)/libmcds.a -l xsde -std=c++11
