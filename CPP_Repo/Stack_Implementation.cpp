#include <iostream>
using namespace std;

void clearScreen();
void performTask(int taskInput);

int main() {

        clearScreen();
        cout << "STACK IMPLEMENTATION PROGRAMS" << endl
        << "1. Push in the stack\n2. Pop from stack \n3. Iterate through the stack\n4. Return index of an object\n5. Remove object at index\n\nEnter your choice : ";

        int a;
        cin >> a;
        performTask(a);

        main();

        return 0; 
        //  implies that the program is executed with no errors
}

void clearScreen() {

        for ( int i = 0; i <= 100; i++) {
                cout << "\n";
        }
}

void performTask(int taskInput) {
        switch (taskInput) {
                case 1:
                        cout << "Your chose to push an element";
                        break;
                default:
                        cout << "Unknown input";
        }
}