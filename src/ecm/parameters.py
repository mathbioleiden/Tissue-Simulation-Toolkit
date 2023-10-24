from dataclasses import dataclass


@dataclass
class GenerationParameters:
    """Relevant parameters for ECM generation

    The spatial domain of the model is [-Lx, Lx] x [-Ly, Ly], but fibers will
    be generated outside of this to ensure density is uniform also near the
    edges.

    Attributes:
        box_size_x (int): Twice Lx, make sure it matches `sizex` in the .par
                file
        box_size_y (int): Twice Ly, make sure it matches `sizey` in the .par
                file
        Lx (float): Maximum absolute coordinate in the x direction
        Ly (float): Maximum absolute coordinate in the y direction

        fixed_boundary (bool): Whether to fix particles outside the domain
        bottom_fixed (bool): Whether to fix particles below the bottom (-Ly)
                border of the domain. Only applies if `fixed_boundary` is
                False.
        top_fixed (bool): Whether to fix particles above the top (+Ly)
                border of the domain. Only applies if `fixed_boundary` is
                False.

        contour_length (float): Length of fiber along the curve
        strands (int): Number of fibers to generate
        beads (int): Number of particles per fiber to create

        spring_r0 (float): Bond reference length
        spring_k (float): Stiffness of bond springs
        crosslink_k (float): Stiffness of crosslinker bond springs

        helix_angle (float): Curvature of the fibers
        bend_t0 (float): Angle constraint reference angle
        bend_k (float): Angle constraint stiffness

        num_init_crosslinks (int): Number of initial crosslinks to generate.
        crosslink_max_r (float): Maximum distance over which a crosslink
                will be generated.
        crosslink_quant_step (float): Quantisation step for crosslinker
                rest lengths, to limit the number of distinct bond types.
        crosslink_bin_size (float): Size of bins used to distribute
                crosslinkers evenly.
    """
    box_size_x: int
    box_size_y: int
    Lx: float
    Ly: float

    fixed_boundary: bool
    bottom_fixed: bool
    top_fixed: bool

    contour_length: float
    strands: int
    beads: int

    spring_r0: float
    spring_k: float
    crosslink_k: float

    helix_angle: float
    bend_t0: float
    bend_k: float

    num_init_crosslinks: int
    crosslink_max_r: float
    crosslink_quant_step: float
    crosslink_bin_size: float
