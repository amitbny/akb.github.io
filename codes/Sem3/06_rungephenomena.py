"""
Registration: xxxx; 
Description: Runge phenomena
Author: AKB
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    a = 0.2
    return 1./(x*x+a*a)

def interpol(x, G):
    A = np.ones(len(x))
    A = A.reshape(-1,1)            # convert row to column vector
    for k in range(1, len(x)):
        x1 = np.power(x,k)
        x1 = x1.reshape(-1,1)      # convert into column vector
        A = np.hstack([A, x1])     # concatenate to form matrix
    cf = np.linalg.solve(A, f(x))  # solve 
    cf = cf[::-1]                  # reverse 
    return np.polyval(cf, G) 


n = 10                             # Number of grid points 
x = -1 + 2*np.linspace(0,n,n+1)/n  # x-grid [-1,1]
g = np.arange(-1,1.02,.02)         # g-grid 101 points
y = interpol(x, g)

# Plot
plt.figure(1)
plt.plot(g, f(g), 'kx', label=r'$f(x)=\frac{1}{x^2+.2^2}$')
plt.plot(g, y, 'r.--', label=r'$P(x)$')
plt.axis([-1.1, 1.1, -10, 50])
plt.xlabel(r'$x$', size=16)
plt.ylabel(r'$f(x)$', size=16)
plt.title('Runge phenomena with %s grid Points'%(10*n), size=16);
plt.grid()
plt.legend(loc='best', prop={'size':20})
plt.savefig('plot/06_runge.pdf')
plt.show()
