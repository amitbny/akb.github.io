"""
Registration : xxxx
Description  : Square Wave Fourier Series
Author       : AKB
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

period    = 30                     # periodicity
harmonics = 2                      # fourier mode
x = np.linspace(0,4*period,1e3) # x-grid

# generate square waveform
def sqwave(x, period):
    return np.sign(np.sin(2*np.pi*x/period))
    
# Fourier coefficients; an=0
def bn(n):                       
    if (n%2 != 0):
        return 4/(np.pi*n)
    else:
        return 0

def wn(n, period):
    return (2*np.pi*n)/period

# Fourier series
def fourierSq(harmonics,x,period):
    summ = 0
    for i in range(1, harmonics):
        summ += bn(i)*np.sin(wn(i,period)*x)
    return summ

# Main 
y = []; f1 = []; f2 = []; f3 = []
for i in x:
    y.append(sqwave(i, period))
    f1.append(fourierSq(  harmonics,i,period))
    f2.append(fourierSq(2*harmonics,i,period))
    f3.append(fourierSq(3*harmonics,i,period))

# Plot
sg = signal.square(2*np.pi*x/period)
plt.plot(x, sg, '-',  lw='4', color="red",  label="Signal(scipy)")
plt.plot(x,  y, '-o', lw='4', color="teal", label="Signal(user)")
plt.plot(x, f1, '-*', lw='.5',color="black",label=str(1)+" harmonics")
plt.plot(x, f2, '--+',lw='.5',color="gold", label=str(2*harmonics)+" harmonics")
plt.plot(x, f3, '--x',lw='.5',color="olive",label=str(3*harmonics)+" harmonics")
plt.title("Square Wave Fourier Series", size=16)
plt.legend(loc='best', prop={'size':16})
plt.xlabel('x', size=16)
plt.xticks(size=14)
plt.ylabel('f(x)', size=16)
plt.yticks(size=14)
plt.grid()
plt.savefig('plot/03_fouriersq.pdf')
plt.tight_layout()
plt.show()
