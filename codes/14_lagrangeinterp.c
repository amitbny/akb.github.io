/* Registration: xxxx; Lagrange Interpolation Method */

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
    k = k + ((s/t)*y[i]);
  }
  printf("Corresponding value of the variable y is: %g\n", k);
  
  return 0;
}

/* Results */
