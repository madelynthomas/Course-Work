//
// client.c
// Daemon
//
//

#include "client.h"

int main(int argc, char *arg[]) {
    int sock;
    struct sockaddr_in server;
    char message[1024];
    char server_reply[1024];

    // create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock == -1) {
        perror("COULD NOT CREATE SOCKET");
    }

    puts("SOCKET CREATED");

    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons(8888);

    // connect to server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("CONNECTION FAILED");
        exit(EXIT_FAILURE);
    }

    puts("CONNECTION ESTABLISHED");

    // the big loop
    while (TRUE) {
        printf("ENTER MESSAGE: ");
        scanf("%s", message);

        // send the data to the daemon server
        if (send(sock, message, strlen(message), 0) < 0) {
            puts("MESSAGE FAILED TO SEND");
            exit(EXIT_FAILURE);
        }

        // receive reply from server
        if (recv(sock, server_reply, 1024, 0) < 0) {
            puts("RESPONSE FAILED TO SEND");
            break;
        }

        // successful transmission
        puts("SERVER: ");
        puts(server_reply);
    }

    // close socket
    close(sock);
    exit(EXIT_SUCCESS);

}
