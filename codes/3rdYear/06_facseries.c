/* Regn.No.: xxxx; 
   Description: Sum of factorials and various series solution.
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

 /* Integer case switch for different problems to choose from */
 int series1=1, series2=0, series3=0, series4=0; 
 int series5=0, series6=0, series7=0, series8=0, series9=0;

 /* Sum of factorial 1! + 2! + 3! + ... */
 if(series1){ 
   
    int n,fact=1,sum=0,i=1; 
    printf("Enter the limit of the factorial series\n");
    scanf("%d",&n);
 
    do{
      fact *= i;
      sum  += fact;
      i++;
    } while(i<=n);
 
    printf("The Sum of factorial series upto %d! is %d\n", n, sum);
 }

 /* Sum of inverse factorial 1/1! + 1/2! + 1/3!+ ... */
 else if(series2){ 
   
    int n, fact=1, i=1; 
    float sum=0.0;
    printf("Enter the limit of the factorial series\n");
    scanf("%d",&n);
 
    do{
      fact *= i;
      sum  += (float) 1/fact;
      i++;
    } while(i<=n);
 
    printf("The sum of inverse factorial series upto %d! is %f\n", n, sum);
 }

 /* Exponential series exp(x) = 1+ x/1! + x^2/2! + x^3/3!+ ... */
 else if(series3){ 

    int   fact=1, i=1; 
    float x,term,sum=0.0;
    printf("Enter value of x for exp(x)\n");
    scanf("%f",&x);
 
    do{
      fact *= i;
      term  = (float) pow(x,i)/fact;
      sum  += term;
      //printf("fact=%d, term=%f, sum=%f\n",fact, term, sum);
      i++;
    } while(fabs(term)>1E-4);

    sum += 1.0; /* Don't forget to add the extra 1 */ 
    printf("exp(%g) = %f & convergence took %d steps\n", x, sum, i-1);
 }

 /* Sine series sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... */
 else if(series4){
   
    int n=2,fact;
    float x,term,sum=0.0;
    printf("Enter value of x in degrees for sin(x)\n");
    scanf("%f",&x);
    x = x*M_PI/180.0; /* Convert to radian */
    term = x;

    do{
      sum += term;
      fact = n*(n+1);
      term = -term*pow(x,2)/fact;
      //printf("n=%d, fact=%d, term=%f, sum=%f\n",n, fact, term, sum);
      n   += 2;
    } while(fabs(term)>1E-4);

    printf("sin(%g) =  %f & convergence took %d steps\n", 180.0*x/M_PI, sum, n/2);
 }

 /* Sum of series 1 - 1/3^3 + 1/5^3 - 1/7^3 + ... = pi^3/32 */
 else if(series5){

    int i=1, c=0; 
    float sum=0.0, term, theo=pow(M_PI,3)/32.0;
 
    do{
      term = (float) pow(-1,c)/pow(i,3);
      sum  += term;
      //printf("i=%d term=%f sum=%f c=%d\n", i, term, theo-sum, c); 
      i    += 2; 
      c++;
    } while(fabs(theo-sum)>=1E-5);
    
    printf("1/1^3 - 1/2^2 + 1/3^2 - 1/4^2 + ... =  %f, pi^2/12 = %f & convergence took %d steps\n", sum, theo, i/2);
 
 }

 /* Sum of inverse n-square 1/1^2 + 1/2^2 + 1/3^2+ ... = pi^2/6 */
 else if(series6){ 
   
    int i=1; 
    float sum=0.0, term, theo=pow(M_PI,2)/6.0;
 
    do{
      term  = (float) 1/pow(i,2);
      sum  += term; 
      //printf("i=%d term=%f sum=%f \n", i, term, sum); 
      i++;
    } while(fabs(theo-sum)>3E-4);
 
    printf("1/1^2 + 1/2^2 + 1/3^2 + ... =  %f, pi^2/6 = %f & convergence took %d steps\n", sum, theo, i-1);
 }
 
 /* Sum of inverse n-square 1/1^2 - 1/2^2 + 1/3^2 - 1/4^2 ... = pi^2/12 */
 else if(series7){ 
    
    int i=1; 
    float sum=0.0, term, theo=pow(M_PI,2)/12.0;
 
    do{
      if (i%2==0) term = (float) -1/pow(i,2);
      else        term = (float) 1/pow(i,2);
      sum  += term;
      //printf("i=%d term=%f sum=%f \n", i, term, sum); 
      i++;
    } while(fabs(theo-sum)>1E-4);
 
    printf("1/1^2 - 1/2^2 + 1/3^2 - 1/4^2 + ... =  %f, pi^2/12 = %f & convergence took %d steps\n", sum, theo, i-1);
 }

 /* Sum of inverse n^k: 1/2^0 + 1/2^1 + 1/2^2 + 1/2^3 + ...  */
 else if(series8){ 
   
    int n,k=0; 
    float term,sum=0.0; 
    printf("Enter the base of the n^k series\n");
    scanf("%d",&n);
    
    do{
      term  = (float) 1/pow(n,k);
      sum  += term;
      //printf("k=%d term=%f sum=%f \n", k, term, sum); 
      k++;
    } while(fabs(term)>1E-4);
 
    printf("Sum from 0 to infinity of (1/%d^k) is %f & convergence took %d steps\n", n, sum, k);
 }

 /* Sum of inverse Fibonacci series S = Sum 1/Fi, where F(i+1) = F(i) + F(i-1) with F(1) = F(2) = 1 */
 else if(series9){ 
   
    int i=1, Fip, Fi=1, Fim=1; 
    float sum=0.0, term;
 
    do{
      if (i>2){ 
         Fip = Fi + Fim;
         Fim = Fi;
         Fi  = Fip;
      } 
      term = (float) 1/Fi;
      sum  += term; 
      //printf("i=%d Fip=%d Fi=%d Fim=%d sum=%f term=%f \n", i, Fip, Fi, Fim, sum, term);
      i++;
    } while(fabs(term)>1E-4);
 
    printf("Sum of reciprocal Fibonacci sequence =  %f, & convergence took %d steps\n", sum, i-1);
 }

return 0;
}

/* Results 
   Excercise : Try it for other series of harmonic/hyperbolic functions */
