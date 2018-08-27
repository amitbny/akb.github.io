"""
Roll Number: xxxx
Description: Area of a Circle, Triangle, Volume of Sphere, Cylinder. 
Author: AKB
"""

import math, time
start_time = time.time()

# Logical case switch for different problems to choose from 
area_cir = False
area_tri = True
vol_sph  = False
vol_cyl  = False

# Area of a Circle 
if(area_cir):
   r = input('Enter the radius of Circle \n')
   area = math.pi*r*r
   print 'Area of Circle = ', area

# Area of a Triangle (by Heron's formula)
elif(area_tri):
   a, b, theta = input('Give two sides & angle (in degree) of Triangle \n')
   theta = math.pi*theta/180.0   # Convert angle into radian
   c = math.sqrt(a*a + b*b - 2*a*b*math.cos(theta))
   s = (a+b+c)*0.5
   area = math.sqrt(s*(s-a)*(s-b)*(s-c))
   print 'Area of Triangle with side', a, 'and', b, 'with angle', theta*180/math.pi, 'degree is =', area

# Volume of a Sphere 
elif(vol_sph):
   r = input('Enter the radius of Sphere \n')
   vol = math.pi*math.pow(r,3)*4.0/3.0
   print 'Volume of Sphere = ', vol

# Volume of a Cylinder
elif(vol_cyl):
   r, h = input('Enter the radius and height of Cylinder \n')
   vol = math.pi*r*r*h
   print 'Volume of Cylinder = ', vol

exec_time = time.time() - start_time
print 'Execution time is = ', exec_time, ' seconds'

""" 
Results

"""    
