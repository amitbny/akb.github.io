"""
Registration: xxxx; 
Description: Integration of ODE by RK4's Method dy/dt = g(x,y)
Author: AKB
"""
import numpy as np
import matplotlib.pyplot as plt

# Choose first solve=1 to generate files and then plot=1 to plot them all
solve=0; plot=1;

if(solve):

   def f(x,y): return (1+x)*y + 1 - 3*x + pow(x,2)   

   # Enter the integration limits  
   # Take x0=0, y0=0.065 and h=[5e-2,5e-3,5e-4,5e-5]
   x, y, h = input('Enter initial value x0, y0 and timestep h : ')
   time = 3; step = int(time/h)
   X = Y = []

   # Open a file (in C, fp is file pointer)
   if  (h==0.05):    fp = open("data/rk4_h0.05.dat","w") 
   elif(h==0.005):   fp = open("data/rk4_h0.005.dat","w") 
   elif(h==0.0005):  fp = open("data/rk4_h0.0005.dat","w") 
   elif(h==0.00005): fp = open("data/rk4_h0.00005.dat","w") 

   # RK4's step
   for i in range(step):
       a = h*f(x,y)
       b = h*f(x+0.5*h, y+0.5*a)
       c = h*f(x+0.5*h, y+0.5*b)
       d = h*f(x+h,     y+c)
       y += (a + 2*b + 2*c + d)/6.0
       x += h
       print >> fp,x,y   # Print it using file pointer
       Y.append(y)
       X.append(x)

   # Close the file
   fp.close()

if(plot):

   # Read the datafiles
   fp1 = np.loadtxt('data/rk4_h0.05.dat');    X1 = fp1[:,0]; Y1 = fp1[:,1] 
   fp2 = np.loadtxt('data/rk4_h0.005.dat');   X2 = fp2[:,0]; Y2 = fp2[:,1] 
   fp3 = np.loadtxt('data/rk4_h0.0005.dat');  X3 = fp3[:,0]; Y3 = fp3[:,1] 
   fp4 = np.loadtxt('data/rk4_h0.00005.dat'); X4 = fp4[:,0]; Y4 = fp4[:,1]   

   # Plot the data
   plt.figure(1)
   plt.plot(X1, Y1, '-', lw=2, c='g', label=r'$h=5\times 10^{-2}$')
   plt.plot(X2, Y2, '-', lw=2, c='b', label=r'$h=5\times 10^{-3}$')
   plt.plot(X3, Y3, '-', lw=2, c='k', label=r'$h=5\times 10^{-4}$')
   plt.plot(X4, Y4, '-', lw=2, c='r', label=r'$h=5\times 10^{-5}$')
   plt.legend(loc='best', prop={'size':16})
   plt.suptitle(r'RK4 Method : $\frac{dy}{dx} = (1+x)y+1-3x+x^2$',size=16)
   plt.xlabel('x', size = 14)
   plt.xticks(size = 14)
   plt.ylabel('y', size = 14)
   plt.yticks(size = 14)
   plt.grid()
   plt.savefig('plot/09_rk4.pdf') 
   plt.show()

"""
Results:
Enter initial value x0, y0 and timestep h : 0, 0.065, 0.05
   
"""
