MCDS_DIR  = lib/MultiCellDS/v1.0/v1.0.0
XSDE_DIR  = $(MCDS_DIR)/libMCDS/xsde
LIBCS_DIR = lib/libCellShape
TST_DIR   = src

.PHONY: all XSDE MCDS LIBCS TST clean

all: TST

XSDE:
	$(MAKE) -C $(XSDE_DIR)

MCDS: XSDE
	$(MAKE) -C $(MCDS_DIR) objects

LIBCS: MCDS
	$(MAKE) -C $(LIBCS_DIR)

TST: MCDS LIBCS
	cd $(TST_DIR) && qmake
	$(MAKE) -C $(TST_DIR)

clean:
	$(MAKE) -C $(XSDE_DIR) clean
	# MCDS make clean is broken, so do it by hand here
	rm -f $(MCDS_DIR)/libMCDS/mcds_api/*.o $(MCDS_DIR)/libMCDS/mcds_api/*.a
	$(MAKE) -C $(LIBCS_DIR) clean
	$(MAKE) -C $(TST_DIR) clean
	rm -rf bin $(TST_DIR)/Makefile $(TST_DIR)/.qmake.stash
