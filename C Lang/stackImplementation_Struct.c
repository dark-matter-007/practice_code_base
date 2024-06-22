#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define MAX 5 // Defining maximum size of stack

typedef struct Stack
{
    int top;
    int *arr;
} Stack;

int main()
{
    Stack* masterStack = createStack();

    while (1)
    {
        int userChoice = printMenuAndGetChoice();

        switch (userChoice)
        {
        case 1:
            push(masterStack, getElementToPush());
            break;

        case 2:
            printf("Popped the element -> %d", pop(masterStack));
            break;

        case 3:
            printf("The element at top is  -> %d", peek(masterStack));
            break;

        case 4:
            printf("The stack is :\n"), display(masterStack);
            break;

        case 5:
            printf("Coming soon...\n");
            break;

        default:
            break;
        }

        printf("Hit enter to continue...");
        getch();
    }
    return 0;
}

// USER INTERFACE
int printMenuAndGetChoice()
{
    printf("Input : Operations\n");
    printf("1 : Push\n");
    printf("2 : Pop\n");
    printf("3 : Peek element\n");
    printf("4 : Display stack\n");
    printf("5 : Check overflow and underflow\n");
    printf("Enter your choice here : ");
    static int userInput;
    return scanf("%d", &userInput), userInput;
}

int getElementToPush()
{
    printf("Enter the element to push : ");
    static int buffer;
    return scanf("%d", &buffer), buffer;
}

// STACK OPERATIONS

// This function returns a pointer to the stack.
Stack* createStack()
{
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    stack->top = -1;
    stack->arr = (int *)malloc(MAX * sizeof(int)); // get pointer to the first element after allocating the memory to array of max size
    return stack;
}

void push(Stack *stack, int val)
{
    if (stack->top == MAX - 1)
    {
        printf("Could not push the element : %d to the stack...\n", val);
        printf("ERROR >> Stack Overflow\n\n");
    }
    else
    {
        stack->top++;
        stack->arr[stack->top] = val;
    }
}

int pop(Stack *stack)
{
    if (stack->top == -1)
    {
        printf("\n\nERROR >> Stack Underflow");
        exit(1);
    }
    else
    {
        return stack->arr[stack->top--];
    }
}

int peek(Stack *stack)
{
    if (stack->top == -1)
    {
        printf("\n\nERROR >> Stack Underflow\n");
        exit(1);
    }
    else
    {
        return stack->arr[stack->top];
    }
}

void display(Stack *stack)
{
    if (stack->top == -1)
        printf("EmptyStack\n");
    else
    {
        for (int i = stack->top; i >= 0; i--)
            printf("%d   ", stack->arr[i]);
        printf("\n");
    }
}

int isfull(Stack *stack)
{
    if (stack->top == MAX - 1)
        return 1;
    else
        return 0;
}

int isempty(Stack *stack)
{
    if (stack->top == -1)
        return 1;
    else
        return 0;
}