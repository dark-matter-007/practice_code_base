#include <stdio.h>

struct Teacher
{
    int teacherNumber;
    char teacherClass;
};

struct Student
{
    int rollNumber;
    char grade;
    struct Student *Teacher;
};

union Weight
{
    int integerWeight;
    float floatingWeight;
};

union PerformanceOfStudent
{
    int marks;
    char grade;
    double cgpa;
};

int main()
{

    // struct Student Jatin;
    // Jatin.rollNumber = 28;
    // Jatin.grade = 'A';

    // // Jatin.Teacher->teacherNumber = 23;

    // struct Student Shubham;
    // Shubham.rollNumber = 78;
    // Shubham.grade = 'B';

    // printf("The roll number of Jatin is %d", Jatin.rollNumber);
    // printf("The roll grade of Jatin is %c", Jatin.grade);
    // printf("The roll number of Shubham is %d", Shubham.rollNumber);
    // printf("The roll grade of Shubham is %c", Shubham.grade);

    // union Weight myWeightUnion;
    // myWeightUnion.floatingWeight = 10.02;

    // printf("The weight of myWeightUnion is : %f", myWeightUnion.floatingWeight);
    // printf(" and integer value is : %d", myWeightUnion.integerWeight);

    // myWeightUnion.integerWeight = 10;

    // printf("\nThe weight of myWeightUnion is : %d", myWeightUnion.integerWeight);
    // printf(" and float value is : %f", myWeightUnion.floatingWeight);

    //  ARRAY : INT, CHAR

    //  array of structures, array of unions

    // 5 elements : int :: 20 : 4


    // int *dynamicArray;
    // dynamicArray = (int *) malloc(sizeof(int) * 3);

    // int buffer;
    // for (int i = 0; i < 3; i++)
    // {
    //     printf("Enter the value of element %d : ", i);
    //     buffer = scanf("%d", &buffer);
    //     dynamicArray[i] = buffer;
    // }

    // printf("\n\nThe value at index 2 is %d", dynamicArray[2]);
    

    // int dynamicArray[] = {2, 3, 4};

    // dynamicArray[3] = 34;
    // malloc(dynamicArray, (dynamicArray));
    // int *dynamicArrayPointer = &dynamicArray;

    // int buffer;

    // for (int i = 0; i < 5; i++)
    // {
    //     printf("The value at address %d is %d", dynamicArrayPointer, *(dynamicArrayPointer + i));
    // }

    // printf("\n\n%d is the size of my array", sizeof dynamicArray);
    // printf("\n and %d is the address of first element", dynamicArrayPointer);

    // realloc(dynamicArray, sizeof(int) * 5);

    // for (int i = 0; i < 5; i++)
    // {
    //     printf("The value at address %d is %d", dynamicArrayPointer, *(dynamicArrayPointer + i));
    // }

    return 0;
}