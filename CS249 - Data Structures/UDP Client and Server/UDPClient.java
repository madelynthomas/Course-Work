/**
 * Odd-Even UDP Client
 */

// Included libraries
import java.io.*;
import java.net.*;

public class UDPClient {
    public static void main(String args[]) throws Exception {
        // Create BufferedReader object for input
        BufferedReader input =
                new BufferedReader(new InputStreamReader(System.in));
        // Create DatagramSocket object
        DatagramSocket datagramSocket = new DatagramSocket();
        // Connect to localhost
        InetAddress IPAddress = InetAddress.getByName("LOCALHOST");
        // Create byte arrays for sending and receiving data
        byte[] sendData;
        byte[] rcvData = new byte[1024];
        // Ask user for a number
        System.out.print("GIMME A NUMBER: ");
        // Take the input and store it as a string
        String msg = input.readLine();
        // Prepare it for sending it to the server
        sendData = msg.getBytes();
        // Create DatagramPacket object to send to the server
        DatagramPacket sendPacket =
                new DatagramPacket(sendData, sendData.length, IPAddress, 8080);
        // Send to the server
        datagramSocket.send(sendPacket);
        // Create DatagramPacket received object
        DatagramPacket rcvPacket =
                new DatagramPacket(rcvData, rcvData.length);
        // Receive output from server
        datagramSocket.receive(rcvPacket);
        // Format it as a string
        String numRet = new String(rcvPacket.getData());
        // Tell the user ODD, EVEN, or NOT A NUMBER
        System.out.println("FROM SERVER: " + numRet);
        // Close the socket
        datagramSocket.close();
    }
}