"""
Registration : xxxx
Description  : Compute/Plot first 7 Legendre, Hermite polynomials and Bessel functions (1st kind)
               using recurrence relations. WARNING: Legendre (Handcoded & Scipy-library-coded)
               gives inacurate result for n > 26 (possibly) due to truncation error. 
Author       : Sutirtha Paul
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import jv

# logical case switch to choose
legendre = 0; hermite = 0; bessel = 1;

"""
Generate nth order polynomial using recursion relation nPn(x) = (2n-1)xP(n-1)(x) - (n-1)P(n-2)(x).
The function takes the order n of the required polynomial and returns the result as a poly1d object.
"""
def legendrerecur(n): 
    if (n == 0):
        Pn = [1.]
    elif (n == 1):
        Pn = [1.,0.]
    else:
        Pn_2 = legendrerecur(0)
        Pn_1 = legendrerecur(1)
        for i in range(2,n+1):
            Pn =  ((2*i - 1)*np.append(Pn_1,0) - (i-1)*np.insert(Pn_2,0,[0,0]))/i
            Pn_2 = Pn_1
            Pn_1 = Pn
    P = np.poly1d(Pn) # Convert array into poly1D object to allow natural operations with polynomials
    return P

# Recursion relation Hn(x) = 2xH(n-1)(x) - 2*(n-1)H(n-2)(x)
def hermiterecur(n):
    Hn_2 = np.array([1.])
    Hn_1 = np.array([2.,0.])
    if (n == 0):
        Hn = Hn_2
    elif (n == 1):
        Hn = Hn_1
    for i in range(2,n+1):
        Hn =  2*np.append(Hn_1,0) - 2*(i-1)*np.insert(Hn_2,0,[0,0])
        Hn_2 = Hn_1
        Hn_1 = Hn
    H = np.poly1d(Hn) 
    return H

"""
As pioneered by Miller, instead of directly implementing 3-term recurrence relation
Jv(x) = (2*(v-1)/x)J(v-1)(x) - J(v-2)(x), function uses backward recurrence to converge
on a value. Normalisation is J0 + 2J2 + 2J4 + .... = 1. 
"""
def besselrecur(n,z):
    if (z==0): return (1/np.pi)*quad(lambda x: np.cos(n*x),0,np.pi)[0] #Uses Bessel's integral to evaluate at 0
    m = n + 20                                                         #m>n; but choice of initial m is arbitrary.  
    tol = 1e-16
    J = np.zeros(m,dtype='float128')
    while True:
        Jold = J[n]
        J = np.zeros(m,dtype='float128')
        J[m-2] = 1
        norm = 0
        for i in range(m-3,-1,-1):
            J[i] = (2*(i+1)/float(z))*J[i+1] - J[i+2]
            if (i%2==0): norm += 2*J[i]
        norm -= J[0]
        J = J/norm
        m += 1
        if (abs(Jold - J[n]) < tol*abs(Jold)):
            break            
    return J[n]
vbesselrecur = np.vectorize(besselrecur,otypes=['float128'])

#Plot
if (legendre):
    lb=-1; ub=1; x = np.linspace(lb,ub,100)
    plt.figure(1)
    plt.plot(x, legendrerecur(0)(x), lw=2, ls='--', color='y', marker='^', label=r'$P_0$')
    plt.plot(x, legendrerecur(1)(x), lw=2, ls=':',  color='k', marker='d', label=r'$P_1$')
    plt.plot(x, legendrerecur(2)(x), lw=2, ls='--', color='r', marker='<', label=r'$P_2$')
    plt.plot(x, legendrerecur(3)(x), lw=2, ls='-.', color='g', marker='>', label=r'$P_3$')
    plt.plot(x, legendrerecur(4)(x), lw=2, ls=':',  color='m', marker='+', label=r'$P_4$')
    plt.plot(x, legendrerecur(5)(x), lw=2, ls='-',  color='b', marker='x', label=r'$P_5$')
    plt.plot(x, legendrerecur(6)(x), lw=2, ls=':',  color='k', marker='o', label=r'$P_6$')
    plt.legend(loc='best',prop={'size':12})
    plt.grid()
    plt.axis([lb, ub, -1.25, 1.25])
    plt.title('Legendre Polynomials', fontsize = 16)
    plt.xlabel('$x$', fontsize = 16)
    plt.ylabel(r'$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n$',fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.show()

if(hermite):
    lb=-10; ub=10; x = np.linspace(lb,ub,100)
    plt.figure(2)
    plt.plot(x, hermiterecur(0)(x), lw=2, ls='--', color='y', marker='^', label=r'$H_0$')
    plt.plot(x, hermiterecur(1)(x), lw=2, ls=':',  color='k', marker='d', label=r'$H_1$')
    plt.plot(x, hermiterecur(2)(x), lw=2, ls='--', color='r', marker='<', label=r'$H_2$')
    plt.plot(x, hermiterecur(3)(x), lw=2, ls='-.', color='g', marker='>', label=r'$H_3$')
    plt.plot(x, hermiterecur(4)(x), lw=2, ls=':',  color='m', marker='+', label=r'$H_4$')
    plt.plot(x, hermiterecur(5)(x), lw=2, ls='-',  color='b', marker='x', label=r'$H_5$')
    plt.plot(x, hermiterecur(6)(x), lw=2, ls=':',  color='k', marker='o', label=r'$H_6$')
    plt.legend(loc='best',prop={'size':12})
    plt.grid()
    plt.axis([lb, ub, -2000, 2000])
    plt.title('Hermite Polynomials', fontsize = 16)
    plt.xlabel('$x$', fontsize = 18)
    plt.xticks(fontsize = 14)
    plt.ylabel(r'$H_n(x) = (-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2}$',fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.show()

if(bessel):
    lb=-10; ub=10; x = np.arange(lb,ub,0.1)
    plt.figure(3)
    plt.plot(x, vbesselrecur(0,x), lw=2, ls='--', color='y', marker='^', label=r'$J_0$')
    plt.plot(x, vbesselrecur(1,x), lw=2, ls=':',  color='k', marker='d', label=r'$J_1$')
    plt.plot(x, vbesselrecur(2,x), lw=2, ls='--', color='r', marker='<', label=r'$J_2$')
    plt.plot(x, vbesselrecur(3,x), lw=2, ls='-.', color='g', marker='>', label=r'$J_3$')
    plt.plot(x, vbesselrecur(4,x), lw=2, ls=':',  color='m', marker='+', label=r'$J_4$')
    plt.plot(x, vbesselrecur(5,x), lw=2, ls='-',  color='b', marker='x', label=r'$J_5$')
    plt.plot(x, vbesselrecur(6,x), lw=2, ls=':',  color='k', marker='o', label=r'$J_6$')
    plt.legend(loc='best',prop={'size':12})
    plt.grid()
    plt.axis([lb, ub, -1, 1])
    plt.title('Bessel Functions of the first kind', fontsize = 16)
    plt.xlabel('$x$', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.ylabel(r'$J_n(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m!\Gamma(m+n+1)}(\frac{x}{2})^{2m+n}$',fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.show()
