/* Registration Number: xxxx; 
   Description: Calculate A_(n+1)/A_n upto given tolerance for a series 
                A_n = A_(n-1) + A_(n-2) + A_(n-3)
   Author: AKB */

#include<stdio.h>
#include<math.h>
int main()
{
  int an, anm1=0, anm2=1, anm3=2;
  float frac, term, tol=1E-7;
 
  do{

    an = anm1 + anm2 + anm3;
    frac = (float) an/anm1; /* An+1/An */
    anm3 = anm2;
    anm2 = anm1;
    anm1 = an;
    term = (float) 1/an;    
    printf("%f\n",frac);

  }while(fabs(term)>tol);
  
return 0;
}

/*
Result: 

1.333333
1.750000
2.000000
1.785714
1.840000
1.847826
1.835294
1.839744
1.839721
1.839015
1.839341
1.839306
1.839269
1.839292
1.839287
1.839286
1.839287
1.839287
1.839287
1.839287
1.839287
1.839287
1.839287
1.839287
1.839287
1.839287

*/
