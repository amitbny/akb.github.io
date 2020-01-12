"""
Registration : xxxx
Description  : Wave propagation to boundary for middle-plucked string. 
Author       : AKB
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Feed Final time (tf), System size (L), sound speed (c) from keyboard.
# Take either L large or tf small so that wave packet never reaches boundary.
tf  = 3.5;  tn = 201; dt = tf/(tn-1)
L   = 10.0; xn = 201; dx = L/(xn-1); c = 1.0;
cfl = (c*dt/dx)**2

# Initialize Gaussian wave
x = np.linspace(0, L, xn)
u = np.zeros((xn, tn))        
u[:,1] = u[:,0] = np.exp(-((x-L/2)**2)/0.25)

# Kinetics
for t in range(1,tn-1):
    for i in range(1,xn-1):
        u[i,t+1] = 2*(1-cfl)*u[i,t]-u[i,t-1]+cfl*(u[i-1,t]+u[i+1,t])

# Plot
fig = plt.figure()
colour=iter(cm.rainbow(np.linspace(0,10,tn)))
for i in range(0,tn,10):
    c = next(colour)
    plt.plot(x, u[:,i], c=c)
plt.xlabel('Distance (in cm)')
plt.ylabel('U(x,t)')
plt.grid()
plt.title('CFL='+str(cfl)+', tf='+str(tf)+', L='+str(L))
plt.xlim([0, L])
plt.ylim([-0.05, 1.05])
plt.show()
