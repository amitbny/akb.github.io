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
 
  /* Multiply the matrices */
  /* Number of column of first matrix = Number of row of second matrix */
  if(n == p){ /* A*B */
     printf("\n A*B = \n");
     for(i=1; i<=m; i++){
        for(j=1; j<=q; j++){
          C[i][j] = 0;
          for(k=1; k<=n; k++){
             C[i][j] += A[i][k]*B[k][j];
          }
          printf("%d ",C[i][j]);
        }
        printf("\n");
      }
      if (m == q){ /* Calculate Trace for square matrix only */
         for(k=1; k<=m; k++) trace += C[k][k];  
         printf("\nTrace = %d\n", trace);
      }
    }
    else if(m == p){ /* Transpose(A)*B */
      printf("\n Transpose(A)*B = \n");
      for(i=1; i<=n; i++){
        for(j=1; j<=q; j++){
          C[i][j] = 0;
          for(k=1; k<=m; k++){
             C[i][j] += A[k][i]*B[k][j];
          }
          printf("%d ",C[i][j]);
        }
        printf("\n");
      } 
      if (n == q){ /* Calculate Trace for square matrix only */
         for(k=1; k<=n; k++) trace += C[k][k];  
         printf("\nTrace = %d\n", trace);
      }
    }
    else{
      printf("Invalid operation\n");
      exit(1);
  }
  
  return 0;
}

/* Results */ 

