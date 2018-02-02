/* Registration: xxxx; Arithmetic Progression (A.P.) and Geometric Progression (G.P.). 

AP series is a sequence of terms in which next term is obtained by adding common difference 
to previous term. If tn be the nth term of A.P., then (n+1)th term of can be calculated as 
(n+1)th = tn + D, where D is the common difference (n+1)th - tn. Formula to calculate Nth 
term tn = a + (n – 1)d, where a is first term of AP and d is the common difference. 

GP series is a sequence of terms in which next term is obtained by multiplying common ratio 
to previous term. The (n+1)th term of GP can be calculated as (n+1)th = nth x R, where R is 
the common ratio (n+1)th/nth. Formula to calculate Nth term of GP : tn = a x R^(n-1), where a 
is first term of GP. 

*/

#include<stdio.h>
int main(){

  /* Switch to choose whether ap (=1) or gp (=0) */ 
  int ap=0;

  /* Type declaration */ 
  int first, diff, ratio, terms, value, i, sum=0;
    
  printf("Enter the number of terms\n");
  scanf("%d", &terms);
  
  if(ap){ /* Selecting AP series */ 

    printf("Enter first term and common difference of AP series\n");
    scanf("%d %d", &first, &diff);
 
    /* print the series and add all elements to sum */
    value = first;
    printf("AP Series is\n");
    for(i = 0; i < terms; i++) {
        printf("%d ", value);
        sum += value;
        value = value + diff;
    }
    printf("\nSum of the AP series till %d terms is %d\n", terms, sum);

  }
  else{  /* Selecting AP series */ 
    
    printf("Enter first term and common ratio of GP series\n");
    scanf("%d %d", &first, &ratio);
 
    /* print the series and add all elements to sum */
    value = first;
    printf("GP Series\n");
    for(i = 0; i < terms; i++) {
        printf("%d ", value);
        sum += value;
        value = value * ratio;
    }
    printf("\nSum of the GP series till %d terms is %d\n", terms, sum);

  }
 
  return 0;
}

/* Results 

Cut paste from screen

*/
