import math
import scipy as sp
import scipy.fftpack as ft
import numpy as np
from math import pi

def wigner_distribution(psi):
    #psi is assumed to be a numpy array
    if psi.size%2==0:
        psi=np.pad(psi, (0,1),mode="constant")
    npts=psi.size
    wigner=sp.zeros((npts,npts), complex)
    for position in np.arange(0,npts):
        psi_copy_low=psi
        shift=position-psi.size/2
        psi_copy_low=np.roll(psi_copy_low,-shift)
        if shift<0:
            psi_copy_low[:-shift]=0.0
        elif shift>0:
            psi_copy_low[-shift:]=0.0
        acorr=psi_copy_low*np.conj(psi_copy_low[::-1])
        ftrans=ft.fft(acorr,overwrite_x=True)
        ftrans=1/sp.pi*ftrans
        #Removing the linear phase induced by the fft function
        #considering the first element as 0 rather than the
        #middle element. This uses the fourier shifting theorem.
        shift=ftrans.size/2+1
        permuted_fft=ftrans*np.exp(-2j*math.pi*shift*np.arange(0,ftrans.size)/ftrans.size)
        #Shifting the fft itself back into place.
        ftrans=ft.fftshift(permuted_fft)
        wigner[position]=ftrans
    return wigner.transpose()

def wigner_distribution_2(psi):
    wigner=sp.zeros((psi.size,psi.size))
    for position in np.arange(0,psi.size):
        width=min(position+1, psi.size-position)
        up=psi[position:position+width]
        down=psi[position-width+1:position+1]
        down=down[::-1]
        acorr=down*np.conj(up)
        ftrans=np.fft.irfft(acorr,n=psi.size)
        ftrans=ftrans*psi.size/pi
        #Shifting the fft itself back into place.
        ftrans=ft.fftshift(ftrans)
        wigner[position]=ftrans
    return wigner.transpose()

