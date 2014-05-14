#!/usr/bin/env python
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
import sys, itertools, os
from my_wigner import wigner_distribution_2

#Reading in the wavefunction and initializing parameters that only depend on the
#parameters of the wavefunction.
datafile_name=sys.argv[1]
store=pd.HDFStore(datafile_name)
wfn_timeseries=store['wavefunction']
times=filter(lambda x: x>1000 and x<2000, wfn_timeseries.columns)
wavefunction=wfn_timeseries[times[0]].values
N=wavefunction.size
t=np.array(wfn_timeseries.index)
ell = sp.asarray(range(0,N)) - N/2
dt = t[1]-t[0]
s =  ell / (dt * N)
T, S = sp.meshgrid(t,s)
del t,s

#Creating the figure and setting the figure parameters.
fig=plt.figure()
plt.xlabel("x")
plt.ylabel("p")
wigner_function=wigner_distribution_2(wavefunction)
ax=fig.add_subplot(111,autoscale_on=False, xlim=(-10,10), ylim=(-1.5,1.5))
wigner_figure =ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap="jet")

#Animate function: this is called sequentially by FuncAnimation
def animate(i):
    wigner_function=wigner_distribution_2(wfn_timeseries[times[i]].values)
    wigner_figure=ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap="RdBu")
    return wigner_figure

#Animating and saving the resulting video.
anim=animation.FuncAnimation(fig, animate, frames=50)
store.close()
anim.save("/users/becker/weflen/momentum_gates/norio_dup.mp4", fps=10)

