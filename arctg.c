#include <stdio.h>
#include <math.h>


int main(){

    float pi = 3.141592653589793238462643; 
    float angle_degree = 60; 
    float angle_rad = (angle_degree * pi) / 180;



    //// CASE 1: 
    float R1 = 20;
    float y20 = R1*sin(angle_rad);
    float x20 = R1*cos(angle_rad);
    float atan20_rad = atan(y20/x20);
    float atan20_degree = (atan20_rad * 180) / pi; 
    printf(" \r\n \r\n \r\n \r\n \r\n \r\n \r\n");
    printf("Q(x20, y20) = Q(%f, %f).\r\n", x20, y20);
    printf("angle_ard = %f.\r\n", atan20_rad);
    printf("angle_degree = %f.\r\n\n", atan20_degree);
    //// CASE 2: 
    float R2 = 6;
    float y6 = R2*sin(angle_rad);
    float x6 = R2*cos(angle_rad);
    float atan6_rad = atan(y6/x6);
    float atan6_degree = (atan6_rad * 180) / pi; 
    printf("Q(x6, y6) = Q(%f, %f).\r\n", x6, y6);
    printf("angle_ard = %f.\r\n", atan6_rad);
    printf("angle_degree = %f.\r\n", atan6_degree);
    printf(" \r\n \r\n");
    //// CASE 3: 
    float R3 = 14;
    float y14 = R3*sin(angle_rad);
    float x14 = R3*cos(angle_rad);
    float atan14_rad = atan(y14/x14);
    float atan14_degree = (atan14_rad * 180) / pi; 
    printf("Q(x14, y14) = Q(%f, %f).\r\n", x14, y14);
    printf("angle_ard = %f.\r\n", atan14_rad);
    printf("angle_degree = %f.\r\n", atan14_degree);
    printf(" \r\n \r\n");


    return 0; 
}