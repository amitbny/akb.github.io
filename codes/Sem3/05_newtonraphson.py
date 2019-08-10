"""
Registration: xxxx; 
Description: To find roots of an equation by Newton-Raphson method 
Author: AKB
"""

# Define a function 
def f(x):
    return pow(x,2)-25;
    #return pow(x,2)*log(x)-5.72;
    #return pow(x,2)-2*exp(-x);

# Define derivative of respective function 
def df(x):
    return 2*x;
    #return x*(log(pow(x,2))+1);
    #return 2*(x + exp(-x));

# Main function
tol = 1E-4   # Tolerance
x0 = input('Enter the initial guess x0: ')
  
# Main iteration
iter=0
x1 = x0-f(x0)/df(x0)
error=x1-x0

while(abs(error)>tol):   
    x1 = x0-f(x0)/df(x0);
    error = x1-x0;
    x0 = x1;
    iter+=1
  
# Print the solution 
print 'Root is ', x1, 'and ', iter, 'steps are taken to reach from initial guess\n'

"""
Results:
Enter the initial guess x0: 0.01
Root is  5.0 and  13 steps are taken to reach from initial guess

Enter the initial guess x0: -0.01
Root is  -5.0 and  13 steps are taken to reach from initial guess
"""
