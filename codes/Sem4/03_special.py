"""
Registration : xxxx
Description  : Special functions
Author       : AKB
"""

import numpy as np
from scipy.special import legendre, hermite, jn, yn
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Logical case switch for different problems to choose from 
legendr=1; hermit=1; bessl=1;

if(legendr):
   #==================================================================#
   print      '~~~ LEGENDRE POLYNOMIAL ~~~'                           #
   #==================================================================#
   lp3rd=1; lpsevord=1;

   if(lp3rd):
      #=== 3rd Order L.P. ==#
      print 'P0(x)=', legendre(0), '\nP1(x)=', legendre(1)  # P0(x)=1, P1(x)=x
      print 'P2(x)=', legendre(2), '\nP3(x)=', legendre(3)  # P2(x)=(3x^2-1)/2, P3(x)=(5x^3-3x)/2
      p3 = legendre(3); [a3, a2, a1, a0] = p3 
      print 'Coefficients in decreasing power: ', p3[0],p3[1],p3[2],p3[3]
      # construct polynomial at point x : p3(x) = a3*x**3 + a2*x**2 + a1*x + a0
      print 'Polynomial at x = 0.5 is : ', legendre(3)(0.5), 'or ', p3(0.5)
      x = np.arange(0,1,0.2) # construct various points x

      plt.figure(1)
      plt.plot(x, p3(x), lw=2)
      #plt.show()
      
   if(lpsevord):
      #=== Several Order L.P. ==#
      x = np.arange(-1,1,0.01)
      p1 = legendre(1); p2 = legendre(2); p3 = legendre(3); p4 = legendre(4); 
      p5 = legendre(5); p6 = legendre(6);

      plt.figure(2)
      plt.plot(x, p1(x), lw=2, ls='-',  color='k', label=r'$P_1$')
      plt.plot(x, p2(x), lw=2, ls='--', color='r', label=r'$P_2$')
      plt.plot(x, p3(x), lw=2, ls='-.', color='g', label=r'$P_3$')
      plt.plot(x, p4(x), lw=2, ls=':',  color='m', label=r'$P_4$')
      plt.plot(x, p5(x), lw=2, ls='-',  color='b', label=r'$P_5$')
      plt.plot(x, p6(x), lw=2, ls=':',  color='k', label=r'$P_6$')
      plt.legend(loc='best',prop={'size':12})
      plt.grid()
      plt.axis([-1, 1, -1, 1])
      plt.title('Legendre Polynomials', fontsize = 16)
      plt.xlabel('$x$', fontsize = 16)
      plt.xticks(fontsize = 14)
      plt.ylabel(r'$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n$',fontsize = 16)
      plt.yticks(fontsize = 14)
      plt.savefig('plot/04_legendre.pdf') 
      #plt.show()

if(hermit):
   #==================================================================#
   print      '~~~ HERMITE POLYNOMIAL ~~~'                            #
   #==================================================================#
   print 'H0(x)=', hermite(0), '\nH1(x)=', hermite(1)  # H0(x)=1, H1(x)=2*x
   print 'H2(x)=', hermite(2), '\nH3(x)=', hermite(3)  # H2(x)=4x^2-2, H3(x)=8x^3-12x
   x = np.arange(-10,10,0.01)
   h1 = hermite(1); h2 = hermite(2); h3 = hermite(3);  

   plt.figure(3)
   plt.plot(x, h1(x), lw=2, ls=':',  color='k', label=r'$H_1$')
   plt.plot(x, h2(x), lw=2, ls='--', color='r', label=r'$H_2$')
   plt.plot(x, h3(x), lw=2, ls='-.', color='g', label=r'$H_3$')
   plt.legend(loc='best',prop={'size':16})
   plt.grid()
   plt.axis([-10, 10, -8000, 8000])
   plt.title('Hermite Polynomials', fontsize = 16)
   plt.xlabel('$x$', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel(r'$H_n(x) = (-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2}$',fontsize = 14)
   plt.yticks(fontsize = 14)
   plt.savefig('plot/04_hermite.pdf') 
   #plt.show()

if(bessl):
   #==================================================================#
   print      '~~~ BESSEL FUNCTION ~~~'                               #
   #==================================================================#
   print 'J0(1)=', jn(0,1), '\nJ1(5 )=', jn(1,5)  # First Kind
   print 'Y0(1)=', yn(0,1), '\nY0(30)=', yn(0,30) # Second Kind
   x = np.linspace(0,20,300)
   j0 = jn(0,x); j1 = jn(1,x); y0 = yn(0,x); y1 = yn(1,x);

   plt.figure(4)
   plt.plot(x, j0, lw=2, ls=':',  color='k', label=r'$J_0$')
   plt.plot(x, j1, lw=2, ls='--', color='r', label=r'$J_1$')
   plt.plot(x, y0, lw=2, ls='-.', color='b', label=r'$Y_0$')
   plt.plot(x, y1, lw=2, ls='-',  color='g', label=r'$Y_1$')
   plt.legend(loc='best',prop={'size':16})
   plt.grid()
   plt.axis([0, 20, -1, 1])
   plt.title('Bessel Function: $1^{st}$ & $2^{nd}$ kind', fontsize = 16)
   plt.xlabel('$x$', fontsize = 16)
   plt.xticks(fontsize = 14)
   plt.ylabel(r'$J_n(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m!\Gamma(m+n+1)}(\frac{x}{2})^{2m+n}; Y_n(x) = \frac{J_n(x)[cos n\pi - (-1)^n]}{sin(n)}$',fontsize = 14)
   plt.yticks(fontsize = 14)
   plt.savefig('plot/04_bessel.pdf') 
   plt.show()

"""
Results:
~~~ LEGENDRE POLYNOMIAL ~~~
P0(x)=1, P1(x)=  x, P2(x)=1.5 x^2 - 0.5, P3(x)=2.5 x^3 - 1.5 x
Coefficients in decreasing power:  0.0 -1.5 0.0 2.5
Polynomial at x = 0.5 is :  -0.4375 or  -0.4375
~~~ HERMITE POLYNOMIAL ~~~
H0(x)=1, H1(x)=  2x, H2(x)= 4 x^2 - 2, H3(x)= 8 x^3 - 12 x
~~~ BESSEL FUNCTION ~~~
J0(1)= 0.765197686558 
J1(5 )= -0.327579137591
Y0(1)= 0.0882569642157 
Y0(30)= -0.117295731687
"""
