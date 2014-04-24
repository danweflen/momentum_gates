import math
import scipy as sp
import scipy.fftpack as ft
import numpy as np

def wigner_distribution(psi):
    #psi is assumed to be a numpy array
    wigner=np.zeros((psi.size,psi.size))
    for position in np.arange(0,psi.size):
        psi_copy_low=psi
        psi_copy_high=psi
        psi_copy_low=np.roll(psi_copy_low,position)
        psi_copy_low[0:position]=0.0
        psi_copy_high=psi_copy_high[::-1]
        psi_copy_high=np.roll(psi_copy_high,-position)
        print "Matchup: "
        print psi_copy_low
        print psi_copy_high
        if position != 0:
            psi_copy_high[-position:]=0.0
        acorr=psi_copy_low*np.conj(psi_copy_high)
        ftrans=ft.fft(acorr,overwrite_x=True)
        print "Position: ", position
        ftrans=2/sp.pi*np.real(ftrans)
        wigner[position]ftrans
    return wigner
