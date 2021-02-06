//
//  reverse.c
//
//

// Included libraries
#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>

// This main method reverses a file to a new file by reversing the bytes
int main(int argc, char *argv[]) {
    // Load in function varaibles
    char buffer;
    int destination_file;
    int source_file;
    long file_size;
    long file_incr;
    long i;
    
    // Skip the path to the file
    argv++;
    // Load in the source file
    source_file = open(*argv++, 0400);
    // Load in the destination file
    destination_file = creat(*argv++, 0700);
    // Get the file size using lseek
    file_size = lseek(source_file, (off_t) 0, SEEK_END);
    
    // Read the file backwards
    for(i = file_size - 1; i >= 0; i--) {
        // Start with the source file
        lseek(source_file, (off_t) i, SEEK_SET);
        // Read the source file
        file_incr = read(source_file, &buffer, 1);
        // Write the source file backwards into the destination file
        file_incr = write(destination_file, &buffer, 1);
    }
    
    // Used for testing to know it sucessfully ran
    //write(STDOUT_FILENO, "File Reversed\n", 14);
    // Close the source file
    close(source_file);
    // Close the destination file
    close(destination_file);
    
    // Return EXIT_SUCCESS
    return 0;
}
