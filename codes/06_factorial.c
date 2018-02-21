/* Regn.No.: ; Sum of factorials and various series solution.
   Goal is also to optimize the convergence of the series for higher order 
   terms without manual truncation. */

#include<stdio.h>
#include<math.h>

int main(){

 /* Simple integer switch for different problems to choose from */
 int fac=0, invfac=0, expx=0, sinx=1;

 /* Sum of factorial 1! + 2! + 3! + ... */
 if(fac){ 
   
    int n,fact=1,sum=0,i=1; 
    printf("Enter the limit of the factorial series\n");
    scanf("%d",&n);
 
    do{
      fact *= i;
      sum  += fact;
      i++;
    } while(i<=n);
 
    printf("The sum of factorial series of %d order are %d\n", n, sum);
 }

 /* Sum of inverse factorial 1/1! + 1/2! + 1/3!+ ... */
 if(invfac){ 
   
    int n, fact=1, i=1; 
    float sum=0.0;
    printf("Enter the limit of the factorial series\n");
    scanf("%d",&n);
 
    do{
      fact *= i;
      sum  += (float) 1/fact;
      i++;
    } while(i<=n);
 
    printf("The sum of factorial series of %d order are %f\n", n, sum);
 }

 /* Exponential series exp(x) = 1+ x/1! + x^2/2! + x^3/3!+ ... */
 if(expx){ 

    int   n, fact=1, i=1; 
    float x, sum=0.0, term;
    printf("Enter value of x for exp(x)\n");
    scanf("%f",&x);
 
    do{
      fact *= i;
      term  = (float) pow(x,i)/fact;
      sum  += term;
      i++;
    } while(fabs(term)>1E-4);

    sum += 1.0; /* Don't forget to add the extra 1 */ 
    printf("exp(%g) = %f & convergence took %d steps\n", x, sum, i);
 }

 /* Sine series sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... */
 if(sinx){
   
    int n=2,p,fact;
    float x,term,sum=0.0;
    printf("Enter value of x in degrees for sin(x)\n");
    scanf("%f",&x);
    x = x*M_PI/180.0; /* Convert to radian */
    term = x;

    do{
      sum += term;
      fact = n*(n+1);
      term = -term*pow(x,2)/fact;
      n   += 2;
    } while(fabs(term)>1E-4);

    printf("sin(%g) =  %f & convergence took %d steps\n", 180.0*x/M_PI, sum, n/2);
 }

 return 0;
}

/* Results */
/* Excercise : Try it for other harmonic functions and hyperbolic functions */
