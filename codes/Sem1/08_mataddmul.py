"""
Roll Number:
Description: Code for Matrix A+B, A*B, A^T*B. 
@author: AKB
"""

import math, time

# Integer switch to choose problems from
matadd=0; matmul=1;

#==== Zero initialize and populate A =====#
m, n = input("number of rows and columns of A: ")

# Either initialize 0 as number of rows and then multiply with number of columns,
A = list()   
for i in range(m):
    A   += [0]
    A[i] = [0]*n

# Alternatively,
#A = [[0 for j in range(n)] for i in range(m)]

# Enter the matrices A from keyboard
print 'Enter matrix A'
for i in range (m):
    for j in range (n):
        A[i][j] = int(input("A"+str(i)+str(j)+" :"))
print 'A_{'+str(m)+'x'+str(n)+'} = ', A

#==== Zero initialize and populate B =====#
p, q = input("number of rows and columns of B: ")
B = [[0 for j in range(q)] for i in range(p)]

# Enter the matrix B from keyboard
print 'Enter matrix B'
for i in range (0,p):
    for j in range (0,q):
        B[i][j] = int(input("B"+str(i)+str(j)+" :"))
print 'B_{'+str(p)+'x'+str(q)+'} = ', B

# Add the matrices after checking their dimensions 
start_time = time.time()
if(matadd):
    if m==p & n==q:
       C = [[0 for j in range(n)] for i in range(m)] # Construct C_{mn} with zeroes
       for i in range(m):
           for j in range (n):
               C[i][j] = A[i][j] + B[i][j]
       print 'A + B = ', C
    else:
       print 'Invalid operation\n'
       exit(1)

# Multiply the matrices after checking their dimensions 
elif(matmul):
    # Number of column of first matrix = Number of row of second matrix 
    if n==p:    # A*B
       C = [[0 for j in range(q)] for i in range(m)] # Construct C_{mq} with zeroes
       for i in range(m):
           for j in range(q):
               C[i][j] = 0;
               for k in range(n):
                   C[i][j] += A[i][k]*B[k][j]
       print 'A * B = ', C
    
    elif m==p:  # Transpose(A)*B
         C = [[0 for j in range(q)] for i in range(n)] # Construct C_{nq} with zeroes
         print '\n A^T * B = \n'
         for i in range(n):
             for j in range(q):
                 C[i][j] = 0
                 for k in range(m):
                     C[i][j] += A[k][i]*B[k][j];
         print 'A^T * B = ', C
      
    else:
      printf("Invalid operation\n");
      exit(1);

else:
   print 'Invalid choice of problem\n'
   exit(1)

exec_time = time.time() - start_time
print 'Execution time is = ', exec_time, ' seconds'

"""
Results: 
CAUTION: A = [[0*n]*m] DOES NOT WORK AS YOU UPDATE ELEMENTS, THE CODE BREAKS.
Exercise: Try doing inverse of 2X2 and 3X3 matrix. Try constucting the Similarity transformation.

"""
