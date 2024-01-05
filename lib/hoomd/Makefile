.PHONY: all
all: hoomd

ifndef HOOMD_CORES
    HOOMD_CORES := $(shell nproc 2>/dev/null || echo NOTFOUND)
    ifeq ($(HOOMD_CORES),NOTFOUND)
        # try macOS, or if that doesn't work default to 2
        HOOMD_CORES := $(shell sysctl -n hw.logicalcpu 2>/dev/null || echo 2)
    endif
endif

PY_EXT_SUFFIX := $(shell python3 -c 'import sysconfig as s ; print(s.get_config_var("EXT_SUFFIX"))')
HOOMD_LIB := build/hoomd/hoomd/_hoomd.$(PY_EXT_SUFFIX)

.PHONY: hoomd
hoomd: $(HOOMD_LIB)

# Set HOOMD_BUILD_OPTIONS to e.g. -DENABLE_GPU=ON -DENABLE_MPI=ON
# Build with venv enabled, hoomd will pick it up and install into it later
$(HOOMD_LIB):
	python3 hoomd-blue/install-prereq-headers.py -y
	mkdir -p build/hoomd
	cd build/hoomd && cmake ../../hoomd-blue -DBUILD_TESTING=OFF $(HOOMD_BUILD_OPTIONS)
	cmake --build build/hoomd -j $(HOOMD_CORES)

# Build with venv enabled to install dependencies correctly
.PHONY: install
install: $(HOOMD_LIB)
	python3 hoomd-blue/install-prereq-headers.py -y
	cmake --install build/hoomd

.PHONY: clean
clean:
	rm -rf build

