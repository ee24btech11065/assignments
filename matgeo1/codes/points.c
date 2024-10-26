   #include <stdio.h>
#include <math.h>
double *points() {
    
    static double arr[36];
    double Bx = 0.0, By = 0.0;
    double Cx = 6.0, Cy = 0.0;
double sinteeta = sqrt(3)/2;
double costeeta = 0.5;
double d1 = 3.2;
    double AB1 = 7.23;  
    double AC1 = AB1 - d1;
    double AC_1 = 7.23;  
    double AB_1 = AC_1 - d1;
    double A1x = 6 - AC1 * costeeta;
    double A1y = AC1 * sinteeta;
    double A1_1x = A1x;
    double A1_1y = -A1y;
    double A11x = 6 - (AC_1)*costeeta;
    double A11y = (AC_1)*sinteeta;
    double A11_1x = A11x;
    double A11_1y = -A11y;
 double d2 = 3.1;
    double AB2 = 7.36,AC2 = AB2 - d2,AC_2 = 7.36,AB_2 = AC_2 - d2;
    double A2x = 6 - AC2*costeeta,A2y = AC2*sinteeta,A2_1x = A2x,A2_1y = -A2y;
    double A22x = 6 - (AC_2)*costeeta,A22y = (AC_2)*sinteeta,A22_1x = A22x,A22_1y = - A22y;double d3 = 3;
    double AB3 = 7.5,AC3 = AB3 - d3,AC_3 = 7.5,AB_3 = AC_3 - d3;
    double A3x = 6 - AC3*costeeta,A3y = AC3*sinteeta,A3_1x = A3x,A3_1y = - A3y;
    double A33x = 6 - (AC_3)*costeeta,A33y = (AC_3)*sinteeta,A33_1x = A33x,A33_1y = -A33y; double d4 = 2.8;
    double AB4 = 7.82,AC4 = AB4 - d4,AC_4 = 7.82,AB_4 = AC_4 - d4;
    double A4x = 6 - AC4*costeeta,A4y = AC4*sinteeta,A4_1x = A4x,A4_1y = -A4y;
    double A44x = 6- (AC_4)*costeeta,A44y = (AC_4)*sinteeta,A44_1x = A44x,A44_1y = - A44y;
 arr[0] = A1x;
     arr[1]=A1y;
     arr[2] = A1_1x;
     arr[3] = A1_1y;
     arr[4] = A11x;
     arr[5] = A11y;
     arr[6] = A11_1x;
     arr[7]=A11_1y;
     arr[8]=A2x;
     arr[9]=A2y;
     arr[10]=A2_1x;
     arr[11]=A2_1y;
     arr[12]=A22x; 
     arr[13]= A22y;
     arr[14]= A22_1x;
     arr[15] = A22_1y;
     arr[16]= A3x;
     arr[17]=A3y;
     arr[18]=A3_1x;
     arr[19]=A3_1y;
     arr[20]=A33x;
     arr[21]=A33y;
     arr[22]=A33_1x;
     arr[23]=A33_1y;
     arr[24]= A4x;
     arr[25]=A4y;
     arr[26]=A4_1x;
     arr[27]=A4_1y;
     arr[28]=A44x;
     arr[29]=A44y;
     arr[30]=A44_1x;
     arr[31]=A44_1y;
     arr[32]=Bx;
     arr[33]=By;
     arr[34]=Cx;
     arr[35]=Cy;
    return arr;
}
int main() {
    double* coordinates = points();

    
    printf("Coordinates of points:\n");
    for (int i = 0; i <= 34; i += 2) {
        printf("Point %d: (%.2f, %.2f)\n", i / 2 + 1, coordinates[i], coordinates[i + 1]);
    }

    return 0;
}
	
    

    
