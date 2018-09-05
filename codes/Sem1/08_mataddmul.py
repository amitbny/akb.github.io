"""
Registration Number:
Description: Code for Matrix A+B, A*B, A^T*B. 
@author: AKB
"""

import math, time

# Integer switch to choose problems from
matadd=0; matmul=1;

#==== Zero initialize and populate A =====#
m = int(input('number of rows of A, m = '))
n = int(input('number of columns of A, n = '))

A = list();   # Create an empty list 
# initialize 0 as number of rows and then multiply with number 
# of columns to initialize matrix
for i in range(0,m):
    A   += [0]
    A[i] = [0]*n

# Enter the matrices A from keyboard
print 'Enter matrix A'
for i in range (0,m):
    for j in range (0,n):
        A[i][j] = int(input("A"+str(i)+str(j)+" :"))
print 'A=', A

#==== Zero initialize and populate B =====#
p = int(input('number of rows of B, p = '))
q = int(input('number of columns of B, q = '))

B = list();   
for i in range(0,p):
    B   += [0]
    B[i] = [0]*q

# Enter the matrix B from keyboard
print 'Enter matrix B'
for i in range (0,p):
    for j in range (0,q):
        B[i][j] = int(input("B"+str(i)+str(j)+" :"))
print 'B=',B

start_time = time.time()
# Add the matrices after checking their dimensions 
if(matadd):
    if m==p & n==q:
       C = list()   # Construct C_{mn} with zeroes
       for i in range(0,m):
           C   += [0]
           C[i] = [0]*n
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
       C = list()   # Construct C_{mq} with zeroes
       for i in range(0,m):
           C   += [0]
           C[i] = [0]*q
       print 'A * B = \n'
       for i in range(m):
           for j in range(q):
               C[i][j] = 0;
               for k in range(n):
                   C[i][j] += A[i][k]*B[k][j]
       print(C)
    
    elif m==p:  # Transpose(A)*B
         C = list()   # Construct C_{nq} with zeroes
         for i in range(0,n):
             C   += [0]
             C[i] = [0]*q
         print '\n A^T * B = \n'
         for i in range(n):
             for j in range(q):
                 C[i][j] = 0
                 for k in range(m):
                     C[i][j] += A[k][i]*B[k][j];
         print(C)
      
    else:
      printf("Invalid operation\n");
      exit(1);

else:
   print 'Invalid choice of problem\n'
   exit(1)

exec_time = time.time() - start_time
print 'Execution time is = ', exec_time, ' seconds'
