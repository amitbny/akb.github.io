"""
Registration : xxxx
Description  : Generating Random Numbers & Histogram 
Author       : AKB
"""

import numpy as np
import scipy.special as sps      # To use Gamma function
from scipy.special import factorial
import matplotlib.pyplot as plt
from collections import Counter  # Counter counts how many times a number appears in Histogram
import warnings
warnings.filterwarnings("ignore")

# ============================ #
# Generation of Random Numbers #
# ============================ #

#a = np.random.rand(1000,5); print a; plt.hist(a); plt.show()  # Uniform distribution

#a = np.random.random(size=1000); print a; plt.hist(a); plt.show() # Uniform distribution within half-open interval [0.0,1.0) {include 0, exclude 1}
#a = np.random.ranf(size=1000); print a; plt.hist(a); plt.show()  # Uniform distribution within half-open interval [0,1) {include 0, exclude 1}
#a = np.random.sample(size=1000); print a; plt.hist(a); plt.show()  # Uniform distribution within half-open interval [0,1) {include 0, exclude 1}

#a = np.random.randn(20,1); print a; plt.hist(a); plt.show()  # Normal distribution 

#a = np.random.randint(1,10,size=(1000,2)); print a; plt.hist(a); plt.show() # Integers from Uniform distribution within [1,10]

# Random Permutations
#a = np.arange(10); np.random.shuffle(a); print a;
#a = np.random.permutation(10); print a;


# ============= #
# Distributions #
# ============= #

# Chi Square Distribution
df, npts, nbin = 20, 4000, 40  # Independent Normal Distributed (mu=0,sig=1) Random Variables, Number of Points and bin  
N = np.random.chisquare(df, npts);
plt.figure(1);
plt.subplot(2,3,1)
nn, bins, patches = plt.hist(N, nbin, density=True, color='darkorange', edgecolor='teal', label=r'$N=$'+str(N.size));
plt.legend(loc='best',prop={'size':16})
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)]); plt.xlabel('x', size=16); plt.xticks(size=16)
plt.ylabel('$P(x)$', size=16); plt.yticks(size=16); #plt.show()

# Binomial Distribution (Discrete)
n, p = 10, 0.5  # Total Number of Trials & Success Probability
npts, nbin = 2000, 20
N = np.random.binomial(n, p, npts);
plt.figure(1);
plt.subplot(2,3,2)
nn, bins, patches = plt.hist(N, nbin, density=True, color='seagreen', edgecolor='slategray', label=r'$N=$'+str(N.size));
plt.plot(bins, factorial(n,exact=False)/(factorial(bins,exact=False)*factorial(n-bins,exact=False))*pow(p,bins)*pow(1-p,n-bins),
         linewidth=2, color='k', label=r'$P(x) = \frac{n!}{k!(n-k)!}p^k (1-p)^{n-k}$')
plt.legend(loc='best',prop={'size':16})
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)]); plt.xlabel('x', size=16); plt.xticks(size=16)
plt.ylabel('$P(x)$', size=16); plt.yticks(size=16); #plt.show()


# Exponential Distribution
scale, size, nbin = 1.0, 1000, 20  # Scale Parameter (inverse of Rate Parameter), size and how many bins  
N = np.random.exponential(scale, size);
plt.figure(1);
plt.subplot(2,3,3)
n, bins, patches = plt.hist(N, nbin, density=True, color='chocolate', edgecolor='maroon', label=r'$N=$'+str(N.size));
plt.plot(bins, 1/scale*np.exp(-bins/scale), linewidth=2, color='k', label=r'$P(x) = \frac{1}{\beta}e^{-x/\beta}$')
plt.legend(loc='best',prop={'size':16})
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)]); plt.xlabel('x', size=16); plt.xticks(size=16)
plt.ylabel('$P(x)$', size=16); plt.yticks(size=16) #plt.show()


# Gamma Distribution
k, theta, npts, nbin = 2.0, 2.0, 5000, 50  
N = np.random.gamma(k, theta, npts);
plt.figure(1);
plt.subplot(2,3,4)
count, bins, ignored = plt.hist(N, nbin, density=True, color='skyblue', edgecolor='blue', label=r'$N=$'+str(N.size))  
plt.plot(bins, bins**(k-1)*(np.exp(-bins/theta)/(sps.gamma(k)*theta**k)), linewidth=2, color='k',
         label=r'$P(x) = x^{k-1} \frac{e^{-x/\theta}}{\theta^k \Gamma(k)}$')
plt.legend(loc='best',prop={'size':16})
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)]); plt.xlabel('x', size=16); plt.xticks(size=16)
plt.ylabel('$P(x)$', size=16); plt.yticks(size=16); #plt.show() 


# Gaussian Distribution
npts, nbin = 6000, 40; # Total Number of Points & Bins
mu, sigma = 0.0, 10;  # Mean & Standard Deviation of PDF
x = np.random.normal(mu, sigma, npts);
plt.figure(1);
plt.subplot(2,3,5)
n, bins, patches = plt.hist(x, nbin, density=True, color='tan', edgecolor='brown', label=r'$N=$'+str(npts))
plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)),
         linewidth=2, color='k',label=r'$P(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{(x-\mu)^2/{2\sigma^2}}$') 
plt.legend(loc='best',prop={'size':16})
plt.title(r'$\mu='+str(mu)+',\ \sigma='+str(sigma)+'$', size=16)
plt.grid(axis='y', alpha=0.75)
plt.xlim([min(bins), max(bins)]); plt.xlabel('x', size=16); plt.xticks(size=16)
plt.ylabel('$P(x)$', size=16); plt.yticks(size=16)
plt.show()

