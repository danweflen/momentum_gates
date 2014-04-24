#####################################################################################
# The MIT License                                                                   #
#                                                                                   #
# Copyright (c) 2011, Alex Yuffa (ayuffa@gmail.com)                                 #
#                                                                                   #
# Permission is hereby granted, free of charge, to any person obtaining a copy      #
# of this software and associated documentation files (the "Software"), to deal     #
# in the Software without restriction, including without limitation the rights      #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell         #
# copies of the Software, and to permit persons to whom the Software is             #
# furnished to do so, subject to the following conditions:                          #
#                                                                                   #
# The above copyright notice and this permission notice shall be included in        #
# all copies or substantial portions of the Software.                               #
#                                                                                   #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR        #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,          #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE       #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER            #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,     #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN         #
# THE SOFTWARE.                                                                     #
#####################################################################################

import scipy as sp
import scipy.fftpack as ft
import math

def wdf(x):
    '''
    Wigner Distribution function (wdf) [aka Wigner transform] of a function x(t) is
    defined by
    $ W(t,s) = \int_{-\infty}^{\infty} x(t+\tau/2) x^*(t-\tau/2) \exp(-2\pi i \tau s) d\tau $.
    We do wdf numerically.
    
    INPUT:
    x = $x(t_i)$ for $i=0,1,\ldots,N-1$.  It's assumed that outside the sampling interval $x(t)=0$.

    OUTPUT:
    W = is real $N \times N$ array. Each ROW of W corresponds to a given $t_i$.
        Examples:
        1st row of W is $wdf(x(t_0))$. 
        2nd row W is $wdf(x(t_1))$.
        Last row of W is $wdf(x(t_{N-1}))$.

    '''
    N = x.size
    # make f a column vector
    x = x.reshape(N,1)
    X = ft.fft(x, axis=0)

    # shift row vector
    shift = sp.array(range(0,N)).reshape(1,N) - N/2.0

    # k column vector; appropriate for F
    k = shift.copy().reshape(N,1) - N/2.0
    k = ft.ifftshift(k)
    
    ones = sp.ones((1,N), float)
    # shift function to the left, f(x+\tau/2) and to the right f(x-\tau/2)
    # via Fourier shifting theorem
    arg = ft.fftshift(2.0J*sp.pi/N * sp.dot(k, shift), axes=(1,))
    xShiftedLeft = ft.ifft(sp.dot(X,ones) * sp.exp(arg), axis=0)
    xShiftedRight = ft.ifft( sp.dot(X,ones) * sp.exp(-arg), axis=0)
    # each column of fShifted is shifted by the same amount.
    
    W = ft.fft(xShiftedLeft * xShiftedRight.conjugate())
    return sp.real(W)/sp.pi
#---------------------------------------------------------------------------------------------------
def plotExample():
    '''
    Example of wdf contour plot.
    '''
    import matplotlib.pyplot as plt
    N = 500
    t = sp.linspace(-5,5,N)
    x = sp.exp(-t**2)
    W = wdf(x)
    
    ell = sp.asarray(range(0,N)) - N/2
    dt = t[1]-t[0]
    s =  ell / (dt * N) 

    T, S = sp.meshgrid(t,s)
    
    plt.figure()
    plt.contourf(T.transpose(), S.transpose(), W)
    plt.xlabel('t', fontsize=16)
    plt.ylabel('s', fontsize=16)
    plt.show()
