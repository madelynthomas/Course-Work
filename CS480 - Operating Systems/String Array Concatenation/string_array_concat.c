//
//  string_array_concat.c
//
//

// Initalize libraries
#include <stdio.h>
#include <stdlib.h>

// Pre-declare functions
char* string_array_concat(char** array);

// Driver method. Takes in command-line arguments and increments
// and appends them to each other with string_array_concat
int main(int argc, char** argv) {
    argv++;
    while (*argv) {
        printf("%s ", string_array_concat(argv++)); // Increment the next argv to pass
    }
    return 0; // Application passed
}

char* string_array_concat(char** array) {
    char* mem_bank = (char*)malloc(sizeof(char)*80); // Initalize memory to store strings
    char* ptr_to_string = *array; // Initalize the pointer to the string and set it equal to array
    char* start_of_array = mem_bank; // Remember the start of the memmory
    while (*ptr_to_string) { // Iterate till we see the end of a string
        *mem_bank = *ptr_to_string; // Store the character in the memory
        ptr_to_string++; // Increment to next character
        mem_bank++; // Increment to next string in memory
    }
    return start_of_array; // Take us back to the start of the array
}
