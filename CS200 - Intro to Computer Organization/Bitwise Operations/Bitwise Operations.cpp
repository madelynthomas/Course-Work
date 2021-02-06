//
//  main.cpp
//  Bitwise Ops
//
//

#include <iostream>
#include <string>
using namespace std;

// Pre-declare functions
unsigned bitwise_and(unsigned, unsigned);
unsigned bitwise_or(unsigned, unsigned);
unsigned bitwise_xor(unsigned, unsigned);
unsigned bitwise_complement(unsigned, unsigned);
unsigned bitwise_right_shift(unsigned, unsigned);
unsigned bitwise_left_shift(unsigned, unsigned);
unsigned bitwise_to_decimal(unsigned);
string decimal_to_binary(unsigned);

// Global variables
unsigned a;
unsigned b;
unsigned c;

// Bitwise functions
unsigned bitwise_and(unsigned a, unsigned b)
{
    c = (a & b);
    return (a & b);
}

unsigned bitwise_or(unsigned a, unsigned b)
{
    c = (a | b);
    return (a | b);
}

unsigned bitwise_xor(unsigned a, unsigned b)
{
    c = (a ^ b);
    return (a ^ b);
}

unsigned bitwise_complement(unsigned a)
{
    c = (~a);
    return (~a);
}

unsigned bitwise_right_shift(unsigned a, unsigned b) {
    c = (a >> b);
    return (a >> b);
}

unsigned bitwise_left_shift(unsigned a, unsigned b)
{
    c = (a << b);
    return (a << b);
}

/*
 This recursive function converts the decimal to binary. The function takes in an
 unsigned variable c that is the solution for the below function.
*/
string decimal_to_binary(unsigned c)
{
    if (c == 0)
        return ("0");
    if (c == 1)
        return ("1");
    if (c % 2 == 0)
        return (decimal_to_binary(c / 2) + "0");
    else
        return (decimal_to_binary(c / 2) + "1");
}

/*
 The main function of this program welcomes the user to the program and askes for two
 variables (a and b) and returns the answer to varies bitwise functions and shifts.
 It also takes the answers from those equations and converts them to decimal, binary,
 and hexadecimal.
*/
 
int main(int argc, const char * argv[])
{
    cout << "Welcome to the Bitwise OPS Calculator!" << endl;   // Welcome user
    cout << endl;
    cout << "Please enter a number for A: ";                    // Ask for first input
    cin >> a;                                                   // Store first input as a
    cout << "Please enter a number for B: ";                    // Ask for second input
    cin >> b;                                                   // Store second input as b
    cout << endl;
    
    cout << "a & b = " << bitwise_and(a, b) << endl;            // Start Bitwise AND display answer
    cout << "Decimal: " << dec << c << endl;                    // Display answer as decimal
    cout << "Binary: " << decimal_to_binary(c) << endl;         // Display answer as binary
    cout << "Hexadecimal: " << hex << c << endl;                // Display answer as hexadecimal
    cout << endl;                                               // End of Bitwise AND
    
    cout << "a | b = " << bitwise_or(a, b) << endl;             // Start Bitwise OR
    cout << "Decimal: " << dec << c << endl;                    // Display answer as decimal
    cout << "Binary: " << decimal_to_binary(c) << endl;         // Display answer as binary
    cout << "Hexadecimal: " << hex << c << endl;                // Display answer as hexadecimal
    cout << endl;                                               // End of Bitwise OR
    
    cout << "a ^ b = " << bitwise_xor(a, b) << endl;            // Start Bitwsie XOR
    cout << "Decimal: " << dec << c << endl;                    // Display answer as decimal
    cout << "Binary: " << decimal_to_binary(c) << endl;         // Display answer as binary
    cout << "Hexadecimal: " << hex << c << endl;                // Display answer as hexadecimal
    cout << endl;                                               // End of Bitwise XOR
    
    cout << "~a = " << bitwise_complement(a) << endl;           // Start Bitwise COMPLEMENT
    cout << "Decimal: " << dec << c << endl;                    // Display answer as decimal
    cout << "Binary: " << decimal_to_binary(c) << endl;         // Display answer as binary
    cout << "Hexadecimal: " << hex << c << endl;                // Display answer as hexadecimal
    cout << endl;                                               // End of Bitwise COMPLEMENT
    
    cout << "a >> b = " << bitwise_right_shift(a, b) << endl;   // Start of Bitwise RIGHT-SHIFT
    cout << "Decimal: " << dec << c << endl;                    // Display answer as decimal
    cout << "Binary: " << decimal_to_binary(c) << endl;         // Display answer as binary
    cout << "Hexadecimal: " << hex << c << endl;                // Display answer as hexadecimal
    cout << endl;                                               // End of Bitwise RIGHT-SHIFT
    
    cout << "a << b = " << bitwise_left_shift(a, b) << endl;    // Start of Bitwise LEFT-SHIFT
    cout << "Decimal: " << dec << c << endl;                    // Display answer as decimal
    cout << "Binary: " << decimal_to_binary(c) << endl;         // Display answer as binary
    cout << "Hexadecimal: " << hex << c << endl;                // Display answer as hexadecimal
    cout << endl;                                               // END of Bitwise RIGHT-SHIFT
    
    return 0;
}
