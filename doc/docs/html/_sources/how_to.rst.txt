How to ...
========================================================

This section outlines various common procedures and tasks using the Tissue Simulation Toolkit 2.0.

How to add a new model?
--------------
There are a list of default models in the Tissue Simulation Toolkit in the ``src/models/`` directory. However, you can add your own models as well. To add a model named, say ``my_model``, following steps should be taken:

#. Create a new model definition file, ``my_model.cpp``, in the ``src/models/`` directory. For this you can copy one of existing ``.cpp`` files and modify it to suit your needs, or you can create a new one from scratch.

#. Add a file named ``my_model.pro`` to the ``src/`` directory. This file configures a Qt project to build an executable named my_model.
    * If your model uses only Cellular Potts Model (CPM), you can use the following template:

        .. code-block:: pro

            TARGET = my_model
            MAINFILE = "models/my_model.cpp"

            include(Tissue_Simulation_Toolkit.pri)

    * If your model requires ECM model to be built, you can use the following template:

        .. code-block:: pro

            MUSCLE3_DIR = "../lib/muscle3/muscle3"

            TARGET = my_model
            MAINFILE = "models/my_model.cpp"

            include(Tissue_Simulation_Toolkit.pri)

            HEADERS += util/muscle3/*.hpp cpm_ecm/*.hpp
            SOURCES += util/muscle3/*.cpp cpm_ecm/*.cpp

            INCLUDEPATH += $$MUSCLE3_DIR/include
            LIBS += -L$$MUSCLE3_DIR/lib -lmuscle -lymmsl

#. Add the new model definition file to the ``Makefile`` in the root of the repository, so that it will be built.
    * If your model only includes CPM components. Add the model name to the ``MODELS`` variable in the ``Makefile``. For example, if your model is named ``my_model``, you can add it like this below the existing models:

        .. code-block:: make

            MODELS = bin/vessel bin/qPotts bin/sorting bin/Act_model    # already present models
            MODELS += bin/my_model                                      # Newly added model

    * If your model requires a connection to the ECM model. You can add it to the ``with_adhesions`` target in the ``Makefile`` like this:

        .. code-block:: make

            with_adhesions: $(MODELS) bin/adhesions bin/my_model ecm ymmsl/my_model.ymmsl ymmsl/plot_state.ymmsl ymmsl/dump_state.ymmsl

    Alternativly, you can also add a new target to the ``Makefile`` for your model, so that it can be built separately.

        .. code-block:: make

            .NOTPARALLEL: with_my_model
            with_my_model: $(MODELS) bin/my_model ecm ymmsl/my_model.ymmsl ymmsl/plot_state.ymmsl ymmsl/dump_state.ymmsl

        here ``my_model.ymmsl`` is an YAML file containing parameters that defines the model.


How to run Tissue Simulation Toolkit 2.0 without a graphical user interface?
-----------------

Tissue Simulation Toolkit 2.0 can be executed in headless (offscreen) mode, which is useful for remote or automated environments without graphical display support. The following steps describe how to configure and run the simulation in this mode and how to post-process the results.

Running
''''''''''''''''
#. Set environment variables in the main ``.ymmsl`` file.

   Update the ``implementations`` section of main ``.ymmsl`` file (here ``adhesions.ymmsl``) to include the environment variable ``QT_QPA_PLATFORM: offscreen`` under the ``tst_adhesions`` entry. This ensures that Qt operates in offscreen mode.

   Example:

   .. code-block:: yaml

      tst_adhesions:
        env:
          +LD_LIBRARY_PATH: :/PATH/TO/Tissue-Simulation-Toolkit/lib/muscle3/muscle3/lib
          QT_QPA_PLATFORM: offscreen
        executable: /PATH/TO/Tissue-Simulation-Toolkit/bin/adhesions

#. Do not disable graphics output.

   Ensure that ``cellular_potts.graphics`` is **not** explicitly set to ``false`` in ``adhesions.ymmsl``. Disabling this option may interfere with certain internal processing steps.

#. Run the simulation with ``dump_state.ymmsl`` instead of ``plot_state.ymmsl``.

   Replace the ``plot_state.ymmsl`` configuration with ``dump_state.ymmsl`` when executing the simulation with the ``muscle_manager``:

   .. code-block:: console

       muscle_manager --start-all ymmsl/adhesions.ymmsl ymmsl/dump_state.ymmsl

   During execution, simulation data will be written to ``.pickle`` files located in the directory ``run_adhesions_<date>_<time>/instances/state_dumper/workdir``. These files contain state information for both cellular components and the extracellular matrix (ECM).

Post-processing
''''''''''''''''
#. Generate images from the outputs.

    To generate plots from the output files, activate the appropriate Python virtual environment and run:

    .. code-block:: console

        plot_states /PATH/TO/run_adhesions_<date>_<time>

    You can also run ``plot_states`` in a offscreen mode by running:  

    .. code-block:: console

        plot_states -offscreen /PATH/TO/run_adhesions_<date>_<time>

#. Generate a video

    Instructions for generating a video from the output data can be found :ref:`here <dumping-state>`.



