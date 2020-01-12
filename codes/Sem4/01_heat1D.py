"""
Registration : xxxx
Description  : Heat Diffusion 1D
Author       : AKB
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Feed Final time (tf), System size (L), Diffusion constant (D) from keyboard   
tf = 50.0; tn = 1001; dt = tf/(tn-1);
L  = 10.0; xn = 51;  dx = L/(xn-1);
D = 0.01; cfl = D*dt/dx**2.0;

# Initialize Temperature and 1D grid
x = np.linspace(0, L, xn);
T = np.zeros((xn, tn))
T[0,:] = T[xn-1,:] = 1  # Boundary condition
for i in range(1,xn-1):
    if(i > (xn-1)/4 and i < 3*(xn-1)/4):
       T[i,0] = 2
    else:
       T[i,0] = 1

# Kinetics
for t in range(0,tn-1):
    for i in range(0,xn-1):
        T[i,t+1] = T[i,t] + cfl*(T[i+1,t]-2.0*T[i,t]+T[i-1,t])

# Plot
plt.figure()
colour=iter(cm.rainbow(np.linspace(0,10,tn)))
for i in range(0,tn,10):
    c = next(colour)
    plt.plot(x, T[:,i], c=c)
plt.xlabel('Distance (in cm)')
plt.ylabel('Temperature (per degree C)')
plt.title('CFL='+str(cfl)+', tf='+str(tf)+', L='+str(L))
plt.xlim([0, L])
plt.ylim([0.9, 2.1])
plt.grid()
plt.show()
