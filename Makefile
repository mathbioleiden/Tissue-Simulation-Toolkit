MCDS_DIR  = lib/MultiCellDS/v1.0/v1.0.0
XSDE_DIR  = $(MCDS_DIR)/libMCDS/xsde
LIBCS_DIR = lib/libCellShape
CATCH2_DIR = lib/Catch2
TST_DIR   = src
QMAKE     = qmake
# Edit the above line as necessary, e.g., as follows:
#QMAKE 	  = /Applications/Qt5/6.4.0/macos/bin/qmake

MODELS = bin/vessel bin/qPotts bin/sorting bin/Act_model

.PHONY: all XSDE MCDS LIBCS TST test clean


all: $(MODELS)


# Dependencies

XSDE:
	$(MAKE) -C $(XSDE_DIR)

MCDS: XSDE
	$(MAKE) -C $(MCDS_DIR) objects

LIBCS: MCDS
	$(MAKE) -C $(LIBCS_DIR)

Catch2:
	$(MAKE) -C $(CATCH2_DIR)


# Models

bin/%: MCDS LIBCS
	cd $(TST_DIR) && $(QMAKE) $(@:bin/%=%).pro
	$(MAKE) -C $(TST_DIR)


# Tests

CATCH2_BASE = $(CATCH2_DIR)/catch2
export CATCH2_BASE

test: Catch2 MCDS LIBCS
	# Add new directories with tests here and also below under clean:
	$(MAKE) -C $(TST_DIR)/cellular_potts/tests run_all_tests


# Cleanup

clean:
	$(MAKE) -C $(XSDE_DIR) clean
	# MCDS make clean is broken, so do it by hand here
	rm -f $(MCDS_DIR)/libMCDS/mcds_api/*.o $(MCDS_DIR)/libMCDS/mcds_api/*.a
	$(MAKE) -C $(LIBCS_DIR) clean
	$(MAKE) -C $(CATCH2_DIR) clean
	# This fails if it hasn't been built and there's no Makefile, that's fine
	-$(MAKE) -C $(TST_DIR) clean
	rm -rf bin $(TST_DIR)/Makefile $(TST_DIR)/.qmake.stash
	$(MAKE) -C $(TST_DIR)/cellular_potts/tests clean
