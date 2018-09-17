/* Registration: xxxx; 
   Description: Code for finding factors and prime factors of a number
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,N,i,j,prod=1,flag;
  
  /* Input the number */
  printf("Enter the number: ");
  scanf("%d", &n); N=n;  /* store the number for future use */

  /* Factorize the number */
  printf("Factors of %d are ",n);
  for(i=1; i<=(n); i++){
     if(n%i == 0) printf("%d ",i);    
  } 

  /* Prime factor: Every composite number has at least one prime factor less than equals square root of itself */
  printf("\nPrime factors of %d are ", N);
  for(i=2; i<=sqrt(n); i++){
     if(n%i == 0){
       printf("%d ",i);    
       n = n/i;
       i--;
     }
  }
  if(n!=1){
    printf("%d ",n);
  }

  /* Product of prime factors */
  n = N;j=2; 
  if(n%2==0) flag=1;     /* Multiply 2 with end product */
  else       flag=0;     /* No need to multiply */
  
  for(i=2; i<=sqrt(n); i++){
     if(n%i == 0){
        if(i%j != 0){ 
           j     = i;    /* Update j with new i, so that one prime is counted only once */
           prod *= i; 
        }
        n = n/i; 
        i--;
     } 
  }
  if(n != 1){
     if(n%j != 0){       /* n is prime, but if equal to j then its double counting */ 
        prod *= n;
     }
  }
  if(flag==1) printf("\nProduct of prime factors of %d are %d\n", N, 2*prod);
  else        printf("\nProduct of prime factors of %d are %d\n", N, prod);
  
return 0;
}

/* Results 
Enter the number: 4158
Factors of 4158 are 1 2 3 6 7 9 11 14 18 21 22 27 33 42 54 63 66 77 99 126 154 189 198 231 297 378 462 594 693 1386 2079 4158 
Prime factors of 4158 are 2 3 3 3 7 11 
Product of prime factors of 4158 are 462

Enter the number: 168
Factors of 168 are 1 2 3 4 6 7 8 12 14 21 24 28 42 56 84 168 
Prime factors of 168 are 2 2 2 3 7 
Product of prime factors of 168 are 42
*/
