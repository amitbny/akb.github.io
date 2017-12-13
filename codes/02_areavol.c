/* Regn.No.: ; Area and volume of different geometry */
/* Get a feeling of int and float by printing 2/3 */


#include<stdio.h>
#include<math.h>
int main(){

 int circle=0,sphere=0,cylinder=1;

 /* Area of circle */
 if(circle){ 
   
    int r; 
    float area; 
    printf("Enter the radius of circle\n");
    scanf("%d",&r);
    area = M_PI*pow(r,2);
    printf("Area of circle is %f\n", area);
 
 }

 /* Volume of sphere */
 if(sphere){ 
    
    int r; 
    float vol; 
    printf("Enter the radius of sphere\n");
    scanf("%d",&r);
    vol = M_PI*pow(r,3)*4.0/3.0;
    printf("Volume of sphere is %f\n", vol);
 
 }

 /* Volume of cylinder */
 if(cylinder){ 
    
    int r,h; 
    float vol; 
    printf("Enter the radius and height of cylinder\n");
    scanf("%d %d",&r,&h);
    vol = M_PI*pow(r,2)*h;
    printf("Volume of cylinder is %f\n", vol);

 }

return 0;
}

/* Results */
