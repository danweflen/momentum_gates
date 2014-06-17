#!/usr/bin/env python
import sys, itertools, os
from time import sleep
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import scipy as sp
import scipy.fftpack as ft
import scipy.linalg as lin
import numpy as np
import pandas as pd
import math
from multiprocessing import Pool
from matplotlib import animation
from string import *
from my_wigner import wigner_distribution, wigner_distribution_2

datafile_name=sys.argv[1]
store=pd.HDFStore(datafile_name)
wfn_timeseries=store['wavefunction']
times=filter(lambda x: x>0 and x<5000, wfn_timeseries.columns)
nprocs=4
fig=plt.figure()
times=np.array_split(times,nprocs)

procid=0 #Forks the program into nprocs programs, each with a procid from 0 to nprocs-1
for x in range(1,nprocs):
    if (os.fork()==0):
        procid=x
        break

times=times[procid]
for time in times:
    wavefunction=wfn_timeseries[time].values
    N=wavefunction.size
    t=np.array(wfn_timeseries.index)
    ell = sp.asarray(range(0,N)) - N/2
    dx = t[1]-t[0]
    s =  2*ell / (dx * N) 
    T, S = sp.meshgrid(t,s)
    store.close()
    wigner_function=dx*wigner_distribution_2(wavefunction)
    wig_ax=fig.add_subplot(111, xlim=(-10,10), ylim=(-1.5,1.5))
    wig_ax.set_xlabel("x")
    wig_ax.set_ylabel("p")
    wig_ax.set_title("Wigner distribution, time="+str(time)+"au")
    levels=np.arange(-0.35,0.35,0.01)
    image=wig_ax.contour(T.transpose(), S.transpose(), np.real(wigner_function.transpose()),levels,cmap="RdBu")
    fig.colorbar(image)
    plt.savefig("/users/becker/weflen/momentum_gates/plots/high/wigner_"+str(time)+"_au.png")
    plt.clf()

