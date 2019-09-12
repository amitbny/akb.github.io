/* Registration Number: xxxx; 
   Description: Code for finding prime numbers within a range. 
                Note that 25 primes are there within [0,1e2],
                         168 primes are there within [1,1e3],
                        1229 primes are there within [1,1e4], 
                        9592 primes are there within [1,1e5], 
                       78498 primes are there within [1,1e6] and so on 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

  /* Type declaration */
  int u,l,i,j,flag,count=0,add=0;
  int num=4,prime[100000]; /* array size > number of primes */ 
  
  printf("Enter the upper and lower limit: ");
  scanf("%d %d", &l, &u);

  /* Do the iteration */
  printf("Prime numbers within this range are\n");
  for(i=l; i<=u; i++){
     flag = 0;
     for(j=2; j<=sqrt(i); j++){
        if(i%j==0){
          flag = 1;
          break;
        }
     }
     if(i>1 && flag==0){
        printf("%d ",i);
        count++;           /* Count how many primes are there */
        prime[count] = i;  /* Store prime numbers in an array */
     }
  } 
  printf("\nThere are %d primes in this range\n", count);
  
  /* Compute addition of few prime numbers */
  if (count >= num){
     add=0;  /* forward */
     for(i=1; i<=num; i++) add += prime[i];
     printf("Addition of first %d primes within this range is %d\n", num, add);
  
     add=0;  /* reverse */
     for(i=count; i>=count-num+1; i--) add += prime[i];
     printf("Addition of last %d primes within this range is %d\n", num, add);
  }
return 0;
}

/* Results: 
Enter the two limits: 10 50
Prime factors within the range are
11 13 17 19 23 29 31 37 41 43 47
There are 11 primes in this range
Addition of first 4 primes within this range is 60
Addition of last 4 primes within this range is 168

Enter the two limits: 1 100
Prime factors within the range are
1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
There are 26 primes in this range
Addition of first 4 primes within this range is 11
Addition of last 4 primes within this range is 348

Enter the upper and lower limit: 1 1000
Prime factors within the range are
1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997 
There are 169 primes in this range
Addition of first 4 primes within this range is 11
Addition of last 4 primes within this range is 3948
*/
