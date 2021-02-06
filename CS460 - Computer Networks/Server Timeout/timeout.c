#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void timeoutHandler(int signo);

int main() {
    printf("\nPID: %d\n", getpid());

    for (;;) {
        signal(SIGALRM, timeoutHandler);
        alarm(1);
        pause();
    }
}

void timeoutHandler(int signo) {
    printf("\ntimeout occured!");
}
