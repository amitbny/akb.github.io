/* Registration: xxxx; 
   Description: Code for finding prime factors of a number
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,i;
  
  /* Input the number */
  printf("Enter the number: ");
  scanf("%d", &n);

  /* Do the iteration */
  printf("Prime factors of %d are ",n);
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
    
  printf("\n");
  return 0;
}

/* Results */
