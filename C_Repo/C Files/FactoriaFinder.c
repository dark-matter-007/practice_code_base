#include <stdio.h>

int getFactorial(int n)
{
    if (n == 1)
    {
        return n;
    }
    else
    {
        return n * getFactorial(n - 1);
    }
}

int main()
{
    printf("Enter the number to find factorial of : ");
    int buffer;
    scanf("%d", &buffer);

    printf("The factorial is : %d", getFactorial(buffer));
}