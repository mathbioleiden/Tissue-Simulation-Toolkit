############################################################
#
# Makefile for creating sample simulation snapshot
#
############################################################

#CXX := /opt/local/bin/g++-mp-5
CXX := g++ 
COMPILE_CFLAGS :=  -m64 -std=c++11
#-mfpmath=both -O3 -s 
COMPILE_COMMAND := $(CXX) $(COMPILE_CFLAGS) 
LINK_COMMAND := $(CXX)
mcds_api := ../mcds_api
libMultiCellDS_DIR := $(mcds_api)
XSDE_DIR := ../xsde/libxsde/

#-I ../mcds_api_test -I xsde_val/libxsde/ ../mcds_api_test/mcds_api.a -L xsde_val/libxsde/xsde/ -l xsde -o Read_Chaste -std=c++11

example_snapshot.o: example_snapshot.cpp
	$(COMPILE_COMMAND) -c example_snapshot.cpp -I $(libMultiCellDS_DIR) -I $(XSDE_DIR)

custom-simpl.o : custom-simpl.cpp
	$(COMPILE_COMMAND) -c custom-simpl.cpp -I  $(libMultiCellDS_DIR) -I $(XSDE_DIR)

#all: example_snapshot.o custom-simpl.o
#	$(LINK_COMMAND) -o example_snapshot custom-simpl.o example_snapshot.o -L $(XSDE_DIR)/xsde/ $(libMultiCellDS_DIR)/libmcds.a -l xsde -std=c++11

all: example_snapshot.o 
	$(LINK_COMMAND) -o example_snapshot example_snapshot.o -L $(XSDE_DIR)/xsde/ $(libMultiCellDS_DIR)/libmcds.a -l xsde -std=c++11
