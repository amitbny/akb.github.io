"""
Registration : xxxx
Description  : Basics of Scipy
Author       : AKB
"""

import numpy as np
from scipy.integrate import quad
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Logical case switch for different problems to choose from 
gquad=0; radiodec=0; dampshm=0; lorentz=1; 

if(gquad):
   #=== Gauss Quadrature ==#
   def f(x) :
       return x**2
   print 'Integral 0 to 2 x^2dx using Gauss Quadrature : ', quad(f,0,2)

if(radiodec):
   #==========================================================================#
   print    '~~~ 1ST ORDER ODE : Radioactive Decay of Nuclear Mass ~~~'       #
   #==========================================================================#

   k = 1.0 # parameter
   def f(x,t):
       dxdt = -k*x
       return dxdt
   t = np.linspace(0,10,100) # Creating t-values, 100 values in [0-100]
   x0 = 100  # initial value
   sol = odeint(f, x0, t) # solution by odeint()

   # plot
   plt.figure(1)
   plt.subplot(2,2,1)
   plt.plot(t, sol, 'r+-', label='x(t)', lw=2, ms=8)
   plt.legend(loc='best', prop={'size':16}) 
   plt.axis([0, 10, 0, 100])
   plt.title('Decay Curve', fontsize=16)
   plt.xlabel('Time', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel('Nuclear Mass', fontsize = 16)
   plt.yticks(fontsize = 14)
   plt.savefig('plot/01_radiodecay.pdf')
   plt.show()

if(dampshm):
   #==================================================================================#
   print '~~~ 2ND ORDER ODE : Damped SHM d2x/dt2 + lambda*dx/dt + kx = 0 ~~~'         #
   print '                    Damped SHM d2x/dt2 + lambda*dx/dt + kx = acos(wt) ~~~'  #
   #==================================================================================#

   k, lam = 1.0, 0.2    # Parameters for Damped Oscillation
   a, omega = 0.1, 0.1  # Parameters for Forced Oscillation

   def dshm(u,t):
       x = u[0]; y = u[1];
       dxdt = y
       dydt = -k*x - lam*y
       return np.array([dxdt, dydt])

   def fshm(u,t):
       x = u[0]; y = u[1];
       dxdt = y
       dydt = -k*x - lam*y - a*np.cos(omega*t)
       return np.array([dxdt, dydt])
    
   u0 = [1, 0]                  # initial values
   t = np.linspace(0,50,1000)
   sol = odeint(dshm, u0, t)    # Damped
   x1 = sol[:,0]; y1 = sol[:,1]
   sol = odeint(fshm, u0, t)    # Forced
   x2 = sol[:,0]; y2 = sol[:,1]

   # plot
   plt.figure(2)
   plt.plot(t, x1, 'k-',  label='x(t) [Damped]', lw=2, ms=6)
   plt.plot(t, y1, 'r.-',  label='v(t) [Damped]', lw=2, ms=6)
   plt.plot(t, x2, 'kx', label='x(t) [Forced]', lw=2, ms=6)
   plt.plot(t, y2, 'ro', label='v(t) [Forced]', lw=2, ms=6)
   plt.legend(loc='best', prop={'size':16}) 
   plt.axis([0, 50, -1, 1])
   plt.grid()
   plt.axhline(lw=2) # draw a horizontal line
   plt.suptitle('Damped and Forced Simple Harmonic Motion',fontsize=16)
   plt.text(25,-0.3,r'$k=1,\lambda=0.2,a=\omega=0.1$', fontsize=20)
   plt.text(13,-0.65,r'(Damped) $\frac{d^2x}{dt^2}+\lambda\frac{dx}{dt}+kx=0$', fontsize=20)
   plt.text(15,-0.9,r'(Forced) $\frac{d^2x}{dt^2}+\lambda\frac{dx}{dt}+kx=acos(\omega t)$', fontsize=20)
   plt.xlabel('Time', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel('Displacement', fontsize = 16)
   plt.yticks(fontsize = 14)
   plt.savefig('plot/01_dampshm.pdf')
   plt.show()

if(lorentz):
   #========================================================================#
   print '~~~ 2ND ORDER ODE : Lorentz Attractor ~~~ '                       #
   print '~~~ dx/dt=sigma*(y-x), dy/dt=x*(rho-z)-y, dz/dt=x*y-beta*z  ~~~'  #
   #========================================================================#

   sig, rho, beta = 10.0, 28.0, 8.0/3
   def loratr(u, t):
       x,y,z = u[0],u[1],u[2]
       dxdt = sig*(y-x)
       dydt = x*(rho-z)-y
       dzdt = x*y-beta*z
       return [dxdt, dydt, dzdt]
    
   u0 = [0, 1.0, 0]
   t = np.linspace(0,50,5e4)
   sol = odeint(loratr, u0, t)
   x, y, z = sol[:,0], sol[:,1], sol[:,2]

   # Plot
   plt.figure(3)
   plt.subplot(2,2,1)
   plt.plot(x, z, 'r-', label='X-Z', lw=2, ms=8)
   plt.legend(loc='best', prop={'size':16}) 
   plt.axis([-20, 20, 0, 50])
   plt.suptitle('Lorentz Attractor', fontsize=18)
   plt.xlabel('X', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel('Z', fontsize = 16)
   plt.yticks(fontsize = 14)

   plt.subplot(2,2,2)
   plt.plot(x, y, 'k-', label='X-Y', lw=2, ms=8)
   plt.legend(loc='best', prop={'size':16}) 
   plt.axis([-20, 20, -30, 30])
   plt.xlabel('X', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel('Y', fontsize = 16)
   plt.yticks(fontsize = 14)

   plt.subplot(2,2,3)
   plt.plot(y, z, 'g.', label='Y-Z', lw=2, ms=2)
   plt.legend(loc='best', prop={'size':16}) 
   plt.axis([-30, 30, 0, 50])
   plt.xlabel('Y', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel('Z', fontsize = 16)
   plt.yticks(fontsize = 14)
   
   plt.text(50, 35, r'$\frac{dx}{dt}=\sigma(y-x)$', fontsize=20)
   plt.text(50, 20, r'$\frac{dy}{dt}= x(\rho-z)-y$', fontsize=20)
   plt.text(50, 5, r'$\frac{dz}{dt}= xy-\beta z$', fontsize=20)   
   plt.savefig('plot/01_lorentz.pdf')
   plt.show()
