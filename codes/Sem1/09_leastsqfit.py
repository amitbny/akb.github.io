"""
Roll Number: xxxx 
Description: Least square fitting
@author: AKB
"""

import math, time
sx = sy = sxy = sxx = m = c = 0.0

# Input the x & y coordinates
x = list()
y = list()
n = int(input("Enter the number of points :"))
print 'Enter numbers in array: '
for i in range(int(n)):
    xi = float(input("x"+str(i)+" :"))
    yi = float(input("y"+str(i)+" :"))
    x.append(xi)
    y.append(yi)
print 'x coordinates: ',x
print 'y coordinates: ',y

start_time = time.time()
# Calculate sum of sx,sy,sx*sy,sx*sx
for i in range(n):
    sx = sx + x[i]
    sy = sy + y[i]
    sxy = sxy + x[i]*y[i]
    sxx = sxx + x[i]*x[i]
  
m = (float(n)*sxy - sx*sy)/(float(n)*sxx - sx*sx)
c = (sy*sxx - sx*sxy)/(float(n)*sxx - sx*sx)

# Print the solution
print 'Least square fit is f = ', m, '* x + ', c
exec_time = time.time() - start_time
print 'Execution time is = ', exec_time, ' seconds'

"""
Results
Check for x=[8,2,11,6,5,4,12,9,6,1], 
          y=[3,10,3,6,8,12,1,4,9,14], Least square fit f=-1.10641891892*x + 14.0810810811; 

"""
