/* Registration: xxxx; 
   Description: Code for Integration by Simpson's 1/3 Rule 
   Author: AKB */

#include<stdio.h>
#include<math.h>

float f(float x){
    return exp(-pow(x,2))*sin(x);
    //return sqrt(x)*exp(x);
    //return sqrt(1-pow(x,2))*cos(x);
}

int main(){

  /* Type declaration */
  int i=2,j; 
  float a,b,h,s1,s2=0.0,s4,I0,I1,x;
  
  /* Enter the integration limits */
  printf("Enter the lower and upper multiplier of Pi:\n ");
  scanf("%f %f", &a, &b);
  a *= M_PI; b *= M_PI;

  /* Compute I0 */
  h  = (b - a)*0.5; 
  s1 = f(a) + f(b);
  s4 = f(a + h);
  I0 = (h/3.0)*(s1 + 4.0*s4);

  /* Do the integral */
  do{
    x   = a + h * 0.5;
    s2 += s4;
    s4  = 0.0;
    for(j=1; j<=i; j++){
       s4 += f(x);
        x += h;
        //printf("x=%f i=%d h=%f s2=%f s4=%f\n",x,i,h,s2,s4); /* check what's happening */
    } 
    h *= 0.5; 
    i *= 2; 
    I1 = I0;    
    I0 = (s1 + 2.0*s2 + 4.0*s4)*h/3.0;
  } while(fabs((I1-I0)/I1)>1E-4);

  /* Print the solution */
  printf("Number of iterations : %d\n", i/2);
  printf("integral_%g^%g sqrt(1-x^2)*cos(x) dx = %f\n", a*M_PI, b*M_PI, I1);

return 0;
}

/* Results: 
integral_0^pi      e^(-x^2)sin(x) dx =  0.424441, # of iterations = 32 
integral_0^pi       sqrt(x)exp(x) dx = 32.828758, # of iterations = 32
integral_0^pi/4 sqrt(1-x^2)cos(x) dx =  0.632993, # of iterations = 4
*/
