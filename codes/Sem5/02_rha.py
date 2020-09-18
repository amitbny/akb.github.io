# -*- coding: utf-8 -*-
"""
Solve 1-dimensional time-independent Schroedinger Equation (TISE) for 
radial-part of Hydrogen Atom (RHA): V(r) = 2/r - l(l+1)/r^2 a.u. using 
RK4 integrator. (a) Count the roots of the wave function (Newton-Raphson) 
& determine the harmonics. (b) Refine the solution until proper energy 
is obtained. 
"""

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import newton
import matplotlib.pyplot as plt

# Return TISE 
def schroed(y, r, l, E):
    psi, phi = y
    dVdr = [phi, ((l*(l+1))/(r**2) - 2.0/r - 2.0*E)*psi]
    return np.asarray(dVdr)

# Shooting: Solve dphi/dx = f(psi,x,V,E) with psi(x[0]) = psi0 for energy array.
def shoot_odeint(func, psi_init, x, l, E):
    psi_rightb = []
    for EN in E:
        psi = odeint(schroed, psi_init, x, args=(l,EN))[:,0]
        psi_rightb.append(psi[len(psi)-1])
    return np.asarray(psi_rightb)

# Helper function for optimizing results using odeint
def shoot_optim(E, psi_init, x, l):
    sol = odeint(schroed, psi_init, x, args=(l,E))
    return sol[len(sol)-1][0]

# Find zero crossing due to sign change in rightbound array. Return array with
# indices before sign changes
def findZeros(rightb):
    return np.where(np.diff(np.signbit(rightb)))[0]

# Optimize energy for function using Newton-Raphson method
def optimizeEnergy(func, psi0, x, l, E):
    shoot = shoot_odeint(func, psi0, x, l, E)
    crossings = findZeros(shoot)
    energy = []
    for cross in crossings:
        energy.append(newton(shoot_optim, E[cross], args=(psi_init, x, l)))
    return np.asarray(energy)

# Normalize wave function
def normalize(output_wavefunc):
    normal = max(output_wavefunc)
    return output_wavefunc*(1/normal)

# Shooting: returns numeric solution only
def rha_shoot(psi_init, h, l, xl, xr, El, Eh, dE):
    x = np.arange(xl, xr, h)
    E = np.arange(El, Eh, dE)
    eigEnl = optimizeEnergy(schroed, psi_init, x, l, E)
    psi_num = []
    for EN in eigEnl:
        out = odeint(schroed, psi_init, x, args=(l,EN)) 
        psi_num.append(normalize(out[:,0]))
    print 'Eigenstate energy ', eigEnl   
    return x, np.asarray(psi_num)

# Returns Analytical solution
def psi_ana(x, n, l):
    nodes = n-l-1 # Number of should be nodes
    if((nodes==0) and (l==0)):    # 1s(n=1,l=0,nodes=0)
       return x*np.exp(-x)
    elif((nodes==1) and (l==0)):  # 2s(n=2,l=0,nodes=1)
       return (np.sqrt(2.0)*(-x+2.0)*np.exp(-x/2.0)/4.0)*x
    elif ((nodes==2)):            # 3s(n=3,l=0,nodes=2)
       return (2.0*np.sqrt(3.0)*(2.0*x**2.0/9.0-2.0*x+3.0)*np.exp(-x/3.0)/27.0)*x
    elif ((nodes==0) and (l==1)): # 2p(n=2,l=1,nodes=0)
       return (np.sqrt(6.0)*x*np.exp(-x/2.0)/12.0)*x
    else:
       print "No analytic wave function found."
       print "Output will be zero array."
       return np.zeros(len(xrange))

# Output Wave-functions
def plot_wavefun(fig, title_string, x, psi_num, psi_ana):
    plt.cla() 
    plt.clf() 
    plt.plot(x, psi_num,            'k.', linewidth=1, label=r"$\Psi(\hat{x})_{num}$")
    plt.plot(x, normalize(psi_ana), 'r-', linewidth=1, label=r"$\Psi(\hat{x})_{ana}$")
    plt.ylabel(r"$\Psi(\hat{x})$", fontsize=16)
    plt.xlabel(r'$\hat{x}$',       fontsize=16)
    plt.legend(loc='best', fontsize='small')
    plt.axis([x.min()-0.2, x.max()+0.2, -2.2, 1.2])
    plt.title(title_string)
    plt.grid()
    fig.savefig("plot/wavefunc_"+title_string+".png")

# MAIN
# Initial conditions 
psi_0 = 0.0; phi_0 = 1.0
psi_init = np.asarray([psi_0, phi_0])
h = 1.0/200                       # stepsize 
xl = 0.0001; xr = 32.0+h;           # Abscissa bracket
El = -1.0;   Eh = 0.0; dE = 0.001;  # Energy bracket

# Peform Integration
x,   psi_num    = rha_shoot(psi_init, h, 0, xl, xr, El, Eh, dE) # 1s, 2s, 3s
x2p, psi_num2p  = rha_shoot(psi_init, h, 1, xl, xr, El, Eh, dE) # 2p

# Compute Analytic wavefunctions to compare
psi_ana1s = psi_ana(x,   1, 0) # 1s
psi_ana2s = psi_ana(x,   2, 0) # 2s
psi_ana3s = psi_ana(x,   3, 0) # 3s
psi_ana2p = psi_ana(x2p, 2, 1) # 2p

# Plot wavefunction
fig = plt.figure()
plot_wavefun(fig, "RHA_1s", x,   psi_num[0,:],   psi_ana1s)
plot_wavefun(fig, "RHA_2s", x,   psi_num[1,:],   psi_ana2s)
plot_wavefun(fig, "RHA_3s", x,   psi_num[2,:],   psi_ana3s)
plot_wavefun(fig, "RHA_2p", x2p, psi_num2p[0,:], psi_ana2p)
