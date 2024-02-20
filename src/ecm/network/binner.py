"""
Custom class to bin network.
"""
import copy

import numpy as np
from scipy.stats import binned_statistic_2d

class FiberBin:
    
    def __init__(self, 
                 num_bins_x, num_bins_y,
                 bin_size_x, bin_size_y,
                 beads, strands, 
                 offset_x=0, offset_y=0
                ):

        self.num_bins_x = num_bins_x
        self.num_bins_y = num_bins_y
        self.bin_size_x = bin_size_x
        self.bin_size_y = bin_size_y
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.num_beads = beads
        self.num_strands = strands
    

    def generate_bin_array(self, inner_obj=[]):
        """
        Return 2D array of shape self.num_bins_y, self.num_bins_x 
        filled with 'inner_obj'. 
        """
        newbin = []
        for ny in range(self.num_bins_y):
            tmplist = [] 
            for nx in range(self.num_bins_x):
                tmplist.append(copy.copy(inner_obj))
            newbin.append(tmplist)

        return newbin
  

    def _interpolate_beads(self, pos, interpolation_number):
        """
        Interpolates points between beads.
        Returns array of interpolated coordinates indexed by bond ID
        with shape (interpolation_number*num_strands*(num_beads-1), 2)
        Assumes linear fibers with equal number of beads.
        """
        
        inter = np.zeros( (interpolation_number*self.num_strands*(self.num_beads-1), 2) )
        t = np.linspace(0, 1, interpolation_number)
        for strand in range(self.num_strands):
            for k in range(self.num_beads)[:-1]: #slice to -1 prevents connecting different fibers
                bondid = strand*(self.num_beads-1) + k
                beadid = strand*self.num_beads + k
                P = pos[beadid]
                Q = pos[beadid+1]
                inter[bondid*interpolation_number:(bondid+1)*interpolation_number, 0] = P[0] + t*(Q[0]-P[0]) 
                inter[bondid*interpolation_number:(bondid+1)*interpolation_number, 1] = P[1] + t*(Q[1]-P[1]) 
        return inter
    

    def bin_bonds(self, pos, N=100):
        """ 
        Bins the network in a 2D grid and counts bonds in each bin (bonds_in_bin).
        Estimates fiber density based on interpolated bead positions (point_density).
        """

        # initialize empty bins
        self.bondIDs_in_bin = self.generate_bin_array([])
        self.bonds_in_bin = self.generate_bin_array(0)
        
        # Interpolate N points between subsequent beads in a fiber
        # The returned array is structured such that for any index i
        # i // N is the bond ID of a pair of interpolated beads
        inter = self._interpolate_beads(pos, N)
        X_inter = inter[:,0] 
        Y_inter = inter[:,1]
        
        # Generate bin edges. Add +1 to get the correct number of bins.
        x_edge = np.linspace(-self.offset_x, self.offset_x, self.num_bins_x + 1)
        y_edge = np.linspace(-self.offset_y, self.offset_y, self.num_bins_y + 1)

        # binned_statistic_2d returns:
        ## the x and y edges that were passed as an argument
        ## 'point_density' -- the sum of points in each bin ~ fiber density
        ## 'binnumber' -- the bin location and index of each input point
        ### e.g. binnumber[3] = 4 --> the input point with index 3 is in bin 4
        point_density, x_edge, y_edge, binnumber = binned_statistic_2d(X_inter, Y_inter, values =[] , statistic='count', bins=[x_edge, y_edge], expand_binnumbers=True)
        
        self.point_density = point_density / N # ~ fiber density

        # Get the bond IDs of bonds contained in each bin.
        for k, [nx,ny] in enumerate(binnumber.T):

            # the maximum and minimum bin indices are reserved for "out of scope" points
            # in our case, these contain boundary particles so we ignore them
            if nx == 0 or ny == 0:
                continue
            if nx == self.num_bins_x+1 or ny == self.num_bins_y+1:
                continue
            
            # Because we skip nx == 0 or ny == 0, subtract 1
            bond_set = set(self.bondIDs_in_bin[ny-1][nx-1])
            bond_set.add( k // N ) # get bond id

            self.bondIDs_in_bin[ny-1][nx-1] = list(bond_set)
            self.bonds_in_bin[ny-1][nx-1] = len(self.bondIDs_in_bin[ny-1][nx-1])