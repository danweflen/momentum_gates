#!/bin/bash

#Wall Clock time
#PBS -l walltime=72:00:00

#Merge stdout and stderr
#PBS -j oe

#Output file for stdout
#PBS -o /users/becker/weflen/momentum_gates/wigner_script.out

#Sets my email
#PBS -M weflen@colorado.edu

#Emails when the job fails
#PBS -m a

#Don't rerun a job if it fails
#PBS -r n

#PBS -l nodes=1:ppn=8

#PBS -N wigner_plots

export PYTHONPATH=$PYTHONPATH:/users/becker/weflen/npsf_h/npsflib/python
export PATH=/users/becker/weflen/progs/anaconda/bin:$PATH:/usr/local/cuda/bin

DATA_DIR=/users/becker/weflen/data/poly/momentum_gate_check/momentum_gate_check__2/

DATA_FILE=$DATA_DIR/wavefunction_file_*.h5

/users/becker/weflen/momentum_gates/wigner_plots.py $DATA_FILE

echo "Done"
