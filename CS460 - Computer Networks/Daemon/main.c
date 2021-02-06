//
//  main.c
//  Daemon
//
//

#include "daemon.h"
#include "main.h"

int main(int argc, char *arg[]) {
    daemon_init();
    while (TRUE) {
        syslog(LOG_NOTICE, "DAEMON IS WRITING TO SYSLOG");
        sleep(5);
    }
    EXIT_SUCCESS;
}
