"""
Registration: xxxx; 
Description: nth Root of unity and two square roots.
             Note: Numpy (instead of cmath) is also good (check!)
Author: AKB
"""

import cmath  

def nroot(k,n): return cmath.exp(2*cmath.pi*1j*k/n)
n = input("Compute the nth root of unity for n = ");
for k in range(n):
    print nroot(k,n)

c = input("Input the complex number : ")
print 'Square root of', c, ' is ', cmath.sqrt(c)

"""
Result :
n=2: (1+0j), (-1+1.22464679915e-16j)
n=3: (1+0j),(-0.5+0.866025403784j),(-0.5-0.866025403784j)
n=4: (1+0j),(6.12323399574e-17+1j),(-1+1.22464679915e-16j),(-1.83697019872e-16-1j)

Input the complex number : -5+12j
Square root of (-5+12j)  is  (2+3j)
"""
