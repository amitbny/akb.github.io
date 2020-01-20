"""
Registration : xxxx
Description  : Laplace equation in 2D (Elliptic PDE)
Author       : AKB
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Feed maximum iteration, system size, grid spacing from keyboard
maxiter = 500; L = 64; dx = 1

# boundary conditions
P = np.zeros((L,L))
Ptop = 0; Pbot = 100; Pleft = 10; Pright = 10
P[(L-1):,:     ] = Ptop
P[:1    ,:     ] = Pbot
P[:     ,(L-1):] = Pright
P[:     ,:1    ] = Pleft

# Start the iteration
for iteration in range(0, maxiter):
   for i in range(1, L-1, dx):
       for j in range(1, L-1, dx):
           P[i,j] = 0.25*(P[i+1][j] + P[i-1][j] + P[i][j+1] + P[i][j-1])
            
# Contour plot
X,Y = np.meshgrid(np.arange(0,L), np.arange(0,L))
plt.suptitle("Potential Contour for "+str(L)+"x"+str(L)+" system", size=16)
plt.contourf(X, Y, P, 100, cmap=cm.rainbow) # interpolating points = 100
plt.text(29, 4,r'$\phi_{bot} = $'  +str(Pbot), size = 20)
plt.text(29,58,r'$\phi_{top} = $'  +str(Ptop), size = 20)
plt.text(1, 31,r'$\phi_{left} = $' +str(Pleft),size = 20)
plt.text(45,31,r'$\phi_{right} = $'+str(Pleft),size = 20)
plt.colorbar()
plt.grid()
plt.savefig('plot/01_laplace2D.pdf')
plt.show()
