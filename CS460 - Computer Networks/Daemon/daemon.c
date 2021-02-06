//
//  daemon.c
//  Daemon
//
//

#include "daemon.h"

void daemon_init(void) {
    pid_t pid;
    int file_desc;
    
    // fork off parent process
    if ((pid=fork()) == -1) {
        perror("ERROR FORKING");
        exit(EXIT_FAILURE);
    }
    else if (pid > 0) {
        // this is the parent, exit
        //exit(EXIT_SUCCESS);
    }
    
    // make the child process group leader
    if (setpgrp() == -1) {
        perror("ERROR setpgrp()");
        exit(EXIT_FAILURE);
    }
    
    // close stdin, stdout, and stderr before the second fork
    // so that we don't inherit those file descriptors
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
    
    // open syslog
    setlogmask(LOG_MASK(LOG_NOTICE));
    openlog("DAEMON", LOG_CONS | LOG_PID | LOG_NDELAY, LOG_DAEMON);
    
    // change into the working directory
    if ((chdir("/")) < 0) {
        syslog(LOG_NOTICE, "DAEMON WITH PID %d chdir() FAILED, EXIT", getpid());
        exit(EXIT_FAILURE);
    }
    
    // make sure we can access all the files the daemon creates
    umask(0);
    syslog(LOG_NOTICE, "DAEMON WITH PID %d: umask(0)", getpid());
    
    // open stdin, stdout, and stderror to /dev/null as
    // std libs usually assume these are open
    file_desc = open("/dev/null", O_RDWR); // stdin
    dup(file_desc);                        // stdout
    dup(file_desc);                        // stderror
    syslog(LOG_NOTICE, "DAEMON WITH PID %d: stdin/stdout/stderror SET TO NULL DEVICE", getpid());
    
    // handle termination of daemon via catching  SIGUSR1
    signal(SIGUSR1, daemon_exit);
    syslog(LOG_NOTICE, "DAEMON WITH PID %d: READY TO GO ... TERMINATE WITH (KILL %d)", getpid(), getpid());
    
}

void daemon_exit(int sig_number) {
    syslog(LOG_NOTICE, "THE DAEMON WITH PID %d EXITS", getpid());
    closelog();
    exit(EXIT_SUCCESS);
}
