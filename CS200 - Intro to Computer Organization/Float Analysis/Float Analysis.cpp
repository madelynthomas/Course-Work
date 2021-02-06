//
//  main.cpp
//  Float Analysis
//
//

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Pre-declare functions
int get_float_analysis_bit_pattern(float);
void get_sign(int);
int get_exponent(int);
void get_significand(int);
void get_implied(int);
void get_combined(int);
string binary_to_fraction(string, string);
string decimal_to_binary(int, int);

// Global variables
float f;
int bits = *((int*) & f);
int exponent_form;
int i;
int power;
int total_bits = 32;
int mask;
string bit_pattern;
string fraction;
string sig;
string fraction_form;

/*
 Method: get_float_analysis_bit_pattern
 Parameter(s): float f
 
 Returns the bit representation of the float inputted by the user.
*/
int get_float_analysis_bit_pattern(float f)
{
    bits = *((int*) & f);
    return bits;
}

/* 
 Method: get_sign
 Parameter(s): int bits
 
 Shifts the bits to the highest order bit and checks if equal to 0,
 if true, prints 0 (positive) otherwise prints 1 (negative).
 
*/
void get_sign(int bits)
{
    if (bits >> 31 == 0)
        cout << "0 (positive)";
    else
        cout << "1 (negative)";
}

/*
 Method: get_exponent
 Parameter(s): int bits
 
 Returns the bits shifted to the right by 23.
*/
int get_exponent(int bits)
{
    bits = (bits >> 23) & 0xff;
    return bits;
}

/*
 Method: get_signifcand
 Parameter(s): int bits
 
 Prints the bits multiplied by 0x7FFFFF and applies the substring
 to the output window.
*/
void get_signifcand(int bits)
{
    bits = bits * 0x7FFFFF;
    cout << bit_pattern.substr(9, 31);
    sig = bit_pattern.substr(9, 31);
}

/*
 Method: get_implied
 Parameter(s): int bits
 
 Prints out bits multiplied by 0x7FFFFF and applies the substring
 With the implied 1. to form the following output
 1.significand.
*/
void get_implied(int bits)
{
    bits = bits * 0x7FFFFF;
    cout << bit_pattern.substr(9, 31);
}

/*
 Method: get_combined
 Parameter(s): int bits
 
 Takes the number from implied above and displays it
 multipled by the exponent.
*/
void get_combined(int bits)
{
    bits = bits * 0x7FFFFF;
    cout << bit_pattern.substr(9, 31);
}

/*
 Method: decimal_to_binary
 Parameter(s): int bits, int total_bits
 
 Checks to see if bits is equal to 0 if bits equals 0 returns "0",
 if bits equals 1 returns "1", if bits and mask equals 0,
 appends a 1 to bits, otherwise appends a 0 to bits. After complied
 it decrements the total_bits counter by 1.
 */
string decimal_to_binary(int bits, int total_bits)
{
    total_bits -= 1;
    mask = (1 << total_bits);
    if (total_bits == 0)
    {
        if (bits & mask)
            return "1";
        else
            return "0";
    }
    if (bits & mask)
        return "1" + decimal_to_binary(bits, total_bits--);
    else
        return "0" + decimal_to_binary(bits, total_bits--);
}

/*
 Method: binary_to_fraction
 Parameter(s): string fraction, string sig
 
 Iterates over and takes the output from combined and
 checks if the power is 1 and then appends the power to
 the fraction string creating a fraction representation
 of the combined method.
*/
string binary_to_fraction(string fraction, string sig)
{
    fraction = ""; // Intialize fraction as empty string
    cout << "1";
    for (i = 0; i < 23; i++) // Iterate over the bit pattern
    {
        power = pow(2, (i + 1));
        
        if (char(sig[i] == '1'))
            {
                fraction += " + ";
                fraction += "(1/";
                fraction += to_string(power);
                fraction += ")";
            }
    }
    cout << fraction;
    return fraction;
}

/*
 Method: main
 Parameter(s): int argc, const char * argv[]
 
 Displays the the entire float analysis bit pattern
 of any given real number.
 
 It breaks it apart into the following categories:
    Sign
    Exponent
    Significand
    Significand with Implied 1
    Combines the Significand with Exponent
    Displays combined in fraction form
 
*/
int main(int argc, const char * argv[])
{

    cout << "Enter a real number: ";
    cin >> f;
    cout << endl;

    bits = get_float_analysis_bit_pattern(f);          // Converts input into bits
    bit_pattern = decimal_to_binary(bits, total_bits); // Converts bits into binary
    exponent_form = get_exponent(bits);                // Converts bits into exponent

    cout << "Float Analysis" << endl; // Begin Float Analysis
    cout << "  Bit Pattern: ";
    cout << bit_pattern.substr(0, 1) << " " << bit_pattern.substr(1, 8);
    cout << " " << bit_pattern.substr(9, 31) << endl;
    cout << "               S Exponent Significand/Mantissa";
    cout << endl;                     // End get_float_analysis_bit_pattern

    cout << "Sign:          "; // Begin get_sign
    get_sign(bits);
    cout << endl;

    cout << "Exponent:      "; // Begin Exponent
    cout << bit_pattern.substr(1, 8) << " = ";
    get_exponent(bits);

    // Account for the bias by subtracting 127 from exponent
    cout << exponent_form << "; w/bias 127 -> (";
    cout << exponent_form << " - 127) = " << (exponent_form - 127);
    cout << endl;              // End get_exponent

    cout << "Significand:   "; // Begin get_significand
    get_signifcand(bits);
    cout << endl;              // End get_significand

    cout << " w/ implied 1: 1."; // Begin get_implied
    get_implied(bits);
    cout << endl; // End get_implied

    cout << "Combined:      "; // Begin get_combined

    // Catchs the sign and prints + (positive) or - (negative)
    if ((bits >> 31) == 0)
        cout << "+ ";
    else
        cout << "- ";

    cout << "[1.";
    get_combined(bits);

    // Display exponent after removing bias
    cout << "] * 2^" << (exponent_form - 127);
    cout << endl;              // End get_combined

    cout << "  or:          "; // Begin binary_to_fraction

    // Catchs the sign and prints + (positive) or - (negative)
    if ((bits >> 31) == 0)
        cout << "+ ";
    else
        cout << "- ";

    cout << "[";
    binary_to_fraction(fraction, sig);
    cout << "]";
    cout << " * 2^" << (exponent_form - 127); // Remove bias from exponent
    cout << endl; // End binary_to_fraction

    system("pause"); // Hold output on screen till key pressed
}
