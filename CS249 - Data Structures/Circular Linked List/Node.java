/**
 * Node
 */

public class Node {
    private int data;
    public Node next;

    public Node(int data) { // constructor
        this.data = data; // data in node
    } // end of constructor

    public void display() {
        System.out.println(data);
    } // end of display
} // end of Node
