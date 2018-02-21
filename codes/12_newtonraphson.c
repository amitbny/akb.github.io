/* Registration: xxxx; Code for finding roots of an equation by Newton-Raphson method */

#include<stdio.h>
#include<math.h>

float f(float x){
    return pow(x,2)-25;
}

float df(float x){
    return 2*x;
}

int main(){

  /* Type declaration */
  float x0, x1, t;
  int steps;
  
  /* Input the initial guess */
  printf("Enter the initial guess x0: ");
  scanf("%f", &x0);
  
  /* Do the iteration */
  do{
    x1 = x0-f(x0)/df(x0);
    t = x1-x0;
    x0 = x1;
    steps++;
  } while(fabs(t)>1E-4);
   
  /* Print the solution */
  printf("Root is %f and %d steps is taken to reach from initial guess\n", x1, steps);
  return 0;
}

/* Results: Check for x0=4.99 (Root 5) and x0=-3.5 (Root -5) and 
   test for different absolute error */
