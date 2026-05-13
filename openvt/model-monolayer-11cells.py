import matplotlib.pyplot as plt
import subprocess
import os
import pandas as pd
import numpy as np

def main():
    executable_path = "../bin/openvt-monolayer-11cells"
    parameter_file ="monolayer-11cells.par"
    output_path =  "monolayer-11cells/"
    simulate_flag = True # if set to False only the post-processing will be carried out.
    n_reps=10

    if simulate_flag:
        for rep in range(1,n_reps+1):
            print(f"Running simulation {rep}/{n_reps} ...")

            if n_reps !=1:
                # changing the content of the input parameter file for different replica
                # Read the parameter file and modify lines
                with open(parameter_file, "r") as file:
                    lines = file.readlines()
                # Replace lines containing "this text"
                new_lines = ["datadir = " +output_path +"/rep"+ str(rep) + "\n" if "datadir" in line else line for line in lines]

                new_parameter_file = parameter_file[0:-4] +"_temp.par"
                # Write the modified lines back to the file
                with open(new_parameter_file, "w") as file:
                    file.writelines(new_lines)
                
                # setting the path for the paramter file
                parameter_file_path = new_parameter_file

                # generating the output directories recusively
                os.makedirs(output_path +"/rep"+ str(rep), exist_ok=True)
            else:
                parameter_file_path = parameter_file
                # generating the output directories recusively
                os.makedirs(output_path, exist_ok=True)

            # Run the executable for each replica
            try:
                subprocess.run(
                    [executable_path, parameter_file_path, "--platform minimal"],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Simulation {rep} failed: {e}")
                continue

        if n_reps !=1:
            # Delete the temporarily generated generated parameter file for different replica
            os.remove(new_parameter_file)


    # POST-PROCESSING
    
    # Reading data into a single pandas dataframe
    tracks = pd.DataFrame()
    for rep in range(1,n_reps+1):
        # Read output and write width vs time
        output_path_per_rep=output_path +"/rep"+ str(rep)
        tracks_per_rep = pd.read_csv(os.path.join(output_path_per_rep,'tst.csv'))
        tracks_per_rep["replica"]=rep
        tracks =pd.concat([tracks, tracks_per_rep], ignore_index=True)
    # Saving to a csv file
    tracks.to_csv(output_path+ "/" + "tracks.csv",float_format='%.7E')

    width_flag= True
    CD= 10 #px
    T = 154 #MCS
    T_burnin=200 #MCS
    if width_flag:
        # Plotting the width for each replica
        # Calculate width
        fig, ax = plt.subplots()
        width_df = pd.DataFrame()
        width_df['Normalized time (T)'] = (tracks['time (MCS)'].unique()-T_burnin)/T
        for rep in range(1, n_reps + 1):
            tracks_per_rep = tracks.loc[tracks["replica"] == rep]
            width_per_rep = []
            for time in tracks['time (MCS)'].unique():
                frame_data = tracks_per_rep.loc[tracks_per_rep['time (MCS)'] == time]['com_1 (px)']
                width_per_rep.append(np.max(frame_data) - np.min(frame_data))
            width_df['Tissue width rep' + str(rep)+ ' (CD)'] = np.array(width_per_rep)/CD

            # Plotting the width for ech replica
            ax.plot(width_df['Normalized time (T)'], width_df['Tissue width rep' + str(rep)+' (CD)'],color='gray',linewidth=0.5,alpha=0.5)
        
        width_data=width_df[['Tissue width rep'+ str(rep) + ' (CD)' for rep in range(1,n_reps+1)]].to_numpy()
        mean_data=np.mean(width_data,axis=1)
        std_data=np.std(width_data,axis=1)
        width_df['Mean Tissue width (CD)']= mean_data
        width_df['STD Tissue width (CD)']= std_data
        ax.fill_between(width_df['Normalized time (T)'], mean_data-std_data,mean_data+std_data,alpha=0.5)
        ax.plot(width_df['Normalized time (T)'],mean_data)
        ax.plot([1,1],[5,10],'k--',linewidth=.7)
        ax.plot([0,10],[9,9],'k--',linewidth=.7)
        ax.plot([0,10],[10,10],'k--',linewidth=.7)
        ax.set_xlim((0,10))
        ax.set_ylim((5,10.25))
        ax.set_xlabel('Time (T)')
        ax.set_ylabel('Tissue width (CD)')

        # Saving to a csv file
        width_df.to_csv(output_path+ "/" + "width.csv",float_format='%.7E')
        ax.set_xlim((0,10))
        plt.show()

if __name__ == "__main__":
    main()

