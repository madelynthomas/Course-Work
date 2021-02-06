//
// server.c
// Daemon
//
//


#include "server.h"

void* thread(void* arg) {
    char input[100];
    long bytes_read;
    int client = *(int *)arg;
    
    // send the data to the server on a thread
    do {
        bytes_read = recv(client, input, sizeof(input), 0);
        send(client, input, bytes_read, 0);
    }
    
    // break connection if bye is inserted
    while (strncmp(input, "bye\r", 4) != 0);
    
    close(client);
    
    return arg;
}

int mainServer(int argc, char *argv[]) {
    int sd;
    struct sockaddr_in addr;
    
    // check if socket was created
    if ((sd = socket(PF_INET, SOCK_STREAM, 0)) < 0) {
        perror("ERROR: FAILURE TO CREATE SOCKET");
        exit(EXIT_FAILURE);
    }
    
    // initalize the connection through the sin library
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8888);
    addr.sin_addr.s_addr = INADDR_ANY;
    
    // check if bind was created
    if (bind(sd, (struct sockaddr*)&addr, sizeof(addr)) != 0) {
        perror("ERROR: FAILURE TO BIND");
        exit(EXIT_FAILURE);
    }
    
    // check if port is listening
    if (listen(sd, 20) != 0) {
        perror("ERROR: FAILURE TO LISTEN");
        exit(EXIT_FAILURE);
    }
    
    // the big loop
    while (TRUE) {
        int client;
        unsigned int addr_size = sizeof(addr);
        pthread_t new_thread;
        client = accept(sd, (struct sockaddr*)&addr, &addr_size);
        printf("Connected: %s:%d\n", inet_ntoa(addr.sin_addr), ntohs(addr.sin_port));
        
        // check if thread was created
        if (pthread_create(&new_thread, NULL, thread, &client) != 0) {
            perror("ERROR: FAILURE TO CREATE THREAD");
            exit(EXIT_FAILURE);
        }
        
        // thread successfully created
        else {
            pthread_detach(new_thread);
        }
    }
}

