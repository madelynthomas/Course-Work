//
//  daemon.h
//  Daemon
//
//

#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <syslog.h>
#include <string.h>
#include <signal.h>

/******************************
 *    function prototypes
 ******************************/

void daemon_init(void);
void daemon_exit(int sig_number);
