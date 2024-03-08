How TST is built
================

The Tissue Simulation Toolkit consists mainly of C++ code, but there are also
parts written in Python, it depends on several externally developed libraries,
and it uses the Qt framework for graphics. As a result, building a working model
from the sources takes quite a few steps. It's all automated, so doing it should
be relatively easy, but if you need to change something then you need to
understand how it all works, and that's what this document explains.

The compilation process is driven my the ``Makefile`` in the root of the
repository. It defines two main targets as well as a number of additional
targets that are useful while developing. The main targets are ``all``, which
builds all the C++ code and the C++-only models, and ``with_adhesions`` which
builds everything needed for a coupled CPM-ECM simulation with adhesions, as
needed to model adhesions in detail. This second target will also build Python
and MUSCLE3, as they are needed for that setup. Some of the TST code comes with
unit tests, which can be built and run using ``make test``.


C++
---

The basic target in the central ``Makefile`` for building the C++ CPM-only
simulations is ``all``. This builds a set of executables in the ``bin/``
subdirectory from the main model definitions in ``src/models``.

These models plot their state on the screen, for which they use the Qt
framework. Qt comes with its own build tool called ``qmake``, which generates a
Makefile from which an executable can then be built. In the ``src/`` directory,
you'll find a ``.pro`` file for each model with settings specific to that model.
The file ``Tissue_Simulation_Toolkit.pri`` contains all the shared definitions.

So, to build a model binary, the main ``Makefile``, in its ``bin/%`` target,
calls QMake in the ``src/`` directory to create a ``src/Makefile`` from
``src/<model>.pro``, and then it calls ``make`` in ``src/`` to build the model.
Running QMake again will overwrite the generated ``src/Makefile``, so the models
have to be built one after the other. Fortunately, GNU make can do that if we
tell it to using ``.NOTPARALLEL``.


Tests
-----

Some of the C++ code has unit tests, which are located in various ``tests/``
subdirectories within ``src/``. Each of these directories has a ``Makefile``
that can build and run the tests in that directory. These directories are
referenced from the main ``Makefile`` and they're not discovered automatically,
so if you add tests in a new directory, then that directory needs to be added in
the main ``Makefile`` for them to be built and run. ``make test`` will call
``make`` in each of these directories to build and run the tests. Note that
QMake isn't used here.


Dependencies
------------

The C++ code has several dependencies, which can be found in the ``lib/``
directory. These are developed externally, but are included in the git
repository as `submodules
<https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_. Git submodules
are a nice idea, but the user interface is fairly awful, making them tricky to
use. It does make sense to use them here though, so we do, and hope that the git
maintainers will fix things in the future.

Hopefully, you've cloned the repository using ``git clone --recursive``. If you
forgot the ``--recursive`` part, running ``git submodule init`` and then ``git
submodule update`` should fix things up and get you a complete tree with the TST
code in ``src/`` and also the dependencies in ``lib/``.

The main C++ code uses ``MultiCellDS``, ``libCellShape``, ``json``, and
``Catch2`` for the tests. For ``MultiCellDS`` and ``libCellShape``, the main
``Makefile`` calls their own build systems (which are also make-based) directly.
Note that ``libCellShape`` depends on ``MultiCellDS`` which in turn includes a
dependency called ``XSDE`` that needs to be built separately, so it's all a bit
messy. You're unlikely to need to touch this though.

``json`` is a header-only library that does not need to be compiled separately.
``Catch2`` used to be header-only, but unfortunately feature creep has set in
and it needs to be compiled and installed these days. There's a separate
``lib/Catch2/Makefile`` that takes care of this. ``Catch2`` is built using
CMake, so the ``Makefile`` calls ``cmake`` and ``make`` to build it, and then
installs ``Catch2`` into ``lib/Catch2/catch2``. The Makefiles for the tests will
pick it up there (see below).

``hoomd`` is a molecular dynamics package that we use to simulate the
extracellular matrix in TST-ECM coupled simulations. It is written in C++ but
has a Python interface, so it needs to be compiled first, and then installed
with the rest of the Python code (see below for that). The setup is the same as
for ``Catch2``, there's a ``lib//hoomd/Makefile`` which calls ``hoomd``'s build
system.

MUSCLE3 is a model coupling framework that we use to connect the Cellular Potts
Model and the hoomd-based ECM simulation together. Like ``Catch2`` it needs to
be compiled and installed, which is done by ``lib/muscle3/Makefile`` after which
``lib/muscle3/muscle3`` contains a working ``libmuscle`` library that the C++
code in ``TST`` can link against. There's also a Python version of
``libmuscle``, which is installed separately with the rest of the Python parts.


Python
------

Some parts of the Tissue Simulation Toolkit are written in Python, in particular
the coarse-grained molecular dynamics-based simulation of the extracellular
matrix. Python source code, like the C++ source code, lives in the ``src/``
subdirectory. When building with ``make python``, a Python virtual environment
will be set up in ``venv/``, and the Python code will be installed into it. This
is done using ``pip install -e``, which results in a so-called editable install.
What that means is that you don't need to reinstall after changing any of the
Python code, you can just rerun and the changed will be available immediately.

The Python code does not currently have any unit tests, but it does have type
annotations which can be checked using ``mypy``. To do this, you need to install
the ``mypy`` and ``tox`` Python packages, and then run ``make test``. Settings
for all this are in ``pyproject.toml`` as usual for Python packages.

A few things are worth noting:

- The ``src/`` directory gets mapped to a top-level
  ``tissue_simulation_toolkit`` package, so that e.g. the class ``MDState`` in
  ``/src/ecm/ecm.py`` can be imported from Python using ``from
  tissue_simulation_toolkit.ecm.ecm import MDState``.

- ``hoomd`` cannot be installed from PyPI, so it's not listed as a dependency in
  ``pyproject.toml``. Instead, the main ``Makefile`` will build it (as described
  above) and then install it into the ``venv/`` virtual environment as needed.

- ``mpi4py`` can be installed from PyPI, but requires an MPI library with
  development headers to be available to install correctly. It's installed by
  the main ``Makefile`` only if building ``with_adhesions``, because it's needed
  for that. Building with ``make python`` will not install ``mpi4py``, so that
  any Python parts we may make in the future that don't use MPI can be used
  without installing an MPI library.

- ``muscle3`` can be installed from PyPI, but this will only install the main
  system and the Python bindings. The C++ bindings need to be compiled and
  installed separately (see above). The version needs to be the same on both
  sides for the Python-based ECM and the C++-based CPM to be able to talk to
  each other, so if you upgrade, make sure to update both the submodule and the
  ``pyproject.toml`` to the same new version.


MUSCLE3
-------

As mentioned, we use the MUSCLE3 model coupling framework to connect the
Cellular Potts Model to the Extracellular Matrix simulation. In a MUSCLE3
coupled simulation, each model is its own separate program. These programs run
simultaneously and exchange messages over the network (see `cpm_ecm.rst`_ for a
detailed description).

In the CPM-ECM case, the CPM part is a normal TST model (see
``src/models/adhesions.cpp``) that is built as described above using QMake,
except that it has an additional dependency on MUSCLE3 (which is built as
described above). The ECM model is a Python script (see
``src/ecm/simulate_ecm.py``) that gets installed into the virtual environment at
``venv/`` with the rest of the Python code.

The coupled simulation is controlled by a configuration file called the yMMSL
file. This is a YAML file that contains a description of which models there are,
how they can be started, how they should be wired together, and it has a list of
settings that models can access.

The main configuration file for the CPM-ECM simulation is built from a source
file in ``src/models/`` by the main ``Makefile``. This step really just replaces
the string ``Tissue-Simulation-Toolkit`` with the actual directory that you
cloned TST into, so that MUSCLE3 can find the virtual environment and the model
executables. The result is placed in ``ymmsl/``, from where it can be used to
start the simulation as described in `cpm_ecm.rst`_.

