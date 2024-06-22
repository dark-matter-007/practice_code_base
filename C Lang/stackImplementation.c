#include <stdio.h>
#define MAX 10 // Defining maximum size of stack

int stack[MAX], top = -1;

int main()
{
    push(23);
    push(27);
    push(28);
    printf("The last element is : %d", pop());

    return 0;
}

// USER INTERFACE
void printMenu()
{
    printf("Here are the possible operations on a stack : ");
    printf("1 : Push element");
    printf("2 : Pop element");
    printf("3 : Peek element");
    printf("4 : Display whole stack");
}

// STACK OPERATIONS
void push(int val)
{
    if (top == MAX - 1)
        printf("Stack Overflow\n");
    else
    {
        top++;
        stack[top] = val;
    }
}

int pop()
{
    if (top == -1)
        printf("Stack Underflow\n");
    else
        return stack[top--]; // return top element and reduce top index by 1 after it.
}

int peek()
{
    if (top == -1)
        printf("Stack Underflow\n");
    else
        return stack[top];
}

void display()
{
    if (top == -1)
        printf("Stack is empty\n");
    else
    {
        for (int i = top; i >= 0; i--)
            printf("%d ", stack[i]);
        printf("\n");
    }
}

int isfull()
{
    if (top == MAX - 1)
        return 1;
    else
        return 0;
}

int isempty()
{
    if (top == -1)
        return 1;
    else
        return 0;
}

int peekElement(int index)
{
    if (index == MAX || index < 0)
    {
        printf("OutOfBoundsException");
    }
    else
    {
        return stack[index];
    }
}