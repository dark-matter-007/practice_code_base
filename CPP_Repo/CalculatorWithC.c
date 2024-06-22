#include <stdio.h>
int main () {
    printf ("Hello there! \n\nWELCOME TO MY TINY CALCULATOR...\nBy Ashwin Sharma");
    int a; int b;
    printf("\nInput the first number : "); scanf ("%d", &a);
    printf("Input the second number : "); scanf ("%d", &b);
    printf("Please enter a number that resembles to your operation : \nAdd : 1\nSubtract : 2\nMultiply : 3\nDivide : 4\nFind Remainder : 5\n\nYour input here : ");
    int op;
    scanf ("%d", &op);

    int result;
    switch (op){
        case 1:
            result = a+b;
            printf("The result is : %d", result);
            break;

        case 2:
            result = a-b;
            printf("The result is : %d", result);
            break;

        case 3:
            result = a*b;
            printf("The result is : %d", result);
            break;

        case 4:
            result = a/b;
            printf("The result is : %d", result);
            break;

        case 5:
            result = a%b;
            printf("Ther result is : %d", result);
            break;

        default:
            printf("Unknown command");
    }
    return 0;
}