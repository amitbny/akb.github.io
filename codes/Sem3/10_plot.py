"""
Registration : xxxx
Description  : 2D/3D Plot
Author       : AKB
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Logical case switch for different problems to choose from 
cont2D=1; surf3D=1; param3D=1; 

if(cont2D):
   #=========================================================================#
   print      '~~~ 2D CONTOUR & COLOUR PLOT ~~~'                             #
   #=========================================================================#

   x = np.linspace(0, 10, 100) 
   y = np.linspace(0, 10, 100)
   X, Y = np.meshgrid(x, y)    # prepare XY-grid

   plt.subplot(2,2,1)
   plt.plot(X, Y, '.', ms=1, c='b') # plot XY-grid
   plt.title('X-Y Grid', size=14)
   plt.xlabel('x', size = 14)
   plt.xticks(size = 14)
   plt.ylabel('y', size = 14)
   plt.yticks(size = 14)
   #plt.show()       

   func1 = 1; func2 = 0; # choose desired function to plot
   def f(x,y):
       if(func1): return np.sin(X)**2 + np.cos(Y)**2
       if(func2): return np.sin(X)**3 + np.cos(Y)*np.sin(X)

   Z = f(X,Y)

   plt.subplot(2,2,2)
   plt.contour(X, Y, Z, 20, cmap='binary')  # draw contours
   plt.pcolor(X, Y, Z,      cmap='rainbow') # color values
   plt.colorbar()
   if(func1): plt.title(r'$z = sin^2(x) + cos^2(y)$',     size = 14)
   if(func2): plt.title(r'$z = sin^3(x) + sin(x)cos(y)$', size = 14)
   plt.xlabel('x', size = 14)
   plt.xticks(size = 14)
   plt.ylabel('y', size = 14)
   plt.yticks(size = 14)
   #plt.show()       

if(surf3D):
   #=========================================================================#
   print                '~~~~ 3D SURFACE PLOT ~~~~'                          #
   #=========================================================================#
   from mpl_toolkits import mplot3d

   x = np.linspace(-10, 10, 100) 
   y = np.linspace(-10, 10, 100)
   X, Y = np.meshgrid(x, y)   # prepare XY-grid  

   func3 = 1; func4 = 0; func5 = 0; # choose desired function to plot
   def f(x,y):
       if(func3): return np.sin(np.sqrt(X**2 + Y**2))
       if(func4): return np.sin(X)**2 + np.cos(Y)**2
       if(func5): return np.sin(X)**3 + np.cos(Y)*np.sin(X)

   Z = f(X,Y)
   
   fig = plt.figure(1)
   #ax = fig.gca(projection='3d')
   ax = fig.add_subplot(223, projection = '3d')
   ax.contour3D(X,Y,Z,100,cmap='rainbow')
   plt.colorbar()
   if(func3): plt.title(r'$sin(\sqrt{x^2+y^2})$',   size = 14)
   if(func4): plt.title(r'$sin(x)^2+cos(y)^2$',     size = 14)
   if(func5): plt.title(r'$sin(x)^3+cos(y)sin(x)$', size = 14)
   #plt.show()             

if(param3D):
   #=========================================================================#
   print           '~~~ 3D PARAMETRIC PLOT ~~~'                              #
   #=========================================================================#
   # This import registers the 3D projection, but is otherwise unused.
   from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

   fig = plt.figure(1)
   #ax = fig.gca(projection='3d')
   ax = fig.add_subplot(224, projection = '3d')

   # Prepare arrays x, y, z
   theta = np.linspace(-4*np.pi, 4*np.pi, 100)
   z = np.linspace(-2, 2, 100)
   r = z**2 + 1
   x = r*np.sin(theta)
   y = r*np.cos(theta)

   ax.plot(x, y, z, color='red')
   plt.title(r'$x^2+y^2 = (z^2+1)^2$',     size = 14)
   plt.xlabel(r'$x = (z^2+1)sin(\theta)$', size = 14)
   plt.ylabel(r'$y = (z^2+1)cos(\theta)$', size = 14)   
   ax.legend()
   plt.savefig('plot/10_surf.pdf') 
   plt.show()

# colormaps : 'viridis','plasma','inferno','magma','Accent','Blues','BrBG','BuGn',
   #             'BuPu','CMRmap','Dark2','GnBu','Greens','Greys','OrRd','Oranges','PRGn',  
   #             'Paired','Pastel1','Pastel2','PiYG','PuBu','PuBuGn','PuOr','PuRd',
   #             'Purples','RdBu','RdGy','RdPu','RdYlBu','RdYlGn','Reds','Set1','Set2',
   #             'Set3','Spectral','Wistia','YlGn','YlGnBu','YlOrBr','YlOrRd','afmhot',
   #             'autumn','binary','bone','brg','bwr','cool','coolwarm','copper','cubehelix',
   #             'flag','gist_earth','gist_gray','gist_heat','gist_ncar','gist_rainbow','gist_stern',
   #             'gist_yarg','gnuplot','gnuplot2','gray','hot','hsv','jet','nipy_spectral','ocean',
   #             'pink','prism','rainbow','seismic','spectral','spring','summer','terrain','winter'
