"""
Registration: xxxx; 
Description: Finite Square Well (Transcendental Equation)
Author: AKB
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

def evenparity(z, z0):
    return np.tan(z) - np.sqrt((z0/z)**2 - 1)

def oddparity(z, z0):
    return 1.0/np.tan(z) + np.sqrt((z0/z)**2 - 1)

# Potential parameters; W=width, D=depth 
L = 6; V0 = 6; h_bar = 1; m = 1;

# ND parameter
z0 =  L*np.sqrt(2*m*V0)/h_bar

# Plot even-parity transcendental equation to find the intersection
z = np.linspace(0.1, 12, 10000)
plt.figure(1)
plt.plot(z, np.tan(z), '--k+', lw=.4, label="tan(z)")
plt.plot(z, np.sqrt((z0/z)**2-1), '--r.', lw=.4, label = r"$\sqrt{(\frac{z_0}{z})^2-1}$")
plt.title("Finite Square Well (Even Parity)")
plt.legend(loc='best', prop={'size':18})
plt.xlabel("z", size=16)
plt.xticks(size = 14)
plt.ylabel(r"$f(z)$", size=16)
plt.yticks(size = 14)
plt.grid(b=True, which='both', color='0.65', linestyle='-')
plt.ylim([-20, 20])
plt.tight_layout()
#plt.show()

# Plot odd-parity transcendental equation to find the intersection
plt.figure(2)
plt.plot(z, 1.0/np.tan(z), '--bx', lw=.4, label="cot(z)")
plt.plot(z, -np.sqrt(pow(z0/z,2)-1), '--g>', lw=.4, label = r"-$\sqrt{(\frac{z_0}{z})^2-1}$")
plt.title("Finite Square Well (Odd Parity)")
plt.legend(loc='best', prop={'size':18})
plt.xlabel("z", size=16)
plt.xticks(size = 14)
plt.ylabel(r"$f(z)$", size=16)
plt.yticks(size = 14)
plt.grid(b=True, which='both', color='0.65', linestyle='-')
plt.ylim([-20, 20])
plt.tight_layout()
plt.show()

# Appropriately guess the roots from graph
evenroot_guess = [1.5, 4.1, 7.1, 10.1]
oddroot_guess  = [2.5, 5.8, 8.5, 11.8]

# Compute z and check the authenticity of the roots
evenroot = opt.root(evenparity, evenroot_guess, args = (z0, ))
oddroot =  opt.root(oddparity,  oddroot_guess,  args = (z0, ))
#print evenroot.x
#print oddroot.x

# Compute energy 
print 'Energy (even) = ', (evenroot.x*h_bar)**2/(2.0*m)-V0
print 'Energy (odd)  = ', (oddroot.x *h_bar)**2/(2.0*m)-V0
