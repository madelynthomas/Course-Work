/**
 * Queue
 */

public class Queue {
    public int maxSize;
    public long[] queueArray;
    public int front;
    private int rear;
    public int nItems;

    public Queue(int s) { // constructor
        maxSize = s;
        queueArray = new long[maxSize];
        front = 0;
        rear = -1;
        nItems = 0;
    } // end of Queue constructor

    public void insert(long j) { // put item at rear of queue
        if(rear == maxSize - 1) // deal with wraparound
            rear = -1;
        queueArray[++rear] = j; // increment rear and insert
        nItems++; // one more item
    } // end of insert method

    public long delete() { // take item from front of queue
        long temp = queueArray[front++]; // get value and increment front
        if(front == maxSize) // deal with wraparound
            front = 0;
        nItems--; // one less item
        return temp;
    } // end of delete method

    public void display() {
        int pointer;
        if (nItems == 0) {
            System.out.println("Empty Queue");
        } else if (front == rear) {
            System.out.println(queueArray[front]);
        } else if (front < rear) {
            for (pointer = front; pointer <= rear; pointer++) {
                System.out.print(queueArray[pointer] + " ");
            } // end of for
        } else {
            for (pointer = front; pointer < maxSize; pointer++) {
                System.out.print(queueArray[pointer] + " ");
            } // end of for
            for (int i = 0; i <= rear; i++) {
                System.out.print(queueArray[i] + " ");
            } // end of for
        } // end of if/else if/else
    } // end of display methods

    public boolean isEmpty() { // true if queue is empty
        return (nItems == 0);
    } // end of isEmpty method

    public boolean isFull() { // true if queue is full
        return (nItems == maxSize);
    } // end of isFull method

    public long peekFront(){
        return queueArray[front];
    }
} // end class Queue
