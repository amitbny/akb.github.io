/* Mean/Median Code */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
 
 //int i,j,k,tmp,n,sum=0,*a; 
 int   i,j,k,tmp,n,sum=0,a[20], tally[20];
 int   maxCount=0, mode=0;
 float mean=0.0, median=0.0;

 printf("Enter the number of inputs\n");
 scanf("%d",&n);
 
 //a = (int*) malloc(n*sizeof(int));
 
 printf("Enter the numbers\n");
 for(i=1; i<=n; i++){
     scanf("%d",&a[i]);
     sum = sum + a[i];
 }

 /* Calculate mean */ 
 mean = (float)sum/n;
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

 /* Calculate median */ 
 if(n%2==0){
    median = (a[n/2]+a[n/2+1])/2.0;
 }
 else if(n%2!=0){
    median = a[(n+1)/2];
 }
 
 /* Calculate mode */ 
 for(i=1; i<=n; i++){
    for(k=i; k<=n; k++){
       if(a[i]==a[k]) tally[i]++;
    }
 }
    
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
