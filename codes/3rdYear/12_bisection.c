/* Registration: xxxx; 
   Description: To find roots of an equation by Bisection method
   Author: AKB */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float f(float x){
    return pow(x,2)-4;
    //return pow(x,3)-5.816*pow(x,2)+9.632*x-7.632;  /*    0 < x < 5;   Root = 3.815994 */ 
    //return 20-2.5*x-0.01*pow(x,3);                 /*    0 < x < 10;  Root = 6.762772 */ 
    //return pow(x+5,2) + 10*x - 11;                 /* -1.5 < x < 0;   Root = -0.726471 */ 
    //return pow(cos(x),2)-5.6*pow(x,2)+x+20;        /*    1 < x < 2.5; Root = 1.989044 */ 
    //return 3*sin(x)-3.5-5*cos(x);                  /*    3 < x < 4;   Root = 3.528137 */ 
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
  do{
     x2 = (x0+x1)/2.0;  
     if(f(x2)*f(x0)>0)
       x0 = x2;
     else
       x1 = x2;
     i++;
  } while(fabs(x1-x0)>1E-4);
   
  /* Print the solution */
  printf("Root is : %f\n", x2);
  printf("number of iterations : %d\n", i);
  return 0;
}

/* Results: 
Enter the initial guess points: 1.5 2.5
Root is: __, number of iterations: __

Enter the initial guess points: -1.5 -3.5
Root is __, number of iterations __ */
