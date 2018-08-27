/* Regn.No.:xxxx
   Description: Root of a quadratic equation ax^2+bx+c=0 
   Author: AKB */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){

  /* Type Declaration */ 
  float a, b, c, root1, root2;
  float realp, imagp, discr;
  printf("Enter the values of a, b & c\n");
  scanf("%f %f %f",&a, &b, &c);

  /* If a or b or c is 0, it is not a quadratic equation, so break */
  if(a==0 || b==0 || c==0){
    printf("Error: Roots cannot be determined");
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
    else if (discr > 0){ 
      printf("Roots are real and distinct\n");
      root1 = (-b + sqrt(discr))/(2.0*a); 
      root2 = (-b - sqrt(discr))/(2.0*a); 
      printf("Root1 = %f\n",root1);
      printf("Root2 = %f\n",root2);
    }
  }
  return 0;
}

/* Results */
