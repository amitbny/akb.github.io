#-*- coding: utf-8 -*-
"""
Registration Number: xxxx 
Description: Arithmetic Progression (A.P.), Geometric Progression (G.P.)
AP: tn = a + (n – 1) * d and Sn = ( 2a + (n-1) * d ) * (n/2) 
GP: tn = a * r^(n-1) and Sn = a * (r^n - 1) / (r - 1)
Author: AKB
"""

import math, time
start_time = time.time()

# Case switch for different problems to choose from 
ap = 1; gp = 0
value = sumf = 0 # free garbage values 

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
        sumf  += value
        value += d
    
    print 'Sum of AP series till ', n, ' terms in term-by-term is ', sumf
    
    # Compare with direct Calculation
    sumf = (2*a + (n-1)*d)*n/2;
    print 'Sum of AP series till ', n, ' terms in direct computation is ', sumf

# Selecting GP series 
else:  
    
    a, r = input("Enter first term and common ratio of GP series\n");
 
    # Print the series and add elements term by term 
    value = a;
    print ("GP Series: ")
    for i in range(n): 
        print (value)
        sumf  += value
        value *= r
    
    print 'Sum of GP series till ', n, ' terms in term-by-term is ', sumf

    # Compare with direct Calculation
    sumf = a*(math.pow(r,n)-1)/(r-1);
    print 'Sum of GP series till ', n, ' terms in direct computation is ', sumf

# Results
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'
