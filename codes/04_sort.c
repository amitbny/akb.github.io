/* Sorting Code */

#include<stdio.h>
#include<math.h>

int main(){
 
 int i,j,t,n,a[20]; 
 printf("Enter the number of inputs\n");
 scanf("%d",&n);
 printf("Enter the numbers\n");
 for(i=1; i<=n; i++){
     scanf("%d",&a[i]);
 }
 for(i=1; i<=n; i++){
    for(j=1; j<=n-i; j++){
        if(a[j]>a[j+1]){
           t = a[j];
           a[j] = a[j+1];
           a[j+1] = t;
        }
     }
 }
 
 printf("The numbers in ascending order are\n");
 for(i=1; i<=n; i++){
   printf("%d ",a[i]);
 }
 printf("\n");
 return 0;
}
