//
//  main.cpp
//  RLE Compression
//
//

// Include following libraries
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>

// Pre-declare methods
void compress(char* data, int count, FILE* outfile);
void decompress(char* data, int count, FILE* outfile);
char* readFileData(char* filename, int* count_ptr);

/*
 Method: main
 Parameter(s): int num_args, char* arg_values[]
 
 Runs the code to compress/decompress the data pulled from
 test.txt to form a new file extension .RLE. RLE converts
 the string into the following example:
    MISSISSIPPI
    1M1I2S1I2S1I2P1I
 
 Where the given numbers before the letters is the total
 number of occurances the letter appears in the sequence.
*/
int main(int num_args, char* arg_values[] )
{
    if (num_args != 2)
    {
        printf("Usage: rle filename (produces filename.rle)\n");
        printf(" rle filename.rle (produces filename.plain)\n");
        exit(1);
    }
    
    char* input_filename = arg_values[1];
    
    // read the file data into an array
    int count;
    char* data = readFileData(input_filename, &count);
    
    // Call compress() or decompress().
    FILE* outfile;
    int len = strlen(input_filename);
    if (len < 4 || strcmp(input_filename + (len - 4), ".rle") != 0)
    {
        char output_filename[80];
        strcpy(output_filename, input_filename);
        strcat(output_filename, ".rle" );
        printf("Compressing %s to %s\n", input_filename, output_filename);
        
        outfile = fopen( output_filename, "wb");
        compress(data, count, outfile );
    }
    else
    {
        char output_filename[80];
        strncpy(output_filename, input_filename, len - 4);
        output_filename[len - 4] = 0;
        strcat(output_filename, ".plain");
        printf("Decompressing %s to %s\n", input_filename, output_filename);
        
        outfile = fopen(output_filename, "wb");
        decompress(data, count, outfile);
    }
    
    // Close the output file to ensure data is saved.
    fclose(outfile);
    
    // Free the array we allocated
    delete data;
    
    return 0;
}
/*
 Method: compress
 Parameter(s): char* data, int count, FILE* outfile
 
 Compresses the data by beginning with setting all
 counters and pointers to zero. As it iterates over
 the data it checks to see if any given character
 is repeated 9 or more times. 
 
 If this happens the code breaks and returns an erorr.
 
 If this condition is not met it proceeds to add the
 total number of times the letter appears and advances
 to the next character.
 
 Example run:
 
    Input file: WWWWWWBBBWW
    Output file: 5W3B2W
*/
void compress(char* data, int count, FILE* outfile)
{
    // Initialize counters all to 0
    int char_count = 0;
    char cur_char = data[0];
    // Iterate over the list and count the number of appearances of each character
    for (int i = 0; i < count; ++i)
    {
        if (data[i] == cur_char)
        {
            char_count += 1;
            if (char_count > 9) // Stop iterating if char_count equals 9
            {
                printf("Hey, stop! Count can't exceed 9! \n");
                system("pause");
                break;
            }
        }
        else
        {
            // Print number of times character appears followed by character
            fprintf(outfile, "%d", char_count);
            putc(cur_char, outfile);
            cur_char = data[i];
            char_count = 1;
        }
    }
    // Print number of times character appears followed by character
    fprintf(outfile, "%d", char_count);
    putc(cur_char, outfile); // Write out a single byte of data
}

/*
 Method: decompress
 Parameter(s): char* data, int count, FILE* outfile
 
 Decompresses the data by beginning with setting all
 counters and pointers to zero. As it iterates over
 the data it prints the character n times for its
 occurances.
 
 It proceeds to append the total number of times the
 letter appears and advances to the next character.
 
 Example output:
 
 Input: 5W3B2W
 Output: WWWWWBBBWW
*/
void decompress(char* data, int count, FILE* outfile)
{
    // Iterate over the array and add 2 to the counter every pass
    for (int i = 0; i < count; i+= 2)
    {
        int char_len = data[i] - '0';
        // Iterate over the array as characters are being added to string
        for (int j = 0; j < char_len; j++)
        {
            // Print character n times where n is the number of appearances
            putc(data[i + 1], outfile);
        }
    }
}

char* readFileData(char* filename, int* count_ptr)
{
    // Returns a pointer to an array storing the file data.
    // Sets the variable pointed to by 'count' to contain the file size.
    // Exits the program if the filename doesn't exist.
    FILE* infile = fopen(filename, "rb");
    if ( !infile )
    {
        printf("No such file \"%s\"!\n", filename);
        exit(1);
    }
    
    // Get file size by going to the end of the file, getting the
    // position, and then going back to the start of the file.
    fseek(infile, 0, SEEK_END);
    int count = ftell(infile);
    fseek(infile, 0, SEEK_SET);
    
    // read the data from the file
    char* data = new char[count];
    
    fread(data, 1, count, infile);
    
    fclose(infile);
    
    *count_ptr = count;
    
    return data;
}
