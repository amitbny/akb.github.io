"""
Roll Number: xxxx 
Description: Comparison of Bubble and Insertion Sort
@author: AKB
"""

import math, time

# Case switch for different sorting algorithm to choice
bubsort = 1; inssort = 0

# Input data from keyboard 
a = list()
n = input("Enter the number of inputs :\n")
print 'Enter the numbers :\n '
for i in range(int(n)):
    ai = input("a"+str(i)+" :")
    a.append(float(ai))  # you should use int, if asked to sort integers
print 'Unsorted numbers: ',a
tmp = 0.0  # auxiliary variable

# Perform Bubble sorting operation
start_time = time.time()
if(bubsort):
   for i in range(int(n)):
       for j in range(n-i-1):
           if a[j]>a[j+1]:
              tmp = a[j];
              a[j] = a[j+1];
              a[j+1] = tmp;
              #a[j], a[j+1] = a[j+1], a[j]  # Alternative Treatment; Forbidden in C/Fortran
              #print i, j, a[:]             # DEBUGGING

# Perform Insertion sorting operation
if(inssort):
   # Since we want to swap an item with previous one, we start from 1
   for i in range(1, int(n)): # you may use len(a) instead of int(n)
       tmp = a[i]
       j = i - 1
       while (j >= 0) and (a[j] < tmp):
              a[j+1] = a[j]   # Move the bigger item 1 step right to make room for tmp
              j -= 1          # Take a[j] all the way left to the place where it has a smaller/no value to its left.
       a[j+1] = tmp 
       #print i, j, a[:]      # DEBUGGING

# Print the results 
if(bubsort): print 'Bubble sorted numbers in ascending order \n ', a
if(inssort): print 'Insertion sorted numbers in ascending order \n ', a
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'

"""
Results

"""