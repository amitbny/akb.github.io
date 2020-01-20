"""
Registration: xxxx; 
Description: Gaussian Integral, Dirac Delta
Author: AKB
"""

import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from scipy.signal import gaussian

# Logical case switch for different problems to choose from 
prob1=0; prob2=1; prob3=0;

#====== Gaussian Integral using Quadrature ======#
if(prob1):
   def f(x,a,b,c): return np.exp(-a*x**2 + b*x + c) #[-np.inf,np.inf]

   # Enter the coefficients and integral bounds
   a,b,c,low,up = input('Enter a,b,c coefficients & integration limits : ')

   # Peform indefinite integral using Quadrature
   I_num, err = sci.quad(f, low, up, args=(a,b,c))
   I_theo     = np.sqrt(np.pi/a)*np.exp(b**2/(4.0*a)+c)

   # Print/compare results
   print 'Integral_',low,'^',up,' e^(-',a,'x^2+',b,'x+',c,') dx = ', I_num
   print 'Theoretical value of the Integral = ', I_theo
   print 'Absolute error = ', err, ', Relative error = ', I_num - I_theo

#====== Convolution of two Gaussian =========#
if(prob2):
   
   def gauss(x,mu,sig):
       return np.exp(-((x-mu)**2.0)/(2.0*sig**2.0))/np.sqrt(2.0*np.pi)/sig

   # Choose two normal distributions to convolve
   mu1 = 0; sig1 = 0.3 
   mu2 = 0; sig2 = 0.2; 
   x = np.linspace(-2, 2, 500)
   dx = x[1]-x[0]
   convolution = np.convolve(gauss(x,mu1,sig1), gauss(x,mu2,sig2), mode="same")*dx
   sigc = np.sqrt(sig1**2 * sig2**2/(sig1**2 + sig2**2))
   ampc = sigc/(np.sqrt(2*np.pi)*sig1*sig2)

   # Plot
   plt.figure()
   plt.plot(x, gauss(x,mu1,sig1), '--b+', lw=.4,
            label=r"$\mathcal{N}_1("+str(mu1)+","+str(sig1)+")$")
   plt.plot(x, gauss(x,mu2,sig2), '--g<', lw=.4,
            label=r"$\mathcal{N}_2("+str(mu2)+","+str(sig2)+")$")
   plt.plot(x, convolution, '--rx', lw=.4, 
            label=r"$\mathcal{N}_c("+str(mu1+mu2)+","+str(round(sigc,2))+")$")
   plt.title("(Convolution) Amplitude="+str(round(ampc,2)))
   plt.legend(loc='best', prop={'size':16})
   plt.xlabel("x", size=16)
   plt.ylabel(r"$\mathcal{N}(\mu,\sigma)$", size=16)
   plt.grid()
   plt.show()

"""
#Result: 
Enter a,b,c coefficients & integration limits : 1,2,1,-np.inf,np.inf
Integral_ -inf ^ inf  e^(- 1 x^2+ 2 x+ 1 ) dx =  13.0967609371
Theoretical value of the Integral =  13.0967609371
Absolute error =  2.7105554618e-10 , Relative error =  0.0
"""
