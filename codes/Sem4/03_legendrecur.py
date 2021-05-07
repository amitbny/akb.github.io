"""
Registration: xxxx; 
Description: Orthonormality and recursion relation for Legendre functions
Author: AKB
"""

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative
import scipy.integrate as sci
import warnings
warnings.filterwarnings("ignore")

# Feed the value of n, m, lower and upper limit, #of points (from keyboard)
n = 4; m = 5; start = -1; stop = 1; Np = 1e6;
x = np.linspace(start, stop, Np);

# Create Poly1D Legendre polynomial and derivatives
pn = legendre(n); pm = legendre(m); pnm1 = legendre(n-1);
pnm2 = legendre(n-2); pnp1 = legendre(n+1); 
pnprime = derivative(pn, x, 1e-6)  # spacing=10^-6
pnm1prime = derivative(pnm1, x, 1e-6) 

# Logical case switch for different recursion relations to choice from
recl1=1; recl2=0; recl3=0; recl4=0; recl5=0; recl6=0;
print 'Compare maximum of |lhs-rhs| (L1 norm) to zero for n = ', n

if(recl1): # \int Pn(x)Pm(x) = 2/(2n+1)*delta(nm)
  I = sci.simps(pn(x)*pm(x),x)*(2.0*n+1)/2.0
  print 'Orthonormality : \int P_',n,'(x)P_',m,'(x)dx = ', I

if(recl2): #nPn(x) = (2n-1)xP(n-1)(x) - (n-1)P(n-2)(x)
  lhs = n*pn(x)
  rhs = (2*n-1)*x*pnm1(x)-(n-1)*pnm2(x)
  print 'Maximum of nPn(x)-(2n-1)xPn(x)+(n-1)P(n-2)(x) = ', abs(max(lhs-rhs))
  
if(recl3): #(n+1)P(n+1)(x) = (2n+1)xPn(x) - nP(n-1)(x)
  lhs = (n+1)*pnp1(x)
  rhs = (2*n+1)*x*pn(x)-n*pnm1(x)
  print 'Maximum of (n+1)P(n+1)(x)-(2n+1)xPn(x)+nP(n-1)(x) = ', abs(max(lhs-rhs))

if(recl4): #(1-x^2)Pn'(x) = n(P(n-1)(x) - xPn(x))
  lhs = (1-x**2)*pnprime
  rhs = n*(pnm1(x)-x*pn(x))
  print 'Maximum of (1-x^2)dPn(x)/dx-n[P(n-1)(x)-xPn(x)] = ', abs(max(lhs-rhs))
  
if(recl5): #nPn(x) = xPn'(x) - P(n-1)'(x)
  lhs = n*pn(x)
  rhs = x*pnprime-pnm1prime
  print 'Maximum of nPn(x)-xdPn(x)/dx+dP(n-1)(x)/dx = ', abs(max(lhs-rhs))
  
if(recl6): #Pn'(x) = xP(n-1)'(x) + nP(n-1)(x)
  lhs = pnprime
  rhs = x*pnm1prime + n*pnm1(x)
  print 'Maximum of dPn(x)/dx-xdP(n-1)(x)/dx-nP(n-1)(x) = ', abs(max(lhs-rhs))

"""
Results (2 Sets) :
Compare maximum of |lhs-rhs| (L1 norm) to zero for n =  2
Orthonormality : \int P_ 2 (x)P_ 2 (x)dx =  1.0
Maximum of nPn(x)-(2n-1)xPn(x)+(n-1)P(n-2)(x) =  1.11022302463e-15
Maximum of (n+1)P(n+1)(x)-(2n+1)xPn(x)+nP(n-1)(x) =  1.7763568394e-15
Maximum of (1-x^2)dPn(x)/dx-n[P(n-1)(x)-xPn(x)] =  1.6266898939e-10
Maximum of nPn(x)-xdPn(x)/dx+dP(n-1)(x)/dx =  3.68844066401e-10
Maximum of dPn(x)/dx-xdP(n-1)(x)/dx-nP(n-1)(x) =  3.71586317272e-10

Compare maximum of |lhs-rhs| (L1 norm) to zero for n =  4
Orthonormality : \int P_ 4 (x)P_ 5 (x)dx =  -1.45422004516e-16
Maximum of nPn(x)-(2n-1)xPn(x)+(n-1)P(n-2)(x) =  3.10862446895e-15
Maximum of (n+1)P(n+1)(x)-(2n+1)xPn(x)+nP(n-1)(x) =  4.4408920985e-15
Maximum of (1-x^2)dPn(x)/dx-n[P(n-1)(x)-xPn(x)] =  2.81584533468e-10
Maximum of nPn(x)-xdPn(x)/dx+dP(n-1)(x)/dx =  7.97428789667e-10
Maximum of dPn(x)/dx-xdP(n-1)(x)/dx-nP(n-1)(x) =  8.11806621925e-10
"""
