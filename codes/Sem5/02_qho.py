# -*- coding: utf-8 -*-
"""
Solve 1-dimensional time-independent Schroedinger Equation (TISE) for 
Quantum Harmonic Oscillator (QHO) V(x)=x^2 using RK4 integrator. 
(a) Count the roots of the wave function (Newton-Raphson) & determine 
the harmonics. (b) Refine the solution until proper energy is obtained.  
"""

import numpy as np
import scipy
from scipy import integrate
from scipy.optimize import newton
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
    return np.asarray(energy)

# Normalize wave function
def normalize(output_wavefunc):
    normal = max(output_wavefunc)
    return output_wavefunc*(1/normal)

# Shoot, optimize energy & return numeric wavefunction
def qho_shoot(psi_init, h, xb, El, Eh, dE):
    x = np.arange(-xb, xb+h, h)
    V = x**2
    E = np.arange(El, Eh, dE)
    eigEn = optimizeEnergy(schroed, psi_init, x, V, E)
    psi_num = []
    for EN in eigEn:
        out = rk4(schroed, psi_init, x, V, EN)
        psi_num.append(normalize(out[:,0]))
    print 'Eigenstate energy ', eigEn

    # Compute analytic wavefunction
    ana_0 = np.exp(-(x)**2/2)                                               # Ground State
    ana_1 = np.sqrt(2.0)*(x)*np.exp(-(x)**2/2)*(-1)                         # First Excited State
    ana_2 = (1.0/np.sqrt(2.0))*(2.0*(x)**2-1.0)*np.exp(-(x)**2/2)           # Second Excited State
    ana_3 = (1.0/np.sqrt(3.0))*(2.0*(x)**3-3.0*x)*np.exp(-(x)**2/2)*(-1)    # Third Excited State
    ana_4 = (1.0/np.sqrt(24.0))*(4.0*(x)**4-12.0*x**2+3.)*np.exp(-(x)**2/2) # Fourth Excited State
    psi_ana = []
    psi_ana.append(ana_0); psi_ana.append(ana_1); psi_ana.append(ana_2);
    psi_ana.append(ana_3); psi_ana.append(ana_4); 
    return x, np.asarray(psi_num), np.asarray(psi_ana)

# Output Wave-functions
def plot_wavefun(fig, title_string, x, psi_num, psi_ana):
    plt.cla() 
    plt.clf() 
    plt.plot(x, psi_num,            'ko', linewidth=1, label=r"$\Psi(\hat{x})_{num}$")
    plt.plot(x, normalize(psi_ana), 'r-', linewidth=1, label=r"$\Psi(\hat{x})_{ana}$")
    plt.ylabel(r"$\Psi(\hat{x})$", fontsize=16)
    plt.xlabel(r'$\hat{x}$', fontsize=16)
    plt.legend(loc='best', fontsize='small')
    plt.axis([x.min()-0.2, x.max()+0.2, -1.2, 1.2])
    plt.title(title_string)
    plt.grid()
    fig.savefig("plot/wavefunc_"+title_string+".jpg")

# MAIN
# Initial conditions
psi_0 = 0.0; phi_0 = 1.0;   
psi_init = np.asarray([psi_0, phi_0])
h = 1.0/200                    # stepsize
xb = 6.0;                      # Abscissa bracket 
El = 1.0; Eh = 12.0; dE = 1.0; # Energy bracket 

# Peform Integration
x, psi_num, psi_ana = qho_shoot(psi_init, h, xb, El, Eh, dE)

# Plot wavefunction
fig = plt.figure()
plot_wavefun(fig, "QHO_Ground_State",      x, psi_num[0,:], psi_ana[0,:])
plot_wavefun(fig, "QHO_1st_Excited_State", x, psi_num[1,:], psi_ana[1,:])
plot_wavefun(fig, "QHO_2nd_Excited_State", x, psi_num[2,:], psi_ana[2,:])
plot_wavefun(fig, "QHO_3rd_Excited State", x, psi_num[3,:], psi_ana[3,:])
plot_wavefun(fig, "QHO_4th_Excited State", x, psi_num[4,:], psi_ana[4,:])
