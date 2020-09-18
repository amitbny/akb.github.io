# -*- coding: utf-8 -*-
"""
Solve 1-dimensional time-independent Schroedinger Equation (TISE) for 
radial-part of Hydrogen Atom (RHA): V(r) = 2/r - l(l+1)/r^2 a.u. using 
RK4 integrator. (a) Count the roots of the wave function (Newton-Raphson) 
& determine the harmonics. (b) Refine the solution until proper energy 
is obtained. 
"""

import numpy as np

# discretise the r grid
dr = 0.001
r = np.arange(1e-2, 60+dr, dr)
N = r.shape[0]

# define the potential V as a function of l
Veff = lambda l: -1/r + l*(l+1)/(2*r**2)

# Hydrogen energy eigenvalues
En = lambda n: -1/(2*n**2)

# initial trial energy and potential
E = En(1)
V = Veff(0)

k = dr**2/12 # a Numerov parameter

# iterate the Numerov-Cooley method for 1000 maximum steps
for i in range(1000):
    P = -2*(V-E)

    # set the two initial conditions for the wavefunction at both boundaries
    psi = np.zeros_like(r)
    psi[1] = 1e-6
    psi[-1] = 1e-6

    # outward integration to point m-1
    for j in range(1, N-1):
        psi[j+1] = 2*psi[j]*(1-5*k*P[j]) - psi[j-1]*(1+k*P[j-1])
        psi[j+1] /= 1+k*P[j+1]

        #print psi[j], psi[j-1]
        # when the first turning point is found, set it as the match point
        if(psi[j] < psi[j-1]):
          m = j+1
          psi_out_m = psi[m]
          print psi_out_m
          break;
        
    # inward integration to point m+1
    for j in range(N-2, m, -1):
        psi[j-1] = 2*psi[j]*(1-5*k*P[j]) - psi[j+1]*(1+k*P[j+1])
        psi[j-1] /= 1+k*P[j-1]

    # scale outward and inward integration so psi(m)=1
    psi[:m] /= psi_out_m
    psi[m:] /= psi[m]

    # Cooley's energy correction formula
    Y = (1+k*P)*psi
    dE = (psi[m].conj()/np.sum(np.abs(psi)**2)) \
         *(-0.5*(Y[m+1]-2*Y[m]+Y[m-1])/(dr**2)+(V[m]-E)*psi[m])
    E += dE

    # if dE is smaller than a set precision, exit the loop early.
    if(np.abs(dE) < 1e-6):
       break
    
# the final wavefunction and energy in Hartrees
print(E*27.21, psi)
