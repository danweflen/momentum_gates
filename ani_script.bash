#!/bin/bash

#Wall Clock time
#PBS -l walltime=48:00:00

#Merge stdout and stderr
#PBS -j oe

#Output file for stdout
#PBS -o /users/becker/weflen/momentum_gates/ani_wigner.out

#Sets my email
#PBS -M weflen@colorado.edu

#Emails when the job fails
#PBS -m a

#Don't rerun a job if it fails
#PBS -r n

#PBS -l nodes=1:ppn=4

#PBS -N animate_wigner

DATA_DIR=/data/becker/weflen/poly/momentum_gate_norio/

FILE=$DATA_DIR/momentum_gate_norio/wavefunction_file_key_2000.wfn.h5

/home/becker/weflen/momentum_gates/p_gate.py $FILE

