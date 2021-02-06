//
//  server.h
//  Daemon
//
//

#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <resolv.h>
#include <arpa/inet.h>
#include <pthread.h>


#define FALSE 0
#define TRUE !FALSE

/******************************
 *    function prototypes
 ******************************/

void *thread(void *arg);
int main(int argc, char *argv[]);
