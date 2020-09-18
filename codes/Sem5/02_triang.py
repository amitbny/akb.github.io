# -*- coding: utf-8 -*-
"""
Solve 1-dimensional time-independent Schroedinger Equation (TISE) for 
Triangular Potential (TRIANG) V(x)= x for x>0 using RK4 integrator. 
(a) Count the roots of the wave function (Newton-Raphson) & determine 
the harmonics. (b) Refine the solution until proper energy is obtained.  
"""

import numpy as np
import scipy
from scipy import integrate
from scipy.optimize import newton, bisect
import matplotlib.pyplot as plt

# Return TISE with potential V
def schroed(y, r, V, E):
    psi, phi = y
    dphidx = [phi, (V-E)*psi]
    return np.asarray(dphidx)

#  Integrate function with inital value psi0 & potential V. 
def rk4(f, psi0, x, V, E):
    n = len(x)
    psi = np.array([psi0]*n)
    for i in range(n-1):
        h = x[i+1] - x[i]
        k1 = h*f(psi[i],        x[i],       V[i], E)
        k2 = h*f(psi[i]+0.5*k1, x[i]+0.5*h, V[i], E)
        k3 = h*f(psi[i]+0.5*k2, x[i]+0.5*h, V[i], E)
        k4 = h*f(psi[i]+    k3, x[i+1],     V[i], E)
        psi[i+1] = psi[i] + (k1 + 2.0*(k2 + k3) + k4)/6.0
    return psi

# Shooting: Solve dphi/dx = f(psi,x,V,E) with psi(x[0]) = psi0 for energy array.
def shoot_rk4(func, psi0, x, V, E):
    psi_rightb = []
    for EN in E:
        psi = rk4(func, psi0, x, V, EN)
        psi_rightb.append(psi[len(psi)-1][0])
    return np.asarray(psi_rightb)

# Helper function to optimize results using RK4
def shoot_optim(E, func, psi0, x, V):
    psi = rk4(func, psi0, x, V, E)
    return psi[len(psi)-1][0]

# Find zero crossing due to sign change in rightbound array. Return array with
# indices before sign changes
def findZeros(rightb):
    return np.where(np.diff(np.signbit(rightb)))[0]

# Optimize energy for function using Newton-Raphson method
def optimizeEnergy(func, psi0, x, V, E):
    shoot = shoot_rk4(func, psi0, x, V, E)
    #print shoot
    crossings = findZeros(shoot)
    #print crossings
    energy = []
    for cross in crossings:
        energy.append(newton(shoot_optim, E[cross], args=(func, psi0, x, V)))
        #energy.append(bisect(shoot_optim, E[cross]-0.01, E[cross]+0.01, args=(func, psi0, x, V)))
    return np.asarray(energy)

# Normalize wave function
def normalize(output_wavefunc):
    normal = max(output_wavefunc)
    return output_wavefunc*(1/normal)

# Shoot, optimize energy & return numeric wavefunction
def triang_shoot(psi_init, h, xl, xr, El, Eh, dE):
    x = np.arange(xl, xr+h, h)
    V = x
    E = np.arange(El, Eh, dE)
    eigEn = optimizeEnergy(schroed, psi_init, x, V, E)
    psi_num = []
    for EN in eigEn:
        out = rk4(schroed, psi_init, x, V, EN)
        psi_num.append(normalize(out[:,0]))
    print 'Eigenstate energy', eigEn
    return x, np.asarray(psi_num)

# Output Wave-functions
def plot_wavefun(fig, title_string, x, psi_plot):
    plt.cla() 
    plt.clf() 
    plt.plot(x, psi_plot, 'k-', linewidth=2, label=r"$\Psi(\hat{x})_{num}$")
    plt.ylabel(r"$\Psi(\hat{x})$", fontsize=16)
    plt.xlabel(r'$\hat{x}$', fontsize=16)
    plt.legend(loc='best', fontsize='small')
    plt.axis([x.min(), x.max(), -1.4, 1.4])
    plt.title(title_string)
    plt.grid()
    fig.savefig("plot/wavefunc_"+title_string+".jpg")

# MAIN
# Initial conditions
psi_0 = 0.0; phi_0 = 1.0;   
psi_init = np.asarray([psi_0, phi_0])
xl = 0.0; xr = 10.0;           # Abscissa bracket 
h = 1.0/200                    # stepsize
El = 1.0; Eh = 14.0; dE = 2.0; # Energy bracket 

# Peform Integration
x, psi_num = triang_shoot(psi_init, h, xl, xr, El, Eh, dE)

# Plot wavefunction
fig = plt.figure()
plot_wavefun(fig, "TRIANG_Ground_State",      x, psi_num[0,:])
plot_wavefun(fig, "TRIANG_1st_Excited_State", x, -psi_num[1,:])
plot_wavefun(fig, "TRIANG_2nd_Excited_State", x, psi_num[2,:])
plot_wavefun(fig, "TRIANG_3rd_Excited State", x, -psi_num[3,:])
