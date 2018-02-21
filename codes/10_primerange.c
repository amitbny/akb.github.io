/* Registration: xxxx; Code for finding prime factors within a range */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int u,l,i,j,flag;
  
  printf("Enter the two limits: ");
  scanf("%d %d", &l, &u);
  printf("The prime factors within the range is\n");

  /* Do the iteration */
  for(i=l;i<=u;i++){
     flag = 0;
     for(j=2;j<=sqrt(i);j++){
        if(i%j==0){
          flag = 1;
          break;
        }
     }
     if(flag==0)
        printf("%d ",i);
  } 
  printf("\n");
  return 0;
}

/* Results: 
Enter the two limits: 10 50
The prime factors within the range is
11 13 17 19 23 29 31 37 41 43 47

Enter the two limits: 1 100
The prime factors within the range is
1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
*/
