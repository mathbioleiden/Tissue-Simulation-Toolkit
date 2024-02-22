Cellular Potts - Extracellular Matrix coupled simulation
========================================================

The Cellular Potts Model (CPM) models one or more cells sitting on or in a
substrate. In an organism, that substrate is the Extracellular Matrix (ECM). In
the CPM, this matrix isn't represented explicitly, which limits the amount of
detail with which cell-ECM interactions can be modelled.

The Tissue Simulation Toolkit solves this by adding a separate simulation of the
ECM using coarse-grained molecular dynamics (MD). CPM cells can then form
adhesions with which they can grab the ECM, thus applying a force to it, which
is resisted by the ECM resulting in a counterforce. As the simulations run,
these forces are exchanged as boundary conditions between the models.


Simulation design
-----------------

The CPM-ECM coupled simulation has two main components: the CPM and the ECM. The
CPM models the cells and their adhesions on a grid of pixels, with each pixel
containing the number of the cell it is a part of, or 0 if there is no cell
present.

The ECM is represented by a large number of simulated collagen fibrils, each
represented by a small number of particles connected by bonds, which resist
stretching, compression and bending loads. The fibrils are connected by
crosslinkers to create a coherent material.

Cells in the CPM can form adhesions, which are represented by a particle as
well. This particle is connected to a CPM cell occupying the pixel it is inside
of, and can be connected to the beads in the ECM fibrils by a bond. These bonds
are modelled as linear springs, which stretch or compress as the cell tries to
move.

The models influence each other via the forces created by the bonds between
the adhesion beads. If a cell in the CPM wants to move an adhesion particle,
then it needs to stretch the bond(s) it is attached to, and the energy this
takes is taken into account in the copy attempt. Likewise, if the ECM wants to
move a fibril particle that is bonded to an adhesion, then it will have to
stretch or compress the bond spring accordingly.

Thus, the models occupy adjacent domains and exchange boundary conditions in the
form of forces between MD particles. The ECM "sees" the adhesion particles of
the CPM, while the CPM "sees" any fibril particles that share a bond or angle
constraint with the ECM. This collection of adhesion and associated fibril
particles we call the *boundary*.

Coupling
''''''''

A coupled simulation run starts with creating an initial ECM, which is done by a
separate component (see below). The ECM is then equilibrated using the main
simulation code, after which the CPM and the ECM run in parallel. After
initialising (which is done internally for the CPM), the CPM sends a set of
interaction attempts to the ECM model. These can be the creation of new
adhesions, or movement of existing ones [1]_. At the same time, the ECM sends
to the CPM the current location of all the fibril particles in the boundary, as
well as the bonds and angle constraints involving them.

The CPM stores the locations of the boundary particles and associated
constraints in a data structure called the ``AdhesionIndex``, which stores them
in a form that allows for efficient access for calculating forces on the
adhesion particles. The ECM meanwhile updates its state based on the requested
interactions.

Now both models run, the CPM performing one Monte Carlo step (MCS) and the ECM
running a number of timesteps to re-equilibrate the forces between the
particles. During the MCS, the CPM considers the fibrils to be fixed in space,
it only (potentially) moves the adhesion particles. Vice versa, the adhesion
particles are fixed in the ECM model, which only moves the fibrils.

When the MCS and equilibration are done, the models loop back and communicate
again as described above, and this process is repeated for however many
timesteps are set in the configuration.


Implementation
--------------

MUSCLE3 coupling
''''''''''''''''

The CPM-ECM coupled simulation is implemented using the MUSCLE3 model coupling
framework. MUSCLE3 coupled simulations consist of separate, independent programs
that exchange messages as they run. The simulation consists of three main
programs, plus an additional optional one that produces output. The main
programs are ``make_ecm``, which makes the initial extracellular matrix,
``simulate_ecm``, which is used to equilibrate the initial ECM and also to
simulate its behaviour during the main part of the run, and ``cellular_potts``,
which simulates the cells.

MUSCLE3 calls these programs simulation components, or components for short.
Components communicate by sending messages to each other. Each component has a
set of named *ports*, which it can send messages to or receive messages from.
The MUSCLE3 configuration file specifies which components there are, and how
their ports are connected. By changing the configuration file, the connections
between the components can be changed as needed to do different kinds of things.

The current simulation is defined in ``src/models/adhesions.ymmsl.in``. It
describes all four components described above, and then connects them together.
The ``make_ecm`` component has a port named ``ecm_out`` on which it sends the
ECM it creates. This port is associated with the so-called ``o_f`` *operator*,
which specifies that this port is used to send the Final Output of the
component. This port gets connected (via a *conduit*, which is a tube that the
messages pass through from one port to another) to the ``ecm_in`` port on the
``equilibrate_ecm`` component. This ``ecm_in`` is an ``f_init`` port, meaning
that ``equilibrate_ecm`` can receive messages on it that it uses to initialise
its state at the beginning of the run.

The ``equilibrate_ecm`` component then runs a number of MD steps to equilibrate
the forces, during which it doesn't communicate, and then it sends the final
result on its ``ecm_out`` port (also ``o_f`` of course). This port is connected
to the ``ecm_in`` port of ``simulate_ecm``, which initialises itself using the
received equilibrated ECM data (and so that ``ecm_in`` port is an ``f_init``
port).  ``simulate_ecm`` then goes and runs, and while it does so it
communicates with ``cellular_potts``.

The ``cellular_potts`` model has its own built-in initialisation, so it does not
have any ``f_init`` ports. It does have three other ports though, which are for
communicating inside of its main loop (the one that does Monte Carlo steps). The
first one of these is called ``cell_ecm_interactions_out``, and it is used to,
at each MCS, send the desired interactions with the ECM. This is not the final
output but an intermediate one, so it's an ``o_i`` type port. Then there is
``state_out``, which is used once in a while to send out the entire state (see
below). Finally there is an ``ecm_boundary_state_in`` port, on which
``cellular_potts`` receives the current state of the boundary between the ECM
and the CPM (more on that below). This is of type ``s``, because the information
received is used during the subsequent state update.

As you can imagine, ``simulate_ecm`` has the opposite ports: an
``ecm_boundary_state_out`` to send the state of the boundary particles (of type
``o_i``, this being an intermediate output), and a ``cell_ecm_interactions_in``
to receive the interactions (of type ``s``). Like ``cellular_potts``,
``simulate_ecm`` has a ``state_out`` port on which it periodically sends its
whole state.

As a result of this coupling scheme, the simulation runs by first running
``make_ecm``, then ``equilibrate_ecm``, and then ``cellular_potts`` and
``simulate_ecm`` simultaneously and in lock-step.

The yMMSL file consists of three more sections, ``settings``, ``resources`` and
``implementations``. The ``settings`` are essentially a dictionary containing
named values that can be used by the models. If an entry here starts with the
name of a component, followed by a period and the name of the setting, then that
setting applies specifically to that component. Otherwise, it applies to all of
them. The TST C++ code has its own Parameters system (see
``src/util/parameters.hpp``), which for the ``cellular_potts`` model these
parameters are loaded into. As a result, you only need to set them once in the
yMMSL file, and they'll show up everywhere automatically.

The ``resources`` section specifies how many cores to use for each component. By
default, the components all run as single-threaded programs, but for larger
simulations the ``simulate_ecm`` program can be run with MPI, in which case it
can use multiple cores. See `Going faster`_ below.

Finally, the ``implementations`` section specifies how to start the different
programs. For the Python programs, it activates the virtualenv at ``venv/``
(which all the Python code gets installed into, see the documentation on the
build system) and runs a command (these are mapped to a specific Python function
in ``pyproject.toml``). For the C++ code, it needs to set the
``LD_LIBRARY_PATH`` to make MUSCLE3 available, and then it runs the executable
in ``bin/``. There are also some configurations for debugging and profiling,
which are explained below in `Developing`_.

So this defines the overall structure. The rest of this section describes the
components in more detail.


Cellular Potts Model
''''''''''''''''''''

The CPM side of the simulation consists mostly of the ``CellularPotts`` class
from TST, with an additional extension for computing the work required to move
the adhesion particles. The source code for this can be found in the
``src/adhesions/`` directory.

As described above, there are two things the CPM needs to do: 1) receive the
locations of the particles in the boundary, and calculate the work required to
move the adhesions, and 2) move the adhesions, and keep track of these moves so
that they can be sent to the ECM.

Part 1) starts with receiving an ``ECMBoundaryState`` object with the particles
and the bonds. This is passed to an ``AdhesionMover``, which is the main class
implementing the adhesions. It uses the received data to (re)build its
``AdhesionIndex``, which stores that data in an efficient-to-access way and
which can use that stored data to calculate the work required to move an
adhesion particle.

The CPM simulation can then ask the ``AdhesionMover`` to calculate the
additional work required to copy a cell that has an adhesion particle in it,
and/or to copy a cell onto a cell that has an adhesion particle in it. This
entails choosing whether and where to move the adhesion, the logic for which is
in a number of functions in ``adhesion_movement.cpp``, and the ``AdhesionIndex``
is used to calculate the resulting energy requirement.

Part 2) starts when an adhesion is moved. As this move needs to be taken into
account for subsequent copy attempts, the ``AdhesionIndex`` needs to be updated,
so that is done by the ``AdhesionMover``. The ``AdhesionIndex`` has an
``ECMInteractionTracker`` which keeps track of the changes that were made. At
the end of the Monte Carlo step, ``CellularPotts`` will ask the
``AdhesionMover`` for these changes, which will get them from its
``AdhesionIndex`` which gets them from the ``ECMInteractionTracker``. The
tracker is then reset for the next MCS.

The main program for the CPM side of the coupled simulation is in
``src/models/adhesions.cpp``. This is currently basically the ``chemotaxis.cpp``
model, but with additional code for communicating with the ECM. When running
with MUSCLE3, no ``.par`` file is used. Instead, parameter values are obtained
from MUSCLE3 via its settings mechanism (see `MUSCLE3 coupling`_) and loaded
into the TST parameters object via a utility function in
``src/util/muscle3/settings.hpp``.

On timestep zero, the CPM sends a special interaction request which asks the ECM
to randomly convert a number of fibril particles into adhesion particles.
Conceptually, this is a bit funny, but it's what was done in the original TST-MD
code as a way of getting started. This and moving adhesions are currently the
only kinds of interactions implemented, so a bit of work needs to be done to be
able to dynamically add and remove adhesion particles. This is left as an
exercise for the reader :).

Note that the code in ``src/models/adhesions.cpp`` is a bit messy, and not a
nice example of what a MUSCLE3 simulation component should look like. This is
currently the way that TST models are written, so it is what it is at least for
now. MUSCLE3 was designed to be flexible though specifically to cater to this
situation, so it all does work.

Extracellular matrix
''''''''''''''''''''

The ECM simulation is implemented in Python using the hoomd particle simulator.
The implementation can be found in ``src/ecm/``. The ``Simulation`` class
implements the simulation of the ECM. It is initialised with an initial ECM via
an object of type ``MDState``, and it receives a set of parameters governing its
operation. ``apply_interactions()`` can be used to apply a received interaction
request represented by a ``CellECMInteractions`` object, after which the
``run()`` method runs a number of timesteps set by the parameters, and then
``get_boundary_state()`` is used to extract the state of the adhesion particles
and the fibril particles attached to them as an object of class
``ECMBoundaryState``, for sending to the CPM.

The state of the ECM, i.e. the particles and bonds and angle constraints and
their types, are kept by ``hoomd``, possibly on the GPU. ``Simulation`` uses an
instance of class ``Boundary`` (also in ``simulation.py``) to keep track of
which particles are in the boundary, so that it can extract only those as
needed. Since the boundary is only a tiny fraction of the whole state, this
saves a lot of time.

The easiest way of interacting with ``hoomd`` is to use a so-called snapshot,
which is a copy of the simulation state. When running on multiple cores with
MPI, the snapshot conveniently collects all the data on the MPI process with
rank 0, so that it's easy to process. Unfortunately, this is also rather slow
and it was holding up the simulation, so we use a ``hoomd`` local snapshot and a
bunch of custom MPI communication to extract the data. For the ECM size I
tested, this brought the duration of one ECM run down from 280 ms to 25 ms, so
it's worth the extra complexity.

The main program is in ``src/ecm/simulate_ecm.py``. It sets up the simulation,
gets parameters from MUSCLE3, receives an initial ECM configuration, and then
runs the main loop, on each iteration communicating with TST. It also sends the
final state of the ECM out at the end of the simulation.

Besides the main part of the code in ``simulation.py`` and ``simulate_ecm.py``,
there are various helpers in ``src/ecm/`` that require some explanation:

``parameters.py``
    Contains two data classes with the parameters used when generating and
    evolving the ECM. These are obtained from MUSCLE3 and loaded into an object
    of these classes by the ``from_settings()`` function in ``muscle3.py``.

``muscle3.py``
    Contains helper functions for encoding and decoding the data we're
    exchanging between dictionaries (which MUSCLE3 knows how to send) and the
    classes we use to represent them in the rest of the code.

``muscle3_mpi_wrapper.py``
    This is a helper class to compensate for the fact that MUSCLE3 doesn't
    support MPI in Python (yet). It defines an ``Instance`` class that wraps
    MUSCLE3's ``Instance`` class and does the things that need to be done when
    running in parallel with MPI (see also `Going faster`_ below). This class
    also works if MPI is not installed at all; if you're on a machine with a
    single GPU then MPI doesn't really add anything so it's nice for it to be
    optional. When MUSCLE3 gets MPI support for Python then this class can be
    removed.

Making the initial ECM
''''''''''''''''''''''

Before we can start the simulation, an initial ECM needs to be generated. This
is done by a separate program at ``src/ecm/make_ecm.py``. This generates the ECM
using code taken from TST-MD, and then sends it out to the rest of the
simulation. ``make_ecm.py`` is just a very simple MUSCLE3 component, the actual
generation code is in ``src/ecm/network/``.

Producing output
''''''''''''''''

No science is complete without some pretty pictures, so the simulation needs to
produce some output. The CPM part of the code will plot its state to the screen
when running as usual, but it cannot show the ECM in the plot because it doesn't
have that information. Vice versa, the ECM component has its own state, but
doesn't know where the cells are.

So, in order to create a plot showing both, this information needs to be brought
together. This is optionally done every N timesteps, with N set by the
``state_output_interval`` setting. At these points, both ECM and CPM will send
an extra message containing their entire state. These messages are routed to a
separate component that either writes them to disk
(``src/cpm_ecm/state_dumper.py``) or plots them on the screen
(``src/cpm_ecm/state_viewer.py``). A little program in
``src/scripts/plot_states.py`` can be used to create a series of PNG files from
the dumped states, which can then be encoded into a movie file.

The extra simulation component is not in ``src/models/adhesions.ymmsl.in``, but
``src/models/dump_state.ymmsl.in`` or ``src/models/plot_state.ymmsl.in``. To
enable either (or both), you can add them to the ``muscle_manager`` command
line. See `Running locally`_ below for examples.

Note that the plotting here is done using the Matplotlib-based plotting code
from ``TST-MD``. This is very slow. ``TST-MD-V2`` has some faster Qt-based code,
and making a ``qt_state_viewer.py`` based on that is probably a very nice little
project to get familiar with MUSCLE3 and the whole setup. Meanwhile, this works.


Building the coupled simulation
-------------------------------

(This is for running locally, see `Running on Snellius`_ below if you're on
Snellius or another HPC machine.)

The coupled simulation, and the components needed for it, aren't built by
default if you use ``make``, they need to be built explicitly. This is supported
on Linux and MacOS, and it may require installing some extra dependencies, in
particular Python and possibly MPI and CUDA.

The ECM simulation uses HOOMD, which can use a GPU (if you have one) and/or MPI
(if you want to run on multiple CPUs or multiple GPUs). This will really speed
things up, so it's recommended to make the effort. Depending on your
configuration, here's what you need. (Note that we're counting physical CPU
cores, not hyperthreads, and that if you have a fairly recent midrange laptop or
desktop, then you probably have more than two physical cores.)

Note that the instructions below assume you've already followed the instructions
from the README at least up to ``make``, so that you have Qt and the other
dependencies installed.


No GPU, two CPU cores or less
'''''''''''''''''''''''''''''

Neither MPI or GPU support will help, so we'll build without either. Use

.. code-block:: bash

    Tissue-Simulation-Toolkit$ make with_adhesions


No GPU, more than two CPU cores
'''''''''''''''''''''''''''''''

Build with MPI support to use multiple CPU cores for the ECM simulation.

You'll need to install MPI first if you don't have it already. On Ubuntu:

.. code-block:: bash

   $ sudo apt install openmpi-dev


On MacOS you can use Homebrew or MacPorts:

.. code-block:: bash

   $ brew install open-mpi
   $ sudo port install openmpi


Then, you can build using

.. code-block:: bash

    Tissue-Simulation-Toolkit$ ENABLE_MPI=1 make with_adhesions


One GPU
'''''''

Build with GPU support, MPI won't help and is not needed.

On a local machine, you'll need to install CUDA first following the instructions
on the nVidia website. AMD GPUs can work in theory as long as they support HIP,
but in practice this may be tricky.

Then, you can build using

.. code-block:: bash

    Tissue-Simulation-Toolkit$ HOOMD_BUILD_OPTIONS=-DENABLE_GPU=ON make with_adhesions


Multiple GPUs
'''''''''''''

Build with both MPI and GPU support to use all of them.

You'll need to install MPI first if you don't have it already. On Ubuntu:

.. code-block:: bash

   $ sudo apt install openmpi-dev


On MacOS you can use Homebrew or MacPorts:

.. code-block:: bash

   $ brew install open-mpi
   $ sudo port install openmpi


On a local machine, you'll need to install CUDA first following the instructions
on the nVidia website. AMD GPUs can work in theory as long as they support HIP,
but in practice this may be tricky and we haven't tried it.

Once CUDA is there, you can build using

.. code-block:: bash

    Tissue-Simulation-Toolkit$ ENABLE_MPI=1 HOOMD_BUILD_OPTIONS=-DENABLE_GPU=ON make with_adhesions


Known issues
''''''''''''

Building the coupled simulation will take some time, hoomd in particular is very
slow to build. Not much to do about it other than to go have lunch, or go do
something else for a bit. Note that almost all of that time is spent building
hoomd and the other dependencies, so if you change something in TST and then
rebuild, the rebuild will only rebuild TST, which is nice and quick. So this is
a one time wait.

If you get the following error

.. code-block::

    c++: fatal error: Killed signal terminated program cc1plus


then the hoomd build ran out of memory. Hoomd seems to need a large amount of
memory to build, and we run multiple compilers in parallel to speed things up.
If together they try to use more memory than you, have, this rather unhelpful
error will appear. To solve it, you need to reduce the amount of parallelism by
using fewer cores to build hoomd. The TST build system uses every core you have
by default, but this can be changed by setting HOOMD_CORES:

.. code-block:: bash

    Tissue-Simulation-Toolkit$ HOOMD_CORES=4 ENABLE_MPI=1 make with_adhesions


or whichever combination of options you selected above.


Running locally
---------------

Once the build is done, it's time to run the simulation. The Python parts of the
simulation will have been installed in a virtual environment called ``venv``, in
the top TST directory. MUSCLE3 is also in there, and we're going to start the
simulation via MUSCLE3, so we need to activate it first. Then, we can ask the
MUSCLE3 manager to run the simulation for us:

.. code-block:: bash

    Tissue-Simulation-Toolkit$ . venv/bin/activate
    Tissue-Simulation-Toolkit$ muscle_manager --start-all ymmsl/adhesions.ymmsl ymmsl/plot_state.ymmsl


You will see a two windows pop up, one is the graphics output from the Cellular
Potts Model, the other one the combined display described above under
`Producing output`_. It takes a few seconds for data to appear, because the ECM
needs to be built first, and that has no visible output. Once the ECM is ready,
it is sent to the ECM simulation component and that and the CPM can start
running.

Once the run is done, you'll find a directory named
``run_adhesions_<date>_<time>/``, which we call the *rundir*. This directory
contains a file documenting the configuration of the model as run, a log file
for the manager, performance information (see the `MUSCLE3 documentation`_), and
a subdirectory ``instances/`` in which you can find a directory with output for
each of the components. It's a good idea to have a look through these files and
see what you can find where.

One note: you may see something like this at the end of the
``muscle3_manager.log`` file:

.. code-block::

    muscle_manager 2023-11-14 21:11:47,489 INFO    libmuscle.manager.instance_manager: Instance make_ecm finished with exit code 0
    muscle_manager 2023-11-14 21:11:47,489 INFO    libmuscle.manager.instance_manager: Instance cellular_potts finished with exit code 0
    muscle_manager 2023-11-14 21:11:47,489 INFO    libmuscle.manager.instance_manager: Instance state_dumper finished with exit code 0
    muscle_manager 2023-11-14 21:11:47,489 INFO    libmuscle.manager.instance_manager: Instance equilibrate_ecm finished with exit code 0
    muscle_manager 2023-11-14 21:11:47,489 INFO    libmuscle.manager.instance_manager: Instance simulate_ecm finished with exit code 0
    muscle_manager 2023-11-14 21:11:47,489 ERROR   libmuscle.manager.instance_manager: At this point, one or more instances crashed because they lost their connection to another instance, but no other crashing instance was found that could have caused this.
    muscle_manager 2023-11-14 21:11:47,489 ERROR   libmuscle.manager.instance_manager: This means that either another instance quit before it was supposed to, but with exit code 0, or there was an actual network problem that caused the connection to drop.
    muscle_manager 2023-11-14 21:11:47,489 ERROR   libmuscle.manager.instance_manager: Here is the output of the instances that lost connection:


This looks like there was a problem, and there is a problem, but it's in
MUSCLE3, not in TST. What happened is that in the latest release, I redid the
code that analyses the outcome of the simulation, so as to give a better error
message. The new version now gives better explanations of all sorts of weird
corner cases, but I somehow managed to mess up the case where everything goes
well. So it prints the final three ERROR lines instead of saying that the
simulation ran successfully. Doh!

There's already a fix for this in the MUSCLE3 git repository, which will
be released with the next version, so when that's out we'll upgrade and this
will disappear.


Dumping state
'''''''''''''

If you want to make a movie (and who doesn't like movies?), then you need to
save the state of the simulation regularly. There's a separate component that
does this, which can be added to the simulation by adding the
``ymmsl/dump_state.ymmsl`` to the command line. You can remove the plotting, or
run both. Now, in your rundir there will be an ``instances/state_dumper/`` which
has in its ``workdir/`` a collection of data files. To plot the data in these
files to PNG files, there's a helper script in ``src/scripts/plot_states.py``
which gets installed in the virtual environment. So you can run

.. code-block:: bash

    Tissue-Simulation-Toolkit$ plot_states run_adhesions_<date>_<time>


and it will write one PNG file next to each ``.pickle`` file. On Ubuntu, if you
install ``ffmpeg`` then you can convert that to a video using

.. code-block:: bash

    state_dumper/workdir$ ffmpeg -f image2 -framerate 20 -i state_%04d0.png -c:v libx264 -strict -2 -preset slow -pix_fmt yuv420p -f mp4 video.mp4


if you saved every 10th state.

Creating the PNG images is currently rather slow, because we're using
Matplotlib. Making a faster Qt-based version is left as an exercise for the
reader (who can then also update this documentation :)).


Developing
----------

Debugging
'''''''''

The adhesion model included with TST should run out of the box, but
scientifically it leaves something to be desired. A lot, actually, as it's
intended to be a reasonably representative (from a pure performance standpoint)
simulation for benchmarking purposes. To make it scientifically accurate, you're
going to want to do some programming.

Of course, when you're programming your code is most of the time broken (it's
just the natural state of things), and you find yourself trying to fix it. It
can be useful to run the model in a debugger, so that you can step through it.

If you browse to the bottom of the ``src/models/adhesions.ymmsl.in`` file,
you'll find that there's a ``tst_adhesions_debug`` implementation defined.
You'll probably want to modify it a bit to run your favourite terminal
application, e.g. ``gnome-terminal``. Next, scroll up to ``components:`` and
change the implementation for ``cellular_potts`` to ``tst_adhesions_debug`` to
use it.

Once you've done so, you can do ``make ymmsl/adhesions.ymmsl`` in the top
directory to rebuild that file, and run again. Now when you start the model, a
terminal window will pop up with ``gdb`` active, which will work normally. You
can type ``run`` to start, and if it crashes ``bt`` will produce a backtrace.

If your code throws a C++ exception, then it will crash at the place where the
exception is handled, rather than where it was thrown. You probably don't want
that, because you won't be able to see what the problem was. If you type ``catch
throw <exception_type>`` before doing ``run``, then GDB will stop when the
exception is thrown, and you can do a backtrace there. We refer you to the GDB
manual for more, and to the `MUSCLE3 documentation`_.

Profiling
'''''''''

MUSCLE3 has built-in profiling functionality. If you've had a look around a
run directory, you've probably seen a ``performance.sqlite`` file. If you
activate the ``venv`` virtualenv in the top directory, then you'll have the
``muscle3 profile`` command available which will show you some statistics. See
the `MUSCLE3 documentation`_ for how to use it.


Going faster
------------

ECM with MPI support
''''''''''''''''''''

Simulating the extracellular matrix is quite expensive, and if your performance
data show that it is the most expensive part of the simulation, then making it
faster will get you your results sooner. One way to do this is to run on
multiple CPU cores, or even on multiple GPUs.

Hoomd can do that, but only if it's built with MPI support (see above), and if
we tell MUSCLE3 to start it with MPI. At the bottom of
``src/models/adhesions.ymmsl.in`` you'll find a ``simulate_ecm_mpi``
implementation. It's just like ``simulate_ecm``, except that we tell MUSCLE3 to
start the submodel using OpenMPI. To use it, find ``simulate_ecm`` at the top
under ``model/components`` and set its ``implementation`` to
``simulate_ecm_mpi``.

Next, we need to specify the number of MPI processes we want. This is done in
the ``resources`` section, where without MPI we specify ``threads: 1`` to start
the simulation as an ordinary single-threaded program, but where we will now set
``mpi_processes: <N>``. If you have M CPU cores in your machine, then you will
want to set N to at most M-1 cores, so that the Cellular Potts model has a core
to run on. You may also leave a core for the plotter or state dumper, and use
the remaining M-2 cores for the ECM simulation. If you are running on GPU
(see below), then you need to set N equal to the number of GPUs you are using,
as hoomd is designed to use one MPI process per GPU.

If you're getting a message

.. code-block::

    RuntimeError: Error registering instance: An instance with name simulate_ecm was already registered. Did you start a non-MPI component using mpirun?


then you probably somehow ended up with a virtual environment without ``mpi4py``
installed. You can use

.. code-block:: bash

    $ make mpi4py


in the ``Tissue-Simulation-Toolkit`` directory to resolve this.


ECM with GPU support
''''''''''''''''''''

Molecular Dynamics simulations involve many particles, for each of which the
same calculation needs to be done. GPUs are very good at this, so for large
systems using one is a good idea. To run on a GPU, first hoomd needs to be
compiled with GPU support (see above), and then the ``md_use_gpu`` setting needs
to be set to ``true`` in the ymmsl file. And of course you need to have a GPU
:).

If you have multiple GPUs, as on some HPC machines, then you need to combine the
MPI instructions with the GPU instructions, setting the number of MPI processes
to the number of GPUs. Hoomd will then automatically distribute the work over
the available GPUs.


Running on Snellius
'''''''''''''''''''

If you have a large simulation (many pixels, many particles) then you may need
more hardware to run it quickly. The national supercomputer Snellius has this
hardware, in particular it has GPU nodes with four fast GPUs and 72 CPU cores.
If your laptop or desktop isn't quite keeping up, then it's time to move to
Snellius. Here's how to do that.

First, you need to get a Snellius account (talk to Roeland). Once you have one,
you can use ssh to connect to it (see the `Snellius documentation`_), which will
give you a Linux command line on a Snellius head node. This is where we will
build TST.

Getting TST onto Snellius
"""""""""""""""""""""""""

First though, we need to get it onto the machine. If TST were open source, then
we could just ``git clone`` it, but since it isn't, things get a bit more
complicated. There are basically two options: 1) clone locally and then upload
the files to Snellius using ``scp``, or 2) set up SSH agent forwarding and ``git
clone`` on Snellius itself. Option 1) doesn't require any set-up, but is more
cumbersome every time you do it, while option 2) requires some set-up but is
then probably easier in use. Option 2) also has the advantage that you'll be
able to commit and push changes you make on Snellius back to Github directly, as
opposed to having to download them again and push.

To copy files to Snellius, you can use ``scp``. For example, to copy the
``Tissue-Simulation-Toolkit/`` directory to the Snellius scratch file system,
you can type this:

.. code-block:: bash

   $ scp -r Tissue-Simulation-Toolkit snellius.surf.nl:/home/<username>/


If you have any run directories from local runs in your
``Tissue-Simulation-Toolkit`` directory, then you'll probably want to avoid
copying those. I've used ``tar`` before to create a ``.tar.bz2`` with only the
things I wanted (see its ``--exclude`` option) and copied that, then extracted
it on the Snellius headnode. For example:

.. code-block:: bash

   $ tar -c -f TST2.tar.bz2 --exclude 'Tissue-Simulation-Toolkit/run_*' --exclude 'Tissue-Simulation-Toolkit/venv' --exclude 'Tissue-Simulation-Toolkit/.tox' Tissue-Simulation-Toolkit
   $ scp TST2.tar.bz2 snellius.surf.nl:/home/<username>/
   $ ssh snellius.surf.nl
   # on Snellius
   $ tar xf TST2.tar.bz2


If you're packing up a clean tree, which is definitely recommended, then you
don't need the ``--exclude`` options. It will work without them even if you
don't have a clean tree, but those folders contain a lot of files and a lot of
bytes, so your upload may take a while...

So that's a bit of a hassle, and if you make any local changes to the code
you'll have to upload them again in the same way. Or if you make any changes on
Snellius then you'll have to download them. Git is designed for this of course,
and you can use it if you go with option 2), which is explained in the `Github
documentation on SSH agent forwarding
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/using-ssh-agent-forwarding>`_.
Once you have that set up, you can ``git clone`` and ``git pull`` and ``git
push`` on Snellius as usual. If you set up a work branch, then it becomes really
easy to commit a change locally, push it, then pull it on Snellius, or vice
versa, and keep everything nicely synchronised.

Compiling TST on Snellius
"""""""""""""""""""""""""

Since you're on Snellius, you probably want to go fast, so we need MPI and GPU
support. For this we need OpenMPI and CUDA as well as the other dependencies,
and on Snellius (as on most HPC machines) these are already installed and made
available via the ``module`` command. The ``module`` command changes your
shell's working environment in such a way that the program you ask for can be
found. If you log out, your shell quits and the settings disappear, so you'll
have to run this every time you log in.

.. code-block:: bash

   $ module load 2022
   $ module load Qt5/5.15.5-GCCcore-11.3.0 CMake/3.23.1-GCCcore-11.3.0 OpenMPI/4.1.4-GCC-11.3.0 Python/3.10.4-GCCcore-11.3.0 CUDA/11.8.0


With that done, and assuming that you have got the source code onto Snellius, we
can compile everything:

.. code-block:: bash

   $ cd Tissue-Simulation-Toolkit
   Tissue-Simulation-Toolkit$ make clean clean_hoomd
   Tissue-Simulation-Toolkit$ HOOMD_BUILD_OPTIONS='-DENABLE_GPU=ON -DENABLE_MPI=ON' HOOMD_CORES=4 make -j 16 with_adhesions

7:42 TODO -j 16 hoomd -j 4
12:25 -> 4:43 hours


Compiling will take quite a while (more than an hour), so you'll want to go do
something else in the mean time. Do keep the connection open! Otherwise the
shell will crash and compilation will stop.

Once this is done the model is ready to run, except that starting programs works
a bit differently on an HPC machine, and we need to tell MUSCLE3 about this in
the ``src/models/adhesions.ymmsl.in`` file. You can edit this file using
``nano`` (or ``vim``, if you are familiar with it), changing the implementations
for ``equilibrate_ecm`` and ``simulate_ecm`` to ``simulate_ecm_snellius``, and
the implementation for ``cellular_potts`` to ``tst_adhesions_snellius``.

If you look at the bottom of the file, then you'll see that these
implementations differ from the local ones in that they load the modules
required to run the corresponding model programs, and in that the
``simulate_ecm_snellius`` one uses MPI. Because of that, you need to go to
``resources`` and set the resources for ``simulate_ecm`` and ``equilibrate_ecm``
to ``mpi_processes: <N>``, where <N> is the number of GPUs you want to use.

Finally, we want to actually use the GPU, so set ``use_gpu: true`` under
``settings``.

In nano, you can use Ctrl-O to save your changes and Ctrl-X to quit, after which
you can use ``make ymmsl/adhesions.ymmsl`` to rebuild that file.

Running TST on Snellius
"""""""""""""""""""""""

Running programs on a supercomputer works a bit different than locally. So far,
you have logged in to a *head node*, which is a helper computer that is used for
accessing the cluster and compiling software. The head node is not for running
calculations however, and should never be used for that.

To run simulations, you need to submit a job to the scheduler. The scheduler on
Snellius is called Slurm, and its job is to keep a queue of jobs that users want
to run, and run them on the available *worker nodes*. These worker nodes are
often busy (there are many people using Snellius at any one time), so your job
will typically sit in the queue for a bit until there's a worker node available,
after which it will be started on the worker node and run. Any output must be
written to disk, so that you can pick it up when the job is done.

Every job you run consumes a certain number of System Billing Units, or SBUs.
Your account is associated with a budget, from which these SBUs are deducted.
The ``accinfo`` will, after a few seconds, print an overview of the budget
you're using and how many SBUs are left. A full GPU node costs 512 SBUs per
hour, a 1/4 node costs 1/4 of that.

Submitting a job is done using the ``sbatch`` command, which expects to be given
a shell script with the commands to run. There's one for running CPM-ECM on
Snellius in ``src/scripts/snellius_cpm_ecm.sh``. This file looks like this:

.. code-block:: bash

    #!/bin/bash

    #SBATCH -J cpm_ecm
    #SBATCH --time=00:10:00
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=18
    #SBATCH --cpus-per-task=1
    #SBATCH --gpus=1


    module load 2022
    module load Python/3.10.4-GCCcore-11.3.0

    cd ${HOME}/Tissue-Simulation-Toolkit

    source venv/bin/activate

    export QT_QPA_PLATFORM=offscreen

    muscle_manager --start-all ymmsl/adhesions.ymmsl ymmsl/dump_state.ymmsl


Many of the commands here will look familiar if you've run locally and have
built TST. There's a new section at the top however which tells Slurm how many
hardware resources we want. Here's what these options mean:

-J cpm_ecm
    Says that this job is called ``cpm_ecm``. It will be listed as such in the
    queue.

--time=00:10:00
    Specifies for how long we will calculate. The simulation will be shut down
    by the system after this time, *even if it isn't done yet*. The value here
    is 10 minutes. If your settings result in a simulation that takes longer to
    run, then you'll have to ask for more time to make sure that it has a chance
    to finish. Note that it's fine to ask for more time than you end up needing
    (you only pay for what you use), but the longer a period you ask for, the
    longer it may take for Slurm to find you a free worker node.

--partition=gpu
    Snellius has different kinds of worker nodes, some with GPUs, some with
    extra memory, and so on. They are grouped by type into *partitions*, and
    this says that we want a node with GPUs.

--nodes=1
    We're asking for one node here. One worker node in the GPU partition has 72
    CPU cores and four GPUs, which is a huge amount of compute power. It's also
    the maximum we can run on at the moment, because of a limitation in MUSCLE3
    (it doesn't know what a GPU is, and when running on multiple nodes it wouldn't
    distribute the hoomd MPI processes over the nodes correctly). This is not
    much of an issue in practice, because with four GPUs the CPM is already the
    limiting factor so that adding more wouldn't speed things up.

--ntasks=18
    This tells Slurm that we want to have 18 CPU nodes, or 1/4 of the node.
    Since a single GPU node has such a large amount of compute capability, they
    are actually split into four quarter nodes. For large-but-not-huge
    simulations, using more than one GPU doesn't help (it even slows things
    down, because there's more communication overhead) and it doesn't make sense
    to pay for a whole node. This option will ask for a quarter node (18 out of
    72 CPU cores). Note that the ECM model uses as many CPU cores as there are
    GPUs, CPM uses a single core, and so does the state dumper, so most of these
    cores will actually sit idle during the simulation. We could ask for less,
    but accounting is done by the quarter node so we're paying for them anyway.

--cpus-per-task=1
    Actually, what we're doing here is to tell Slurm we're going to start 18
    programs (ntasks=18) with one thread each (this option). That will get us 18
    CPU cores, which MUSCLE3 will then use to start our actual simulation. Slurm
    doesn't understand coupled simulations, but it will just give us our CPUs
    and MUSCLE3 knows what to do with them, so it's all good.

--gpus=1
    This asks for a single GPU, which is one quarter of the total available.


Depending on your settings, you will probably have to change the time requested,
and if you need to go faster then you can go to 36 tasks and 2 GPUs, or even the
full 72 and 4 (be user to set the ``mpi_processes`` for ``simulate_ecm`` to the
number of GPUs too!). It's good to experiment a little here with some short runs
to see how fast you're going and whether the additional resources help (or help
enough to be worth it, paying four times as many SBUs per hour for a 10%
increase in speed doesn't make much sense for example, also because it costs
more energy and we only have one planet) before launching a run with the full
number of timesteps.

If you have put the TST source code somewhere else than in
``Tissue-Simulation-Toolkit`` in your home directory, then you'll have to modify
the ``cd`` command to point to the right place.

The line ``export QT_QPA_PLATFORM=offscreen`` tells Qt to not create a window,
and to draw nothing. Supercomputers don't have monitors, so it would crash if it
tried.

If you're producing large amounts of output, then it may be better to put the
output on the scratch filesystem. The easiest way to do that is to put another
``cd`` command just before the ``muscle_manager`` one to change to the directory
where you want your output. See the `Snellius documentation`_, in particular the
page about file systems.

With the script in order, we can now submit a job using

.. code-block:: bash

    Tissue-Simulation-Toolkit$ sbatch src/scripts/snellius_cpm_ecm.sh


This will print a message saying that the job has been submitted, with its job
id. You can see it in the queue using

.. code-block:: bash

    $ squeue


and get more information with

.. code-block:: bash

    $ scontrol show job <job id>


The job will only show in ``squeue`` while it is queued and waiting to run and
while it is running. Once it's done, it will disappear there.

When the job is started, a ``slurm-<job id>.out`` file is created in the
directory in which you ran the ``sbatch`` command that contains the output that
would otherwise have been printed to the screen. You can use ``less slurm-<job
id>.out`` to view its contents while the job is running and after it's done.

Debugging on Snellius
"""""""""""""""""""""

If something goes awry, then the first thing to do is to check the log output.
The ``slurm-<job id>.out`` file will contain the things that are normally
printed to the screen. If the simulation crashed, then there will be an error
message here that will point you to the log files in the run directory. Those
should contain more information, which will hopefully help you figure out what
went wrong in the same way as when running locally.

Note that because of the batch system, doing interactive debugging on an HPC
machine isn't so easy. It's better to do that locally if the problem is with the
code rather than the configuration, and then go back to the cluster with the fix
in place.



.. [1] This will very likely be extended over time as more complex cell-ECM
   interactions are added.

.. _MUSCLE3 documentation: https://muscle3.readthedocs.io

.. _Snellius documentation: https://servicedesk.surf.nl/wiki/display/WIKI/Snellius

