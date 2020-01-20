"""
Registration: xxxx; 
Description: FFT

Author: AKB
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

N = 600; period = 1.0/800;
x = np.linspace(0.0, N*period, N)
f = np.exp(-x**2)
#f = np.sin(50.0*2.0*np.pi*x) + 0.5*np.sin(100.0*2.0*np.pi*x)
fk = fft(f); 
xk = np.linspace(0.0, 1.0/(2*period), N/2)
plt.semilogy(xk, 2.0/N*np.abs(fk[0:N/2]))
plt.title(r'Fourier Transform of $\exp(-x^2)$')
plt.xlabel(r'$x_k$',size=16)
plt.ylabel(r'$FT[exp(-x^2)]$',size=16)
plt.grid()
plt.show()
