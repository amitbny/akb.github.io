/* Registration: xxxx; 
   Description: Arithmetic Progression (A.P.) 
   AP: tn = a + (n – 1)*d and Sn = ( 2a + (n-1)*d ) * (n/2) 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */ 
  int a, d, r, n, value, i, sum=0;
    
  printf("Enter the number of terms\n");
  scanf("%d", &n);
  
  printf("Enter first term and common difference of AP series\n");
  scanf("%d %d", &a, &d);
 
  /* print the series and add all elements to sum */
  value = a;
  printf("AP Series: ");
  for(i = 0; i < n; i++){
      printf("%d ", value);
      sum += value;
      value = value + d;
  }
  printf("\nSum of AP series till %d terms in term-by-term is %d\n", n, sum);
    
  /* Compare with direct Calculation */
  sum = (2*a + (n-1)*d)*n/2;
  printf("Sum of AP series till %d terms in direct computation is %d\n", n, sum);

  return 0;
}

/* Results */
