/** \file Parameter definitions
 *
 * Add your parameters here, using PARAMETER(type, name, default value, description)
 *
 * Supported types are bool, double, int, and std::string.
 *
 * Parameters are organised in sections, which don't matter to the model itself but
 * will be rendered as comments when the settings are saved. Use SECTION("text") to
 * create a section.
 *
 * Constraints may be placed on the parameter values. These are checked by
 * Parameter::Validate(). Use CONSTRAINT(expression, message) to define them. If
 * expression returns false, an exception will be thrown with message as the text.
 *
 * Note that the descriptions were derived from the source code by someone who didn't
 * create the model, and the source code isn't very well documented. So they may not
 * be entirely correct, and they're vague in places where I couldn't figure it out.
 * Feel free to fix them where you can, in the mean time it's better than nothing.
 */

SECTION("General settings")

    PARAMETER(bool, useopencl, false, "Whether to use OpenCL for PDE calculations")
    PARAMETER(std::string, opencl_core_path, "../src/reaction_diffusion/pdecore.cl", \
            "Path to the OpenCL compute kernel source")
    PARAMETER(int, opencl_pref_platform, 0, \
            "Preferred OpenCL platform, in case more than one is available")

    PARAMETER(bool, graphics, true, "Whether to enable graphics")
    PARAMETER(bool, store, true, "Whether to store output to disk")
    PARAMETER(int, storage_stride, 10, "Interval at which to store/show plots")
    PARAMETER(std::string, datadir, "data_film", "Directory to store plots in")
    PARAMETER(std::string, colortable, "../data/default.ctb", \
            "Colortable to use for plotting")

    PARAMETER(bool, pause_on_start, false, \
            "Whether to start the simulation in the paused state. Not used by most"
            " models.")

    PARAMETER(int, rseed, -1, "Random seed for the simulation")


SECTION("MultiCellDS input/output")

    PARAMETER(bool, load_mcds, false, "Whether to load an MCDS file to start from")

    PARAMETER(std::string, mcds_input, "false", "Path to MCDS file to load")

    PARAMETER(std::string, mcds_output, "outstate.xml", "MCDS output file path")

    PARAMETER(int, mcds_anneal_steps, 0, \
            "Number of annealing steps to perform when saving MCDS")

    PARAMETER(int, mcds_denoise_steps, 0, \
            "Number of denoising steps to perform when saving MCDS")


SECTION("Cellular Potts Model - Grid")

    PARAMETER(int, sizex, 200, "Horizontal size of the grid")

    PARAMETER(int, sizey, 200, "Vertical size of the grid")

    PARAMETER(bool, periodic_boundaries, false, \
            "Whether to use periodic boundaries for the CPM grid")

    PARAMETER(int, mcs, 10000, "Number of Monte Carlo Steps to run")


SECTION("Cellular Potts Model - Initialisation")

    PARAMETER(int, n_init_cells, 100, "Number of cells to generate")

    PARAMETER(double, subfield, 1.0, "Fraction of the grid to create them in")

    PARAMETER(int, size_init_cells, 10, \
            "Approximate initial size of the cells, in pixels")

    PARAMETER(int, divisions, 0, \
            "Number of times to divide each cell after creating them")


SECTION("Cellular Potts Model - Dynamics")

    PARAMETER(double, T, 50.0, \
            "Thermodynamic temperature of the CPM. Higher values increase the"
            " probability that a copy attempt is taken.")

    PARAMETER(double, lambda, 50.0, "Energy parameter for copy or flip attempt")
    PARAMETER(double, lambda2, 5.0, "Energy parameter for copy or flip attempt")

    PARAMETER(int, target_area, 100, "Target area for all cells")
    PARAMETER(int, target_perimeter, 0, "Target perimeter length for all cells")

    PARAMETER(int, conn_diss, 2000, "Energy required to split a cell in two")

    PARAMETER(std::string, Jtable, "J.dat", \
            "Path to file with J values, which describe the energy required" \
            " for cells of different types to be adjacent")
    PARAMETER(int, border_energy, 100, "J value for being adjacent to the border")
    PARAMETER(int, neighbours, 2, \
            "Size of neighbourhood to take into account when computing adjacency"
            " energy. 0: no neighbours, 1: 4 orthogonal neighbours (von Neumann),"
            "  2: 8 direct neighbours (Moore), 3: 5x5 block minus the corners.")


SECTION("Actin model")

    PARAMETER(int, ref_adhesive_area, 100, \
            "Reference adhesive area for a cell (UNUSED/REMOVED?)")
    PARAMETER(double, threshold, 0.0, \
            "Adhesion fraction threshold above which the model is fully functional")
    PARAMETER(double, start_level, 1.0, \
            "Base effect strength if the adhesive area is zero")
    PARAMETER(int, area_constraint_type, 0, \
            "If set to 0, enables area and perimeter constraints in Actin model")
    PARAMETER(bool, cluster_connectivity, false, \
            "Whether to preserve cluster connectivity in the Actin model")
    PARAMETER(bool, extended_neighbour_border, false, \
            "Modifies adjacency neighbourhood for Actin model")

    PARAMETER(double, lambda_Act, 0.0, "Energy per Actin concentration")
    PARAMETER(double, max_Act, 0.0, "Maximum Actin concentration")
    PARAMETER(int, lambda_perimeter, 0, "Energy parameter for perimeter length term")
    PARAMETER(double, lambda_matrix, 0.0, \
            "Energy required to retract a lattice site that contains an adhesion")
    PARAMETER(double, spontaneous_p, 0.001, "Something to do with adhesion generation?")
    PARAMETER(double, decay_p, 0.02, "Something to do with adhesion destruction?")
    PARAMETER(double, eden_p, 0.25, "Something to do with adhesion generation?")


SECTION("Chemotaxis - reaction-diffusion")

    PARAMETER(double, dx, 2.0e-6, "Reaction-diffusion grid spacing")

    PARAMETER(double, dt, 2.0, "Reaction-diffusion timestep")

    PARAMETER(int, relaxation, 0, "Timestep from which to enable reaction-diffusion")

    PARAMETER(int, pde_its, 15, "Number of PDE timesteps per CPM MCS")

    PARAMETER(int, n_chem, 1, \
            "Number of chemicals in the reaction-diffusion (PDE) model")

    PARAMETER(std::vector<double>, diff_coeff, {1e-13}, \
            "List of diffusion coefficients, one for each chemical")

    CONSTRAINT(diff_coeff.size() == n_chem, \
            "Number of diff_coeff values does not match n_chem")

    PARAMETER(std::vector<double>, decay_rate, {1.8e-4}, \
            "List of decay rates, one for each chemical")

    CONSTRAINT(decay_rate.size() == n_chem, \
            "Number of decay_rate values does not match n_chem")

    PARAMETER(std::vector<double>, secr_rate, {1.8e-4}, \
            "List of secretion rates, one for each chemical")

    CONSTRAINT(secr_rate.size() == n_chem, \
            "Number of secr_rate values does not match n_chem")


SECTION("Chemotaxis - cell response to chemicals")

    PARAMETER(int, chemotaxis, 1000, \
            "Multiplication factor from difference in effective concentration to DH")
    PARAMETER(double, saturation, 0.0, \
            "Concentration saturation value. The maximum effective concentration is" \
            " 1/saturation. Set to 0 to disable saturating.")

    PARAMETER(bool, vecadherinknockout, false, \
            "Enable VE-cadherin knockout, which enables chemotaxis on a copy attempt" \
            " from one cell into another")
    PARAMETER(bool, extensiononly, false, \
            "Make only chemotactic extensions contribute to energy change" \
            " (CompuCell's method)")


SECTION("Adhesions")

    PARAMETER(bool, adhesions_enabled, false, \
            "Whether to use the adhesion simulation")
    PARAMETER(double, adhesion_zone_radius, 10.0, \
            "Radius of the adhesion creation zone\n"
            "\n"
            "Adhesions are created in the adhesion creation zone, which contains all\n"
            "pixels that are in a cell and within a certain radius from the edge of\n"
            "the cell. This parameter specifies that radius.\n")
    PARAMETER(int, num_initial_adhesions, 50, \
            "Number of adhesions to initially create.")
    PARAMETER(std::string, adhesion_extension_mechanism, "sticky", \
            "How to move adhesions at the source pixel of a copy attempt\n"
            "\n"
            "lazy: Leave them where they are\n"
            "sticky: Move them to the target pixel\n"
            "mixed: Randomly either leave them where they are, or move them to the\n"
            "        target pixel\n"
            "random: Move them in a random direction within the cell\n")
    PARAMETER(std::string, adhesion_displacement_selection, "uniform", \
            "How to select an adhesion displacement\n"
            "\n"
            "uniform: Pick one at random from the available possibilities\n"
            "gradient: Pick the one with the lowest DH\n"
            "\n"
            "Formerly called nbhd_selection\n")
    PARAMETER(int, adhesion_annihilation_penalty, 0, \
            "Work required to annihilate an adhesion (in DH units)")
    PARAMETER(int, adhesions_per_pixel_overflow, 0, \
            "Number of adhesions per pixel above which a crowding penalty is applied")
    PARAMETER(int, adhesions_per_pixel_overflow_penalty, 600, \
            "Per-adhesion penalty (in DH units) in case of crowding")


SECTION("Obsolete and unused")

    PARAMETER(bool, gradient, false, "Obsolete, unused")
    PARAMETER(int, adhesion_storage_stride, 0, "Unused")
    PARAMETER(int, target_length, 60, "Target cell length for all cells, unused")
    PARAMETER(int, J_pol, 0, "Unused")

