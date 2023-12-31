#include <stdio.h>
#include <math.h>

// #define M_PI acos(-1.0)

int main(){
    // clear screen
    printf(" \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n \r\n");
    double x_origin[] = {28, 27, 16, 40, 8,  6, 28, 39, 12, 36, 22, 33, 41, 41, 14,  6, 46, 17, 28,  2};
    double  y_origin[] = {42, 46, 22, 50, 6, 19,  5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12}; 
    // double number[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}; 
    char *direction[] = {"North", "East", "South", "West", "North", "East", "South", "West","North", "East", "South", "West","North", "East", "South", "West","North", "East", "South", "West"};
    double pi = 3.14159265358979323846;
    double R;  // generator = radius R 
    double angle_deg; // angel in degree 
    double angle_rad; // angle in radians 
    double angle1_deg, angle2_deg, angle1_rad, angle2_rad, angle_point; 
    int rows = 20;
    int columns = 3;
    double points[20][3] = {}; // matrix[rows][columns]
    int nr; 

    int len_x = sizeof(x_origin)/sizeof(x_origin[0]); 
    int len_direction = sizeof(direction)/sizeof(direction[0]);

    printf("Number      X       Y    Direction\r\n\r\n");
    // printf("--------------------------------\n");
    for (int i =0; i < rows; i++){
            points[i][0] = i+1;
            points[i][1] = x_origin[i]; 
            points[i][2] = y_origin[i]; 
            for(int j =0; j < columns; j++){
                printf("%5.f   ",points[i][j]); 
            }
            printf(" %s \n", direction[i]);
            // printf(" --------------------------------\n");
    }
    printf("----------------------------------- \r\n\r\n");

    printf("The length of vector x is: %d \n\r", len_x);
    printf("The length of vector DIRECTION is: %d \r\n", len_direction);
    printf("----------------------------------- \r\n");


    //////////////////////////////////////////////////////////////////////////////
    R = 20;
    nr = 1; 
    angle_deg = 45; 
    angle_rad = (angle_deg * pi)/180; // angle in radians  

    
    double x0, y0, x,y, x1, y1, x2, y2, pox, poy; 

    double angle_sin = sin(angle_rad); 
    double angle_cos = cos(angle_rad); 
    printf("VALUE OF SIN AND COS FOR ANGLE %f IN RADIANS\r\n", angle_rad);
    printf("sin(%f) = %f \n \r", angle_rad, angle_sin);
    printf("cos(%f) = %f \n \r", angle_rad, angle_cos );
    printf("----------------------------------- \r\n");

    x0 = x_origin[0];
    y0 = y_origin[0];
    x = x_origin[0];
    y = y_origin[0]+R; 

    pox = x0 - x;
    poy = y0 - y; 


    x1 = x0 - cos(angle_rad) * pox - sin(angle_rad) * poy; 
    y1 = y0 - cos(angle_rad) * poy + sin(angle_rad) * pox;


    x2 = x0 - cos(angle_rad) * pox + sin(angle_rad) * poy; 
    y2 = y0 - cos(angle_rad) * poy - sin(angle_rad) * pox;

    printf("THE VALIUES OF P1 and P2: \r\n");
    printf("P1 (x1,y1) = P1 (%f, %f) \r\n", x1,y1); 
    printf("P2 (x2,y2) = P2 (%f, %f) \r\n", x2,y2);
    printf("----------------------------------- \r\n");

    angle1_rad = atan((y2 - y0)/(x2 - x0)); 
    angle2_rad = atan((y1 - y0)/(x1 - x0)); 
    // angle1_rad = atan((y1)/(x1)); 
    // angle2_rad = atan((y2)/(x2)); 


    angle1_deg = (angle1_rad *180) / pi; // angle in degree 
    angle2_deg = (angle2_rad *180) / pi;
    printf("angle 1: %f\r\n", angle1_deg);
    printf("angle 2: %f\r\n", angle2_deg);
    printf("----------------------------------- \r\n");

    double angle_point_rad, angle_point_deg; 
    double point_in_sector[][3] = {}; 
    for (int i = 0; i< len_x; i++){
        double d = sqrt((x_origin[i]-x0)*(x_origin[i]-x0)+(y_origin[i]-y0)*(y_origin[i]-y0)); 
        if (((int)x_origin[i] == (int)x0) && ((int)y_origin[i] == (int)y0)){
            angle_point_rad = 0; 
            angle_point_deg = (angle_point_rad * 180)/pi;
            printf("angle point (egal): %f\r\n", angle_point_deg);

        }else{
            angle_point_rad = atan((y_origin[i] - y0)/(x_origin[i] - x0));
            angle_point_deg =  (angle_point_rad * 180)/pi;
            printf("angle point (diferit): %f\r\n", angle_point_deg);
        }
  
        // if ((angle2_deg <= angle_point_deg <= angle1_deg)){
        //     // point_in_sector[i][0] = points[i][0]; 
        //     // point_in_sector[i][1] = points[i][1]; 
        //     // point_in_sector[i][2] = points[i][2];

        //     point_in_sector[i][0] = 1; 
        //     point_in_sector[i][1] = 2; 
        //     point_in_sector[i][2] = 3; 
        // }
    }


    // printf("POINTS IN SECTOR:\r\n");
    // for (int i =0; i < 3; i++){
    //         for(int j =0; j < 3; j++){
    //             printf("%f   ",point_in_sector[i][j]); 
    //         }
    //         printf("\n");
    // }
    // printf("----------------------------------- \r\n");
    return 0; 
}