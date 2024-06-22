#include <stdio.h>

int findMax(int thisArray[], int thisRange) {
    int max = 0;
    for ( int i = 0; i < thisRange; i++ ) {
        if ( thisArray[i] > max ) {
            max = thisArray[i];
        }
    }
    return max;
}

int findMin(int thisArray[], int thisRange, int thisMax) {
    int min = thisMax;
    for ( int i = 0; i < thisRange; i++ ) {
        if ( thisArray[i] < min ) {
            min = thisArray[i];
        }
    }
    return min;
}

int main()
{
    printf("PROGRAM TO FIND MIN AND MAX NUMBERS IN N NUMBERS ");

    int range, buffer;
    printf("\n\nEnter the number of elements : ");
    scanf("%d", &range);

    int myArray[range];
    for (int i = 0; i < range; i++)
    {
        printf("Enter element to put at index [ %d ] : ", i),
            scanf("%d", &buffer), myArray[i] = buffer;
    }

    printf("\n\nThe min element is : %d\nThe max element is : %d", findMax(myArray, range), findMin(myArray, range, findMax(myArray, range)));
    return 0;

}