// Array Sorter Program, refurbished

#include <stdio.h>

int viewProcedure = 0;

void swapElements(int *firstElementPointer, int *secondElementPointer)
{
    int buffer;
    buffer = *firstElementPointer;
    *firstElementPointer = *secondElementPointer;
    *secondElementPointer = buffer;
    // return 0; // Means, no errors were faced
}

int printArray(int *arrayPointer, int sizeOfArray)
{
    for (int index = 0; index < sizeOfArray; index++)
    {
        printf("%d  ", *(arrayPointer + index));
    }
}

int sortArray(int *arrayPointer, int sizeOfArray)
{
    int found = 0;
    for (int index = 0; index < sizeOfArray - 1; index++)
    {

        if (*(arrayPointer + index) > *(arrayPointer + index + 1))
        {
            swapElements((arrayPointer + index), (arrayPointer + index + 1));
            found = 1;
            if (viewProcedure == 1)
            {
                printf("Sorted once -> ");
                printArray(arrayPointer, sizeOfArray);
                printf("\n");
            }
        }
    }

    if (found == 1)
    {
        sortArray(arrayPointer, sizeOfArray); // re-check and sort if there are existing descending pairs of 2
    }
}

int main()
{
    int sizeOfArray;

    printf("PROGRAM TO SORT AN ARRAY - BUBBLE SORT\nBy - Ashwin Sharma");
    printf("\n____________________________\n");

    // Input the array size
    printf("\nEnter the size of array : ");
    scanf("%d", &sizeOfArray);
    printf("\n");

    // Initialise the suitable array and populate it
    int masterArray[sizeOfArray], buffer;
    printf("\nThe size of the array is : %d \nBytes in memory, occupied by this array is = %d\nBecause one element ( here int ) occuppies 4 bytes\n\n", sizeOfArray, sizeof masterArray);

    for (int index = 0; index < (sizeof masterArray) / 4; index++)
    {
        printf("Enter element at index %d : ", index);
        scanf("%d", &buffer);
        masterArray[index] = buffer;
    }

    printf("The original array, that you just framed = ");
    printArray(&masterArray, sizeOfArray);
    printf("\n\n");

    printf("Do you want to see the procedure of sorting? [ yes = 1 | no = 0 ( default ) ] : ");
    scanf("%d", &viewProcedure);

    // Sorting the array
    sortArray(&masterArray, sizeOfArray);
    printf("\n\nTHE SORTED ARRAY IS : ");
    printArray(&masterArray, sizeOfArray);

    printf("\nHit enter to exit console...");
    getch();
    return 0;
}