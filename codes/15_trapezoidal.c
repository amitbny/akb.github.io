/* Registration: xxxx; Integration by Trapezoidal Method 
   int_(a*Pi)^(b*Pi) f(x)dx = 1/2*h*[ (y_a + y_b) + 2*(y_1+y_2+...+y_{n-1}) ] 
                              OR optimize the last part. */

#include<stdio.h>
#include<math.h>

float f(float x){
    return sqrt(1-pow(x,2))*cos(x);
}

int main(){

  /* Type declaration */ 
  int i=1,j;
  float a,b,h,s1,I0,I1,x=0.0;

  /* Enter the integration limits */
  printf("Enter the lower and upper multiplier of Pi:\n ");
  scanf("%f %f",&a, &b);
  a *= M_PI; b *= M_PI;
 
  /* Compute 1/2*h*(y_a + y_b) */ 
  h  = b - a; 
  s1 = (f(a) + f(b))*0.5;
  I1 = h*s1;

  /* (i) We reach to h/2 & add f(x), (ii) h/4 it, compare error & add 4 f(x), 
     h/8 it, compare error & add 8 f(x), h/16 it, compare error & add 8 f(x) & so on .... */
  do{
    x = a + h/2;
    for(j=1; j<=i; j++){
       s1 += f(x); 
       x  += h;
       //printf("x=%f i=%d h=%f\n",x,i,h); /* check what's happening */
    }
    i *= 2;
    h  = h/2.0;
    I0 = I1;
    I1 = h*s1;
  } while(fabs(I1-I0)>1.0E-4); 

  printf("Number of iterations : %d\n", i);
  printf("integral_%g^%g sqrt(1-x^2)*cos(x) dx = %f\n", a*M_PI, b*M_PI, I1);
  return 0;
}

/* Results 
Enter the lower and upper multiplier of Pi: 0 0.25
Number of iterations : 64
integral_0^2.4674 sqrt(1-x^2)*cos(x) dx = 0.632995
*/
