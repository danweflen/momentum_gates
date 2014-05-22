#! /usr/bin/env python
from math import pi
import numpy as np
import scipy as sp
from my_wigner import wigner_distribution, wigner_distribution_2
import matplotlib.pyplot as plt
import time

grid=np.arange(-10,10.05,0.05)
N=grid.size
t=grid
ell = sp.asarray(range(0,N)) - N/2
dx = t[1]-t[0]
s =  2*ell / (dx * N) 
T, S = sp.meshgrid(t,s)
a=0.2
k=-9
arg=np.exp(-a*(grid)**2)*np.exp(1j*k*grid)
x=np.arange(-10,10.05,0.05).reshape((1,grid.size))
p=np.arange(-10,10.05,0.05).reshape((grid.size,1))
#The pi comes from the fact that the calculated and analytical grids
#don't match up. The definition of the fourier transform has a pi
#in the exponent, this means that p_ana=p_wig/pi. Currently I get
#
#
ana=1/np.sqrt(2*pi)*np.exp(-2*a*x**2)*np.exp(-(pi*p-k)**2/(2*a))
xgrid=np.ones(grid.size).reshape((grid.size,1))*x
pgrid=np.ones(grid.size).reshape((1,grid.size))*p
start=time.time()
wig=wigner_distribution(arg)*(grid[1]-grid[0])
wig2=wigner_distribution_2(arg)*(grid[1]-grid[0])/2.0
end=time.time()
print "Wigner calculation time: ", end-start
real=wig2
test=real-ana
#test=2*(ana-wig)/(ana+wig)
print "ana[0,0]: ", ana[0,0]
print "real[0,0]: ", real[0,0]
print "max absolute value error: ",np.max(np.abs(test))
print "mean absolute error: ", np.abs(test).mean()
argmax=np.argmax(test)
amax=np.amax(test)
print "max error", amax
print "real at max absolute error: ",real.flat[argmax]
print "ana at max absolute error: ",ana.flat[argmax]
np.save("test.npy",test)
grid.resize(wig.shape[1])
plt.contourf(T,S,test,50,cmap="jet")
plt.title("test")
plt.colorbar()
plt.xlim(-10,10)
plt.ylim(-10,10)
np.save("real.npy",real)
plt.savefig("test.png")
plt.show()
