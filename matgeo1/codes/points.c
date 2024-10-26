   #include <stdio.h>
#include <math.h>
double *points() {
    // Points B and C
    static double arr[20];
    double Bx = 0.0, By = 0.0;
    double Cx = 6.0, Cy = 0.0;
double sinteeta = sqrt(3)/2;
double costeeta = 0.5;
double d1 = 3.2,d2 = 3.1,d3=3,d4=2.8;

double AC1 = (36 - d1*d1)/(6 + 2*d1);
    
    double Aax = 6 - AC1 * costeeta,Aay = AC1 * sinteeta;
    double Aa_1x = Aax, Aa_1y = -Aay;

double AC2 = (36 - d2*d2)/(6 + 2*d2);
    double Abx = 6 - (AC2)*costeeta,Aby = (AC2)*sinteeta;
    double Ab_1x = Abx,Ab_1y = -Aby;
 
double AC3 = (36 - d3*d3)/(6 + 2*d3);
    
    double Acx = 6 - AC3*costeeta,Acy = AC3*sinteeta;
    double Ac_1x = Acx,Ac_1y = -Acy;
    

double AC4 = (36 - d4*d4)/(6 + 2*d4);

    double Adx = 6 - AC4*costeeta,Ady = AC4*sinteeta;
    double Ad_1x = Adx,Ad_1y = - Ady;
    
    
 arr[0] = Aax;
     arr[1]=Aay;
     arr[2] = Aa_1x;
     arr[3] = Aa_1y;
     arr[4] = Abx;
     arr[5] = Aby;
     arr[6] = Ab_1x;
     arr[7]=Ab_1y;
     arr[8]=Acx;
     arr[9]=Acy;
     arr[10]=Ac_1x;
     arr[11]=Ac_1y;
     arr[12]=Adx; 
     arr[13]= Ady;
     arr[14]= Ad_1x;
     arr[15] = Ad_1y;
     arr[16]=Bx;
     arr[17]=By;
     arr[18]=Cx;
     arr[19]=Cy;
    return arr;
}
int main() {
    double* coordinates = points();

    // Print the coordinates of the points
    printf("Coordinates of points:\n");
    for (int i = 0; i <= 18; i += 2) {
        printf("Point %d: (%.2f, %.2f)\n", i / 2 + 1, coordinates[i], coordinates[i + 1]);
    }

    return 0;
}
	
    

    
