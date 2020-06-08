"""
Registration: xxxx; 
Description: Finite Square Well (Eigenfunctions & Eigenenergies by Direct Matrix Method)
Author: AKB
"""
import numpy as np
from scipy.linalg import eigh 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
  
def finite_well_input(W=None,D=None):
    W=float(raw_input('\nEnter width of well.\n\tSelect a value between 1.0 and 15. '))
    D=-float(raw_input('Enter depth of well.\n\tSelect a value between 20 and 500. '))
    return W,D
    
def finite_well_plot(E,V,xvec,steps,n,U):
    V_new,ScaleFactor,U_new,n=finite_well_plot_scaling(E,V,xvec,U,n,steps)
    f = plt.figure()
    ax = f.add_subplot(111)
    # plot potential
    ax.plot(xvec,U_new,c='lightslategray')

    # find appropriate x limits and set x limit
    MinX=0
    MaxX=len(xvec)-1
    while U_new[MinX]==0:
        MinX = MinX+1
    while U_new[MaxX]==0:
        MaxX = MaxX-1
    for m in range(n):
        V_old = V_new[MinX+1,m]
        while(np.abs(V_old - V_new[MinX,m])>1e-6 and MinX>0):
            V_old=V_new[MinX,m]
            MinX=MinX-1
        V_old=V_new[MaxX-1,m]
        while(np.abs(V_old - V_new[MaxX,m])>1e-6 and MaxX<len(xvec)-1):
            V_old=V_new[MaxX,m]
            MaxX=MaxX+1
    plt.xlim(xvec[MinX],xvec[MaxX])

    # find appropriate y limits and set y limit
    if(np.max(V_new)>0):
        if(np.min(V_new)>np.min(U_new)):
            plt.ylim(1.05*np.min(U_new),np.max(V_new)+abs(0.05*np.min(U_new)))
        else:
            plt.ylim(1.05*np.min(V_new),np.max(V_new)+abs(0.05*np.min(U_new)))
    else:
        if(np.min(V_new)>np.min(U_new)):
            plt.ylim(1.05*np.min(U_new),np.max(U_new)+abs(0.05*np.min(U_new)))
        else:
            plt.ylim(1.05*np.min(V_new),np.max(U_new)+abs(0.05*np.min(U_new)))

    #plot wave functions
    for i in np.arange(n-1,-1,-1):
        color=mpl.cm.jet_r((i)/(float)(n),1)
        wavefunc=ax.plot(xvec,V_new[0:steps,i],c=color,label='E(a.u.)={}'.format(np.round(E[i]*1000)/1000.0))
        ax.axhline(y=V_new[0,i],xmin=-10,xmax=10,c=color,ls='--')
    plt.title('Particle in a Finite Well')
    plt.xlabel('Width of Well (in a.u.)')
    plt.ylabel('Energy (in a.u.)')
    plt.legend(loc='best', prop={'size':18})
    ax.set_yticklabels(np.round(ax.yaxis.get_ticklocs()*ScaleFactor))
    box=ax.get_position()
    ax.set_position([box.x0,box.y0,0.7*box.width,box.height])
    plt.show()

def finite_well_plot_scaling(E,V,xvec,U,n,steps):
    # scale the wave functions
    order=np.argsort(E)
    Converged=False
    while(Converged is False):
        E_copy=E[0:n]
        V_copy=V[0:steps,order]
        V_copy=V[0:steps,0:n]
        max_E_diff = E_copy[n-1] - E_copy[0]
        found_step = False
        step = 1
        while found_step is False:
            if(E_copy[step]-E_copy[0]<0.2):
                step+=1
            else:
                found_step = True
        ScaleFactorStep=0.05
        ScaleFactor=1.00
        Overlap=1
        while(Overlap==1):
            for i in range(0,n,step):
                MaxV2=np.max(V_copy[0:steps,i])+E_copy[i]/ScaleFactor
                MinV2=np.min(V_copy[0:steps,i])+E_copy[i]/ScaleFactor
                MaxV1=np.max(V_copy[0:steps,i-step])+E_copy[i-step]/ScaleFactor
                if((MaxV2-MinV2)<(np.abs(MinV2-MaxV1)*10)):
                    Overlap=1
                else:
                    Overlap=0
                    break
            ScaleFactor=ScaleFactor+ScaleFactorStep
        V_copy_new=(E_copy/ScaleFactor)+V_copy
        if np.max(V_copy_new[n])>0:
            Converged=True
            n=n-1
        else:
            n=n+1
        V_copy_old=V_copy_new
    V_new=V_copy_old
    U_new=U/ScaleFactor
    return V_new,ScaleFactor,U_new,n

# Particle in a finite well of width W and depth D
steps=2000
hbar = m = 1.0              # atomic units
A, D = finite_well_input()  # get well depth and width
W = A/2.0                   # well [-W  W] is input width
steps = 2000
x = np.linspace(-A,A,steps)
h = x[1] - x[0]             # step size
U = D*(0.5*(1+np.sign(x+W))-0.5*(1+np.sign(x-W)))         # create the potential from step function
Laplacian = (-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
            + np.diag(np.ones(steps-1),-1))/(float)(h**2) # central difference Laplacian 
Hamiltonian = np.zeros((steps,steps))                     # create Hamiltonian
[i, j] = np.indices(Hamiltonian.shape)
Hamiltonian[i==j] = U
Hamiltonian += (-0.5)*((hbar**2)/m)*Laplacian
E, V = eigh(Hamiltonian)  # diagonalize the Hamiltonian to get wavefunctions and energies
n = 0                          # determine number of energy levels to plot (n)
while E[n]<0:
      n+=1
finite_well_plot(E,V,x,steps,n,U)                              # create plot
