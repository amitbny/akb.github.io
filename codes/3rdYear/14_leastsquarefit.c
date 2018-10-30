/* Registration: xxxx; 
   Description: Code for fitting exponential using Least Square Fitting 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,i,j;
  float a,b,x[20],y[20],sx=0,sy=0,sxy=0,sxx=0,a1,b1;
  
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
  a = (n*sxy-sx*sy)/(n*sxx-sx*sx);
  b = (sxx*sy-sx*sxy)/(n*sxx-sx*sx);
  b1 = a;
  a1 = exp(b); 
 
  /* Print the solution */
  printf("Multiplier is a=%f\n", a1);
  printf("Power is b=%f\n", b1);
  return 0;
}

/* Results: 
Enter the number of inputs: 10
Enter the coordinates x[i] and y[i]:
.25 3.1
.5 1.7
.75 1
1 .68
1.25 .42
1.5 .26
1.75 .14
2 .09
2.25 .04
2.5 .03
Multiplier is a=5.144139
Power is b=-2.066639
*/
