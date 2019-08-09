/* Regn No:xxxx; 
   Description: Bubble Sorting Algorithm
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

 /* Type Declaration */ 
 int i,j,t,n,a[20];

 /* Input data from keyboard */  
 printf("Enter the number of inputs :\n");
 scanf("%d",&n);
 printf("Enter the numbers :\n");
 for(i=1; i<=n; i++){
     scanf("%d",&a[i]);
 }

 /* Perform Bubble sorting */
 for(i=1; i<=n; i++){
    for(j=1; j<=n-i; j++){
        if(a[j]>a[j+1]){
           t = a[j];
           a[j] = a[j+1];
           a[j+1] = t;
        }
     }
 }

 /* Print the results */ 
 printf("The numbers in ascending order are\n");
 for(i=1; i<=n; i++){
   printf("%d ",a[i]); 
 }
 printf("\n");
 return 0;
}

/* Results
   Enter the number of inputs : 10
   Enter the numbers : 1 4 7 9 2 4 3 2 1 5
   The numbers in ascending order are 1 1 2 2 3 4 4 5 7 9 

   Exercise: Do Insertion Sorting and compare the execution time for
             different sized array */

