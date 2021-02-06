//
//  string_manipulation.c
//
//

// Included libraries
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Function declarations
char* char_double(char*);
char* char_shift(char*);
char* char_flip(char*);
char** string_central(char* (*fn_array[])(char*), char* test);

// Takes in a string and converts it to double each character
// Example output: RRaaVVEEnn
char* char_double(char* str) {
    int i; // Initialize increment variable i
    char* mem_bank_double = (char*)malloc(sizeof(char)*80); // Allocate my memory
    char* result_of_double = mem_bank_double; // set the result to the beginning of the memory
    //char* ptr_str = str; // Instantiate a ptr_str to str to keep the pointers from overwriting each other
    while(*str != '\0') { // While not on ASCII 0
        for(i = 0; i < 2; i++) { // Iterate till we are less than two
            *mem_bank_double++ = *str; // Store double the contents of ptr_str into memory
        }
        str++; // Increment ptr_str to next character
    }
    return result_of_double; // Return my result
}

// Takes in a string and shifts each subsequent character
// Example output: RSabVWEFno
char* char_shift(char* str) {
    char* mem_bank_shift = (char*)malloc(sizeof(char)*80); // Allocate my memory
    char* result_of_shift = mem_bank_shift; // set the result to the beginning of the memory
    //char* ptr_str = str; // Instantiate a ptr_str to str to keep the pointers from overwriting each other
    while(*str != '\0') { // While not on ASCII 0
        *mem_bank_shift = *str; // Store the contents of ptr_str into memory
        mem_bank_shift++; // Increment memory bank to the next location
        *mem_bank_shift = *str + 1; // Shift over by one character
        mem_bank_shift++; // Increment memory bank to the next location
        str++; // Increment ptr_str to next character
    }
    return result_of_shift;
}

// Takes in a string and flips the casing of the characters
// Example output: rAveN
char* char_flip(char* str) {
    char* mem_bank_flip = (char*)malloc(sizeof(char)*80); // Allocate my memory
    char* result_of_flip = mem_bank_flip; // set the result to the beginning of the memory
    //char* ptr_str = str; // Instantiate a ptr_str to str to keep the pointers from overwriting each other
    while(*str != '\0') { // While not on ASCII 0
        putchar(isupper(*str) ? tolower(*str) : toupper(*str)); // Use ternary to determine what casing to apply on the character
        str++; // Increment ptr_str to next character
        mem_bank_flip++;
    }
    return result_of_flip;
}

char** string_central(char*(*fn_array[])(char*), char* test) {
    char** fn_output_bank = (char**)malloc(sizeof(char*)*4); // Allocate my memory
    char** fn_ptr; // Instantiate a pointer to a vector of pointers
    while (*fn_array) { // While not NULL
        *fn_ptr = (*fn_array)(test); // Grab the first function
        *fn_output_bank = *fn_ptr; // Store the output of the function into memory
        fn_array++; // Increment to the next function
        fn_output_bank++; // Increment to the next spot in memory
    }
    return fn_output_bank; // Return the results
}

int main(void) {
    char* (*fn_array[])(char*) = {char_double, char_shift, char_flip, NULL}; // List of all available functions
    char* test = "RaVen"; // Instantiate my test word
    printf("__%s__\n", string_central(fn_array, test)); // Print the results of string central
    // TESTING
    //printf("%s\n", char_shift(test));
    //printf("%s\n", char_flip(test));
    //printf("%s\n", char_double(test));
    return 0; // Successful program execution
}
