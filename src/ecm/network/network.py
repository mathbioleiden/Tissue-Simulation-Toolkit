"""
Initialises the matrix network based on the passed parameter file 'par'.
Defines a network class, which uses the local binner module.
Provides functions to initialise and query network properties. 
"""

# system modules
import itertools
import decimal
from collections import defaultdict
import logging

# installed modules
import numpy as np
from scipy.signal import convolve2d

# local modules
import tissue_simulation_toolkit.ecm.network.binner as binner


_logger = logging.getLogger(__name__)


class Network:
    """
    Network construction.
    """

    def __init__(self):
        # particles
        self.pos = []
        self.particles_typeid = []
        self.particle_types = ['free', 'boundary', 'adhesion', 'excluded']

        # linear bonds between particles
        self.bonds_group = []
        self.bonds_typeid = []
        self.bonds_k = []
        self.bonds_r0 =[]
        self.bond_types = ['polymer']

        # angular bonds between particles
        self.angles_group = []
        self.angles_typeid = []
        self.angle_types_k = []
        self.angle_types_t0 = []
        self.angle_types = ['polymer_bend']

        # crosslinkers
        self.crosslink_vertices = [] # not needed for hoomd, but useful for computing DH
        self.crosslink_list = []
        self.crosslink_typeid = []
        self.crosslink_types = []
        self.crosslink_k = []
        self.crosslink_r0 = []


    def build_strands(self, par):
        """
        Instantiate position of fiber particles, and their linear and angular bonds.
        
        ####################################################
        #  Bond generation and angle generation example:   #
        #  beads = 3 strands = 4                           #
        #  bond_group should be as ((beads-1)*3, 2 matrix) #
        #  0 ,1  strand 0                                  #
        #  1 ,2                                            #
        #  3 ,4  strand 1                                  #
        #  4 ,5                                            #
        #  5 ,6  strand 2                                  #
        #  7 ,8                                            #
        #  8 ,9  strand 3                                  #
        #  10,11                                           #
        #  11,12                                           #
        # The first column can be written as:              #
        #         [0,     [0,                              #
        #          0,      1                               #
        #          1,      0                               #
        #  beads*  1,  +   1                               #
        #          2,      0                               #
        #          2,      1                               #
        #          3,      0                               #
        #          3]      1]                              #
        # And the second column slightly different.        #
        ####################################################
        """

        ### Read parameter values
        num_total_particles = par.strands*par.beads
        num_fibers          = par.strands
        particles_per_fiber = par.beads

        # The particles are seeded in a slightly larger area than the simulation box.
        # This prevents low fiber concentration at the edges.
        xbox = par.Lx * 2.0 + par.contour_length
        ybox = par.Ly *2.0 + par.contour_length

        pos = np.zeros((num_fibers, particles_per_fiber, 2))
        pos[:, 0, 0] = np.random.uniform(-par.contour_length, xbox, size=num_fibers)
        pos[:, 0, 1] = np.random.uniform(-par.contour_length, ybox, size=num_fibers)

        angles = np.random.uniform(0, 2*np.pi, size=num_fibers)

        # compute segment length based upon contour length
        # if the helix angle is 0, this is equivalent to (particles_per_fiber-1)*par.spring_r0
        segment_rest_length = par.contour_length / (particles_per_fiber-1)

        if np.cos(par.helix_angle) != 0:
            h = segment_rest_length / np.cos(par.helix_angle)   # was: h = par.contour_length / (particles_per_fiber - 1)
        else:
            _logger.warning("np.cos(par.helix_angle) = 0, check stand generation!")
            h = par.contour_length / (particles_per_fiber - 1) # I don't think this is right, but let's leave it for now.

        for bead in range(particles_per_fiber)[1:]:
            coss = np.cos(angles)
            sins = np.sin(angles)
            pos[:, bead, :] = pos[:, bead-1, :] + h*np.column_stack([coss, sins])

        # populate position array
        self.pos = pos.reshape( (num_total_particles, 2))

        self.particles_typeid = np.zeros( num_total_particles, dtype=int ) # 0 is the id for type 'free'
        if par.fixed_boundary:
            boundary_particles = ( abs(self.pos[:, 0]) > par.Lx ) | ( abs( self.pos[:,1] ) > par.Ly )
            self.particles_typeid[boundary_particles] = 1
            _logger.info("all boundary particles are fixed")
        else:
            if par.bottom_fixed:
                boundary_particles = ( self.pos[:,1] < -par.Ly )
                self.particles_typeid[boundary_particles] = 1
                _logger.info("bottom particles are fixed")
            if par.top_fixed:
                boundary_particles = ( self.pos[:,1] > par.Ly )
                self.particles_typeid[boundary_particles] = 1
                _logger.info("top particles are fixed")


        ### Bond generation
        bonds_indices = np.repeat(particles_per_fiber*np.arange( 0, num_fibers, dtype = int), particles_per_fiber-1)

        self.bonds_group = np.empty( shape=(num_fibers*(particles_per_fiber-1), 2), dtype=int)
        self.bonds_group[:, 0] = bonds_indices + np.tile( np.arange(0, particles_per_fiber-1, 1, dtype = int), num_fibers)
        self.bonds_group[:, 1] = bonds_indices + np.tile( np.arange(1, particles_per_fiber, 1, dtype=int), num_fibers )
        self.bonds_group = self.bonds_group.tolist()

        self.bonds_typeid = [0] * len(self.bonds_group)
        self.bonds_k = [par.spring_k] * len(self.bonds_group)
        self.bonds_r0 = [par.spring_r0] * len(self.bonds_group)

        ### Angle generation
        angles_indices = np.repeat(particles_per_fiber*np.arange( 0, num_fibers, dtype = int), particles_per_fiber-2)

        self.angles_group = np.empty( shape=(num_fibers*(particles_per_fiber-2), 3), dtype=int)
        self.angles_group[:, 0] = angles_indices + np.tile( np.arange(0, particles_per_fiber-2, 1, dtype = int), num_fibers)
        self.angles_group[:, 1] = angles_indices + np.tile( np.arange(1, particles_per_fiber-1, 1, dtype=int), num_fibers )
        self.angles_group[:, 2] = angles_indices + np.tile( np.arange(2, particles_per_fiber, 1, dtype=int), num_fibers )
        self.angles_group = self.angles_group.tolist()
        
        self.angles_typeid = [0] * len(self.angles_group)
        self.angle_types_k = [par.bend_k]
        self.angle_types_t0 = [par.bend_t0]


    def distribute_crosslinkers(self, par):
        """
        Assumption: Crosslink formation probability is proportional to local fiber density.
        The network is binned with a lattice (!= CPM lattice).
        For each bin p, count the number n of distinct fibers going through p and its Moore neighbourhood (duplicates are removed).
        Divide n in each bin p by the sum of n_p over all bins to get the probability density.
        Draw a number of bins (sample size = number of crosslinks requested) with probability given by calculated density.
        Check the distance between any two pair of beads from different fibers in the bin.
        Sample one pair of beads with probability weighted by their distance.
        If at least one pair is close enough: Add crosslinking bond to this location. If no: No crosslink is formed.
        """

        def sample_from_2d_array(array, size):
            """
            Sample 'size' indices from array with weights as in the array.
            """
            # Create a flat copy of the array
            flat = array.flatten()

            # Then, sample an index from the 1D array with the
            # probability distribution from the original array
            sample_index = np.random.choice(a=flat.size, p=flat, replace=True, size=size)

            # Take this index and adjust it so it matches the original array
            adjusted_index = np.unravel_index(sample_index, array.shape)
            return list(zip(*adjusted_index))


        def map_bead_to_fiber(bead):
            """
            Returns the ID of the fiber that bead belongs to.
            """
            b = par.beads
            fiber_id = bead // b
            return fiber_id


        def crosslink_r_dist(r):  
            """
            Returns the probabilty of forming a crosslink at distance r.
            The probabilty decreases linearly with increasing r as:
            p = -(2/(max_r**2))*r + 2/max_r     
            """
            max_r = par.crosslink_max_r
            p = 0
            if r <= max_r:
                p = -(2/(max_r**2))*r + 2/max_r  # mx + b
            return p


        def magnitude(x):
            """
            Returns magnitude of vector x.
            Faster than calling np.linalg.norm()
            """
            mag = np.sqrt(x.dot(x))
            return(mag)


        def roundNearestDecimal(num, dec, digits):
            """
            Round a number to the nearest decimal with digits precision.
            E.g. 
            - roundNearestDecimal(0.4, 0.5) = 0.5
            - roundNearestDecimal(0.6, 0.5) = 0.5
            - roundNearestDecimal(0.8, 0.5) = 1.0
            """
            return round(round(num / dec) * dec, digits)


        pos = self.pos
        bonds_group = self.bonds_group 

        # limit number of distinct bond types for hoomd by quantization of crosslinker rest lengths
        max_r = par.crosslink_max_r
        qstep = par.crosslink_quant_step
        d = decimal.Decimal(str(qstep))
        crosslinker_rounding_digits = -d.as_tuple().exponent

        # want order 10 bonds at most, rounding needed to avoid numerical errors
        self.possible_r0     = [ roundNearestDecimal(i, qstep, crosslinker_rounding_digits) 
                            for i in np.linspace(qstep, max_r, int(max_r/qstep)) ]
        self.possible_typeid = [i+1 for i in range(len(self.possible_r0))]  # start at 1 because bonds are type id 0
        self.possible_types  = ['crosslink_' + str(i) for i in self.possible_typeid]
        self.possible_k      = [par.crosslink_k]*len(self.possible_r0)               # right now all the same
        

        # bin the network - note that the binning lattice is not the same as the CPM lattice!
        bin_size_x = par.crosslink_bin_size
        bin_size_y = par.crosslink_bin_size
        num_bins_x = int(par.box_size_x / bin_size_x)
        num_bins_y = int(par.box_size_y / bin_size_y)

        # initialise the binner
        crosslink_binner = binner.FiberBin(num_bins_x, num_bins_y, 
                                           bin_size_x, bin_size_y, 
                                           par.beads, par.strands, 
                                           par.Lx, par.Ly)
                
        # bin by taking all fiber beads and interpolating points between them
        # also generates 'bonds_in_bin' -- count of bonds in each bin
        crosslink_binner.bin_bonds(np.array(pos))

        # number of bonds in each bin
        bonds_in_bin = np.array(crosslink_binner.bonds_in_bin)

        # get the density = bond segments in the Moore neighbourhood
        filt = np.ones((3, 3))  # Moore NBH
        bonds_nbhd_sum = convolve2d(bonds_in_bin, filt, mode='same') # discard padding

        # this overcounts pairings! self-pairings are allowed!
        num_pairing_bin_array = (0.5 * (bonds_nbhd_sum - 1) * bonds_nbhd_sum) # n choose 2
        total_num_pairings = num_pairing_bin_array.sum()
                    
        
        if total_num_pairings > 0:
            sampled_bins = sample_from_2d_array(num_pairing_bin_array / total_num_pairings, par.num_init_crosslinks)

            for (ny, nx) in sampled_bins:

                # collect all bonds in bin and its Moore neighbourhood
                bonds_in_nbhd = []
                for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]): # Moore NBH
                    if 0 <= nx+dx and nx+dx < num_bins_x and 0 <= ny+dy and ny+dy < num_bins_y:  # check for lattice boundaries
                        bonds_in_nbhd.extend(crosslink_binner.bondIDs_in_bin[ny+dy][nx+dx])
                bonds_in_nbhd = list(set(bonds_in_nbhd))  # remove duplicates

                # get unique pairings between different beads of fibers
                """
                - works as follows:
                -- simple example with 3 beads per strand
                -- beads => [ 0, 1, 3, 4, 5, 7, 8 ]                             <--- list of bead indices
                -- fiber_dict.values => [ [0, 1], [3, 4, 5], [7, 8]  ]          <--- group bead indices of same fiber
                -- fiberpair in itertools.combinations(fiber_dict.values(), 2)  <--- iterator of 2-fiber combos
                -- beadpairs = itertools.product(*fiberpair)                    <--- all possible pairs of beads from distinct fibers
                """

                fiber_dict = defaultdict(list)
                for bond in bonds_in_nbhd:
                    for bead in bonds_group[bond]:
                        fiber_id = map_bead_to_fiber(bead)
                        fiber_dict[fiber_id].append(bead)

                all_vertex_pairs = []
                for fiberpair in itertools.combinations(fiber_dict.values(), 2):
                    beadpair = itertools.product(*fiberpair)
                    all_vertex_pairs.extend(beadpair)
                
                # for each vertex pair, determine probability of choosing it based on pair distance
                if len(all_vertex_pairs) == 0:
                    continue

                dist = []
                cum_p = 0
                for k0, k1 in all_vertex_pairs:
                    r = magnitude( np.array(pos[k0]) - np.array(pos[k1]) )
                    p = crosslink_r_dist(r)
                    dist.append(p)
                    cum_p += p

                if cum_p == 0:  # Could not make a crosslinker
                    continue

                # normalize
                prob = [p / cum_p for p in dist]

                # sample all vertex pairs without replacement
                # closer pairs more likely to be chosen according to 'prob'
                size = len(prob) - prob.count(0) # can only sample a number equivalent to non-zero entries
                pair_index_list = np.random.choice(len(all_vertex_pairs), size=size, replace=False, p=prob)

                # hoomd does not like multiple bonds at the same location!
                # so we loop through our sampled pairs until we find the first free one
                found_free_pair = False
                sample_index = 0

                while not found_free_pair:
                    if sample_index < len(pair_index_list):
                        selected_bond = all_vertex_pairs[ pair_index_list[sample_index] ]
                        sample_index += 1

                        if selected_bond not in self.crosslink_list: # found a unique unbonded vertex pair
                            found_free_pair = True
                            self.crosslink_list.append(selected_bond)
                            bead1 = np.array(pos[selected_bond[0]])
                            bead2 = np.array(pos[selected_bond[1]])
                            r0 = magnitude(bead1 - bead2)

                            # at least par.crosslink_quant_step (qstep) --> avoid 0-length crosslinkers!
                            r0_rounded = roundNearestDecimal(r0, qstep, crosslinker_rounding_digits)
                            quantized_r0 = max(r0_rounded, qstep)
                            self.crosslink_r0.append(quantized_r0)
                        
                            r0_index = self.possible_r0.index(quantized_r0)
                            self.crosslink_typeid.append(self.possible_typeid[r0_index])
                            self.crosslink_k.append(self.possible_k[r0_index])

                            self.crosslink_vertices.extend(selected_bond) # useful for computing DH
                    else:
                        break
        
        self.crosslink_types = self.possible_types
        self.bond_types.extend(self.crosslink_types)

        # done with crosslinks !
        _logger.info('')

        # Created crosslinks may be fewer than requested, e.g. due to low strand density
        _logger.info(f"Number of crosslinks requested: {len(sampled_bins)}")
        _logger.info(f"Number of crosslinks created: {len(self.crosslink_list)}")
        
        self.bonds_group.extend(self.crosslink_list)
        self.bonds_typeid.extend(self.crosslink_typeid)
        self.bonds_k.extend(self.crosslink_k)
        self.bonds_r0.extend(self.crosslink_r0)


    def addDummyBondTypes(self):
        """
        Extend bond types with a dummy bond.
        """
        self.bond_types.append("nobond")
        self.dummy_bondID = len(self.bond_types) - 1

        self.angle_types.append("noangle")
        self.dummy_angleID = len(self.angle_types) - 1


def generate_network(par):
    """
    Instantiates a Network object and populates it based on the parameter file 'par'. 
    1. Define positions and connectivity of beads for the polymer network
    2. Define crosslink locations
    Returns the Network object.
    """

    net = Network() 
    net.build_strands(par)
    net.distribute_crosslinkers(par)
    net.addDummyBondTypes()

    return net


def map_bead_to_bonds(bead, par):
    """
    map id of a bead to a list of bondids which contain said bead
    """
    beads = par.beads
    out = []
    k = bead % beads
    q = (bead - k) // beads
    if k > 0:  # bead is not a left end bead
        out.append(q*(beads-1) + k - 1)
    if k != beads - 1:  # bead is not a right end bead
        out.append(q*(beads-1) + k)
    return out



def map_bead_to_angle(bead, par):
    """
    map id of a bond to a list of angleid
    """
    out = []
    k = bead % par.beads
    q = (bead - k) // par.beads
    if k != par.beads - 1 and k != par.beads - 2:
        out.append(q*(par.beads-2) + k)
    if k != 0 and k != par.beads - 1:
        out.append(q*(par.beads-2) + k - 1)
    if k > 1:
        out.extend([q*(par.beads-2) + k - 2])
    return out
