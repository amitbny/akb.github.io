/* Regn.No.:xxxx-xx-xxxx; 
   Description: Area and volume of different geometry; 
                Get a feeling of int and float by printing fractions. 
   Author: AKB */

#include<stdio.h>
#include<math.h>

int main(){

 /* Use an integer switch */
 int area_cir=0, area_tri=0, vol_sph=0, vol_cyl=1; 

 /* Area of circle */
 if(area_cir){ 
    int r; 
    float area; 
    printf("Enter the radius of circle :\n");
    scanf("%d",&r);
    area = M_PI*pow(r,2);
    printf("Area of circle is %f\n", area);
 }

 /* Area of triangle (using Heron's Formula) */
 else if(area_tri){ 
    float a,b,c,s,theta,area; 
    printf("Enter the two sides and angle of triangle :\n");
    scanf("%f %f %f", &a, &b, &theta);
    theta = M_PI*theta/180.0;  // Convert angle into radian
    c = sqrt(a*a + b*b - 2.0*a*b*cos(theta));
    s = (a+b+c)*0.5;
    area = sqrt(s*(s-a)*(s-b)*(s-c));
    printf("Area of triangle of two sides %g and %g with angle %g degree is %g\n", a, b, 180.0*theta/M_PI, area);
 }

 /* Volume of sphere */
 else if(vol_sph){ 
    int r; 
    float vol; 
    printf("Enter the radius of sphere :\n");
    scanf("%d",&r);
    vol = M_PI*pow(r,3)*4.0/3.0;
    printf("Volume of sphere is %f\n", vol);
 }

 /* Volume of cylinder */
 else if(vol_cyl){ 
    int r,h; 
    float vol; 
    printf("Enter the radius and height of cylinder :\n");
    scanf("%d %d",&r,&h);
    vol = M_PI*pow(r,2)*h;
    printf("Volume of cylinder is %f\n", vol);
 }

return 0;
}

/* Results: 
   Enter the radius of circle : 1
   Area of circle is 3.141593

   Enter the two sides and angle of triangle : 1 2 30
   Area of triangle of two sides 1 and 2 with angle 30 degree is 0.5

   Enter the radius of sphere : 1
   Volume of sphere is 4.188790
   
   Enter the radius and height of cylinder : 1 2
   Volume of cylinder is 6.283185 
 
   Exercise: Try other geometry with a bit more involved formula/computation 
*/
