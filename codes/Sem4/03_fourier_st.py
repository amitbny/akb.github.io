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
t      = np.linspace(-2*period, 2*period, 256) 
harmonics = 2;   # Harmonics

# generate saw-tooth waveform
def stwave(t, period):
    return A*2*(t/period - np.floor(.5+t/period))
    
# Fourier coefficients; an=0
def bn(n):                       
    return pow(-1,n+1)*2/(np.pi*n)

# generate angular frequency
def wn(n, period):
    return (2*np.pi*n)/period

# Fourier series
def fourierSt(harmonics,t,period):
    summ = 0
    for i in range(1, harmonics):
        summ += A*bn(i)*np.sin(wn(i,period)*t)
    return summ

# Main 
y = []; f1 = []; f2 = []; f3 = []
for i in t:
    y.append(stwave(i,period))
    f1.append(fourierSt(  harmonics,i,period))
    f2.append(fourierSt(4*harmonics,i,period))
    f3.append(fourierSt(8*harmonics,i,period))

# Plot
sg = A*signal.sawtooth(2*(t-period/2)) # Constructed signal
plt.plot(t, sg, '-',  lw='4', color="red",    label="Signal(scipy)")
plt.plot(t,  y, '-o', lw='2', color="teal",   label=r'Signal$(2A(\frac{t}{period} - floor({\frac{1}{2}+\frac{t}{period})}$')
plt.plot(t, f1, '-*', lw='1', color="black",  label=str(harmonics)+" harmonics")
plt.plot(t, f2, '-+', lw='1', color="magenta",label=str(4*harmonics)+" harmonics")
plt.plot(t, f3, '-x', lw='1', color="olive",  label=str(8*harmonics)+" harmonics")
plt.title("Saw-tooth Wave Fourier Series", size=16)
plt.legend(loc='best', prop={'size':16})
plt.xlabel('t', size=16)
plt.xticks(size=14)
plt.ylabel(r'$f(t)=\sum_{n=1}^\infty\;\frac{2}{n\pi}(-1)^{n+1} sin(n\omega t)$', size=20)
plt.yticks(size=14)
plt.xlim([-2*period, 2*period])
plt.ylim([-A-.5, A+.5])
plt.grid()
#plt.savefig('plot/03_fourierst.pdf')
plt.tight_layout()
plt.show()
