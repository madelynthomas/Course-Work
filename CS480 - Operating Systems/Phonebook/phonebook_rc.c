//
//  phonebook_rc.c
//  Phonebook
//
//

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <pthread.h>

/************************************************************************
 * preprocessor directives - define file name to be used for storage
 ************************************************************************/
#define DB ("phone_book.txt")
#define NUM_THREADS 10


/*******************************************
 * type definitions
 ******************************************/
typedef struct phone_record {
    long phone_number;
    char name  [20];
} PhoneRecord;

// Create a new struct to hold the mutex as well as PhoneRecord
typedef struct Phone_Entries {
    PhoneRecord *record; //
    pthread_mutex_t *mtx; //
} PhoneEntries;


/*******************************************
 * function prototype declarations
 ******************************************/
void add_record(struct phone_record* phone_record);
long get_number(char* name);
void remove_record(char* name);
void printDB();
void *data_access(void *record); // New method for accessing the data


/*******************************************
 * auxiliary function prototypes
 ******************************************/
int init_db();
void set_to_record(int fd, int recordNumber);




//-----------------------------------------------------------------------
/*
 * main()
 */
int main(int argc, char** argv) {
    pthread_t threads[NUM_THREADS]; // Create a new array of threads
    int i = 0; // Loop counter
    void *status; // Set a pointer to status
    int rc; // Used for error checking
    int j; // Loop counter
    pthread_mutex_t *lock = malloc(sizeof(pthread_mutex_t)); // Allocate the memory needed
    
    struct phone_record person = { // Create a person from phone record
        9286008799, // Phone number
        "Moody" // Name of person
    };
    
    struct Phone_Entries phone_entry = { // Create a phone entry
        &person, // Put our person in it
        lock // LOCK IT!
    };
    
    if (pthread_mutex_init(lock, NULL) != 0) { // Check if mutex initalized correctly
        printf("\nMutex failed to initialize\n"); // Oh no! We failed to initialize correctly
        return 1; // Return 1
    }
    
    while (i < NUM_THREADS) { // Iterate over the number of threads
        printf("\nCreating threads in main %d\n", i); // Let the user know what we are doing
        rc = pthread_create(&threads[i], NULL, data_access, (void *)&phone_entry); // Creat the threads!
        if (rc) { // Check if it really worked
            printf("Error, return code is %d\n", rc); // Oh no! We failed to create threads...
        }
        i++; // Increment the loop counter
    }
    
    for (j = 0; j < NUM_THREADS; j++) { // Loop to join the threads together
        pthread_join(threads[j], &status); // YES! Status has worked and we have created a thread
    }
    
    add_record(&person); // Add the person one last time
    printDB(); // Print the results
    return 0; // Return 0! Success!
}


//-----------------------------------------------------------------------
/*
 * database access
 */
void *data_access(void *record) {
    struct Phone_Entries *phone_entries = (struct Phone_Entries *)record; // Link our structures
    struct phone_record *person = phone_entries->record; // Link our record to our entries
    
    pthread_mutex_t *lock = phone_entries->mtx; // Link the mutex with a lock
    add_record(person); // Add the person
    pthread_mutex_unlock(lock); // Unlock the locked mutex
    pthread_mutex_lock(lock); // Lock the mutex
    remove_record(person->name); // Remove the record
    pthread_mutex_unlock(lock); // And lastly unlock again
    pthread_exit(NULL); // Exit when NULL
}

//-----------------------------------------------------------------------
/*
 * add an entry
 */
void add_record(PhoneRecord* phone_record) {
    int dbfile = init_db();
    int record_count;
    
    // read number of entries
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &record_count, sizeof(int));
    
    // set pointer after the last entry and append new person
    set_to_record(dbfile, record_count + 1);
    write(dbfile, phone_record, sizeof (PhoneRecord));
    
    // update the record number
    record_count++;
    lseek(dbfile, 0, SEEK_SET);
    write(dbfile, &record_count, sizeof(int));
    
    printf("[add] - added %s, phone number: %ld, number of entries: %d\n", phone_record->name, phone_record->phone_number, record_count);
}



//-----------------------------------------------------------------------
/*
 * get a person from the database
 *
 * returns phone# or -1 if not found
 */
long get_number(char* name) {
    int dbfile = init_db();
    int record_count = 0;
    PhoneRecord phone_record;
    
    // see, how many entries the db has ...
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &record_count, sizeof (int));
    if (record_count == 0) {
        return -1;
    }
    
    // set the pointer to the last entry
    set_to_record(dbfile, record_count);
    // run through all entries towards the beginning, if you find an entry that matches the name, bail out
    while (record_count--) {
        read(dbfile, &phone_record, sizeof (PhoneRecord));
        set_to_record(dbfile, record_count);
        
        if (!strcmp(phone_record.name, name)) {
            return phone_record.phone_number;
        }
    }
    return -1;
}



//-----------------------------------------------------------------------
/*
 * remove a person from the database, given the name
 * if the name is not found, don't do anything
 */
void remove_record(char* name) {
    int dbfile = init_db();
    int record_count = 0;
    int total = 0;
    PhoneRecord phone_record, last_record;
    
    // how many entries altogether?
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &total, sizeof(int));
    if (total == 0) {
        return;
    }
    
    record_count = total;
    // read the last entry, this might be used to "fill a gap"
    set_to_record(dbfile, total);
    read(dbfile, &last_record, sizeof(PhoneRecord));
    
    // go through all entries, starting at the end
    // if you find the person, override the entry with last person's entry and return
    do {
        set_to_record(dbfile, record_count);
        read(dbfile, &phone_record, sizeof (PhoneRecord));
        
        if (!strcmp(phone_record.name, name)) {
            // are we at the end? we don't need to override the last person with itself ...
            // when we have many entries, we might just omit this
            if (total != record_count) {
                set_to_record(dbfile, record_count);
                write(dbfile, &last_record, sizeof (PhoneRecord));
            }
            lseek(dbfile, 0, SEEK_SET);
            total--;
            write(dbfile, &total, sizeof (int));
            truncate(DB, (sizeof(int)+(total*sizeof(PhoneRecord))));
            printf("[remove] - person %s removed, %d record(s) remaining\n", phone_record.name, total);
            
            return;
        }
    } while(--record_count);
        
    printf("[remove] - person %s is not in the database\n", name);
}



//-----------------------------------------------------------------------
/*
 * Prints all of the people and id numbers in the database
 *
 */
void printDB() {
    int dbfile = init_db();
    int record_count = 0;
    PhoneRecord phone_record;
    
    // see, how many entries the db has ...
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &record_count, sizeof (int));
    if (record_count == 0) {
        return;
    }
    
    // set the pointer to the last entry
    set_to_record(dbfile, record_count);
    // run through all entries
    while (record_count--) {
        read(dbfile, &phone_record, sizeof (PhoneRecord));
        set_to_record(dbfile, record_count);
        
        printf("Name: %s, \t\tNumber: %ld\n", phone_record.name, phone_record.phone_number);
    }
}


//-----------------------------------------------------------------------
/*
 * aux function, initializes the database file (if it is not there)
 *
 * return the filedescriptor of the opened db file
 */
int init_db() {
    int fd;
    int record_count = 0;

    // init of dbfile, if not there yet
    if (access(DB, F_OK) != 0) {
        // the file is not accessible, create it ...
        fd = open(DB, O_RDWR | O_CREAT | O_EXCL, S_IRUSR | S_IWUSR);
        // initialize the beginning of the file, which contains the number of structs the db contains
        write(fd, &record_count, sizeof(int));
        
        return fd;
    }

    // the file is there, just return the fd
    return open(DB, O_RDWR);
}


//-----------------------------------------------------------------------
/*
 * aux function to help position the internal file pointer
 * take the record number and put the pointer to that position
 */
void set_to_record(int fd, int recordNumber) {
    lseek(fd, (recordNumber - 1) * sizeof (PhoneRecord) + sizeof(int), SEEK_SET);
}
