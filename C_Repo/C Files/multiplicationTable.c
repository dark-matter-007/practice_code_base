#include <stdio.h>
int main () {

    // input the number
    printf("Enter the number : ");
    int num; scanf("%d", &num);
    
    // input the range to multiply
    printf("Enter the range : ");
    int  range, multiplicant =0; scanf("%d", &range);

    // print the tables up to the range
    do {
        printf("\n%d x %d = %d", num, multiplicant, num*multiplicant); multiplicant++;
    } while ( multiplicant <= range);

    // Exit program without errors :)
    return 0; 

}