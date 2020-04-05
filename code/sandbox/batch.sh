#!/bin/bash

#SBATCH --mem=18G
#SBATCH -c 8
#SBATCH --time=7:00:00


# start up the env
source /usr/people/yaraujjo/.bashrc
conda activate torch

# go to directory where the script lives
cd /scratch/sherlock_neu502b/code/for_slurm

# run script for each participant
python batch.py -bp "/scratch/sherlock_neu502b/data/movie_files/sherlock_movie_s"${c}".nii" -slrad 3 -mbe 6 -pl 1
