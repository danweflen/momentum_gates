#! /usr/bin/env python
import numpy as np
import scipy as sp
from my_wigner import wigner_distribution
import matplotlib.pyplot as plt
from math import pi

grid=np.arange(-10,10.05,0.05)
N=grid.size
t=grid
ell = sp.asarray(range(0,N)) - N/2
dx = t[1]-t[0]
s =  2*ell / (dx * N) 
T, S = sp.meshgrid(t,s)
a=2
k=-2
arg=np.exp(-a*(grid)**2)*np.exp(1j*k*grid)
x=np.arange(-10,10.05,0.05).reshape((1,grid.size))
p=np.arange(-10,10.05,0.05).reshape((grid.size,1))
#The pi comes from the fact that the calculated and analytical grids
#don't match up. The definition of the fourier transform has a pi
#in the exponent, this means that p_ana=p_wig/pi.
ana=1/np.sqrt(2*pi)*np.exp(-2*a*x**2)*np.exp(-(pi*p-k)**2/(2*a))
xgrid=np.ones(grid.size).reshape((grid.size,1))*x
pgrid=np.ones(grid.size).reshape((1,grid.size))*p
start=time.time()
wig=wigner_distribution(arg)*(grid[1]-grid[0])
wig2=wigner_distribution_2(arg)*(grid[1]-grid[0])
end=time.time()
print "Wigner calculation time: ", end-start
real=wig2
test=ana-real
#test=2*(ana-wig)/(ana+wig)
print "ana max: ", np.max(ana)
print "real max: ", np.max(real)
print "max ratio: ", np.max(real)/np.max(ana)
print "max absolute value error: ",np.max(np.abs(test))
print "mean absolute error: ", np.abs(test).mean()
argmax=np.argmax(test)
amax=np.amax(test)
print "max error", amax
print "real at max absolute error: ",real.flat[argmax]
print "ana at max absolute error: ",ana.flat[argmax]
np.save("test.npy",test)
grid.resize(wig.shape[1])
fig=plt.figure()
ana_ax=fig.add_subplot(211)
ana_im=ana_ax.contourf(T,S,ana,np.array([0.01*x for x in range(-1,51)]),cmap="jet")
ana_ax.set_title("ana")
plt.xlim(-10,10)
plt.ylim(-10,10)
fig.colorbar(ana_im)
wig_ax=fig.add_subplot(212)
wig_im=wig_ax.contourf(T,S,real,50,cmap="jet")
wig_ax.set_title("real")
fig.colorbar(wig_im)
plt.xlim(-10,10)
plt.ylim(-10,10)
# test_ax=fig.add_subplot(313)
# test_im=wig_ax.contourf(T,S,test,20,cmap="jet")
# plt.xlim(-10,10)
# plt.ylim(-10,10)
# fig.colorbar(test_im)
np.save("real.npy",real)
plt.show()

