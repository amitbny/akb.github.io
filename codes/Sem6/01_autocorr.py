"""
Registration : xxxx
Description  : Autocorrelation of a Random Time-series
Author       : AKB
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def autocorr1(x,lags):  #Using formula
    mean = np.mean(x)
    var  = np.var(x)
    xp   = x - mean
    corr = [1. if l==0 else np.sum(xp[l:]*xp[:-l])/len(x)/var for l in lags]
    return np.array(corr)

def autocorr2(x,lags):  #Using numpy.corrcoef
    corr = [1. if l==0 else np.corrcoef(x[l:],x[:-l])[0][1] for l in lags]
    return np.array(corr)

def autocorr3(x,lags):  #Using numpy.correlate
    mean = x.mean()
    var  = np.var(x)
    xp   = x-mean
    corr = np.correlate(xp,xp,'full')[len(x)-1:]/var/len(x)
    return corr[:len(lags)]

# Main
y = np.random.randint(low=0, high=20, size=100)
y = np.array(y).astype('float')
lags = np.arange(30); 

# Calculate ACF using different methods
acf = autocorr1(y,lags)
print(acf)

# Plot
plt.figure()
plt.plot(lags, acf, '-o', lw='2', color="teal", label=r'ACF = $\frac{1}{n\sigma}\sum_{i=k+1}^{n}(x_i-\bar{x})(x_{i-k}-\bar{x})}$')
plt.legend(loc='best', prop={'size':20})
plt.xlabel('Lag'); plt.xticks(size = 20);
plt.ylabel('Correlation Coefficient'); plt.yticks(size = 20)
plt.title('ACF of a Randomly distributed Time Series', size=20)
plt.xlim([-1.0, max(lags)+1])
plt.ylim([min(acf)-0.1, 1.1])
plt.grid()
plt.show()
