/* Registration: xxxx; 
   Description: Code for linear Least Square Fitting 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,i,j;
  float m,c,x[20],y[20],sx=0,sy=0,sxy=0,sxx=0;
  
  /* Input the initial guess limits */
  printf("Enter the number of inputs: ");
  scanf("%d", &n);
  printf("Enter the coordinates x[i] and y[i]: ");
  for(i=1; i<=n; i++) scanf("%f %f", &x[i], &y[i]); 

  /* Do the iteration */
  for(i=1;i<=n;i++){
     sx += x[i]; 
     sy += y[i];  
     sxy += x[i]*y[i];  
     sxx += x[i]*x[i];  
  } 
  m = (n*sxy-sx*sy)/(n*sxx-sx*sx);
  c = (sxx*sy-sx*sxy)/(n*sxx-sx*sx);
 
  /* Print the solution */
  printf("Equation is y = %f*x + %f\n", m, c);
  return 0;
}

/* Results: 
Enter the number of inputs: 10
Enter the coordinates x[i] and y[i]:
1 -0.94
2 -0.82
3 -0.72
4 -0.58
5 -0.49
6 -0.32
7 -0.21
8 -0.08
9  0.06
10 0.20

Equation is y = 0.126667*x + -1.086667 

OCTAVE VISUALIZATION
====================
data = load('input.dat');
x = data(:,1); y = data(:,2);
yy = 0.126667*x + -1.086667 
plot(x, y, 'bo'); hold on; plot(x, yy, 'r-'); hold off; xlabel('x'); ylabel('y=f(x)');
p = polyfit(x, y, 1)   % straight line i 1 is polynomial of degree 1
yprime = p(1)*x + p(2) % this can also be obtained as, yprime = polyval(p,x);
yresidue = y - yprime; % residuals
Sresidue = sum(yresidue.^2); 
Stotal   = (length(y)-1)*var(y,1);
Rsq = 1 - Sresidue/Stotal
*/
