#! /usr/bin/env python
import numpy as np
import scipy as sp
from my_wigner import wigner_distribution
import matplotlib.pyplot as plt

grid=np.arange(-10,10,0.05)
arg=np.fmax(np.exp(-(grid)**2),np.zeros(grid.size))
x=np.arange(-10,10.05,0.05).reshape((1,grid.size+1))
p=np.arange(-10,10.05,0.05).reshape((grid.size+1,1))
ana=np.sqrt(1/(2*sp.pi))*np.exp(-2*x**2)*np.exp(-2*np.pi*p*p)
xgrid=np.ones(grid.size).reshape((grid.size,1))*x
pgrid=np.ones(grid.size).reshape((1,grid.size))*p
wig=wigner_distribution(arg)*0.05
real=sp.real(wig)
imag=sp.imag(wig)
test=(real-ana)
np.save("test.npy",test)
grid.resize(wig.shape[1])
plt.contourf(grid,grid,real,50,cmap="jet")
plt.colorbar()
plt.xlim(-5,5)
plt.ylim(-5,5)
np.save("real.npy",real)
plt.show()

