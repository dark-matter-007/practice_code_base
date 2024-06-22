#include <stdio.h>
int main()
{
    printf("\nEnter the size of array : ");
    int range, buffer;
    scanf("%d", &range);

    int myArray[range];
    for (int i = 0; i < range; i++)
    {
        printf("Enter element to put at index [ %d ] : ", i),
            scanf("%d", &buffer), myArray[i] = buffer;
    }

    printf("\n\nEnter the element to search for : ");
    int searchArg;
    scanf("%d", &searchArg);

    for (int index = 0; index < range; index++)
    {
        printf("\nChecking ( index [ %d ] = %d ) and %d", index, myArray[index], searchArg);
        if (myArray[index] == searchArg)
        {
            printf("\n\nFound %d at index [ %d ]", searchArg, index);
            return 0;
        }
    }

    printf("\n\nElement was not found");
    return 0;
}