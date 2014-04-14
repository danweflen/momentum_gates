#!/bin/bash


#Wall Clock time
#PBS -l walltime=999:00:00

#Merge stdout and stderr
#PBS -j oe

#Output file for stdout
#PBS -o /users/becker/weflen/npsf_h/npsf_h.out

#Sets my email
#PBS -M weflen@colorado.edu

#Emails when the job fails
#PBS -m a

sleep 3h