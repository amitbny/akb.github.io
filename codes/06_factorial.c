/* Regn.No.: ; Sum of factorials and series solution */

#include<stdio.h>
#include<math.h>
int main(){

 int fac=0,invfac=0,expx=0,sinx=1;

 /* Sum of factorial 1! + 2! + 3! + ... */
 if(fac){ 
   
    int n,fact=1,sum=0,i=1; 
    printf("Enter the limit of the factorial series\n");
    scanf("%d",&n);
 
   do{
     fact = fact*i;
     sum = sum + fact;
     //printf("i=%d, fact=%d, sum=%d\n", i, fact, sum);
     i = i+1;
   } while(i<=n);
 
   printf("The sum of factorial series of %d order are %d\n", n, sum);
 }

 /* Sum of inverse factorial 1/1! + 1/2! + 1/3!+ ... */
 if(invfac){ 
   int n,fact=1,i=1; 
   float sum=0.0;
   printf("Enter the limit of the factorial series\n");
   scanf("%d",&n);
 
   do{
     fact = fact*i;
     sum += (float) 1/fact;
     //printf("i=%d, fact=%d, sum=%d\n", i, fact, sum);
     i = i+1;
   } while(i<=n);
 
   printf("The sum of factorial series of %d order are %f\n", n, sum);
 }

 /* exponential series exp(x) = 1+ x/1! + x^2/2! + x^3/3!+ ... */
 if(expx){ 
   int x,n,fact=1,i=1; 
   float sum=0.0;
   printf("Enter value of x for exp(x)\n");
   scanf("%d",&x);
   printf("Enter the limit of the factorial series\n");
   scanf("%d",&n);
 
   do{
     fact = fact*i;
     sum += (float) pow(x,i)/fact;
     i = i+1;
   } while(i<=n);

   sum += 1.0; /* Don't forget to add the extra 1 */ 
   printf("The exponential series upto %d order are %f\n", n, sum);
 }

 /* sine series sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... */
 if(sinx){
   int n,p,fact=1,i=1;
   float x,sum=0.0;
   printf("Enter value of x in degrees for sin(x)\n");
   scanf("%f",&x);
   printf("Enter the limit of the factorial series\n");
   scanf("%d",&n);

   x = x*M_PI/180.0; /* Convert to radian */

   do{
     fact = fact*i;
     if(i==1 || i%2 != 0) {
        sum += (float) pow(-1,p)*pow(x,i)/fact;
        p += 1;
     }
     i = i+1;
   } while(i<=n);

   printf("The sum of factorial series of %d order are %f\n", n, sum);
 }

 return 0;
}

/* Results */

