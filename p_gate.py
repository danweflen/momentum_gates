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
from string import *
import sys, itertools, os
import wigner

datafile_name=sys.argv[1]
raw_data=np.load(datafile_name)
tp=raw_data.transpose()
wavefunction=np.vectorize(complex)(tp[2],tp[3])
wfn_df=pd.DataFrame({"time":tp[0],"x":tp[1], "wavefunction":wavefunction})
wfn_timeseries=wfn_df.pivot(index="x",columns="time", values="wavefunction")
store=pd.HDFStore(datafile_name)
store['wavefunction']=wfn_timeseries
del raw_data, tp, wavefunction, wfn_df
wavefunction=np.array([wfn_timeseries[10][x/100.0] for x in range(-5000,5000)])
del wfn_timeseries, store

wigner_function=wigner.wdf(wavefunction)
N=wavefunction.size
t=sp.linspace(-50,50,N)
ell = sp.asarray(range(0,N)) - N/2
dt = t[1]-t[0]
print "dt: ",dt
s =  ell / (dt * N) 
print "s: ",s
T, S = sp.meshgrid(t,s)
print "T: ",T
print "S: ",S

plt.figure()
plt.contourf(T.transpose(), S.transpose(), wigner_function, cmap='jet')
plt.xlim(-10,10)
plt.ylim(-2,2)
plt.colorbar()
plt.xlabel('x', fontsize=16)
plt.ylabel('p', fontsize=16)
plt.legend()
plt.show()

