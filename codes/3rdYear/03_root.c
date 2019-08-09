/* Regn.No.:xxxx-xx-xxxx
   Description: Root of a quadratic equation ax^2+bx+c=0 
   Author: AKB */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){

  /* Type Declaration */ 
  float a, b, c, root1, root2;
  float realp, imagp, discr;
  printf("Enter the values of a, b & c :\n");
  scanf("%f %f %f",&a, &b, &c);

  /* If a or b or c is 0, it is not a quadratic equation, so break */
  if(a==0){
    printf("Error: Roots cannot be determined\n");
    exit(1);
  }
  else{
    discr = pow(b,2) - 4.0*a*c;
    if(discr < 0){
      printf("Imaginary roots\n");
      realp = -b/(2.0*a);
      imagp = sqrt(abs(discr))/(2.0*a);
      printf("Root1 = %f + i%f\n",realp,imagp);
      printf("Root2 = %f - i%f\n",realp,imagp);
    }
    else if (discr == 0){
      printf("Roots are real and equal\n");
      root1 = -b/(2.0*a); 
      printf("Root1 = %f\n",root1);
      printf("Root2 = %f\n",root1);
    }
    else{ 
      printf("Roots are real and distinct\n");
      root1 = (-b + sqrt(discr))/(2.0*a); 
      root2 = (-b - sqrt(discr))/(2.0*a); 
      printf("Root1 = %f\n",root1);
      printf("Root2 = %f\n",root2);
    }
  }
  return 0;
}

/* Results
   Enter the values of a, b & c : 0 1 2
   Error: Roots cannot be determined

   Enter the values of a, b & c : 1 3 6
   Imaginary roots
   Root1 = -1.500000 + i1.936492
   Root2 = -1.500000 - i1.936492
   
   Enter the values of a, b & c : 1 2 1
   Roots are real and equal
   Root1 = -1.000000
   Root2 = -1.000000

   Enter the values of a, b & c : 1 6 2       
   Roots are real and distinct
   Root1 = -0.354249
   Root2 = -5.645751

   Exercise: Check cancellation error and construction of root using root1*root2 = c/a, 
   when discriminant >>> 0. */
