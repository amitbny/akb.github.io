"""
Registration: xxxx; 
Description: Gauss-Seidel Iterative Method 
Author: AKB
"""

import numpy as np
error = 1.0    # Initialize with a random error 
tol   = 1E-6   # Tolerance

# Input 4 equations: 9a+b+c+d=75, a+8b+c+d=54, a+b+7c+d=43, a+b+c+6d=34
n = input("Enter the number of equations: ")
print 'Enter the coefficients in Numpy Array : '
a = np.array([[int(input("a"+str(i)+str(j)+" : ")) for j in range(n+1)] for i in range(n)])
a.astype(float)
   
# Initialize solution vector to zero
x = np.array([0.0 for  i in range(n)])
   
# Do the iteration
count = 0
while error > tol:
   for i in range (n):
       summ = 0.0
       for j in range (n):
           if i!=j:
              summ += a[i,j]*x[j];
       temp = (a[i,n] - summ)/a[i,i]  # Note the last index n
       error = abs(x[i] - temp)
       count += 1
       if error > tol:
          x[i] = temp
   
# Print the solution 
print 'The values of x are ', np.around(x), 'and it took ', count, 'steps to converge'
   
# Results: 
# Enter the number of equations: 4
# Enter the coefficients
# 9 1 1 1 75
# 1 8 1 1 54
# 1 1 7 1 43
# 1 1 1 6 34
# The values of x are [7, 5, 4, 3] and it took 12 steps to converge
