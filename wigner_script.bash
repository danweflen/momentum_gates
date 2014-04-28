#!/bin/bash

#Wall Clock time
#PBS -l walltime=6:00:00

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

#PBS -l nodes=1:ppn=2

#PBS -N one_wigner

export PYTHONPATH=$PYTHONPATH:/users/becker/weflen/npsf_h/npsflib/python
export PATH=/users/becker/weflen/progs/anaconda/bin:$PATH:/usr/local/cuda/bin

DATA_DIR=/data/becker/weflen/poly/momentum_gate_norio_exact/

DATA_FILE=$DATA_DIR/momentum_gate_norio_exact/wavefunction_file_key_2000.wfn.h5

/users/becker/weflen/momentum_gates/one_wigner.py $DATA_FILE

echo "Done"
