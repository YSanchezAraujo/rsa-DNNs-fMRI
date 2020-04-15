* firststeps.ipynb - This notebook computes the correlation matrices to use in the searchlight RSA analysis

* secondlevel.ipynb - This notebook carries out the second level analysis

* proj_utils.py - python function utilities used for various parts in the analysis

* batch.py - python script to run the searchlight analysis on spock

* batch.sh - bash file to submit batch.py to slurm

* auxiliary bash commands, just copy and paste in terminal to submit to slurm

This is the general order of execution for the relevant files:

    1. First firststeps is run to create the neural network correlation matrices
    2. Then batch.py is run on a cluster to generate the searchlight results needed for second_level.ipynb
    3. Then second_level.ipynb is run for the group level.
