#include <stdio.h>
#define PI 3.14
#define AREA_OF_CIRCLE(r)(PI*r*r)
#define SURFACE_AREA_OF_CYLINDER(r,h)(2*PI*r*(r+h))
int main()
  {
   float r,h,area,surface_area;
   printf("Enter the radius of circle and cylinder:");
   scanf("%f",&r);
   printf("Enter the height of the cylinder:");
   scanf("%f",&h);
   area=AREA_OF_CIRCLE(r);
   surface_area=SURFACE_AREA_OF_CYLINDER(r,h);
   printf("The area of the circle:%f\n",area);
   printf("The surface area of the cylinder:%f\n",surface_area);
   return 0;
  }
   
