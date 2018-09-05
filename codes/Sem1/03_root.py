"""
Role Number: xxxx
Description: Roots of a quadratic equation ax^2+bx+c=0
Author     : AKB
"""

import math, time
root1 = root2 = realp = imagp = discr = 0.0
a,b,c = input('Enter the values of a, b & c: ')
start_time = time.time()

# If a or b or c is 0, it is not a quadratic equation, hence exit 
if a==0: 
   print 'Error: Roots cannot be determined'
   exit(1)
else:
    discr = math.pow(b,2) - 4.0*a*c;
    if discr < 0:
        print 'Imaginary roots\n'
        realp = -b/(2.0*a);
        imagp = math.sqrt(abs(discr))/(2.0*a);
        print 'Root1 = ', realp, '+ i', imagp, '\n'
        print 'Root2 = ', realp, '- i', imagp, '\n'    
    elif discr == 0:
        print 'Roots are real and equal\n'
        root1 = -b/(2.0*a)
        print 'Root1 = Root2 = ', root1, '\n'
    else:
        print 'Roots are real and distinct\n'
        root1 = (-b + math.sqrt(discr))/(2.0*a); 
        root2 = (-b - math.sqrt(discr))/(2.0*a); 
        print 'Root1 = ', root1
        print 'Root2 = ', root2
    
exec_time = time.time() - start_time
print 'Execution time = ', exec_time, ' seconds'

"""
Results 
Try say (1,2,1), (1,4,1), (2,3,4)
"""
