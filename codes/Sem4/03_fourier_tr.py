"""
Registration : xxxx
Description  : Triangular Wave Fourier Series
Author       : AKB
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

A      = 2;      # Amplitude
period = np.pi;  # periodicity
t      = np.linspace(-2*period, 2*period, 256) 
harmonics = 2;   # Harmonics

# generate saw-tooth waveform
def trwave(t, period):
    return A*2*np.arcsin(np.sin(np.pi*t/period))/np.pi
    
# Fourier coefficients; an=0
def bn(n):
    if (n%2 != 0):
        return 8*pow(-1,(n-1)/2)/pow(np.pi*n,2)
    else:
        return 0

# Fourier series
def fourierTr(harmonics,t):
    summ = 0.0
    for i in range(1, harmonics):
        summ += A*bn(i)*np.sin(i*np.pi*t/period)
    return summ

# Main 
y = []; f1 = []; f2 = []; f3 = []
for i in t:
    y.append(trwave(i,period))
    f1.append(fourierTr(  harmonics,i))
    f2.append(fourierTr(4*harmonics,i))
    f3.append(fourierTr(8*harmonics,i))

# Plot
sg = A*signal.sawtooth(np.pi*(t+period/2)/period, width=0.5) # Constructed signal
plt.plot(t, sg, '-',  lw='2', color="red",    label="Signal(scipy)")
plt.plot(t,  y, '-o', lw='1', color="teal",   label=r'Signal$(\frac{2A}{\pi}sin^{-1}(sin(\frac{\pi t}{period})$')
plt.plot(t, f1, '-*', lw='1', color="gold",   label=str(harmonics)+" harmonics")
plt.plot(t, f2, '-+', lw='1', color="magenta",label=str(4*harmonics)+" harmonics")
plt.plot(t, f3, '-x', lw='1', color="olive",  label=str(8*harmonics)+" harmonics")
plt.title("Triangular Wave Fourier Series", size=16)
plt.legend(loc='best', prop={'size':16})
plt.xlabel('t', size=16)
plt.xticks(size=14)
plt.ylabel(r'$f(t)=\sum_{n=odd}^\infty\; \frac{8A}{n^2\pi^2}(-1)^{(n-1)/2} sin(n\omega t)$', size=20)
plt.yticks(size=14)
plt.xlim([-2*period, 2*period])
plt.ylim([-A-.25, A+.25])
plt.grid()
#plt.savefig('plot/03_fouriertr.pdf')
plt.tight_layout()
plt.show()
