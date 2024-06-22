#include <stdio.h>

int marks_in_subject_1, marks_in_subject2, marks_in_subject_3;

int main () {

    printf ("Enter the marks of English, Science and Maths ; pressing enter after each  .. \n");
    scanf("%d%d%d", &marks_in_subject_1, &marks_in_subject2, &marks_in_subject_3); // We have input the marks for each subject from the user

    
    printf("%d is the average of your marks in the three subjects ", (marks_in_subject_1 + marks_in_subject2 + marks_in_subject_3)/3 );
    return 0;
}