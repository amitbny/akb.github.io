"""
Registration: xxxx; 
Description: Dirac Delta function
Author: AKB
"""

import numpy as np
import scipy.integrate as sci

prob1=0; prob2=1;

# ===== Improper integral for ddelta ===== #
if(prob1):
   def f(x,sig):
       return np.exp(-(x-2)**2/(2.0*sig**2))*(x+3)/np.sqrt(2.0*np.pi*sig**2) #[-np.inf,np.inf]

   # Enter standard deviation and integration limits
   sig,low,up = input('Enter sigma & integration limits : ')

   # Peform the indefinite integral using Quadrature
   I, err = sci.quad(f,low,up,args=(sig))

   # Print result
   print 'Integral computed value = ', I, ' with error = ', err

# ===== Int f(x) ddelta(x-a) dx = f(a) (Using Sympy & get value by evalf) ==== #
if(prob2):
   from sympy import *
   def f(x) :
       #return x**2
       #return exp(-x**2+x+1)
       return sin(x)
       
   x1 = -1.0; x2 = 1.5; a = 2;
   x = Symbol('x')
   I = integrate(f(x)*DiracDelta(x-a), (x, x1-a, x2+a))  
   print 'Integral_',x1-a,'^',x2+a,' x^2 ddelta(x-',a,')dx = ', I.evalf()

"""
#Results (prob1): 
Enter sigma & integration limits : 1,-np.inf,np.inf
Integral computed value =  5.0
 
Enter sigma & integration limits : 0.1,-np.inf,np.inf
Integral computed value =  5.0
 
Enter sigma & integration limits : 0.01,-np.inf,np.inf
Integral computed value =  7.57910251848e-51

#Results (prob2): 
Integral_ -6.0 ^ 6.5  x^2 ddelta(x- 5 )dx =  25

"""
