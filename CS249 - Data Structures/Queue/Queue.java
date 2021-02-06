/**
 * Queue
 */

class Queue {
    private int maxSize;
    private long[] queArray;
    private int front;
    private int rear;
    private int nItems;

    public Queue(int s) { // constructor
        maxSize = s;
        queArray = new long[maxSize];
        front = 0;
        rear = -1;
        nItems = 0;
    } // end of Queue constructor

    public void insert(long j) { // put item at rear of queue
        if(rear == maxSize-1) // deal with wraparound
            rear = -1;
        queArray[++rear] = j; // increment rear and insert
        nItems++; // one more item
    } // end of insert method

    public long remove() { // take item from front of queue
        long temp = queArray[front++]; // get value and incr front
        if(front == maxSize) // deal with wraparound
            front = 0;
        nItems--; // one less item
        return temp;
    } // end of remove method

    public long peekFront() { // peek at front of queue
        return queArray[front];
    } // end of peekFront method

    public boolean isEmpty() { // true if queue is empty
        return (nItems==0);
    } // end of isEmpty method

    public boolean isFull() { // true if queue is full
        return (nItems==maxSize);
    } // end of isFull method

    public int size() { // number of items in queue
        return nItems;
    } // end of size method

    public void display() { // displays array contents
        for(int i=0; i<nItems; i++) // for each element,
            System.out.print(queArray[i] + " "); // display it
        System.out.println("");
    } // end of display method
} // end class Queue
