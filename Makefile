ROOT_DIR = $(shell pwd)
MCDS_DIR  = $(ROOT_DIR)/lib/MultiCellDS/v1.0/v1.0.0
XSDE_DIR  = $(MCDS_DIR)/libMCDS/xsde
LIBCS_DIR = $(ROOT_DIR)/lib/libCellShape
TST_DIR   = $(ROOT_DIR)/src
QMAKE = /Applications/Qt5/5.15.2/clang_64/bin/qmake

all: TST

XSDE:
	cd  "$(XSDE_DIR)" && $(MAKE)

MCDS: XSDE
	cd "$(MCDS_DIR)" && $(MAKE) objects

LIBCS: MCDS 
	cd "$(LIBCS_DIR)" && $(MAKE)

TST: MCDS LIBCS
	cd "$(TST_DIR)" && $(QMAKE) && $(MAKE)

clean: 
	cd "$(XSDE_DIR)" && $(MAKE) clean
	cd "$(MCDS_DIR)" && $(MAKE) clean
	cd "$(LIBCS_DIR)" && $(MAKE) clean
	cd "$(TST_DIR)" && $(MAKE) clean
