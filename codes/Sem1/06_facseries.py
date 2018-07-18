"""
Registration Number: xxxx
Description: Sum of factorials and various series solution. Goal is also
to optimize the convergence of the series for higher order terms without 
manual truncation. 
@author: AKB
"""

import math, time
start_time = time.time()

# Simple case switch for different problems to choose from 
fac    = False
invfac = False
expx   = False
sinx   = True

#===== Sum of factorial 1! + 2! + 3! + ...  =====#
if(fac):
   fact=i=1
   sum=0
   n = input("Enter the limit of the factorial series :\n")

   while i<=int(n): 
      fact *= i
      sum  += fact
      i = i + 1
    
   print 'The sum of factorial series of', n, ' order are \n', sum

#===== Sum of inverse factorial 1/1! + 1/2! + 1/3!+ ... ====#
if(invfac):
   fact=i=1 
   sum=0.0
   n = input("Enter the limit of the inverse factorial series :\n")
 
   while i<=int(n):
      fact *= i;
      sum  += float(1.0/fact);
      i = i + 1
       
   print 'The sum of factorial series of', n, ' order are \n', sum

#==== Exponential series exp(x) = 1+ x/1! + x^2/2! + x^3/3!+ ... ====#
if(expx): 
    fact=i=1 
    sum=0.0
    x = input("Enter value of x for exp(x) :\n")
    term  = float(math.pow(x,i)/fact)
    
    while math.fabs(term)>1E-4:
      fact *= i;
      term  = float(math.pow(x,i)/fact)
      sum  += term;
      i = i + 1
    sum += 1.0;  # Don't forget to add the extra 1 

    print 'exp(', x, ') = ', sum, '& convergence took ', i, ' steps\n'

#==== Sine series sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... ====#
if(sinx):
    n = 2
    fact = 1
    sum = 0.0
    x = input("Enter value of x in degrees for sin(x) :\n")
    x = x*math.pi/180.0; # Convert to radian 
    term = x;

    while math.fabs(term)>1E-4:
      sum += term
      fact = n*(n+1)
      term = -term*math.pow(x,2)/fact
      n   += 2

    print 'sin(', 180.0*x/math.pi, ') =', sum, ' & convergence took', n/2, ' steps\n'   
  
exec_time = time.time() - start_time

# Results
print 'Execution time = ', exec_time, ' seconds'
