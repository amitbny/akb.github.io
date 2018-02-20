/* Mean/Median Code */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
 
 int i,j,t,n,sum=0,a[20]; 
 float mean, median;

 printf("Enter the number of inputs\n");
 scanf("%d",&n);
 
 printf("Enter the numbers\n");
 for(i=1; i<=n; i++){
     scanf("%d",&a[i]);
     sum = sum + a[i];
 }
 mean = (float)sum/n;
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

 if(n%2==0){
    median = (a[n/2]+a[n/2+1])/2.0;
 }
 else if(n%2!=0){
    median = a[(n+1)/2];
 }
 printf("\nmean = %f\n",mean);
 printf("median = %f\n",median);
 return 0;
}
