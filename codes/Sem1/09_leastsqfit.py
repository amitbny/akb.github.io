"""
Registration Number: xxxx 
Description: Least square fitting
@author: AKB
"""

import math, time
sx = sy = sxy = sxx = a = b = a1 = b1 = 0.0
start_time = time.time()

# Input the x & y coordinates
x = list()
y = list()
n = int(input("Enter the number of points :"))
print 'Enter numbers in array: '
for i in range(int(n)):
    xi = float(input("xi :"))
    yi = float(input("yi :"))
    x.append(xi)
    y.append(yi)
print 'x coordinates: ',x
print 'y coordinates: ',y

# Perform the Iteration
for i in range(n):
    sx = sx + x[i]
    sy = sy + math.log(y[i])
    sxy = sxy + x[i]*math.log(y[i])
    sxx = sxx + x[i]*x[i]
  
a = (float(n)*sxy-sx*sy)/(float(n)*sxx-sx*sx)
b = (sxx*sy-sx*sxy)/(float(n)*sxx-sx*sx)
b1 = a
a1 = math.exp(b)
exec_time = time.time() - start_time

# Print the solution 
print 'Multiplier is a=', a1, ' Power is b=', b1
print 'Execution time is = ', exec_time, ' seconds'
