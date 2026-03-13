import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from TST_analyse import Experiment, cell_data, summary, fa_lifetime, expand_adhesions


params = [
        "it", 
        "spring_k",
        "strands",
        "ns_gamma",
]

exper = Experiment.fromFolder("./" , parameters=params)
print(exper.parameters)

@summary
def tipcell(sim):
    return pd.DataFrame({
        'time': sim.times,
        'tipcell': [sim.State(time)['cpm_state']['tipcell'] for time in sim.times],
        }) 
from scipy.ndimage import label 
def is_connected_moore(A): 
    # Label the connected components using a Moore neighborhood (8-connectivity) 
    structure = np.ones((3, 3), dtype=int)  # Define the 8-connectivity structure 
    labeled, num_features = label(A, structure=structure) 
 
    # Check if all "1"s are part of the same connected component 
    return num_features <= 1 
 
from collections import defaultdict 
@summary 
def connected_vessel(sim): 
    output = defaultdict(list) 
 
    for time in sim.times: 
        sigma = sim.State(time)['cpm_state']['cpm'].array 
        vessel = sigma > 0 
        output['time'].append(time) 
        output['connected'].append(is_connected_moore(vessel)) 
     
    return pd.DataFrame(output) 

exper.GetSummary(expand_adhesions, save=True)
exper.GetSummary(tipcell, save=True)
exper.GetSummary(cell_data, save=True)
exper.GetSummary(fa_lifetime, save=True)
exper.GetSummary(connected_vessel, save=True)
