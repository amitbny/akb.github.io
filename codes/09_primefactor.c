/* Registration: xxxx; Code for finding prime factors of a number */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,i;
  
  /* Input the initial guess limits */
  printf("Enter the number: ");
  scanf("%d", &n);
  printf("Prime factors of the number are\n");

  /* Do the iteration */
  for(i=2;i<=sqrt(n);i++){
     if(n%i==0){
        printf("%d ",i);    
        n = n/i;
        i--; 
     }
  }
  if(n!=1){
    printf("%d ",n);
  } 
  return 0;
}

/* Results: 
Enter the number: 87
Prime factors of the number are 3 29 
*/
