"""
Roll Number: xxxx 
Description: Compute Mean, Median, Mode, Std of list
@author: AKB
"""

import math, time
maxCount = 0 
mean = median = mode = sd = tmp = 0.0

# Input the array from keyboard 
a = list()
n = int(input("Enter the number of inputs :\n"))
print 'Enter the numbers :\n '
for i in range(n):
    ai = input("a"+str(i)+" :")
    a.append(float(ai))
print 'Unsorted numbers: ',a

# Calculate mean (average of array)
mean = sum(a)/n
    
# Perform Bubble sorting
start_time = time.time()
for i in range(int(n)):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
           a[j], a[j+1] = a[j+1], a[j]
print 'Sorted numbers: ',a
        
# Calculate median (middle of sorted array)
if n%2==0: median = (a[n/2-1]+a[n/2])/2.0
else:      median = a[(n-1)/2]
 
# Calculate mode (find tally and Count the maximum)
tally = list([0]*n)   # assign null array 

for i in range(n):
    for j in range (i,n):
        if a[i]==a[j]: tally[i] += 1

for i in range(n):
    if tally[i] > maxCount:
       maxCount = tally[i]
       mode = a[i]
    
# Calculate Standard Deviation 
for i in a: 
   sd += math.pow((i - mean),2)
sd = math.sqrt(sd/(n-1))

# Results 
print '\nmean = ', mean
print 'median = ', median
if(maxCount>1): print 'mode = ', mode
else:           print 'There exists no mode'
print 'Standard deviation = ', sd

exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'
