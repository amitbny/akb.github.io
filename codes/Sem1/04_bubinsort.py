"""
Registration Number: xxxx 
Description: Bubble Sort, Insertion Sort
@author: AKB
"""

import math, time
start_time = time.time()

# Simple case switch for different problems to choose from 
bubsort = False
inssort = True

# Input data from keyboard 
a = list()
n = input("Enter the number of inputs :\n")
print 'Enter the numbers :\n '
for i in range(int(n)):
    ai = input("ai :")
    a.append(float(ai))
print 'Unsorted numbers: ',a
tmp = 0.0  # auxiliary variable

# Perform Bubble sorting operation
if(bubsort):
   for i in range(int(n)):
       for j in range(n-i-1):
           if a[j]>a[j+1]:
              tmp = a[j];
              a[j] = a[j+1];
              a[j+1] = tmp;
              #a[j], a[j+1] = a[j+1], a[j]  # Forbidden in C/Fortran

# Perform Insertion sorting operation
if(inssort):
   # Since we want to swap an item with previous one, we start from 1
   for i in range(1, int(n)): # you may use len(a) instead of int(n)
       tmp = a[i]
       j = i - 1
       while (j >= 0) and (a[j] > tmp):
              a[j+1] = a[j]  # Move the bigger item 1 step right to make room for tmp
              j = j - 1      # Take a[j] all the way left to the place where it has a smaller/no value to its left.
       a[j+1] = tmp 

# Print the results 
if(bubsort): print 'Bubble sorted numbers in ascending order \n ', a
if(inssort): print 'Insertion sorted numbers in ascending order \n ', a
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'