import numpy as np
from scipy.ndimage import label
from TST_analyse import Simulation, summary, Experiment
import pandas as pd

@summary
def crossings(sim):
# sim = Simulation("data_sizex633box_size_x633Lx316_5number_of_ISV10strands600spring_k10_0Ly100_0box_size_y200sizey200adhesion_contraction_force2_0adhesion_yielding_lambda100only_tipcell_adhTruesomite_antitaxis100diff_coeff2_0,1e-13it1")
    output = dict()
    for time in sim.times:
        cpm = sim.State(time)['cpm_state']['cpm'].array
        cpm[cpm > 0] = 1
        cpm[cpm == -1] = 0
        
        # Assume `binary_image` is a 2D numpy array with values 0 (background) and 1 (foreground)
        
        # Define the structure for 4-connectivity
        structure = np.array([[1, 1, 1],
                              [1, 1, 1],
                              [1, 1, 1]])
        
        # Label the connected components
        labeled_array, num_features = label(cpm, structure=structure)
        
        crossings = sim.Parameter("number_of_ISV") - num_features
        
        output.setdefault("time", list()).append(time) 
        output.setdefault("crossings", list()).append(crossings) 
        output.setdefault("components", list()).append(num_features) 
   
    return pd.DataFrame(output)

Experiment.fromFolder(".", parameters=['strands', 'diff_coeff', 'it', 'spring_k']).GetSummary(crossings,save=True)
