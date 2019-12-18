/* Registration Number: xxxx; 
   Description: Fermat Primes 2^2^n+1 for n=0,1,2,3 and 4. 
                https://en.wikipedia.org/wiki/Fermat_number 
   Author: AKB */

#include<stdio.h>
#include<math.h>
int main(){
    long int t,n,count=0,i;
    printf("Enter the Number : ");
    scanf("%ld",&n);
	
    for(i=2;i<=sqrt(n);i++){
       if(n%i==0){
   	  count++;
     	  break;
       }
    }
    if(count==0) printf("%ld is a prime number\n",n);
    else 	 printf("%ld is not a prime number\n",n);
    
    if(n==1||2||3||4){
       t = pow(2,pow(2,n))+1;
       count=0;
       for(i=2;i<=sqrt(fabs(t));i++){
	   if(t%i==0){
	      count++;
	      break;
	   }
       }
       if(count==0) printf("2^2^%ld+1=%ld is a prime number\n",n,t);	
       else         printf("2^2^%ld+1=%ld is not a prime number\n",n,t);	
       printf("Hence Proved\n");
    }
    return 0;
}

/* Results

Enter the Number : 0
0 is a prime number
2^2^0+1=3 is a prime number
Hence Proved

Enter the Number : 1
1 is a prime number
2^2^1+1=5 is a prime number
Hence Proved

Enter the Number : 2
2 is a prime number
2^2^2+1=17 is a prime number
Hence Proved

Enter the Number : 3
3 is a prime number
2^2^3+1=257 is a prime number
Hence Proved

Enter the Number : 4
4 is not a prime number
2^2^4+1=65537 is a prime number
Hence Proved

Enter the Number : 5
5 is a prime number
2^2^5+1=4294967297 is not a prime number
Hence Proved

6 onwards number cannot be handled by computer.

*/
