/* Registration: xxxx; 
   Descripton: Code for Matrix A+B, A*B, A^T*B 
   Author: AKB */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){

  /* Type declaration */
  int i,j,m,n,p,q,k,trace=0,A[4][4],B[4][4],C[4][4];
  
  /* Enter the matrices A and B from keyboard */
  printf("Enter the number of rows and columns of matrix A\n");
  scanf("%d %d",&m, &n);
  printf("Enter the elements of matrix A\n");
  for (i=1; i<=m; i++){
    for (j=1; j<=n; j++){
       scanf("%d",&A[i][j]);
    }
  }
  printf("Enter the number of rows and columns of matrix B\n");
  scanf("%d %d",&p, &q);
  printf("Enter the elements of matrix B\n");
  for (i=1; i<=p; i++){
    for (j=1; j<=q; j++){
       scanf("%d",&B[i][j]);
    }
  }
 
  /* Add the matrices after checking their dimensions */
    if(m == p && n == q){
      printf("Sum of matrix A and B is\n");
      for (i=1; i<=p; i++){
        for (j=1; j<=q; j++){
           C[i][j] = A[i][j] + B[i][j];
           printf("%d ",C[i][j]);
        }
        printf("\n");
      }
      for(k=1; k<=m; k++) trace += C[k][k];  /* Calculate Trace */
      printf("\nTrace = %d\n", trace);
    }
    else{
      printf("Invalid operation\n");
      exit(1);
    }
  
  return 0;
}

/* Results: */ 

