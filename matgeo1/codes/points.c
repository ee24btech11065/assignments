   #include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

double *points() {
    // Points B and C
    static double arr[12];
    double Bx = 0.0, By = 0.0;
    double Cx = 6.0, Cy = 0.0;
double sinteeta = sqrt(3)/2;
double costeeta = 0.5;
    

    // d is the difference between AB and AC
    double d = 3.0;

    // Calculating AB and AC based on d
    // Case 1: AB = AC + d
    double AB1 = 7.5;  // Example value for AB (you can calculate based on context)
    double AC1 = AB1 - d;

    // Case 2: AC = AB + d
    double AC2 = 7.5;  // Example value for AC (you can calculate based on context)
    double AB2 = AC2 - d;

    // Coordinates of A (two possible positions for each case)

    // For Case 1: AB = AC + d
    double A1x = 6 - AC1 * costeeta;
    double A1y = AC1 * sinteeta;

    // Below BC for Case 1
    double A1_2x = A1x;
    double A1_2y = -A1y;

    // For Case 2: AC = AB + d
    double A2x = AC2 * costeeta;
    double A2y = AC2 * sinteeta;

    // Below BC for Case 2
    double A2_2x = A2x;
    double A2_2y = -A2y;
    
     arr[0] = A1x;
     arr[1]=A1y;
     arr[2] = A2x;
     arr[3] = A2y;
     arr[4] = A1_2x;
     arr[5] = A1_2y;
     arr[6] = A2_2x;
     arr[7]=A2_2y;
     arr[8]=Bx;
     arr[9]=By;
     arr[10]=Cx;
     arr[11]=Cy;
    return arr;
}

    

    
