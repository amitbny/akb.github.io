/* Registration: xxxx; Code for Integration by Simpson's 1/3 Rule */

#include<stdio.h>
#include<math.h>
float f(float x){
    return exp(-pow(x,2))*sin(x);
}

int main(){

  /* Type declaration */
  int i=2,j; 
  float x1,x2,s1,s2,s4,I0,I1,h,x;
  
  /* Input the limits: \int_0^1 e^(-x^2)sin(x) = 0.424499 */
  printf("Enter the upper and lower multiplier of limits: ");
  scanf("%f %f",&x2, &x1);
  x2 = M_PI*x2;
  h = (x2-x1)/2.0; 
  s1 = f(x1)+f(x2);
  s2 = 0;
  s4 = f(x1+h);
  I0 = (h/3)*(s1+4*s4);

  /* Do the integral */
  do{
    s2 += s4;
    s4 = 0.0;
    x = x1 + h/2.0;
    for(j=1; j<=i; j++){
       s4 += f(x);
       x += h;
    } 
    h = h/2.0; i = 2*i; I1 = I0;    
    I0 = (s1+2*s2+4*s4)*h/3.0;
  } while(fabs((I1-I0)/I1)>1E-3);
   
  /* Print the solution */
  printf("Result is %f", I1);
  return 0;
}

/* Results: */
