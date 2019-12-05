/* Registration: xxxx; 
   Description: Code for fitting exponential using Least Square Fitting 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,i,j;
  float a,b,x[20],y[20],sx=0,sy=0,sxy=0,sxx=0;
  
  /* Input the initial guess limits */
  printf("Enter the number of inputs: ");
  scanf("%d", &n);
  printf("Enter the coordinates x[i] and y[i]: ");
  for(i=1; i<=n; i++) scanf("%f %f", &x[i], &y[i]); 

  /* Do the iteration */
  for(i=1;i<=n;i++){
     sx += x[i]; 
     sy += log(y[i]);  
     sxy += x[i]*log(y[i]);  
     sxx += x[i]*x[i];  
  } 
  a = (sxx*sy-sx*sxy)/(n*sxx-sx*sx);
  b = (n*sxy-sx*sy)/(n*sxx-sx*sx);
 
  /* Print the solution */
  printf("Equation is y = %f*x^%f\n", exp(a), b);
  return 0;
}

/* Results: 
Enter the number of inputs: 10
Enter the coordinates x[i] and y[i]:
0.25 3.1
0.5  1.7
0.75 1.0
1.0  0.68
1.25 0.42
1.5  0.26
1.75 0.14
2.0  0.09
2.25 0.04
2.5  0.03

Equation is y = 5.144139*x.^-2.066639

OCTAVE VISUALIZATION
====================
data = load('input.dat');
x = data(:,1); y = data(:,2);
yy = 5.144139*x^(-2.066639);
clf; plot(x, y, 'bo'); hold on; plot(x, yy, 'r-'); hold off; xlabel('x'); ylabel('y=f(x)');
p = polyfit(x, y, 1)   % straight line i 1 is polynomial of degree 1
yprime = p(1)*x + p(2) % this can also be obtained as, yprime = polyval(p,x);
yresidue = y - yprime; % residuals
Sresidue = sum(yresidue.^2); 
Stotal   = (length(y)-1)*var(y,1);
Rsq = 1 - Sresidue/Stotal
*/
