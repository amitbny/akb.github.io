/* Registration: xxxx; 
   Description: Lagrange Interpolation Method 
   Author: AKB */

#include<stdio.h>
int main(){

  /* Type declaration */ 
  float x[10],y[10],a,s=1,t=1,k=0;
  int n,i,j,d=1;

  /* Enter the table y = f(x) and give x */ 
  printf("Enter the number of terms in the table: ");
  scanf("%d",&n);
  printf("Enter the values of the variables x and y: \n");
  for(i=0; i<n; i++) scanf("%f %f",&x[i], &y[i]);
  printf("Enter the value of x: \n");
  scanf("%f",&a);
  
  /* Do the interpolation & print the results */
  for(i=0; i<n; i++){
    s=1; t=1;
    for(j=0; j<n; j++){
       if(j!=i){
         s = s*(a-x[j]);
         t = t*(x[i]-x[j]); 
       }
    }
    k += (s/t)*y[i];
  }
  printf("Corresponding value of the variable y is: %g\n", k);
  
  return 0;
}

/* Results :
Enter the number of terms in the table: 6
Enter the values of the variables x and y: 
0.1 0.545
0.2 0.331
0.3 0.275
0.4 0.258
0.5 0.240
0.6 0.235
Enter the value of x: 0.25
Corresponding value of the variable y is: 0.292832
*/
