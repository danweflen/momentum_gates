#!/bin/bash

#Wall Clock time
#PBS -l walltime=8:00:00

#Merge stdout and stderr
#PBS -j oe

#Output file for stdout
#PBS -o /home/becker/weflen/npsf_h/plot_population.out

#Sets my email
#PBS -M weflen@colorado.edu

#Emails when the job fails
#PBS -m a

#Rerun a job if it fails
#PBS -r y

#PBS -l nodes=1:ppn=16

#PBS -N plot_population

/home/becker/weflen/momentum_gates/p_gate.py 