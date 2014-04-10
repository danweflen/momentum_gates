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
wfn_timeseries=wfn_df.pivot(index="time",columns="x", values="wavefunction")
store=pd.HDFStore(datafile_name+".h5")
store['wavefunction']=wfn_timeseries
del raw_data, tp, wavefunction, wfn_df
print wfn_timeseries
