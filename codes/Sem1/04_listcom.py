"""
Roll Number: xxxx 
Description: List Comprehension
@author: AKB
"""

# Logical case switch for different problems to choose from 
list_alt = 0; list_sep = 1; 

if(list_alt):
   # Input two lists from keyboard 
   a = list()
   m = int(input("Enter size of first list :\n"))
   print 'Enter elements of first list :\n '
   for i in range(m):
       ai = input("a"+str(i)+" :")
       a.append(float(ai))
   print 'First list: ',a

   b = list()
   n = int(input("Enter size of second list :\n"))
   print 'Enter elements of second list :\n '
   for i in range(n):
       bi = input("b"+str(i)+" :")
       b.append(float(bi))
   print 'Second list: ',b

   # Create altering list from two lists 
   c = list()
   j = k = 0 
   for i in range(m+n):
       if (i%2==0): 
           c.append(a[j])
           j += 1
       else: 
           c.append(b[k]) 
           k += 1
   print 'Created list: ',c

elif(list_sep):
   # Input list from keyboard 
   a = list(); b = list(); c = list()
   m = int(input("Enter size of list :\n"))
   print 'Enter elements of list :\n '
   for i in range(m):
       ai = input("a"+str(i)+" :")
       a.append(float(ai))
   print 'Main list: ',a

   # Separate list according to positive and negative elements
   for i in a:
	if(i>=0):
		b.append(i)
	else:
		c.append(i)
   print 'Separated list of positive elements: ',b
   print 'Separated list of negative elements: ',c

# Results
#First list:   [2.0, 2.3, 3.0, 3.4, 4.0]
#Second list:  [7.0, 7.2, 7.3, 7.4, 7.5]
#Created list: [2.0, 7.0, 2.3, 7.2, 3.0, 7.3, 3.4, 7.4, 4.0, 7.5]

# Main list = [3.1,-6.4,5.21,7.2,-9.11,-11.1,3.45,-4.52,-2.53,-8.87]
# Separated list of positive elements: [3.1, 5.21, 7.2, 3.45]
# Separated list of positive elements: [-6.4, -9.11, -11.1, -4.52, -2.53, -8.87]
