"""
Registration: xxxx; 
Description: Euler's Method dy/dx = f(x,y) with IVP (x0,y0),xn and h.
Author: AKB
"""
import numpy as np
import matplotlib.pyplot as plt

# Choose first solve=1 to generate files and then plot=1 to plot them all
solve = 0;
plot  = 1;

if(solve):

   def f(x,y): return (1+x)*y + 1 - 3*x + pow(x,2)   

   # Enter initial conditions
   #x, y, xn, h = input('Enter initial value x0, y0, xn and timestep h : ')
   x = 0.0; y=0.065; xn = 3.0; h=0.00005; 
   step = int(xn/h)
   X = Y = []

   # Open a file (in C, fp is file pointer)
   if  (h==0.05):    fp = open("data/euler_h0.05.dat","w") 
   elif(h==0.005):   fp = open("data/euler_h0.005.dat","w") 
   elif(h==0.0005):  fp = open("data/euler_h0.0005.dat","w") 
   elif(h==0.00005): fp = open("data/euler_h0.00005.dat","w") 

   # Euler's step
   for i in range(step):
       y += h*f(x,y)
       x += h
       print >> fp,x,y   # Print it using file pointer
       Y.append(y)
       X.append(x)

   # Close the file
   fp.close()
   print 'Final value at x = ',x,' is y = ', y

if(plot):

   # Read the datafiles
   fp1 = np.loadtxt('data/euler_h0.05.dat');    X1 = fp1[:,0]; Y1 = fp1[:,1] 
   fp2 = np.loadtxt('data/euler_h0.005.dat');   X2 = fp2[:,0]; Y2 = fp2[:,1] 
   fp3 = np.loadtxt('data/euler_h0.0005.dat');  X3 = fp3[:,0]; Y3 = fp3[:,1] 
   fp4 = np.loadtxt('data/euler_h0.00005.dat'); X4 = fp4[:,0]; Y4 = fp4[:,1]   

   # Plot the data
   plt.figure(1)
   plt.plot(X1, Y1, '-', lw=2, c='g', label=r'$h=5\times 10^{-2}$')
   plt.plot(X2, Y2, '-', lw=2, c='b', label=r'$h=5\times 10^{-3}$')
   plt.plot(X3, Y3, '-', lw=2, c='k', label=r'$h=5\times 10^{-4}$')
   plt.plot(X4, Y4, '-', lw=2, c='r', label=r'$h=5\times 10^{-5}$')
   plt.legend(loc='best', prop={'size':18})
   plt.suptitle(r'Euler Method : $\frac{dy}{dx} = (1+x)y+1-3x+x^2$',size=16)
   plt.xlabel('x', size = 16)
   plt.xticks(size = 14)
   plt.ylabel('y', size = 16)
   plt.yticks(size = 14)
   plt.grid()
   plt.savefig('plot/09_euler.pdf') 
   plt.show()
