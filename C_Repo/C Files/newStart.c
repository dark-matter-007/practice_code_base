// compiler _. read file -> include : prepare all libraries -> mujhe reserve kitni memory krni h  -> mera main fucntion -> by default main function run krta h

#include <stdio.h>

// int a,b,c; // memory me jagah bana lo in variables ki

// Function is a set of statements that have some special purpose or outcomes.
// Statement is a line of code in any programming language.
// This set of statements is enclosed in curly braces { } and are collectively known as a block

// returnType FunctionName ( formal parameters ) { } // body ya block : functionc all -> block/body -> execute

// data : it is any raw entities : himanshu 23 2023 17 89 true 57.5
// information : It is processed data, that can yield some meaning : name -> Himanshu, weight -> 57.5, male -> true

// "ashwin" : [ 'a' , 's' , 'h' ... 'n' ] : 001, 002, 003, 004

// DataTypes 
// Int
// float
// char
// Boolean : 0 ya 1

// array, list, structure, union

// String -> derived : array of characters

// add : 2+3; subt : 2-3l; multiply 2*3; divide 2 / 3; floor division : 5 // 2 : integer, == , =
int main () {

    int op;
    printf("Enter a number for operation : "), scanf("%d", &op);

    if ( op == 1 ) {
        printf("The value of the operation was one");
    } else if ( op == 2) {
        printf("The value of the operation was two");
    } else {
        printf("The value of the operation was random");
    }

    return 0; 
    // Boolean : True ya False : 1 ya 0 -> Errors were faced -> false : 0 ::: true : 1
}