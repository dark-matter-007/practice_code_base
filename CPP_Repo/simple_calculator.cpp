#include <iostream>
using namespace std;

int main () {
    int a, b; float result; bool cont = true; char op; // initialising all the variables
    cout << "::: | HERE'S THE PROGRAM FOR CLI OPERATIONS |:::";
    cout << endl << endl;

    do
    {
        cout << endl << endl << "Enter num 1: ";
        cin >> a;
        cout << endl << "Enter the operation : ";
        cin >> op;
        cout << endl << "Enter num 2 : ";
        cin >> b;

        switch (op) { // check op and insert the value in it accordingly
            case 'a' : // for add
                result = a + b;
                break;

            case 's' : // for subtract
                result = a - b;
                break;

            case 'm' : // for multiply
                result = a * b;
                break;

            case 'd' : // for quotient of  a/b
                result = a / b;
                break;

            case 'r' : // for remainder of a/b
                result = a % b;
                break;

            case 'p' : // for power
                result = a ^ b;
                break;

            default :
                cout << "The Operation was not identified.";
                continue;
                break;
        }

        cout << endl << result << " is the answer." ;

        // whether to loop the whole process or just to quit now
        cout << "Continue further ?\n" ;
        char a; cin >> a;
        if ( a == 'n') { 
            cont = false; 
            break; 
        }
    } while ( cont==true );
    
    cout << "\n\n EXITTED THE LOOP SUCCESSFULLY";
    char useless; cin.ignore(); cin.get(useless);
    cout << endl << endl << endl;
    return 0;
}