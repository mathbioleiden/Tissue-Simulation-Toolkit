import json
import subprocess
import os
import pandas as pd
import numpy as np

stdout=subprocess.PIPE

def unwrap_tracks_vectorized(input_file,output_file,sizex=100,sizey=100):
    Lx = sizex - 2 # -2 because of the boundary layers
    Ly = sizey - 2 # -2 because of the boundary layers

    df = pd.read_csv(input_file)
    df = df.sort_values(["id", "time"]).reset_index(drop=True)

    df["com_1_unwrapped"] = np.nan
    df["com_2_unwrapped"] = np.nan

    for cell_id, group in df.groupby("id", sort=False):
        group = group.sort_values("time")

        x = group["com_1"].to_numpy()
        y = group["com_2"].to_numpy()

        # ---- X direction ----
        dx = np.diff(x)
        dx = np.where(dx >  Lx / 2, dx - Lx, dx)
        dx = np.where(dx < -Lx / 2, dx + Lx, dx)

        ux = np.empty_like(x)
        ux[0] = x[0]
        ux[1:] = x[0] + np.cumsum(dx)

        # ---- Y direction ----
        dy = np.diff(y)
        dy = np.where(dy >  Ly / 2, dy - Ly, dy)
        dy = np.where(dy < -Ly / 2, dy + Ly, dy)

        uy = np.empty_like(y)
        uy[0] = y[0]
        uy[1:] = y[0] + np.cumsum(dy)

        df.loc[group.index, "com_1_unwrapped"] = ux
        df.loc[group.index, "com_2_unwrapped"] = uy

    # overwrite original columns
    df["com_1"] = df["com_1_unwrapped"]
    df["com_2"] = df["com_2_unwrapped"]

    df = df.drop(columns=["com_1_unwrapped", "com_2_unwrapped"])

    df.to_csv(output_file, index=False)

def main():
    # Path to the JSON config and executable (assumed to be in the same directory)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "input-model006.json")
    executable_path = os.path.join(base_dir, "../bin/openvt-persistentrandomwalk-model006-tst")
    
    simulation_flag = True
    post_processing_flag = True
    
    # Read JSON file
    try:
        with open(json_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {json_path}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON config. {e}")
        return

    # Get number of simulations
    try:
        num_sims = config["sim"]["num_sims"]
        #num_sims = 1
    except KeyError:
        print("Error: 'num_sims' not found in JSON config under ['sim']['num_sims']")
        return

    if simulation_flag:
        # Run the executable for each simulation ID
        for sim_id in range(num_sims):
            print(f"Running simulation {sim_id + 1}/{num_sims} with ID {sim_id}...")
            try:
                subprocess.run(
                    [executable_path, "openvt-persistentrandomwalk-model006.par", str(sim_id), "--platform minimal"], # argv[1] = parameterfile, argv[2] = id
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Simulation {sim_id} failed: {e}")
                continue

    if post_processing_flag:
        print(f"Post processing ...")
        directory = config["sim"]["output_name"]
        unwrap_tracks_vectorized(input_file= f"{directory}/tst_before_unwrapping.csv",output_file=f"{directory}/tst.csv",sizex=config["model"]["len_1"],sizey=config["model"]["len_2"])

if __name__ == "__main__":
    main()
