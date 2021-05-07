"""
Registration: xxxx; 
Description: Recursion relations for Bessel functions
Author: AKB
"""

import numpy as np
from scipy.special import jn, yn, jvp
from scipy.misc import derivative
import warnings
warnings.filterwarnings("ignore")

# Feed the value of nu, start, stop, Np from keyboard
# NOTE: we start from 0+ to avoid NAN in recb5
nu = 20; start = 1e-2; stop = 10; Np = 1000; 
z = np.linspace(start, stop, Np);  

# Logical case switch for different recursions to choose from
recb1=1; recb2=1; recb3=1; recb4=1; recb5=1;
print 'Compare maximum of |lhs-rhs| (L1 norm) to zero for nu = ', nu

if(recb1): # z*J(nu)'(z) = z*J(nu-1)-nu*J(nu)
  lhs = z*jvp(nu,z,1) 
  rhs = z*jn(nu-1,z) - nu*jn(nu,z) 
  print 'Maximum of z*dJ(nu)(z)/dz-z*J(nu-1)+nu*J(nu) = ', abs(max(lhs-rhs))

if(recb2): # 2*J(nu)'(z) = J(nu-1)(z)-J(nu+1)(z)
  lhs = 2*jvp(nu,z,1)
  rhs = jn(nu-1,z) - jn(nu+1,z)  
  print 'Maximum of 2*dJ(nu)(z)/dz-J(nu-1)(z)+J(nu+1)(z) = ', abs(max(lhs-rhs))

if(recb3): # (2*nu/z)*J(nu)(z) = J(nu+1)(z)+J(nu-1)(z)
  lhs = np.divide(2*nu*jn(nu,z), z)
  rhs = jn(nu+1,z) + jn(nu-1,z)
  print 'Maximum of (2*nu/z)*J(nu)(z)-J(nu+1)(z)+J(nu-1)(z) = ', abs(max(lhs-rhs))

if(recb4): # (z^n*Jn(z))' = z^n*J(n-1)(z)
  def fa(z) : return jn(nu,z)*pow(z,nu)
  lhs = derivative(fa, z, 1e-16) # evaluate f' at z with spacing epsilon
  rhs = pow(z,nu)*jn(nu-1,z)  
  print 'Maximum of d(z^n*Jn(z))/dz-z^n*J(n-1)(z) = ', abs(max(lhs-rhs))

if(recb5): # (z^(-nu)*J(nu)(z))' = -z^(-nu)*J(nu+1)(z)
  def fa(z) : return jn(nu,z)*pow(z,-nu)
  lhs = derivative(fa, z, 1e-6) 
  rhs = -pow(z,-nu)*jn(nu+1,z)  
  print 'Maximum of d(z^(-nu)*J(nu)(z))/dz+z^(-nu)*J(nu+1)(z) = ', abs(max(lhs-rhs))

# Excercise : Perform above for Yn recursion relations.

"""
# Results (2 Sets)
Compare maximum of |lhs-rhs| (L1 norm) to zero for nu =  2
Maximum of z*dJ(nu)(z)/dz-z*J(nu-1)+nu*J(nu) =  9.99200722163e-16
Maximum of 2*dJ(nu)(z)/dz-J(nu-1)(z)+J(nu+1)(z) =  0.0
Maximum of (2*nu/z)*J(nu)(z)-J(nu+1)(z)+J(nu-1)(z) =  5.55111512313e-16
Maximum of d(z^n*Jn(z))/dz-z^n*J(n-1)(z) =  10.5319728564
Maximum of d(z^(-nu)*J(nu)(z))/dz+z^(-nu)*J(nu+1)(z) =  4.28123894843e-11

Compare maximum of |lhs-rhs| (L1 norm) to zero for nu =  20
Maximum of z*dJ(nu)(z)/dz-z*J(nu-1)+nu*J(nu) =  1.01643953671e-19
Maximum of 2*dJ(nu)(z)/dz-J(nu-1)(z)+J(nu+1)(z) =  0.0
Maximum of (2*nu/z)*J(nu)(z)-J(nu+1)(z)+J(nu-1)(z) =  2.37169225231e-20
Maximum of d(z^n*Jn(z))/dz-z^n*J(n-1)(z) =  4.45714481998e-24
Maximum of d(z^(-nu)*J(nu)(z))/dz+z^(-nu)*J(nu+1)(z) =  3.68271459939e-33
"""
