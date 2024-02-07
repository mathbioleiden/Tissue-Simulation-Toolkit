#pragma once
#include "vec2.hpp"

typedef Vec2<double> Force;


Force getAngularHarmonicForceOnA(ParPos A, ParPos B, ParPos C, double k, double theta0);


/**
    Returns the linear harmonic forces (F_a, F_b) in the bond
    A---B

    Returns vectors of NaNs if A and B are the same point.

    - A and B are lists with coordinates of the two points.
    - k is the spring constant.
    - r0 the rest length of the bond.

    The forces on A and on B are calculated as:

    F_a = k*(r-r0)*u
    
    F_b = -F_a
    
    - u is the norm of the vector (BA)
    - r the distance between A and B
    - when r > r0 ==> F_a < 0 --> attractive force
    - when r < r0 ==> F_a > 0 --> repulsive force
*/
Force getLinearHarmonicForceOnB(ParPos A, ParPos B, double k, double r0);
    

/**
    Monasse, Bernard, and Frédéric Boussinot. 
    "Determination of forces from a potential in molecular dynamics." 
    arXiv preprint arXiv:1401.1181 (2014).

    Returns the angular harmonic forces (F_a, F_b, F_c) in the bond
    A--B--C

    - A, B, and C are lists with coordinates of the points.
    - k is the spring constant.
    - theta0 the rest length of the bond in radians.

    The forces on A, B, and C are calculated as:
    
    F_a = k*(theta - theta0) * p_a # was: F_a = ( -k*(theta - theta0) / |BA| ) * p_a
    
    F_c = k*(theta - theta0) * p_c # was: F_c = ( -k*(theta - theta0) / |BC| ) * p_c 
    
    F_b = -F_a - F_c
    
    - p_a is a unit vector in the ABC plane orthogonal to (BA)
    - p_c is a unit vector in the ABC plane orthogonal to (CB)
    - theta is the angle ABC in radians
    */
Force getAngularHarmonicForceOnB(ParPos A, ParPos B, ParPos C, double k, double theta0);



/*
def mag(x):
    """ Return vector magnitude using numpy. """
    return( np.sqrt(x.dot(x)) )

def getLinearHarmonicForce(A, B, k, r0):
    """
    Returns the linear harmonic forces (F_a, F_b) in the bond
    A---B

    Returns vectors of NaNs if A and B are the same point.

    - A and B are lists with coordinates of the two points.
    - k is the spring constant.
    - r0 the rest length of the bond.

    The forces on A and on B are calculated as:

    F_a = k*(r-r0)*u
    
    F_b = -F_a
    
    - u is the norm of the vector (BA)
    - r the distance between A and B
    - when r > r0 ==> F_a < 0 --> attractive force
    - when r < r0 ==> F_a > 0 --> repulsive force
    """
    A = np.array(A)
    B = np.array(B)

    # initialize with NaN for case r=0
    # this shouldn't happen due to numerics
    F_a = np.full(A.shape, np.nan)
    F_b = np.full(B.shape, np.nan)

    BA = B - A
    r = mag(BA)

    if r > 0:
        u = BA / r

        F_a = k*(r-r0)*u
        F_b = -F_a

    return(F_a, F_b)


def getAngularHarmonicForce(A, B, C, k, theta0):

    F_a, F_b, F_c = getAngularHarmonicForce_Monasse(A, B, C, k, theta0)
    
    return(F_a, F_b, F_c)


def getAngularHarmonicForce_mathExchange(A, B, C, k, theta0):
    """
    Based on:
    nben (https://math.stackexchange.com/users/247901/nben), 
    Gradient of an angle in terms of the vertices, 
    URL (version: 2016-02-05): https://math.stackexchange.com/q/1239613

    AB = A - B
    CB = C - B

    delta_theta = -k *(theta - theta0)
    F_a = delta_theta / ( ||AB|| * sin(theta) ) * [ ( CB ) / ||CB|| - (AB) / || AB ||  * cos(theta) ]
    F_c = delta_theta / ( ||CB|| * sin(theta) ) * [ ( AB ) / ||AB|| - (CB) / || CB ||  * cos(theta) ]
    F_b = F_a + F_c
    """
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)

    AB = A - B
    CB = C - B

    AB_mag = mag(AB)
    CB_mag = mag(CB)

    # rounding is necessary to avoid numerical errors 
    # when vectors are colinear the argument can be = 1.0000000000000002
    # which is outside of the range of np.arccos, defined for [-1, 1]
    theta = np.arccos( round( AB.dot(CB) / ( AB_mag * CB_mag ), 10) )


    sintheta = np.sin(theta)

    print("theta radians", round(theta,3), 
          "degrees", round(theta*180/np.pi ,3), 
          "sintheta", sintheta )
    
    if sintheta != 0 and AB_mag != 0 and CB_mag != 0:
        unit_AB = (AB / AB_mag)
        unit_CB = (CB / CB_mag)
        delta_theta = -k*(theta - theta0)
        F_a = ( delta_theta / (AB_mag * sintheta) ) * ( unit_CB - unit_AB*np.cos(theta) ) 
        F_c = ( delta_theta / (CB_mag * sintheta) ) * ( unit_AB - unit_CB*np.cos(theta) ) 
        F_b = F_a + F_c 

    return(F_a, F_b, F_c)


def getAngularHarmonicForce_Tildesley(A, B, C, k, theta0):
    """
    Allen, Michael P., and Dominic J. Tildesley. 
    Computer simulation of liquids. 
    Oxford university press, 2017.
    Appendix C

    Returns the angular harmonic forces (F_a, F_b, F_c) in the bond
    A--B--C

    Potential of the form 
        U(theta) = 1/2 * k (theta - theta_0)**2

    with theta given by
        theta = arccos( AB * BC / ( |AB| * |BC|) )
    or equivalently
        cos(theta) = AB * BC / ( |AB| * |BC|)
     
    Obtain force by taking derivative wrt to ith particle position: 
        del U / del r_i

    Apply chain rule:
        d U / d theta * d theta / d cos(theta) * del cos(theta) / del r_i

    Derivative of arccos:
        d/dx arccos(x) = -1 / sqrt(1 - x**2)

    """
    #TODO
    # I don't know how to express U as a function of cos(theta)
    pass

def getAngularHarmonicForce_Monasse(A, B, C, k, theta0):
    """
    Monasse, Bernard, and Frédéric Boussinot. 
    "Determination of forces from a potential in molecular dynamics." 
    arXiv preprint arXiv:1401.1181 (2014).

    Returns the angular harmonic forces (F_a, F_b, F_c) in the bond
    A--B--C

    - A, B, and C are lists with coordinates of the points.
    - k is the spring constant.
    - theta0 the rest length of the bond in radians.

    The forces on A, B, and C are calculated as:
    
    F_a = k*(theta - theta0) * p_a # was: F_a = ( -k*(theta - theta0) / |BA| ) * p_a
    
    F_c = k*(theta - theta0) * p_c # was: F_c = ( -k*(theta - theta0) / |BC| ) * p_c 
    
    F_b = -F_a - F_c
    
    - p_a is a unit vector in the ABC plane orthogonal to (BA)
    - p_c is a unit vector in the ABC plane orthogonal to (CB)
    - theta is the angle ABC in radians
    """
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)

    BA = B - A
    BC = B - C
    CB = C - B

    BA_mag = mag(BA)   # |BA|
    BC_mag = mag(BC)   # |BC|

    # If BA and BC are colinear, take an arbitrary orthogonal vector
    # https://math.stackexchange.com/q/3077100
    BA_cross_BC = np.cross( BA, BC )
    if mag(BA_cross_BC) == 0:
        orthogonal_vector = np.array( [BA[1] + BA[2], BA[2] - BA[0], - BA[0] - BA[1]] )
        p_a = np.cross( BA , orthogonal_vector )
        p_a = p_a / mag(p_a)
        p_c = np.cross( CB , orthogonal_vector )
        p_c = p_c / mag(p_c)
    else:
        p_a = np.cross( BA , BA_cross_BC )
        p_a = p_a / mag(p_a)
        p_c = np.cross( CB , BA_cross_BC )
        p_c = p_c / mag(p_c)

    # rounding is necessary to avoid numerical errors 
    # when vectors are colinear the argument can be = 1.0000000000000002
    # which is outside of the range of np.arccos, defined for [-1, 1]
    theta = np.arccos( round( BA.dot(BC) / ( BA_mag * BC_mag ), 10) )

    delta_theta = k*(theta - theta0)

    F_a = delta_theta/BA_mag * p_a 
    F_c = delta_theta/BC_mag * p_c 

    F_b = -F_a - F_c

    return(F_a, F_b, F_c)


def getForcesOnParticles(particles_df, sub_df, bonds_df, angles_df, sample_times):
    """
    Returns a dataframe with the sum of forces on linear bonds 
    and the sum of forces on angular bonds for each particle in sub_df.
    """

    return_dflist = []

    old_colnames    = ['x', 'y', 'z', 'type']
    new_colnames_p1 = ['x1', 'y1', 'z1', 'type_p1']
    new_colnames_p2 = ['x2', 'y2', 'z2', 'type_p2']

    bonds_df.rename(columns= {'type' : 'bondtype'}, inplace=True) # prevent overlap with particle type

    for _, time in enumerate( sample_times ):
        print("processing timepoint", time)

        # Pick timepoint
        tlist = [time]
        df_all_timepoint = particles_df.query('time in @tlist').copy()
        df_sub_timepoint = sub_df.query('time in @tlist').copy()

        if not df_sub_timepoint.empty: # check if the dataframe has data in it

            # Use pandas merge to get the coordinates of the participating beads in the bonds dataframe
            pxyz = df_all_timepoint[['particleID'] + old_colnames ].copy()

            pxyz.rename(columns= {'particleID' : 'p1'}, inplace=True)
            cur_bonds_df = bonds_df.merge(pxyz, how='left', on='p1')
            colnamesdict = {i : j for i,j in zip(old_colnames, new_colnames_p1)}
            cur_bonds_df.rename(columns=colnamesdict, inplace=True)

            pxyz.rename(columns= {'p1' : 'p2'}, inplace=True)
            cur_bonds_df = cur_bonds_df.merge(pxyz, how='left', on='p2')
            colnamesdict = {i : j for i,j in zip(old_colnames, new_colnames_p2)}
            cur_bonds_df.rename(columns=colnamesdict, inplace=True)           

            # Get all bonds that do not involve excluded particles
            valid_bonds = cur_bonds_df.loc[(cur_bonds_df['type_p1'] != 'excluded') & (cur_bonds_df['type_p2'] != 'excluded')]

            # Get all bonds with particles of interest
            particles_of_interest = df_sub_timepoint['particleID'].unique()
            relevant_linear_bonds = valid_bonds.loc[ ( valid_bonds['p1'].isin(particles_of_interest) ) | ( valid_bonds['p2'].isin(particles_of_interest) ) ]
            
            particledict = { 
                            'particleID'         : [],
                            'totalLinForce'      : [],
                            'magTotalLinForce'   : [],
                            'totalAngForce'      : [],
                            'magTotalAngForce'   : []
            }
            
            # loop over particles
            for particle in particles_of_interest:

                total_linear_force_on_particle = np.array( [ 0.0 , 0.0 , 0.0 ])
                total_angular_force_on_particle = np.array( [ 0.0 , 0.0 , 0.0 ])

                p1_ID = particle
                p1_x = df_sub_timepoint.loc[df_sub_timepoint['particleID']==p1_ID]['x'].tolist()[0]
                p1_y = df_sub_timepoint.loc[df_sub_timepoint['particleID']==p1_ID]['y'].tolist()[0]
                p1_z = df_sub_timepoint.loc[df_sub_timepoint['particleID']==p1_ID]['z'].tolist()[0]

                thisparticlebonds = relevant_linear_bonds.loc[ ( relevant_linear_bonds['p1'] == p1_ID ) | ( relevant_linear_bonds['p2'] == p1_ID ) ]
            
                # all linear bonds with this particle including crosslinkers
                for _, bond_row in thisparticlebonds.iterrows(): # loop over linear bonds

                    bond_k  = bond_row['k']
                    bond_r0 = bond_row['r0']

                    # get the bond partner ID
                    if bond_row['p1'] == p1_ID:
                        p2_ID = bond_row['p2']
                        p2_x  = bond_row['x2']
                        p2_y  = bond_row['y2']
                        p2_z  = bond_row['z2']
                    else:
                        p2_ID = bond_row['p1']
                        p2_x  = bond_row['x1']
                        p2_y  = bond_row['y1']
                        p2_z  = bond_row['z1']
                        
                    A = [ p1_x, p1_y, p1_z ]
                    B = [ p2_x, p2_y, p2_z ]

                    force_a, force_b = getLinearHarmonicForce(A, B, bond_k, bond_r0)

                    total_linear_force_on_particle += force_a

                # all angular bonds with this particle - at most 2
                relevant_angle_bonds = angles_df.loc[ (angles_df['p1'] == p1_ID) | (angles_df['p2'] == p1_ID) | (angles_df['p3'] == p1_ID) ]
                for _, ang_row in relevant_angle_bonds.iterrows(): # loop over angular bonds
                    
                    A_id = ang_row['p1']
                    B_id = ang_row['p2']
                    C_id = ang_row['p3']

                    # partner particles ID
                    if A_id == p1_ID:
                        partners = [B_id, C_id]
                    elif B_id == p1_ID:
                        partners = [A_id, C_id]
                    elif C_id == p1_ID:
                        partners = [A_id, B_id]
                    else:
                        print("Something went wrong when selecting particle ID in angular bond!")

                    type1 = df_all_timepoint.loc[df_all_timepoint['particleID']==partners[0]]['type'].tolist()[0]
                    type2 = df_all_timepoint.loc[df_all_timepoint['particleID']==partners[1]]['type'].tolist()[0]

                    angle_k      = ang_row['k']
                    angle_theta0 = ang_row['t0']

                    # check that both partners are free
                    if type1 == 'free' and type2 == 'free':

                        # get the three points a -- b -- c
                        a_x = df_all_timepoint.loc[df_all_timepoint['particleID']==A_id]['x'].tolist()[0]
                        a_y = df_all_timepoint.loc[df_all_timepoint['particleID']==A_id]['y'].tolist()[0]
                        a_z = df_all_timepoint.loc[df_all_timepoint['particleID']==A_id]['z'].tolist()[0]
                        
                        b_x = df_all_timepoint.loc[df_all_timepoint['particleID']==B_id]['x'].tolist()[0]
                        b_y = df_all_timepoint.loc[df_all_timepoint['particleID']==B_id]['y'].tolist()[0]
                        b_z = df_all_timepoint.loc[df_all_timepoint['particleID']==B_id]['z'].tolist()[0]

                        c_x = df_all_timepoint.loc[df_all_timepoint['particleID']==C_id]['x'].tolist()[0]
                        c_y = df_all_timepoint.loc[df_all_timepoint['particleID']==C_id]['y'].tolist()[0]
                        c_z = df_all_timepoint.loc[df_all_timepoint['particleID']==C_id]['z'].tolist()[0]

                        A = [ a_x, a_y, a_z ]
                        B = [ b_x, b_y, b_z ]
                        C = [ c_x, c_y, c_z ]

                        force_a, force_b, force_c = getAngularHarmonicForce(A, B, C, angle_k, angle_theta0)

                        if A_id == p1_ID:
                            angForce = force_a
                        elif B_id == p1_ID:
                            angForce = force_b
                        elif C_id == p1_ID:
                            angForce = force_c
                        else:
                            print("Something went wrong when getting angForce!")

                        total_angular_force_on_particle += angForce

                # collect results for this particle
                particledict['particleID'].append(particle)

                # force vectors
                particledict['totalLinForce'].append(total_linear_force_on_particle)
                particledict['totalAngForce'].append(total_angular_force_on_particle)

                # force magnitudes
                particledict['magTotalLinForce'].append(mag(total_linear_force_on_particle))
                particledict['magTotalAngForce'].append(mag(total_angular_force_on_particle))

            df_sub_timepoint = df_sub_timepoint.merge(pd.DataFrame(particledict), left_on='particleID', right_on='particleID')

            return_dflist.append(df_sub_timepoint)
        
    sub_df_extended = pd.concat(return_dflist).reset_index()
    return(sub_df_extended)
*/