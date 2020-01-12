"""
Registration : xxxx
Description  : BVP y'' = 12x^2; y(0)=0; y(1)=0; Exactsol y = x^4-x
Author       : AKB
"""

import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

# Central-difference matrix 
L = 100; dx = 1.0/L # fixed step-size
x = np.linspace(0, 1, L+1).transpose()
b = np.zeros((L+1, 1)).ravel()
b[1:L] = 12 * pow(dx,2) * (x[1:L]**2)
main_diag = -2*np.ones((L+1,1)).ravel()
off_diag =   1*np.ones((L,  1)).ravel()
a = main_diag.shape[0]
diagonals = [main_diag, off_diag, off_diag]
A = sparse.diags(diagonals, [0,-1,1], shape=(a,a)).toarray()
A[0, 0  ] = 1
A[0, 1  ] = 0
A[L, L  ] = 1
A[L, L-1] = 0

y = np.linalg.solve(A,b)

xf = np.linspace(0, 1, 10*L)
yexact = pow(xf,4) - xf

# Plot
plt.plot(x, y, 'ro')
plt.plot(xf, yexact)
plt.legend(['Finite difference', 'Exact solution'])
plt.tight_layout()
plt.show()
