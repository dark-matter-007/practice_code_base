// WRITE A PROGRAM TO FIND MIN AND MAX IN A RANGE OF N NUMBERS

#include <stdio.h>

int findMax(int arrayOfNumbers[], int assumedMax ) {
    int max = assumedMax; int found = 0;
    for ( int i = 0; i <= ( sizeof arrayOfNumbers ) / 4; i ++ ) {
        if ( arrayOfNumbers[i] > max ) {
            max = arrayOfNumbers[i]; found=1;
        }
    }

    if ( found == 1 ) { return findMax ( arrayOfNumbers, max );}
    return max;
}

int findMin(int arrayOfNumbers[], int assumedMin) {
    int min = assumedMin; int found = 0;
    for ( int i = 0; i <= ( sizeof arrayOfNumbers ) / 4; i ++ ) {
        if ( arrayOfNumbers[i] < min ) {
            min = arrayOfNumbers[i]; found=1;
        }
    }

    if ( found == 1 ) { return findMin ( arrayOfNumbers, min );}
    return min;
}


int main()
{
    printf("Program to find min and max among n numbers \n");

    int range; 
    printf("Enter, how many numbers are there : "), scanf("%d", &range);

    int arrayOfNumbersMaster[range], buffer;

    for ( int i = 0; i < range; i++) {
        printf("Enter num %d of %d nums", i, range), scanf("%d", &buffer);
        arrayOfNumbersMaster[i] = buffer;
    }

    printf("The max number is : %d\nand min number is : %d", 
        findMax(arrayOfNumbersMaster, 0),
        findMin(arrayOfNumbersMaster, findMax(arrayOfNumbersMaster, 0)));
}