"""
Registration : xxxx
Description  : Curve Fitting using numpy and scipy 
Author       : AKB
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")

# Parameter values
a = 2.5; b = 1.2; c = 1; var = 0.005;
N = 5;                         # number of point in x
x  = np.linspace(0,  N,   50)  # define x-axis
xp = np.linspace(-1, N+1, 100) # define x-axis on which interpolation is performed

# define y = f(x)
def func(x, a, b, c):
    return a*np.exp(-b*x) + c
    #return a*pow(x,3)-b*pow(x,2)+c*x

y = func(x, a, b, c)
y = y + var*np.random.randn(x.size) # Add noise to y for better visibility of Fitting
plt.plot(x,y,'r+-',lw=5,ms=15,label=r'$y = '+str(a)+'e^{-'+str(b)+'x}+'+str(c)+'+\mathcal{N}(0,'+str(var)+')$')  # Plot the Raw Data

# use scipy optimize to construct the polynomial object by fitting
popt, pcov = curve_fit(func, x, y)
plt.plot(x, func(x, *popt), 'o-.', lw=2, ms=10, c='olive', label=r'Fit: $y = %ge^{-%gx}+%g$' %tuple(popt))
#plt.plot(x, func(x, *popt), 'o-.', lw=2, ms=10, c='olive', label='fit: a=%g, b=%g, c=%g' %tuple(popt))

# optimize within the region 0<=a<=1, 0<=b<=9, 0<=c<=1.0 for educated fit
popt, pcov = curve_fit(func, x, y, bounds=(0, [2.5, 1.2, 1.0]))
plt.plot(x, func(x, *popt), 'gx--', lw=2, ms=15, label=r'Optimized Fit: $y = %ge^{-%gx}+%g$' %tuple(popt))

# use numpy to construct the polynomial object by fitting
p3  = np.poly1d(np.polyfit(x, y, 3))
p12 = np.poly1d(np.polyfit(x, y, 12))
plt.plot(xp, p3(xp),  'd-.', lw=2, ms=9, c='b', label=r'$3^{rd}$ Order Polynomial')
plt.plot(xp, p12(xp), '>--', lw=2, ms=6, c='m', label=r'$12^{th}$ Order Polynomial')

plt.legend(loc='best', prop={'size':24})
plt.title('Curve Fitting', size=30)
plt.xlabel('X Data', size = 26)
plt.xticks(size = 20)
plt.ylabel('Y Data', size=26)
plt.yticks(size = 20)
plt.xlim(-1, 6); plt.ylim(-1, 4)
plt.grid()
plt.show()
