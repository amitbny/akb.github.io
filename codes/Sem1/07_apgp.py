#-*- coding: utf-8 -*-
"""
Registration Number: xxxx 
Description: Arithmetic Progression (A.P.), Geometric Progression (G.P.)
AP: tn = a + (n – 1) * d and Sn = ( 2a + (n-1) * d ) * (n/2) 
GP: tn = a * r^(n-1) and Sn = a * (r^n - 1) / (r - 1)
@author: AKB
"""

import math, time
start_time = time.time()

# Simple case switch for different problems to choose from 
ap = False
gp = True

value = summ = 0 # free garbage values 

# Input data from keyboard 
a = list()
n = input("Enter the number of terms :\n")

# Selecting AP series 
if(ap):

    a, d = input("Enter first term and common difference of AP series\n");
 
    # Print the series and add all elements to sum
    value = a;
    print ("AP Series: ")
    for i in range(n): 
        print (value)
        summ += value
        value += d
    
    print 'Sum of AP series till ', n, ' terms in term-by-term is ', summ
    
    # Compare with direct Calculation
    summ = (2*a + (n-1)*d)*n/2;
    print 'Sum of AP series till ', n, ' terms in direct computation is ', summ

# Selecting GP series 
else:  
    
    a, r = input("Enter first term and common ratio of GP series\n");
 
    # Print the series and add elements term by term 
    value = a;
    print ("GP Series: ")
    for i in range(n): 
        print (value)
        summ += value
        value *= r
    
    print 'Sum of GP series till ', n, ' terms in term-by-term is ', summ

    # Compare with direct Calculation
    summ = a*(math.pow(r,n)-1)/(r-1);
    print 'Sum of GP series till ', n, ' terms in direct computation is ', summ

# Results
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'
