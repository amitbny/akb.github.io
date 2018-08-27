"""
Registration Number:
Description: Code for Matrix A+B, A*B, A^T*B. 
@author: AKB
"""

import math, time
start_time = time.time()

# Integer switch to choose problems
matadd=0
matmul=1

#==== Initialize and populate A =====#
m = int(input('number of rows of A, m = '))
n = int(input('number of columns of A, n = '))
A = list();   # you may use [] also
# initialize the number of rows ...
for i in range(0,m):
    A += [0]
# ... multiply with number of columns to initialize matrix
for i in range (0,m):
    A[i] = [0]*n

# Enter the matrices A from keyboard
print 'Enter matrix A'
for i in range (0,m):
    for j in range (0,n):
        print 'row',i+1,',column',j+1
        A[i][j] = int(input())
print 'A=', A

#==== Initialize and populate B =====#
p = int(input('number of rows of B, p = '))
q = int(input('number of columns of B, q = '))
B = list(); C = list();
# initialize the number of rows ...
for i in range(0,p):
    B += [0]
# ... multiply with number of columns to initialize matrix
for i in range (0,p):
    B[i] = [0]*q

# Enter the matrix B from keyboard
print 'Enter matrix B'
for i in range (0,p):
    for j in range (0,q):
        print 'row',i+1,',column',j+1
        B[i][j] = int(input())
print 'B=',B

# Add the matrices after checking their dimensions 
if(matadd):
    if m==p & n==q:
       # Construct C_{mn} with zeroes
       for i in range(0,m):
           C += [0]
       for i in range (0,m):
           C[i] = [0]*n
       print 'Sum of matrix A and B is\n'
       for i in range(p):
           for j in range (q):
               C[i][j] = A[i][j] + B[i][j]
       print(C)
    else:
       print 'Invalid operation\n'
       exit(1)

elif(matmul):
# Number of column of first matrix = Number of row of second matrix 
    if n==p:    # A*B
       # Construct C_{mq} with zeroes
       for i in range(0,m):
           C += [0]
       for i in range (0,m):
           C[i] = [0]*q
       print 'A*B = \n'
       for i in range(m):
           for j in range(q):
               C[i][j] = 0;
               for k in range(n):
                   C[i][j] += A[i][k]*B[k][j]
       print(C)
    
    elif m==p:  # Transpose(A)*B
         # Construct C_{nq} with zeroes
         for i in range(0,n):
             C += [0]
         for i in range (0,n):
             C[i] = [0]*q
         print '\n A^T*B = \n'
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
   print 'Invalid operation\n'
   exit(1)

exec_time = time.time() - start_time
print 'Execution time is = ', exec_time, ' seconds'
  
