#!/bin/bash

#SBATCH --mem-per-cpu=20G
#SBATCH --time=15:00:00
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 8

# start up the env
source /usr/people/yaraujjo/.bashrc
conda activate torch

# go to directory where the script lives
cd /scratch/sherlock_neu502b/code/for_slurm/second_runk10

# run script for each participant
srun -n 8 --mpi=pmi2 python batch.py -bp "/scratch/sherlock_neu502b/data/movie_files/sherlock_movie_s"${c}".nii" -slrad 3 -mbe 6 -pl 1

