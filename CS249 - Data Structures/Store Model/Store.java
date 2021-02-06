/**
 * Store
 */

import java.util.Random;

public class Store {
    private Clerk[] clerk;
    private int maxClerks;
    private int lineLength;
    private int timeLapsed;
    private int custID;
    private int Random;


    public Store(int numClerks, int line) {
        clerk = new Clerk[numClerks]; // assign a new clerk queue
        lineLength = line; // set lineLength to line
        maxClerks = numClerks; // sets max number of clerks
        custID = 1; // initalize custID to 1
        for(int i = 0; i < numClerks; i++) {
            Clerk employee = new Clerk(i, line);  // loops through entire amount of clerks
        } // end of for
    } // end of Store

    public void display() {
        for (int i = 0; i < maxClerks; i++) {
            clerk[i].display();
        } // end of for
    } // end of display

    public Clerk findShortestLine() {
        int min = clerk[0].getLength(); // sets min to first clerk
        Clerk shortest = clerk[0];
        for(int i = 1; i < maxClerks; i++){ // iterates through the list
            if (clerk[i].getLength() < min){ // checks if the length is smaller than the min
                min = clerk[i].getLength(); // sets min
                shortest = clerk[i]; // sets shortest shortest
            } // end of if
        } // end of for
        return shortest;
    } // end of findShortestLine


    public void addCustomer() {
        Clerk shortest = findShortestLine(); // best line to add to
        shortest.addCustomer(custID); // adds a customer
        if (shortest.isFull()) { // checks if full
            System.out.println("ALL AISLES FULL"); // prints out an apology if the list is full
        }
        else {
            shortest.addCustomer(custID); // sets new customer
            custID++; // increments customer id
        } // end of if/else
    } // end of addCustomer

    public void tick() {
        for (int i=0; i < maxClerks; i++) {
            clerk[i].tick();
        } // end of for
        timeLapsed++;
        display();
    } // end of tick
} // end of Store
