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
complexified_data=np.array([tp[0],tp[1],wavefunction]).transpose()
wfn_timeseries=pd.DataFrame(complexified_data, columns=["time","x","wavefunction"])
del complexified_data, raw_data, tp, wavefunction
print wfn_timeseries
