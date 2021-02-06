#!/usr/bin/env python

"""

A simple client for connecting with a server.

"""

# Include the following libraries
import select
import socket
import sys

# Client method that passes in 2 command arguments
# Run the file under terminal as python client.py <hostname> <port>


def main():
    if(len(sys.argv) < 3):
        print("Usage: python client.py <hostname> <port>")
        sys.exit()  # Break if proper usage not met

    # Declare host as the first command-line argument
    host = sys.argv[1]
    # Declare port as second command-line argument
    port = int(sys.argv[2])

    # Create socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set timeout
    my_socket.settimeout(2)

    # Try and connect to the host and port
    try:
        my_socket.connect((host, port))
        print("Connection established")  # Connection passed
    except Exception:
        # Uh oh, failed to connect to host
        print("Failed to connect")
        sys.exit()  # Break out

    # While we are connected
    while True:
        # Set the socket list to the standed input and my socket
        socket_list = [sys.stdin, my_socket]

        # Read the sockets, write to the sockets, and error sockets
        read_sockets, write_sockets, error_sockets = select.select(
            socket_list, [], [])

        # Iterate over read_sockets
        for sockets in read_sockets:
            # If the sockets have the current socket on the local machine
            if sockets == my_socket:
                # Process input
                data = sockets.recv(4096)
                # If it's not data, it's a terminated character ie ctr+c
                if not data:
                    # Terminate
                    print("Connection terminated")
                    sys.exit()  # Exit
                if isinstance(data, str) == "bye":
                    # If the user puts in bye we terminate as well
                    print("Connection terminated")
                    sys.exit()  # Exit
                else:
                    # Write the data to the server
                    sys.stdout.write(data)
            # Otherwise
            else:
                # Read the message to the input
                message = sys.stdin.readline()
                # Send the input to the server on my socket
                my_socket.send(message)


# Run the client
if __name__ == "__main__":
    main()
