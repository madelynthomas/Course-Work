/**
 * Odd-Even UDP Server
 */

import java.net.*;

public class OddEvenUDPServer {
    public static void main(String[] args) throws Exception {
        try {
            DatagramSocket dgSocket = new DatagramSocket(8080);
            byte[] rcvData;
            byte[] sendData;
            while (true) {
                rcvData = new byte[2048];
                DatagramPacket rcvPacket =
                        new DatagramPacket(rcvData, rcvData.length);
                System.out.println("Ready for datagram packet");
                dgSocket.receive(rcvPacket);
                String msg = new String(rcvPacket.getData());
                InetAddress IP = rcvPacket.getAddress();
                int port = rcvPacket.getPort();
                System.out.println ("From: " + IP + ":" + port);
                System.out.println ("Message: " + msg);
                String capitalizedSentence = msg.toUpperCase();
                sendData = capitalizedSentence.getBytes();
                DatagramPacket sendPacket =
                        new DatagramPacket(sendData, sendData.length, IP,
                                port);
                dgSocket.send(sendPacket);
            }
        }
        catch (SocketException ex) {
            System.out.println("Port 8080 is in use. Try again later.");
            System.exit(1);
        }
    }
}
