#include <stdio.h>
#include <math.h>


int main(){
    double pi = 3.14159265358979323846;
    double angle_degree, angle_rad, angle_sin, angle_cos;
    angle_degree = 45; 
    angle_rad = (angle_degree * pi) / 180;
    angle_cos = cos(angle_rad);
    angle_sin = sin(angle_rad);
    printf("unghi = %f", angle_cos);


    return 0; 
}