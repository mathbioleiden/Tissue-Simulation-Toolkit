#!/bin/bash

#SBATCH -J cpm_ecm
#SBATCH --time=00:10:00
#SBATCH -p gpu
#SBATCH -N 1
#SBATCH --gpus-per-node=4


module load 2022
module load Qt5/5.15.5-GCCcore-11.3.0 OpenMPI/4.1.4-GCC-11.3.0 Python/3.10.4-GCCcore-11.3.0 CUDA/11.8.0

cd /scratch-shared/lveen/tissueopt/Tissue-Simulation-Toolkit

source venv/bin/activate

export QT_QPA_PLATFORM=offscreen

muscle_manager --start-all ymmsl/adhesions.ymmsl ymmsl/dump_state.ymmsl

