//
//  phonebook_race.c
//  Phonebook
//
//

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

/************************************************************************
 * preprocessor directives - define file name to be used for storage
 ************************************************************************/
#define DB ("phone_book.txt")

#ifdef LOCK

void unlock() {
    unlink(LOCK)
}

void lock() {
    int fd;
    while ((fd = open(LOCK, O_CREAT|O_EXCL)) == -1);
    close(fd);
}

#else

void unlock();
void lock();

#endif


/*******************************************
 * type definitions
 ******************************************/
typedef struct phone_record {
    long phone_number;
    char name  [20];
} PhoneRecord;


/*******************************************
 * function prototype declarations
 ******************************************/
void add_record(struct phone_record* phone_record);
long get_number(char* name);
void remove_record(char* name);
void printDB();


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
    if (strcmp(argv[1], "print") == 0) {
        printDB();
    }
    else if (strcmp(argv[1], "add") == 0) {
        struct phone_record(person);
        strcpy(person.name, argv[2]);
        person.phone_number = atol(argv[3]);
        add_record(&person);
    }
    else if (strcmp(argv[1], "remove") == 0) {
        remove_record(argv[2]);
    }
    else if (strcmp(argv[1], "addremove") == 0) {
        struct phone_record(person);
        strcpy(person.name, argv[2]);
        person.phone_number = atol(argv[3]);
        add_record(&person);
        remove_record(argv[2]);
    }
    else if (strcmp(argv[1], "get") == 0) {
        long num = get_number(argv[2]);
        if (num < 0) {
            printf("No contact with name: %s", argv[2]);
        }
    }
}



//-----------------------------------------------------------------------
/*
 * add an entry
 */
void add_record(PhoneRecord* phone_record) {
    int dbfile = init_db();
    int record_count;
    
    lock();
    
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
    
    unlock();
    
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
    
    unlock();
    
    // see, how many entries the db has ...
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &record_count, sizeof (int));
    if (record_count == 0) {
        unlock();
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
    unlock();
    
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
    
    lock();
    
    // how many entries altogether?
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &total, sizeof(int));
    if (total == 0) {
        unlock();
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
            
            unlock();
            
            printf("[remove] - person %s removed, %d record(s) remaining\n", phone_record.name, total);
            
            return;
        }
    } while(--record_count);
    
    unlock();
    
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
    
    lock();
    
    // see, how many entries the db has ...
    lseek(dbfile, 0, SEEK_SET);
    read(dbfile, &record_count, sizeof (int));
    if (record_count == 0) {
        unlock();
        return;
    }
    
    // set the pointer to the last entry
    set_to_record(dbfile, record_count);
    // run through all entries
    while (record_count--) {
        read(dbfile, &phone_record, sizeof (PhoneRecord));
        set_to_record(dbfile, record_count);
        
        unlock();
        
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
        
        unlock();
        
        return fd;
    }

    unlock();
    
    // the file is there, just return the fd
    return open(DB, O_RDWR);
}


//-----------------------------------------------------------------------
/*
 * aux function to help position the internal file pointer
 * take the record number and put the pointer to that position
 */
void set_to_record(int fd, int recordNumber) {
    lock();
    lseek(fd, (recordNumber - 1) * sizeof (PhoneRecord) + sizeof(int), SEEK_SET);
    unlock();
}
