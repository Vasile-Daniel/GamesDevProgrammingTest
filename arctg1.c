#include <stdio.h>
#include <math.h>

int main(){
    float pi = 3.141592653589793238462643; 

    float x0 =4;
    float y0 = 6; 
    float R0 = sqrt(x0*x0 + y0*y0);
    printf("R0 = %f\r\n", R0);

    float R = 5;
    float angle_degree = 45; 
    float angle_rad = (angle_degree * pi)/180;
    float x = x0;
    float y = y0+R; 

    float pox = x0 - x;
    float poy = y0 - y; 


    float x1 = x0 - cos(angle_rad) * pox - sin(angle_rad) * poy; 
    float y1 = y0 - cos(angle_rad) * poy + sin(angle_rad) * pox;



    printf("Point x1 (right) = %f \r\n", x1); 
    printf("Point y1 (right) = %f \r\n", y1);

    float x2 = x0 - cos(angle_rad) * pox + sin(angle_rad) * poy; 
    float y2 = y0 - cos(angle_rad) * poy - sin(angle_rad) * pox;
    printf("Point x2 (left) = %f \r\n", x2); 
    printf("Point y2 (left) = %f \r\n", y2);

    float angle1_rad = atan((y2 - y0)/(x2 - x0));
    float angle2_rad = atan((y1 - y0)/(x1 - x0));

    float angle1_degree = (angle1_rad * 180)/pi;
    float angle2_degree = (angle2_rad * 180)/pi;
    printf("angle1_degree = %f \r\n", angle1_degree);
    printf("angle2_degree = %f \r\n", angle2_degree);
    

    return 0; 
}