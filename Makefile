MCDS_DIR  = lib/MultiCellDS/v1.0/v1.0.0
XSDE_DIR  = $(MCDS_DIR)/libMCDS/xsde
LIBCS_DIR = lib/libCellShape
CATCH2_DIR = lib/Catch2
TST_DIR   = src
QMAKE     = qmake
# Edit the above line as necessary, e.g., as follows:
#QMAKE 	  = /Applications/Qt5/6.4.0/macos/bin/qmake

MODELS = bin/vessel bin/qPotts bin/sorting bin/Act_model

.PHONY: all XSDE MCDS LIBCS TST clean

all: $(MODELS)


XSDE:
	$(MAKE) -C $(XSDE_DIR)

MCDS: XSDE
	$(MAKE) -C $(MCDS_DIR) objects

LIBCS: MCDS
	$(MAKE) -C $(LIBCS_DIR)

Catch2:
	$(MAKE) -C $(CATCH2_DIR)

bin/%: MCDS LIBCS
	cd $(TST_DIR) && $(QMAKE) $(@:bin/%=%).pro
	$(MAKE) -C $(TST_DIR)

clean:
	$(MAKE) -C $(XSDE_DIR) clean
	# MCDS make clean is broken, so do it by hand here
	rm -f $(MCDS_DIR)/libMCDS/mcds_api/*.o $(MCDS_DIR)/libMCDS/mcds_api/*.a
	$(MAKE) -C $(LIBCS_DIR) clean
	$(MAKE) -C $(CATCH2_DIR) clean
	$(MAKE) -C $(TST_DIR) clean
	rm -rf bin $(TST_DIR)/Makefile $(TST_DIR)/.qmake.stash
