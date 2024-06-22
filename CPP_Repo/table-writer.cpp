#include<iostream>
#include<iomanip>

using namespace std;

int main() {
    int up_to_table;
    cout << "****PROGRAM TO PRINT THE TABLES IN THE GIVEN RANGE****" << endl << "By --> Ashwin Sharma" << endl << endl;

    cout << "Enter the table up to which i should print the table : ";
    cin >> up_to_table; cout << endl;

    cout << "              ";
    for (int i = 1; i <= 10; i++) {
        cout << setw(4) << "x" << i << " " ;
    }
    cout << endl << endl; //finally jump to next line

    for (int table = 1; table <= up_to_table; table++) {
        cout <<  "Table of " << setw(3) << table << " : ";
        for (int multiplier = 1; multiplier <= 10; multiplier++){
            cout << setw(4) << table*multiplier << "  "; // to multiply the table number up to 10 and writer with separation... the setw(4) is for reserving 4 digit space on console to ensure equal tablisation
        }
        cout << endl; // so that the writer jumps to next line after printing the table of previous table number
    }

    return 0;

}