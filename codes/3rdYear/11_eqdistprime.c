/* Registration Number: xxxx; 
   Description: Code for finding n prime numbers equally distributed from a given number
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int n,i,j,flag,count,add=0;
  int num=5,prime[num]; 
  for(i=0;i<num;i++) prime[i] = 0; /* Zero initialize */
 
  printf("Enter the number: ");
  scanf("%d", &n);

  /* Do the iteration */
  printf("First %d prime numbers greater than %d are ", num, n);
  i = n; count = 0;
  do{
    flag = 0;
    for(j=2;j<=sqrt(i);j++){
       if(i%j==0){
         flag = 1;
         break;
       }
    }
    if(i>1 && flag==0){
       printf("%d ",i);
       prime[count] = i;  /* Store in array, if asked */
       add         += i; 
       count++;        
    }
  i++;
  } while(count<num);
 
  add=0; for(i=0;i<num;i++) add += prime[i]; /* If stored in array, then add accordingly */ 
  printf("\nSum of first %d prime numbers are %d\n", num, add);

  /* ======================================================= */
 
  printf("Last %d prime numbers lesser than %d are ", num, n);
  i = n; count = 0;
  do{
    flag = 0;
    for(j=2;j<=sqrt(i);j++){
       if(i%j==0){
         flag = 1;
         break;
       }
    }
    if(i>1 && flag==0){
       printf("%d ",i);
       count++;         
       add += i; 
    }
  i--;   /* Only change than previous section */
  } while(count<num); 
  printf("\nSum of these %d prime numbers are %d\n", 2*num, add);
  
return 0;
}

/* Results: 
Enter the number: 4000
First 6 prime numbers greater than 4000 are 4001 4003 4007 4013 4019 4021 
Last 6 prime numbers lesser than 4000 are 3989 3967 3947 3943 3931 3929 
Sum of these prime numbers are 47770.

Enter the number: 50
First 5 prime numbers greater than 50 are 53 59 61 67 71 
Sum of first 5 prime numbers are 311
Last 5 prime numbers lesser than 50 are 47 43 41 37 31 
Sum of these 10 prime numbers are 510
*/
