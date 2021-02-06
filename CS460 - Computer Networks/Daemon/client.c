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
        // send the packet
        threeAPlus1(server_reply);
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
    }

    // close socket
    close(sock);
    exit(EXIT_SUCCESS);

}

//Zach's Program
int threeAPlus1(int a){
//i can't get the daemon background part working, so i'll have you guise fix that part.
    int count = 0;
    //n the beginning an arbitrary integer number greater than 0
    while(TRUE) {
        printf("Enter a number: ");
        //a = getchar();
        //a -= '0';
        scanf("%d", &a);
        printf("The number you have entered is: %d\n", a);
        while(a != 1){                                   // base case for when it reaches 1
            if(a%2 == 0){                                // check if even
                // If the number is even, it needs to be devided by 2.
                //printf("even \n");
                printf("%d, ", a);
                a = a/2;
                count++;
            }
            else{                                        // check if odd
                //If the number is odd, it is going to be multiplied by 3, after which 1 is added.
                //printf("odd \n");
                printf("%d, ", a);            
                a = (3*a)+1;
                count++;
            }
        }//This algorithm keeps going until the number is finally 1,
        //Your server is supposed to implement the algorithm
        printf("\nThere were %d steps\n", count);         // print the number of steps
        count = 0;
    }
    exit(EXIT_SUCCESS);
}
