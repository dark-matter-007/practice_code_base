#include<stdio.h>

int myFunction(int a, int b);

int main () {
    // printf("%d", myFunction(23, 45));

    int myArr[3] = { 1,2,5 };
    int* pointerr = &myArr[0];

    printf("%d", *(pointerr + 2));
    return 0;
}

int myFunction ( int a , int  b ) {
    return a + b;
}