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
from scipy.optimize import newton, bisect
import matplotlib.pyplot as plt

# Return 1DSE with potential V
def schroed(y, r, V, E):
    psi, phi = y
    dphidx = [phi, (V-E)*psi]
    return np.asarray(dphidx)

#  Integrate function f
# with inital values psi0 and potential V. Output is multidimensional
# (in psi) array with len(x)
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

# Shooting method: Solve dphi/dx = f(psi,x,V,E) with psi(x[0]) = psi0 for energy array.
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
    print shoot    
    crossings = findZeros(shoot)
    energy = []
    for cross in crossings:
        energy.append(newton(shoot_optim, E[cross], args=(func, psi0, x, V)))
        #energy.append(bisect(shoot_optim, 0.9*E[cross], 1.1*E[cross], args=(func, psi0, x, V)))
    #print np.asarray(energy)
    return np.asarray(energy)

# Normalize wave function
def normalize(output_wavefunc):
    normal = max(output_wavefunc)
    return output_wavefunc*(1/normal)

def morse_function(a,D,x):
    return D*(np.exp(-2*a*x)-2*np.exp(-a*x))

def morse_potential(omega,D,steps):
    D=np.abs(D)
    a=np.sqrt(omega/2.0*D)
    start=0.0
    stop=0.0
    while morse_function(a,D,start)<0.5*np.abs(D):
        start-=0.01
    while morse_function(a,D,stop)<-0.1:
        stop+=0.01
    # create x-vector
    xvec=np.linspace(2.0*start,2.0*stop,steps,dtype=np.float_)
    # get step size
    h=xvec[1]-xvec[0]
    print h
    pot=morse_function(a,D,xvec)
    for i in range(len(pot)):
        if pot[i]>0:
            pot[i]=0
    #for i in range(len(pot)):
    #    pot[i] +=pot.max()
    #plt.plot(xvec, pot); plt.show()        
    return xvec,h,pot

# Shooting method QHO; returns numeric/analytic wavefunction
def shoot_qho(psi_init, E_low, E_high):
    x_qho, h, V_qho = morse_potential(0.05, 2, 1000)
    E = np.arange(E_low, E_high, 1.0)
    eigEn = optimizeEnergy(schroed, psi_init, x_qho, V_qho, E)
    qho_out = []
    for EN in eigEn:
        out = rk4(schroed, psi_init, x_qho, V_qho, EN)
        qho_out.append(normalize(out[:,0]))
    print 'Eigenstate energy ', eigEn
    
    return x_qho, np.asarray(qho_out)

# Output Wave-functions
def plot_wavefun(fig, title_string, x_arr, num_arr, axis_list):
    plt.cla() 
    plt.clf() 
    plt.plot(x_arr, num_arr, 'ko', linewidth=4, label=r"$\Psi(\hat{x})_{num}$")
    plt.ylabel(r"$\Psi(\hat{x})$", fontsize=16)
    plt.xlabel(r'$\hat{x}$', fontsize=16)
    plt.legend(loc='best', fontsize='small')
    plt.axis(axis_list)
    plt.title(title_string)
    plt.grid()
    fig.savefig("plot/wavefunc_"+title_string+".jpg")

# Initial conditions for QHO
psi_0 = 0.0; phi_0 = 1.0;   
psi_init = np.asarray([psi_0, phi_0])
E_low = 0.1; E_high = 5.0; # Lower and Upper value of E

# Peform Integration
qho_x, qho_num = shoot_qho(psi_init, E_low, E_high)

# Plot wave function
fig = plt.figure()
print "Morse Oscillator Shooting Method"
plot_wavefun(fig, "Morse Ground State",      qho_x, qho_num[0,:], [qho_x.min()-0.2, qho_x.max()+0.2, -1.2, 1.2])
#plot_wavefun(fig, "Morse 1st Excited State", qho_x, qho_num[1,:], qho_ana[1,:], [-xbracket-0.2, 8*xbracket+0.2, -1.2, 1.2])
#plot_wavefun(fig, "Morse 2nd Excited State", qho_x, qho_num[2,:], qho_ana[2,:], [-xbracket-0.2, 8*xbracket+0.2, -1.2, 1.2])
#plot_wavefun(fig, "Morse 3rd Excited State", qho_x, qho_num[3,:], qho_ana[3,:], [-xbracket-0.2, xbracket+0.2, -1.2, 1.2])
#plot_wavefun(fig, "Morse 4th Excited State", qho_x, qho_num[4,:], qho_ana[4,:], [-xbracket-0.2, xbracket+0.2, -1.2, 1.2])
