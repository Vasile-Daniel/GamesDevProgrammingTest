#include <stdio.h>
#include <math.h>


int main(){
    printf(" \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n");
    double x_origin[] = {28, 27, 16, 40, 8,  6, 28, 39, 12, 36, 22, 33, 41, 41, 14,  6, 46, 17, 28,  2};
    double y_origin[] = {42, 46, 22, 50, 6, 19,  5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12}; 
    int len_x = sizeof(x_origin)/sizeof(x_origin[0]);
    double pi = 3.14159265358979323846;
    double R;  // generator = radius R 
    double x0,y0;
    double angle_deg; // angel in degree 
    double angle_rad; // angle in radians 

    R = 20;
    angle_deg = 45;  
    x0 = x_origin[0];
    y0 = y_origin[0];
    printf("Size of x_origin = %d.\r\n", len_x);

    double angle_point_rad, angle_point_deg; 


    // angle_point_rad = atan((y_origin[0] - y0)/(x_origin[0] - x0));
    // angle_point_deg =  (angle_point_rad * 180)/pi;

    // if ( (x0 != x_origin[0]) & (y0 != y_origin[0])){
    //     printf("angle point [rad] = %f\r\n", angle_point_rad);
    //     printf("angel point [deg] = %f\r\n", angle_point_deg);
    // }else{
    //     angle_point_rad = 0; 
    //     angle_point_deg = (angle_point_rad * 180)/pi;
    //     printf("angle point zero: %f\r\n", angle_point_deg);     
    // }


    double point_in_sector[][3] = {}; 
    for (int i = 0; i< len_x; i++){
        // double d = sqrt((x_origin[i]-x0)*(x_origin[i]-x0)+(y_origin[i]-y0)*(y_origin[i]-y0)); 
        if (((int)x_origin[i] == (int)x0) &&  ((int)y_origin[i] == (int)y0) ){

            angle_point_rad = 0; 
            angle_point_deg = (angle_point_rad * 180)/pi;
            printf("angle point zero: %f\r\n", angle_point_deg);

        }
         else{
            angle_point_rad = atan((y_origin[i] - y0)/(x_origin[i] - x0));
            angle_point_deg =  (angle_point_rad * 180)/pi;
            printf("angle point (diferit): %f\r\n", angle_point_deg);
        }
    }



    return 0; 

}