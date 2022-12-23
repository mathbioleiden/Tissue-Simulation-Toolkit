# Tissue-Simulation-Toolkit

Welcome to the Tissue Simulation Toolkit, a library for
two-dimensional simulations of Glazier and Graner's Cellular Potts
model (Glazier and Graner, 1993).

The TST aims to provide a simple set of computational tools to get you
started with Cellular Potts Simulations.

The current version of the TST includes example programs for the
following published simulations:

* Differential adhesion driven cell sorting (Glazier and Graner, 1993)
* Cell elongation dependent vasculogenesis (blood vessel growth) (Merks et al., 2006) 
* Contact-inhibition dependent vasculogenesis and angiogenesis (Merks and Glazier, 2005; Merks and Glazier, 2006; Merks et al, PLoS Comput Biol 2008)

The TST provides many recent extensions to the CPM, including

* Infinite number of PDE layers (forward Euler)
* Interaction of CPM cells and PDE (secretion, absorption)
* Chemotaxis
* Length and connectivity constraints

and visualization of:

* Cells, according to cell type or anything you wish
* Chemical fields, using color ramps and contour lines (level sets)

## Downloading and installing

The TST is available from GitHub at https://github.com/rmerks/Tissue-Simulation-Toolkit. It can be built and run on Windows, macOS and Linux using the instructions below.

### Windows

The easiest way to install and work with the TST on Windows is via the Windows Subsystem for Linux. This provides an Ubuntu Linux-like environment within Windows, within which you can install TST. Opening a WSL2 terminal and following the Linux instructions should get you there.

### macOS

On macOS, you need to install the XCode development environment from Apple to get the required tools, including the command line tools. You will need to specifically select the command line tools in the installer.

To install the dependencies, we recommend installing [Homebrew](https://brew.sh). Once you have that installed, you can install QT5, libpng and zlib using

```
brew install qt@5 libpng zlib
```

You may have to edit `src/Tissue-Simulation-Toolkit.pro` for qmake to be able to find them.

Next, you can get the source by cloning the repository from GitHub. You can use the following commands in a Terminal:

```
git clone git@github.com:rmerks/Tissue-Simulation-Toolkit.git main
cd Tissue-Simulation-Toolkit
Tissue-Simulation-Toolkit$ git submodule init
Tissue-Simulation-Toolkit$ git submodule update
```

If you are on a Mac with Apple Silicon (M1 or M2), then you will have to modify the file `lib/MultiCellDS/v1.0/v1.0.0/Makefile` to get the TST to compile. Find the line

```
export COMPILE_CFLAGS := -O3 -s -mfpmath=both -m64 -std=c++11
```

And remove the `-s -mfpmath=both` so that it reads

```
export COMPILE_CFLAGS := -O3 -m64 -std=c++11
```

If you're not sure whether you have Apple Silicon in your Mac, you can just try to compile and see if you get an error, or you can edit the file and remove these options anyway, as it works fine without them.

The TST can then be built using

```
Tissue-Simulation-Toolkit$ make
```

See below for how to run a simple simulation to test if it's all working.

### Linux

To compile the TST, C and C++ compilers are needed, as well as the usual helper tools like `ar` and `ranlib`, and `make` for the build system. The TST also requires the zlib, libpng, OpenCL and QT5 libraries. On a recent Ubuntu or another Debian-based distribution (we tested Ubuntu 22.04), you can install the requirements using

```apt install gcc g++ binutils make zlib1g-dev libpng-dev ocl-icd-opencl-dev libqt5opengl5-dev```

To get the source, clone the repository from GitHub:

```
git clone git@github.com:rmerks/Tissue-Simulation-Toolkit.git main
cd Tissue-Simulation-Toolkit
Tissue-Simulation-Toolkit$ git submodule init
Tissue-Simulation-Toolkit$ git submodule update
```

The TST can then be built using

```
Tissue-Simulation-Toolkit$ make
```

See below for how to run a simple simulation to test if it's all working.

## Test the Tissue Simulation Toolkit

If compilation was successful, then the `bin/` folder contains an executable called `vessel'. This executable needs to be run from the `bin/` folder, and passed the location of a parameter file. You can run a test simulation like this:

```
Tissue-Simulation-Toolkit$ cd bin
Tissue-Simulation-Toolkit/bin$ ./vessel ../data/chemotaxis.par
```

## Who do I talk to?

* Roeland Merks
