/* Registration: xxxx; Arithmetic Progression (A.P.) and Geometric Progression (G.P.). 
AP: tn = a + (n – 1)*d and Sn = ( 2a + (n-1)*d ) * (n/2) 
GP: tn = a * r^(n-1) and Sn = a*(r^n - 1) / (r - 1); */

#include<stdio.h>
#include<math.h>

int main(){

  /* Switch to choose whether ap (=1) or gp (=0) */ 
  int ap=0;

  /* Type declaration */ 
  int a, d, r, n, value, i, sum=0;
    
  printf("Enter the number of terms\n");
  scanf("%d", &n);
  
  if(ap){ /* Selecting AP series */ 

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

  }
  else{  /* Selecting GP series */ 
    
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

  }
 
  return 0;
}

/* Results */
