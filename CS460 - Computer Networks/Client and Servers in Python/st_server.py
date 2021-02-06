#!/usr/bin/env python

"""

A single thread server.

"""

# Include libraries
import socket
import sys

# Main method to run single threaded server


def main():
    # Set the host to localhost
    host = ""
    # Default port to listen on 8888
    port = 8888

    # Create my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Let the user know it was created successfully
    print("Socket created")

    # Try
    try:
        # Accepting incoming connections
        my_socket.bind((host, port))
    # Uh, oh, hit an exception, print the reason for the error
    except socket.error as message:
        print("Binding to socket failed. Error Code: " \
            + str(message[0]) + " Message: " + message[1])
        sys.exit()  # Exit out of st_server

    # The socket has been bounded successfully
    print("Socket bind complete")

    # Listen for incoming connections
    my_socket.listen(10)

    # Let the user know this
    print("Socket now listening")

    # While we are running
    while True:
        connection, address = my_socket.accept()  # Accept incoming connections
        print("Connected with " + address[0] + ":" + str(address[1]))

        while True:
            # Take in the data they input to 4096 characters
            data = connection.recv(4096)
            # Beginning of the odd-even protocol
            try:
                # Bitwise AND to determine if the number is even
                if int(data) & 1 == 0:
                    connection.send("The number given is even!\n")
                # Bitwise AND to determine if the number is odd
                elif int(data) & 1 == 1:
                    connection.send("The number given is odd!\n")
                # If they give me "bye" we break
                if isinstance(data, str) == "bye":
                    break  # Break
            except ValueError:
                # If they give me "bye" we break
                if isinstance(data, str) == "bye":
                    break  # Break
                # Otherwise
                else:
                    # Tell the user to try again
                    connection.send("Try again: Remember numbers or 'bye'\n")

        # Send the user a farewell
        connection.send("Good-bye!\n")

        # Break out if the connection is closed
        my_socket.close()


if __name__ == "__main__":
    main()
