#include<iostream>
#include<iomanip>
using namespace std;
int main () {
    cout << "**** This is the progarm for printing patterns ****\nBy ---> Ashwin Sharma\n\n" ;
    cout << "Enter the pattern you want to print : ";
    char i;
    cin >> i;
    
    switch (i) {
        case 'r' :
            {int width, height;
            cout << "\nSpecify space separated width and height : ";
            cin >> width >> height;

            for ( int row = 0; row < height; row++)
            {
                for ( int column = 0; column < (width*2); column++) 
                {
                    cout << "O";
                }
                cout << endl;
            }

            break;}

        case 'h' :
            {int width, height;
            cout << "\nSpecify space separated width and height : ";
            cin >> width >> height;
            width *= 2;

            for (int row = 0; row < height; row ++)
            {
                for (int column = 0; column < width; column++) {
                    if ( row == 0 || row == (height-1) ) {
                        cout << "*";
                    }
                    else if ( column == 0 || column == (width-1) ) {
                        cout << "*";
                    }
                    else {
                        cout << " ";
                    }
                }
                cout << endl;
            }}

            break;
    }
    return 0;
}