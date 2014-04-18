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

time=1843.128
datafile_name=sys.argv[1]
store=pd.HDFStore(datafile_name)
wfn_timeseries=store['wavefunction']
wavefunction=wfn_timeseries[time].values
N=wavefunction.size
t=sp.linspace(-299.9736,299.9736,N)
ell = sp.asarray(range(0,N)) - N/2
dt = t[1]-t[0]
print dt
s =  ell / (dt * N)
print s[1]-s[0]
T, S = sp.meshgrid(t,s)
del t,s

fig=plt.figure()
wigner_function=wigner.wdf(wavefunction)
ax=fig.add_subplot(111,autoscale_on=False, xlim=(-10,10), ylim=(-2,2))
ax.set_xlabel("x")
ax.set_ylabel("p")
ax.set_title("Wigner distribution, time="+str(time)+"au")
ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap="jet")

plt.show()

store.close()

