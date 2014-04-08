#!/usr/bin/env python
import matplotlib.pyplot as plt
import scipy as sp
import scipy.fftpack as ft
import scipy.linalg as lin
import numpy as np
import npsf_interface as npsf
import ionization_utilities as ion
import math
from multiprocessing import Pool
from string import *
import sys, itertools, os
import wigner

wigner.plotExample()

