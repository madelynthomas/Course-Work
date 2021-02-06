//
//  phonebook_driver.c
//  Phonebook
//
//

#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv) {
    int status;
    int pid;
    int i;
    char **args;
    
    for (i = 0; i <= 10; i++) {
        if ((pid = fork()) == 0) {
            char num[10];
            sprintf(num, "%d", getpid());
            if (i < 10) {
                execlp("./phonebook", "./phonebook", "addremove", argv[1], num, NULL);
            }
            else {
                execlp("./phonebook", "./phonebook", "add", argv[1], num, NULL);
            }
            break;
        }
    }
    if (pid != 0) {
        for(i = 0; i <= 10; i++) {
            wait();
        }
    }
    execlp("./phonebook", "./phonebook", "print", NULL);
}
