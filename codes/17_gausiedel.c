/* Registration: xxxx; Code for Gauss-Siedel Method */

#include<stdio.h>
#include<math.h>
int main(){

  /* Type declaration */
  int i,j,n; 
  float a[10][10],x[10],sum,temp,error;
  
  /* Input 4 equations: [9a+b+c+d=75, a+8b+c+d=54, a+b+7c+d=43, a+b+c+6d=34] */
  printf("Enter the number of equations: ");
  scanf("%d",&n);
  printf("\nEnter the coefficients\n");
  for (i=1; i<=n; i++){
    for (j=1; j<=n+1; j++){
        scanf("%f",&a[i][j]);
    }
  }

  /* Initialize to zeros */
  for (i=1; i<=n; i++) x[i] = 0;
      
  /* Do the iteration */
  do{
    for(i=1; i<=n; i++){
       sum = 0;
       for(j=1; j<=n; j++){
          if(i!=j)
             sum += a[i][j]*x[j];
       } 
       temp = (a[i][n+1]-sum)/a[i][i];
       error = fabs(x[i]-temp);
       if(error>1E-3)
          x[i]=temp;   
       }
  }while(error>1E-3);
   
  /* Print the solution */
  printf("The values of x are\n");
  for(i=1; i<=n; i++){
     printf("%.2f ", x[i]);
  }
  printf("\n");
  
  return 0;
}

/* Results: 
Enter the number of equations: 4
Enter the coefficients
9 1 1 1 75
1 8 1 1 54
1 1 7 1 43
1 1 1 6 34
The values of x are
7.00 5.00 4.00 3.00
*/
