/* Registration: xxxx; 
   Description: Geometric Progression (G.P.). 
   GP: tn = a * r^(n-1) and Sn = a*(r^n - 1) / (r - 1); 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */ 
  int a, d, r, n, value, i, sum=0;
    
  printf("Enter the number of terms\n");
  scanf("%d", &n);
  
  printf("Enter first term and common ratio of GP series\n");
  scanf("%d %d", &a, &r);
 
  /* Print the series and add elements term by term */
  value = a;
  printf("GP Series: ");
  for(i = 0; i < n; i++){
      printf("%d ", value);
      sum += value;
      value = value * r;
  }
  printf("\nSum of GP series till %d terms in term-by-term is %d\n", n, sum);

  /* Compare with direct Calculation */
  sum = a*(pow(r,n)-1)/(r-1);
  printf("Sum of GP series till %d terms in direct computation is %d\n", n, sum);

  return 0;
}

/* Results */
