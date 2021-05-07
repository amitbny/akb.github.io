"""
Registration : xxxx
Description  : Saw-tooth Wave Fourier Series
Author       : AKB
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

A      = 2;      # Amplitude
period = np.pi;  # periodicity
x      = np.linspace(-2*period, 2*period, 256) 
harmonics = 2;   # Harmonics

# generate saw-tooth waveform
def stwave(x, period):
    return A*(np.mod(x+1,2)-1)
    
# Fourier coefficients; an=0
def bn(n):                       
    return pow(-1,n+1)*2*A/(np.pi*n)

# Fourier series
def fourierSt(harmonics,x):
    summ = 0.0
    for i in range(1, harmonics):
        summ += bn(i)*np.sin(i*np.pi*x)
    return summ

# Main 
y = []; f1 = []; f2 = []; f3 = []
for i in x:
    y.append(stwave(i,period))
    f1.append(fourierSt(  harmonics,i))
    f2.append(fourierSt(4*harmonics,i))
    f3.append(fourierSt(8*harmonics,i))

# Plot
sg = A*signal.sawtooth(np.pi*(x-1)) # Constructed signal
plt.plot(x, sg, '-',  lw='4', color="red",    label="Signal(scipy)")
plt.plot(x,  y, '-o', lw='2', color="teal",   label="Signal(user)")
plt.plot(x, f1, '-*', lw='1', color="black",  label=str(harmonics)+" harmonics")
plt.plot(x, f2, '-+', lw='1', color="magenta",label=str(4*harmonics)+" harmonics")
plt.plot(x, f3, '-x', lw='1', color="olive",  label=str(8*harmonics)+" harmonics")
plt.title("Saw-tooth Wave Fourier Series", size=16)
plt.legend(loc='best', prop={'size':16})
plt.xlabel('x', size=16)
plt.xticks(size=14)
plt.ylabel(r'$f(x)=\sum_{n=1}^\infty\;\frac{2}{n\pi}(-1)^{n+1} sin(n\omega x)$', size=20)
plt.yticks(size=14)
plt.xlim([-2*period, 2*period])
plt.ylim([-A-.5, A+.5])
plt.grid()
plt.savefig('plot/03_fourierst.pdf')
plt.tight_layout()
plt.show()
