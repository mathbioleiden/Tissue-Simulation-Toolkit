#!/bin/bash

#SBATCH -J cpm_ecm
#SBATCH --time=00:10:00
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=18
#SBATCH --cpus-per-task=1
#SBATCH --gpus=1


module load 2022
module load Python/3.10.4-GCCcore-11.3.0

cd ${HOME}/Tissue-Simulation-Toolkit

source venv/bin/activate

export QT_QPA_PLATFORM=offscreen

muscle_manager --start-all ymmsl/adhesions.ymmsl ymmsl/dump_state.ymmsl

