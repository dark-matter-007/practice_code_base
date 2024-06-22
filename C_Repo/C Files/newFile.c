#include <stdio.h>

// void mere_function_ka_name(int argument1) {
//     printf("%d was the argument you passed to me", argument1);
// }

// arguement is a variable inside the function for whom, we can give the value, outside the function when we call it
//  int give_me_sum_of ( int num1, int num2 ) { // parameters : arguments :: formal parameters : actual parameters
//      printf("The value of num1 is : %d", num1);
//      printf("The value of num2 is : %d", num2);
//      return num1 + num2;
//  }

// struct teacher
// {
//     int age;
//     char name;
//     int gender;
// };

// struct student
// {
//     int age;
//     char nameKaFirstChar;
//     int male;
//     struct node *teacher; // this is the line to link another structure in this structure. This is called self-referencing
// };

// void swapper ( int variableSimple ) {
//     variableSimple = 45;
//     printf("value at variable is : %d", variableSimple);
// }

// void swapperWithPointer ( int * pointer1 ) {
//     *pointer1 = 45;
//     printf("value at poitner1 is : %d", *pointer1);
// }

int main()
{
    // body
    // mere_function_ka_name(); // function call
    // printf("The sum of 5 and 8 is : %d", give_me_sum_of( 5, 8 ));

    // int abc = 10;
    // swapper(abc);
    // swapperWithPointer(&abc);
    // // printf("\n\n%d is the value of abc", abc);

    // int jatin[5] = {1, 2, 3, 4, 5}; // integer  : 4 bytes , char : 1byte, boolen : 1 bit, double : 8 bytes
    // char arrayOfChars[] = {'A', 's', 'h', 'w', 'i', 'n', 'c'}; // string -> linear collection of characters <- array of characters : \ se start => escape characters

    // printf("The array is : ");
    // for (int index = 0; index < (sizeof jatin) / 4; index++)
    // {
    //     printf("%d  ", jatin[index]);
    // }

    // for (int index = 0; index <= 7; index++)
    // {
    //     printf("%c", arrayOfChars[index]);
    // }

    // struct student Jatin;
    // Jatin.age = 18;
    // Jatin.nameKaFirstChar = 'j';
    // Jatin.male = 1;
    // Jatin.teacher->age = 45;
    // Jatin.teacher.age = 45;

    // printf("The bytes of my jatin is : %d", sizeof jatin);

    int staticArray[] = {1, 2, 2, 3, 45};


    return 0; // there was no error faced while runnig thsi fucntion
}