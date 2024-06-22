#include <stdio.h>

void clearScreen() {
    for ( int i = 0; i <= 100; i++ ) {
        printf("\n");
    }
}

int main()
{

    // struct Teacher
    // {
    //     char name;
    //     int serial_num;
    // };

    // struct Student
    // {
    //     char structChar;
    //     int structInteger;
    //     char teachername;

    //     struct Student * Teacher;
    // };
 
    // struct Student thisStudent;
    // thisStudent.Teacher->structChar = 'D';

    // thisStudent.structChar = 'A';

    // printf("The name of the student is %c and the teacher is %c", thisStudent.structChar, thisStudent.Teacher->structChar);
    
    // struct MyStruct thisStructure;

    // thisStructure.structChar = 'A';
    // thisStructure.structInteger = 77;

    // printf("The value for structChar is : %c \n", thisStructure.structChar);
    // printf("The value for structChar is : %d", thisStructure.structInteger);

    int myVar = 23;
    int* myPointer = &myVar;

    clearScreen();
    printf("The value at the address of myPointer is %d", *myPointer);
    printf("The value of myVar is also : %d \n\n", myVar);
    printf("\nThe relative-index address stored in the myPointer is : %d", myPointer);
    printf("\nThe proof that the address does not change during execution : %d", myPointer);
    printf("\nThe unsigned int type address stored in myPointer is : %u", myPointer);

    printf("\n\nThe address of the variable myVar is : %u, just the same as myPointer : %u", &myVar, myPointer);
    printf("\nand it is not the same as that of the address where myPointer variable is stored : %u", &myPointer);

    return 0;
}