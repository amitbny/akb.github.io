"""
Role Number: xxxx
Description: Sum of various series & optimize the convergence without manual truncation. 
@author: AKB
"""

import math, time
start_time = time.time()

# Logical case switch for different problems to choose from 
fac      = True; 
invfac   = False; 
expx     = False; 
sinx     = False; 
invnsq   = False; 
invmnsq  = False; 
invnk    = False; 
fibonaci = False;

# Sum of factorial 1! + 2! + 3! + 4! + ...  
if(fac):
   fact = i = 1
   sum  = 0
   n = input("Enter the limit of the factorial series : ")

   while i<=int(n): 
      fact *= i
      sum  += fact
      i    += 1
    
   print 'The sum of factorial series upto factorial', n, 'is', sum, '\n'

# Sum of inverse factorial 1/1! + 1/2! + 1/3! + 1/4! + ... 
elif(invfac):
   fact = i = 1 
   sum  = 0.0
   n = input("Enter the limit of the inverse factorial series : ")
 
   while i<=int(n):
      fact *= i
      sum  += float(1.0)/fact
      i    += 1
       
   print 'The sum of inverse factorial series upto factorial', n, 'is', sum, '\n'

# Exponential series exp(x) = 1 + x/1! + x^2/2! + x^3/3! + ... 
elif(expx): 
    fact = i = 1 
    sum  = 1.0  # We take the first term here.
    x = input("Enter value of x for exp(x) : ")
    term  = float(math.pow(x,i))/fact
    
    while math.fabs(term)>1E-4:
      fact *= i
      term  = float(math.pow(x,i))/fact
      sum  += term
      i    += 1

    print 'exp(',x,') = ', sum, '& convergence took', i, 'steps\n'

# Sine series sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... 
elif(sinx):
    n    = 2; fact = 1;
    sum  = 0.0
    x = input("Enter value of x in degrees for sin(x) : ")
    x = x*math.pi/180.0; # Convert to radian 
    term = x

    while math.fabs(term)>1E-4:
      sum += term
      fact = n*(n+1)
      term = -term*math.pow(x,2)/fact
      n   += 2

    print 'sin(',180.0*x/math.pi,') =', sum, ' and convergence took', n/2, 'steps\n'   
 
# Sum of inverse n-square 1/1^2 + 1/2^2 + 1/3^2+ ... = pi^2/6 
elif(invnsq):
    i   = 1 
    sum = 0.0 
    theo = math.pow(math.pi,2)/6.0

    while math.fabs(theo-sum)>1E-4:
      term  = float(1)/math.pow(i,2)
      sum  += term; 
      #print 'i = ', i, ' term = ', term, ' sum = ', sum, '\n' # INTERNAL CHECK
      i    += 1

    print '1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... =  ', sum, ', pi^2/6 = ', theo, ' and convergence took ', i, ' steps\n'

# Sum of inverse n-square 1/1^2 - 1/2^2 + 1/3^2 - 1/4^2 ... = pi^2/12 
elif(invmnsq):
    i    = 1
    sum  = 0.0 
    theo = math.pow(math.pi,2)/12.0

    while math.fabs(theo-sum)>1E-4:
      if (i%2==0): term = float(-1)/math.pow(i,2)
      else:        term = float(1)/math.pow(i,2)
      sum  += term;
      #print 'i = ', i, ' term = ', term, ' sum = ', sum, '\n' # INTERNAL CHECK
      i    += 1

    print '1/1^2 - 1/2^2 + 1/3^2 - 1/4^2 + ... =  ', sum, ', pi^2/12 = ', theo, ' and convergence took ', i, ' steps\n'

# Sum of inverse n^k: 1/2^0 + 1/2^1 + 1/2^2 + 1/2^3 + ... 
elif(invnk):
    k    = 0
    sum  = 0.0
    n    = input("Enter n of the n^k series : ")
    term = float(1)/math.pow(n,k)

    while math.fabs(term)>1E-4:
      term  = float(1)/math.pow(n,k)
      sum  += term
      #print 'k = ', k, ' term = ', term, ' sum = ', sum, '\n' # INTERNAL CHECK
      k    += 1

    print 'Sum from 0 to infinity of 1/n^k with n =', n, 'is', sum, 'and convergence took', k, 'steps\n'

# Sum of inverse Fibonacci series S = Sum 1/Fi, where F(i+1) = F(i) + F(i-1) with F(1) = F(2) = 1 
elif(fibonaci):
    i    = Fi = Fim = 1 
    term = float(1)/Fi
    sum  = 0.0

    while math.fabs(term)>1E-4:
       if(i>2):
         Fip = Fi + Fim
         Fim = Fi
         Fi  = Fip
       term  = float(1)/Fi
       sum  += term
       #print 'i =', i, 'sum =', sum, 'term =', term, '\n' # INTERNAL CHECK
       i    += 1

    print 'Sum of reciprocal Fibonacci sequence =', sum, 'and convergence took', i, 'steps\n'
 
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'

"""
Results

"""
