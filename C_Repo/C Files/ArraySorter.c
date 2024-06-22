#include <stdio.h>

int *getPointerToSortedArray(int sizeOfArray, int *masterArray[100])
{
    int thisIndexElement, nextIndexElement, buffer;
    for (int index = 0; index < sizeOfArray; index++)
    {
        thisIndexElement = *(masterArray + index);
        nextIndexElement = *(masterArray + index + 1);
        // Swap the elements if they are not in ascending order
        if (thisIndexElement > nextIndexElement)
        {
            buffer = *(masterArray + index);
            *(masterArray + index) = *(masterArray + index + 1);
            *(masterArray + index + 1) = buffer;
            return getPointerToSortedArray(sizeOfArray, masterArray);
        }
        else
        {
            return 0;
        }
    }
}

int main()
{

    int buffer, masterArray[100], sizeOfArray = 100;

    printf("PROGRAM TO SORT AN ARRAY IN ASCENDING ORDER");
    printf("__________________________________________");

    // Taking the size of the array
    printf("Enter the size of the array : ");
    scanf("%d", &sizeOfArray);

    // Taking the input of elements
    for (int index = 0; index < sizeOfArray; index++)
    {
        printf("Enter element %d : ", index);
        scanf("%d", &buffer);

        for (int arrayIndex = 0; arrayIndex <= sizeOfArray; arrayIndex++)
        {
            masterArray[arrayIndex] = buffer;
        }
    }

    // Now sorting the elements
    int *sortedArrayPointer = getPointerToSortedArray(sizeOfArray, % masterArray);
    printf("The elements of this array after sorting are: \n");

    for (int i = 0; i < sizeOfArray; i++)
    {
        printf("%d  ", *(sortedArrayPointer + i));
    }

    return 0;
}