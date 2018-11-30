/* Registration: xxxx; 
   Description: Code for finding factors and prime factors of a number
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,N,i,j,prod,add=0;
  
  /* Input the number */
  printf("Enter the number: ");
  scanf("%d", &n); N=n;  /* store the number for future use */

  /* Factorize the number */
  printf("Factors of %d are ",n);
  for(i=1; i<=n; i++){
     if(n%i == 0) printf("%d ",i);    
  } 

  /* Prime factor: Every composite number has at least one prime factor less than equals square root of itself */
  printf("\nPrime factors of %d are ", n);
  for(i=2; i<=sqrt(n); i++){
     if(n%i == 0){
       printf("%d ",i);   
       add += i; 
       n = n/i;
       i--;
     }
  }
  if(n!=1){
    printf("%d ",n);
    add += n; 
  }
  printf("\nSum of prime factors of %d is %d \n", N, add);
  
  /* Product of only prime factors (without repetition) */
  n = N; j = 2; prod = 1; 
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
  if(n!=1){
     if(n%j!=0){       /* n is prime, but if equal to j then its double counting */ 
        prod *= n;
     }
  }
  if(N%2==0) printf("Product of prime factors of %d are %d\n", N, 2*prod); /* Multiply 2 because its never counted */
  else        printf("Product of prime factors of %d are %d\n", N, prod);
  
return 0;
}

/* Results 
Enter the number: 4158
Factors of 4158 are 1 2 3 6 7 9 11 14 18 21 22 27 33 42 54 63 66 77 99 126 154 189 198 231 297 378 462 594 693 1386 2079 4158 
Prime factors of 4158 are 2 3 3 3 7 11
Sum of prime factors is 29 
Product of prime factors of 4158 are 462

Enter the number: 168
Factors of 168 are 1 2 3 4 6 7 8 12 14 21 24 28 42 56 84 168 
Prime factors of 168 are 2 2 2 3 7
Sum of prime factors is 16 
Product of prime factors of 168 are 42

Enter the number: 30030
Factors of 30030 are 1 2 3 5 6 7 10 11 13 14 15 21 22 26 30 33 35 39 42 55 65 66 70 77 78 91 105 110 130 143 154 165 182 195 210 231 273 286 330 385 390 429 455 462 546 715 770 858 910 1001 1155 1365 1430 2002 2145 2310 2730 3003 4290 5005 6006 10010 15015 30030 
Prime factors of 30030 are 2 3 5 7 11 13 
Sum of prime factors is 41 
Product of prime factors of 30030 are 30030.
*/
