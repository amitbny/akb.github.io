/* Regn.No.: xxxx; 
   Description: Code to compute Mean, Median & Mode 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

 /* Type declaration */ 
 int   i, j, k, tmp, n, a[20], tally[20];
 int   sum=0, maxCount=0, mode=0;
 float mean=0.0, median=0.0;

 /* Input the series from keyboard */
 printf("Enter the number of inputs\n");
 scanf("%d",&n);

 /* Initialize to zeros */
 for(i=1; i<=n; i++) tally[i] = 0; 

 printf("Enter the numbers\n");
 for(i=1; i<=n; i++){
     scanf("%d",&a[i]);
     sum += a[i];
 }
 
 /* Calculate mean : average of array */ 
 mean = (float)sum/n;
 
 /* Perform Bubble sorting */ 
 for(i=1; i<=n; i++){
    for(j=1; j<=n-i; j++){
        if(a[j]>a[j+1]){
           tmp = a[j];
           a[j] = a[j+1];
           a[j+1] = tmp;
        }
     }
 }
 printf("The numbers in ascending order are\n");
 for(i=1; i<=n; i++){
   printf("%d ",a[i]);
 }

 /* Calculate median : find out the middle of sorted array */ 
 if(n%2==0){
    median = (a[n/2]+a[n/2+1])/2.0;
 }
 else if(n%2!=0){
    median = a[(n+1)/2];
 }
 
 /* Calculate mode: find out tally and Count the maximum */ 
 for(i=1; i<=n; i++){
    for(j=i; j<=n; j++){
       if(a[i]==a[j]) tally[i]++;
    }
 }
   
 //for(i=1; i<=n; i++) printf("\n%d %d ", a[i], tally[i]);
 for(i=1; i<=n; i++){
    if(tally[i] > maxCount){
       maxCount = tally[i];
       mode = a[i];
    }
 }

 /* Print the results */ 
 printf("\nmean = %f\n", mean);
 printf("median = %f\n", median);
 printf("mode   = %d\n", mode);
 return 0;
}

/* Results */
