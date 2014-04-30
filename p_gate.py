#!/usr/bin/env python
import matplotlib
matplotlib.use("GDK")
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
import wigner

#Reading in the wavefunction and initializing parameters that only depend on the
#parameters of the wavefunction.
datafile_name=sys.argv[1]
store=pd.HDFStore(datafile_name)
wfn_timeseries=store['wavefunction']
wavefunction=wfn_timeseries[10].values
N=wavefunction.size
t=sp.linspace(-50,50,N)
ell = sp.asarray(range(0,N)) - N/2
dt = t[1]-t[0]
s =  ell / (dt * N)
T, S = sp.meshgrid(t,s)
del t,s

#Creating the figure and setting the figure parameters.
fig=plt.figure()
plt.xlabel("x")
plt.ylabel("p")
wigner_function=np.real(wigner.wdf(wavefunction))
ax=fig.add_subplot(111,autoscale_on=False, xlim=(-10,10), ylim=(-1.5,1.5))
wigner_figure =ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap="jet")

#Animate function: this is called sequentially by FuncAnimation
def animate(i):
    wigner_function=-1*wigner.wdf(wfn_timeseries[10*i+10].values)
    wigner_figure=ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap="RdBu")
    return wigner_figure

#Animating and saving the resulting video.
anim=animation.FuncAnimation(fig, animate, frames=260)
store.close()
anim.save("/users/becker/weflen/momentum_gates/norio.mp4", fps=20)

