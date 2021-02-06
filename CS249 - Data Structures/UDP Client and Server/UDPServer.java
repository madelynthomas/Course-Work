/**
 * Odd-Even UDP Server
 */

// Included libraries
import java.net.*;

public class UDPServer {
    public static void main(String args[]) throws Exception {
        // Create DatagramSocket object to listen on port 8080
        DatagramSocket datagramSocket = new DatagramSocket(8080);
        // Create byte arrays for sending and receiving data
        byte[] rcvData = new byte[1024];
        byte[] sendData;
        // While the server is running
        while(true) {
            // Create DatagramPacket object for receiving packets
            DatagramPacket rcvPacket = new DatagramPacket(rcvData, rcvData.length);
            // Let the server owner know they are waiting for a packet
            System.out.println("WAITING FOR PACKET");
            // We have received a packet
            datagramSocket.receive(rcvPacket);
            // Condense the packet to only the size of the max length
            String msg = new String(rcvPacket.getData(), 0, rcvPacket.getLength());
            // Display to the server owner the received string
            System.out.println("RECEIVED: " + msg);
            // Grab the IPAddress of the sender
            InetAddress IPAddress = rcvPacket.getAddress();
            // Create a port to communicate on
            int port = rcvPacket.getPort();
            // Try
            try {
                // Cast the message as a integer
                int num = Integer.parseInt(msg);
                // Check if it is even
                if (num % 2 == 0) {
                    // Respond to the client if it is even
                    String response = "EVEN";
                    sendData = response.getBytes();
                    DatagramPacket sendPacket =
                            new DatagramPacket(sendData, sendData.length, IPAddress, port);
                    datagramSocket.send(sendPacket);
                }
                // Check if it is odd
                else if (num % 2 == 1) {
                    // Respond to the client if it is odd
                    String response = "ODD";
                    sendData = response.getBytes();
                    DatagramPacket sendPacket =
                            new DatagramPacket(sendData, sendData.length, IPAddress, port);
                    datagramSocket.send(sendPacket);
                }
            } catch (NumberFormatException e) {
                // We got a string and not a number (or if we hit a number larger then int)
                String response = "NOT A NUMBER";
                sendData = response.getBytes();
                DatagramPacket sendPacket =
                        new DatagramPacket(sendData, sendData.length, IPAddress, port);
                datagramSocket.send(sendPacket);
            }
        }
    }
}