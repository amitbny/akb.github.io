"""
Registration: xxxx; 
Description: Complex Integration by Simpson's 1/3 Rule 
Author: AKB
"""

import numpy as np
import scipy.integrate as sci

tol = 1E-6  # Tolerance

# Function to be integrated
def f(x): return np.sin(x)/x

# Simpson's 1/3rd integration
def simps(a, b):

    # Compute integral 
    h  = (b-a)*0.5 
    s1 = f(a) + f(b)
    s4 = f(a+h)
    I0 = 1E-16
    I1 = (s1+4.0*s4)*h/3.0

    i=2; s2=0.0;
    while(abs((I1-I0)/I1) > 0.1*tol):
        x   = a+h*0.5
        s2 += s4
        s4  = 0.0
        for j in range(0,i):
            s4 += f(x)
            x += h 
        h *= 0.5
        i *= 2
        I0 = I1
        I1 = (s1+2.0*s2+4.0*s4)*h/3.0
    return I1

# Enter the limit
m = input('Enter integrals lower limit : ')
I0 = 1E-16

# Optimize m->0, 1/m->infinity
while True:
   b = m
   a = 1.0/m
   I1 = simps(a,b)
   if(abs(I0-I1) < tol):
       break
   I0 = I1
   m += 500;     

# Print the solution
print 'Integral_',a,'^',b,' sin(x)/x dx (numerc) = ', I1

# Direct integration (Note: increasing points increase accuracy)
x = np.linspace(a, b, 10*b)
print 'Integral_',a,'^',b,' sin(x)/x dx (direct) = ', sci.simps(f(x),x)

"""
Results:
Enter integrals lower limit : .1
Integral_ 2.46912970585e-05 ^ 40500.1  sin(x)/x dx (numerc) =  1.57076532828
Integral_ 2.46912970585e-05 ^ 40500.1  sin(x)/x dx (direct) =  1.57076532885
"""
