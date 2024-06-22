#include<iostream>
#include<iomanip>
using namespace std;
int main () {
    cout << "Here's a practice program \n\n";
    int marks[] = {23, 88, 45, 90, 99, 100, 21};
    int * marksPointer = marks; // pointer of the first element of above array

    for (int element = 0; element <=  6; element ++) {
        cout << "The " << element << " element of marks[] is " << marks [ element ] << " or " << marksPointer << " + " << element << " from the pointer" << endl; 
    }

    return 0;
}