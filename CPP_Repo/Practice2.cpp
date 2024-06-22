#include <iostream>
#include <list>
#include <iomanip>
using namespace std;

int main(void) {
    list <string> library;

    for ( auto i = 0; i <= 10; i++){
        library.push_back("Book " + to_string(i));
    }
    
    cout << "abc" << setfill('*') << setw(10) << "Ashwin" << endl;

    for ( auto element : library ) {
        cerr << "Element : " << setw(8) << element << endl;
    }

    return 0;
}