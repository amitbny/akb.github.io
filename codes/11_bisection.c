/* Registration: xxxx; Code for finding roots of an equation by Bisection method */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float f(float x){
    return pow(x,2)-4;
}

int main(){

  /* Type declaration */
  int i=0;
  float x0,x1,x2;
  
  /* Input the initial guess limits */
  printf("Enter the initial guess points: ");
  scanf("%f %f", &x0, &x1);
 
  if(f(x0)*f(x1)>0){
    printf("The interval does not contain the root");
    exit(1); 
  } 

  /* Do the iteration */
  while(fabs(x1-x0)>1E-4){
     x2 = (x0+x1)/2.0;  
     if(f(x2)*f(x0)>0)
       x0 = x2;
     else
       x1 = x2;
     i++;
  } 
   
  /* Print the solution */
  printf("Root is %f\n", x2);
  printf("number of iterations %d\n", i);
  return 0;
}

/* Results: 
Enter the initial guess points: 1.5 2.5
Root is xx, number of iterations xx

Enter the initial guess points: -1.5 -3.5
Root is xx, number of iterations xx
*/
