// Practice Question

#include <stdio.h>
int main () {
    
    int myArray[6] = {2,3,4,5,6}; // 5 elements are given, the 6th will be 0 by default

    // printing the array
    printf("The initial array is : ");
    for ( int index = 0; index <= 5; index++ ) {
        printf("%d ", myArray[index]);
    }

    // swapping values
    // for ( long long unsigned int index = 0; index <= sizeof(myArray); index++) {
    //     myArray[index+1] = *arrayPointer+index;
    // }
    for ( int index = 5; index >= 0; index--) {
        myArray[index] = myArray[index-1];
    }

    // printing the swapped array
    printf("\n\nThe swapped array is : ");
    for ( int index = 0; index <= 5; index++ ) {
        printf("%d ", myArray[index]);
    }


    return 0;
}