"""
Registration: xxxx; 
Description: Newton-Gregory Forward Interpolation Method 
Author: AKB
"""

import numpy as np

# Enter the table y = f(x) and give x 
n = input('Enter the number of table entries equal to degree of polynomial : ')
print 'Input the x coordinate : \n'
x = np.array([float(input("x"+str(i)+" : ")) for i in range(n)])
y = np.sin(x)
xx = input('Enter point at which the polynomial is to be evaluated : \n') 
a = np.zeros(n)  # null-assign the a cofficients

# Compute the divided difference coefficients
a[0] = y[0]
for k in range(0,n):
    w = 1
    p = 0
    for j in range(0,k):
        p += a[j]*w
        w = w*(x[k] - x[j])
    a[k] = (y[k]-p)/w
  
print 'Divided difference coefficients are ', a

# Compute the polynomial at given value

px = a[n-1] # polynomial value at xx
for k in range(n-2,-1,-1):
    xd = xx - x[k]
    px = a[k] + px*xd

print 'Corresponding value of y is ', px

"""
Results :
Enter the number of table entries equal to degree of polynomial : 3
Input the x coordinate : 
x0 : 0
x1 : np.pi/2
x2 : np.pi
Enter point at which the polynomial is to be evaluated : 
np.pi/4
Divided difference coefficients are  [ 0. 0.63661977 -0.40528473]
Corresponding value of y is  0.75
"""
