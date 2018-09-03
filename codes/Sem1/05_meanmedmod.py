"""
Roll Number: xxxx 
Description: Compute Mean, Median & Mode
@author: AKB
"""

import math, time
start_time = time.time()

maxCount = mode = 0 
mean = median = tmp = 0.0

# Input the series from keyboard 
a = list()
n = int(input("Enter the number of inputs :\n"))
print 'Enter the numbers :\n '
for i in range(n):
    ai = input("ai :")
    a.append(float(ai))
print 'Unsorted numbers: ',a

# Calculate mean (average of array)
mean = sum(a)/n
    
# Perform Bubble sorting
for i in range(int(n)):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
           tmp = a[j];
           a[j] = a[j+1];
           a[j+1] = tmp;
print 'Sorted numbers: ',a
        
# Calculate median (middle of sorted array)
if n%2==0:      
     median = (a[n/2]+a[n/2+1])/2.0
elif n%2!=0:
     median = a[(n+1)/2]
 
# Calculate mode (find tally and Count the maximum)
tally = [0]*n   # assign zero 
for i in range(n):
    for j in range (i,n):
        if a[i]==a[j]: tally[i] += 1

for i in range(n):
    if tally[i] > maxCount:
       maxCount = tally[i]
       mode = a[i]
    
# Results 
print '\nmean = ', mean
print '\nmedian = ', median
print '\nmode = ', mode

exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'
