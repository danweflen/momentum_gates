#! /usr/bin/env python
import numpy as np
import scipy as sp
from my_wigner import wigner_distribution
import matplotlib.pyplot as plt

grid=np.arange(-10,10,0.1)
arg=np.exp(-((grid))**2)
wig=bwigner_distribution(arg)
real=sp.real(wig)
imag=sp.imag(wig)
plt.xlim(-3,3)
plt.ylim(-3,3)
grid.resize(wig.shape[1])
plt.contourf(grid,grid,real.transpose(),100,cmap="RdBu")
np.save("real.npy",real)
plt.colorbar()
plt.show()

