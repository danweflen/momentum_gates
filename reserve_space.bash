#!/bin/bash


#Wall Clock time
#PBS -l walltime=999:00:00

#Merge stdout and stderr
#PBS -j oe

#Output file for stdout
#PBS -o /home/becker/weflen/momentum_gates/reserve_space.out

#Sets my email
#PBS -M weflen@colorado.edu

#Emails when the job fails
#PBS -m a

sleep 3h

echo "done!\n"
