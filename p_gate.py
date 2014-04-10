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
store=pd.HDFStore(datafile_name)
wfn_timeseries=store['wavefunction']
print wfn_timeseries[10]

wigner.plotExample()
