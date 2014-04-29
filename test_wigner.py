#! /usr/bin/env python
from math import pi
import numpy as np
import scipy as sp
from my_wigner import wigner_distribution
import matplotlib.pyplot as plt

grid=np.arange(-10,10.05,0.05)
arg=np.fmax(np.exp(-(grid)**2),np.zeros(grid.size))
x=np.arange(-10,10.05,0.05).reshape((1,grid.size))
p=np.arange(-10,10.05,0.05).reshape((grid.size,1))
ana=np.sqrt(1/(2*pi))*np.exp(-2*x**2)*np.exp(-pi**2*p**2/2)
xgrid=np.ones(grid.size).reshape((grid.size,1))*x
pgrid=np.ones(grid.size).reshape((1,grid.size))*p
wig=wigner_distribution(arg)*0.05
real=sp.real(wig)
imag=sp.imag(wig)
test=2*(ana-real)/(ana+real)
print np.max(np.abs(test))
print np.abs(test).mean()
argmax=np.argmax(test)
amax=np.amax(test)
print amax
print real.flat[argmax]
print ana.flat[argmax]
np.save("test.npy",test)
grid.resize(wig.shape[1])
plt.contourf(grid,grid,test,50,cmap="jet")
plt.title("test")
plt.colorbar()
plt.xlim(-10,10)
plt.ylim(-10,10)
np.save("real.npy",real)
plt.show()

