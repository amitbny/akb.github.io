"""
Roll Number: xxxx
Description: Sum of various series & optimize the convergence without manual truncation. 
@author: AKB
"""

import math, time
start_time = time.time()

# Logical case switch for different problems to choose from 
fac    = 0; invfac  = 0; expx  = 0; sinx      = 0; 
invnsq = 0; invmnsq = 0; invnk = 0; fibonacci = 1;

# Sum of factorial 1! + 2! + 3! + 4! + ...  
if(fac):
   fact = i = 1
   sumf  = 0
   n = input("Enter the limit of the factorial series : ")

   while i<=int(n): 
      fact *= i
      sumf += fact
      i    += 1
    
   print 'The sum of factorial series upto factorial', n, 'is', sumf, '\n'

# Sum of inverse factorial 1/1! + 1/2! + 1/3! + 1/4! + ... 
elif(invfac):
   fact = i = 1 
   sumf  = 0.0
   n = input("Enter the limit of the inverse factorial series : ")
 
   while i<=int(n):
      fact *= i
      sumf += float(1.0)/fact
      i    += 1
       
   print 'The sum of inverse factorial series upto factorial', n, 'is', sumf, '\n'

# Exponential series exp(x) = 1 + x/1! + x^2/2! + x^3/3! + ... 
elif(expx): 
    fact = i = 1 
    sumf = 1.0  # We take the first term here.
    x = input("Enter value of x for exp(x) : ")
    term  = float(math.pow(x,i))/fact
    
    while math.fabs(term)>1E-4:
      fact *= i
      term  = float(math.pow(x,i))/fact
      sumf += term
      i    += 1

    print 'exp(',x,') = ', sumf, '& convergence took', i-1, 'steps\n'

# Sine series sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... 
elif(sinx):
    n    = 2; fact = 1
    sumf = 0.0
    x = input("Enter value of x in degrees for sin(x) : ")
    x = x*math.pi/180.0; # Convert to radian 
    term = x

    while math.fabs(term)>1E-4:
      sumf += term
      fact  = n*(n+1)
      term  = -term*math.pow(x,2)/fact
      n    += 2

    print 'sin(',180.0*x/math.pi,') =', sumf, ' and convergence took', n/2-1, 'steps\n'   
 
# Sum of inverse n-square 1/1^2 + 1/2^2 + 1/3^2+ ... = pi^2/6 
elif(invnsq):
    i    = 1 
    sumf = 0.0 
    theo = math.pow(math.pi,2)/6.0

    while math.fabs(theo-sumf)>1E-4:
      term  = float(1)/math.pow(i,2)
      sumf += term; 
      i    += 1

    print '1/1^2 + 1/2^2 + 1/3^2 + 1/4^2 + ... =  ', sumf, ', pi^2/6 = ', theo, ' and convergence took ', i-1, ' steps\n'

# Sum of inverse n-square 1/1^2 - 1/2^2 + 1/3^2 - 1/4^2 ... = pi^2/12 
elif(invmnsq):
    i    = 1
    sumf = 0.0 
    theo = math.pow(math.pi,2)/12.0

    while math.fabs(theo-sumf)>1E-4:
      if (i%2==0): term = float(-1)/math.pow(i,2)
      else:        term = float(1)/math.pow(i,2)
      sumf += term;
      i    += 1

    print '1/1^2 - 1/2^2 + 1/3^2 - 1/4^2 + ... =  ', sumf, ', pi^2/12 = ', theo, ' and convergence took ', i-1, ' steps\n'

# Sum of inverse n^k: 1/2^0 + 1/2^1 + 1/2^2 + 1/2^3 + ... 
elif(invnk):
    k    = 0
    sumf = 0.0
    n    = input("Enter n of the n^k series : ")
    term = float(1)/math.pow(n,k)

    while math.fabs(term)>1E-4:
      term  = float(1)/math.pow(n,k)
      sumf += term
      k    += 1

    print '1/'+str(n)+'^0 + 1/'+str(n)+'^1 + 1/'+str(n)+'^2 + 1/'+str(n)+'^3 + ... = ', sumf, 'and convergence took', k, 'steps\n'

# Sum of inverse Fibonacci series S = Sum 1/Fi, where F(i+1) = F(i) + F(i-1) with F(1) = F(2) = 1 
elif(fibonacci):
    i    = Fi = Fim = 1 
    term = float(1)/Fi
    sumf = 0.0

    while math.fabs(term)>1E-4:
       if(i>2):
         Fip = Fi + Fim
         Fim = Fi
         Fi  = Fip
       term  = float(1)/Fi
       sumf += term
       i    += 1

    print 'Sum of reciprocal Fibonacci sequence =', sumf, 'and convergence took', i-1, 'steps\n'
 
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'

"""
Results
print 'i = ', i, ' term = ', term, ' sum = ', sumf, '\n' # DEBUGGING
Exercise: Try to construct zeta function as series sum (truncate upto specific term) as well as 
          multiplication of primes. Hence find out largest prime needed to converge the series
          upto that specific term.
"""
