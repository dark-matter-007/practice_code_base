#include <stdio.h>

int main()
{
    printf("PROGRAM TO PRINT FIBONACCI SERIES\n\n");

    printf("Print fibonacci series up to? : ");
    int range;
    scanf("%d", &range);

    int thisElement, prevElement = 1, prev2Element = 0;

    while (1)
    {
        thisElement = prev2Element + prevElement;
        if (thisElement > range)
        {
            break;
        }
        prev2Element = prevElement;
        prevElement = thisElement;
        printf("%d  ", thisElement);
    }

    return 0;
}