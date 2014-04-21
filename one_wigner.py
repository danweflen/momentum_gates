#!/usr/bin/env python
import_unsuccessful=True
while(import_unsuccessful):
    try:
        import sys, itertools
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
        import wigner
        import_unsuccessful=False
    except (ImportError):
        import_unsuccessful=True


time=1843.128
datafile_name=sys.argv[1]
store=pd.HDFStore(datafile_name)
wfn_timeseries=store['wavefunction']
wavefunction=wfn_timeseries[time].values
N=wavefunction.size
t=np.array(wfn_timeseries.index)
ell = sp.asarray(range(0,N)) - N/2
dt = t[1]-t[0]
s =  ell / (dt * N)
T, S = sp.meshgrid(t,s)
del t,s

fig=plt.figure()
wigner_function=wigner.wdf(wavefunction)
ax=fig.add_subplot(111,autoscale_on=False, xlim=(-10,10), ylim=(-2,2))
ax.set_xlabel("x")
ax.set_ylabel("p")
ax.set_title("Wigner distribution, time="+str(time)+"au")
ax.contourf(T.transpose(), S.transpose(), wigner_function, cmap="jet")

plt.savefig("/users/becker/weflen/momentum_gates/wigner_"+str(time)+"au.png")

store.close()

