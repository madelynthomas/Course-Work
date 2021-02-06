/**
 * Clerk
 */

import java.util.Random;

public class Clerk {
    private int idNum;
    private Queue line;
    private Queue items;
    private Random groc;
    private int start;


    public Clerk(int clerkID, int maxSize) { // constructor
        idNum = clerkID;
        line = new Queue(maxSize);
        groc = new Random();
        items = new Queue(maxSize);
    } // end of construcotr

    public boolean isFull() {
        return line.isFull();
    } // end of isFull


    public void addCustomer(long j) { //inserts a customer to the line
        int groceries =  groc.nextInt(8) + 2; // number between 2 and 10
        line.insert(j); // inserts to clerk
        items.insert(groceries); // inserts items in cart
    } // end of addCustomer

    public void display() {
        line.display();
    } // end of display

    public int getLength() {
        return line.nItems;
    } // end of getLength

    public void tick() {
        start = items.front;
        long startTime = items.peekFront();
        System.out.println("Clerk " + idNum + ":" + startTime + ", " + start);
        if (startTime == 0){
            items.delete();
            line.delete();
        }
        else {
            items.queueArray[start]--;
        } // end of if/else
    } // end of tick
} // end of Clerk
