// WAP to input 2 numbers, then take an input of the number - operation. 
// If the number operation is one, print sum of previously input two numbers, and do the same for multiply, divide and subtract , for values 2,3,4 of operation
#include<stdio.h>
int main(){
  int a,b;

  printf("Enter number 1 : "), scanf("%d", &a);
  printf("Enter number 2 : "), scanf("%d", &b);

  int op;
  printf("Enter number for operation : "), scanf("%d", &op);

  if ( op == 1) {
    printf("The sum of the numbers is : %d", a+b);
  } else {
    printf("Kon hai be tu");
  }

  return 0;

}