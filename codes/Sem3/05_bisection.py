"""
Registration: xxxx; 
Description: To find roots of an equation by Bisection method
Author: AKB
"""
import numpy as np

# Define a function to call
def f(x):
    return pow(x,2)-4.0;                            # -3.5 < x < -1.5;Root = -2.00006103516
    #return pow(x,3)-5.816*pow(x,2)+9.632*x-7.632;  #    0 < x < 5;   Root = 3.8159942627  
    #return 20-2.5*x-0.01*pow(x,3);                 #    0 < x < 10;  Root = 6.76277160645  
    #return pow(x+5,2) + 10*x - 11;                 # -1.5 < x < 0;   Root = -0.726470947266 
    #return pow(np.cos(x),2)-5.6*pow(x,2)+x+20;     #    1 < x < 2.5; Root = 1.98904418945  
    #return 3*np.sin(x)-3.5-5*np.cos(x);            #    3 < x < 4;   Root = 3.52813720703 

# Main function
tol = 1E-4   # Tolerance
x0,x1 = input('Enter the initial guess points: ') 

# Check if there exists a root, else break the code  
if f(x0)*f(x1)>0:
    print 'The interval does not contain the root'
    exit(1)
    
# Main iteration
iter=0
while(abs(x1-x0)>tol): 
    x2 = (x0+x1)/2.0  
    if f(x2)*f(x0)>0:
       x0 = x2
    else:
       x1 = x2
    iter += 1
   
# Print the solution
print 'Root is', x2, 'and number of iterations is', iter

"""
Results: 
Enter the initial guess points: 1.5,2.5
Root is 1.99993896484 and number of iterations is 14

Enter the initial guess points: -1.5,-3.5
Root is -2.00006103516 and number of iterations is 14
"""
