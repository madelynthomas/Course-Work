//
//  main.cpp
//  Crash Course
//
//

#include <iostream>
using namespace std;

float temp;
char choice;

int main()
{
    cout << "Welcome to the Temperature Converter 3000!\n";
    while (true) {
        cout << "\n";
        cout << "Choose your conversion:" << endl;
        cout << "(F)ahrenheight to Celsius" << endl;
        cout << "(C) Celsius to Fahrenheight" << endl;
        cout << "(Q) Quit" << endl;
        cout << endl;
        cout << "Please enter your choice: ";
        cin >> choice;
        if (choice == 'f')
        {
            cout << endl;
            cout << "Fahrenheight: ";
            cin >> temp;
            temp = ((temp - 32) * (5.0/9.0));
            cout << "In Celsius: " << temp << endl;
            continue;
        }
        else if (choice == 'c')
        {
            cout << endl;
            cout << "Celsius: ";
            cin >> temp;
            temp = ((temp * (9.0/5.0) + 32));
            cout << "In Fahrenheight: " << temp << endl;
            continue;
        }
        else if (choice == 'q')
        {
            cout << endl;
            cout << "Goodbye!" << endl;
            break;
        }
        else
        {
            cout << "Not valid choice. Try again." << endl;
        }
    }
    return 0;
}
