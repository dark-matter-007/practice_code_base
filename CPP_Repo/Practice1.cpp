#include <iostream>
using namespace std;

int main (void) {
    string myName = "Ashwin";
    for ( char i : myName ) {
        cout << i << endl;
    }

    string helloWorld = "helloWorld";
    cout << helloWorld.length() << "is the length of helloWorld String";

    string StringArray[5];
    for ( unsigned int index = 1; index <= size(StringArray); index++) {
        StringArray[index-1] = "Ashwin";
    }

    int counter = 0;
    for ( string i : StringArray ) {
        cout << i << " is the " << counter << " element of the string array" << endl;
        ++counter;
    }
     
    cout << "Execution reaches here as well";
    return 0;       // execution completed with no errors
}