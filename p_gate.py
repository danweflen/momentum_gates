#!/usr/bin/env python
import matplotlib.pyplot as plt
import scipy as sp
import scipy.fftpack as ft
import scipy.linalg as lin
import numpy as np
import npsf_interface as npsf
import ionization_utilities as ion
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
wavefunction=np.array([wfn_timeseries[10][x/100.0] for x in range(-5000,5000)])
N=wavefunction.size
t=sp.linspace(-50,50,N)
ell = sp.asarray(range(0,N)) - N/2
dt = t[1]-t[0]
s =  ell / (dt * N) 
T, S = sp.meshgrid(t,s)

#Creating the figure and setting the figure parameters.
fig=plt.figure()
ax=fig.add_subplot(111,autoscale_on=False, xlim=(-10,10), ylim=(-2,2))

#Animate function: this is called sequentially by FuncAnimation
def animate(i):
    wavefunction=np.array([wfn_timeseries[10*i+10][x/100.0] for x in range(-5000,5000)])
    wigner_function=wigner.wdf(wavefunction)
    image=ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap='jet')
    return image

#Animating and saving the resulting video.
anim=animation.FuncAnimation(fig, animate, frames=300)
anim.save("test_animation.ogv")

plt.show()
