/**
 * Deque
 */

class Deque {
    private int maxSize;
    private long[] dequeArray;
    private int left;
    private int right;
    private int nItems;

    public Deque(int s) { // constructor
        maxSize = s;
        dequeArray = new long[maxSize];
        left = (maxSize/2) - 1;
        right = (maxSize/2);
        nItems = 0;
    } // end of constructor

    public void insertLeft(long l) {
        if(!isFull() || !(left < 0)) {
            dequeArray[left] = l;
            nItems++; // increment counter
            left--;
        }
        if(left == -1) {
            left = maxSize - 1;
        }
    } // end of insertLeft method

    public void insertRight(long r) {
        if(!isFull() || !(right > maxSize - 1)) { // check to see if list full or the right side
            dequeArray[right] = r;
            nItems++; // increments item counter
            right++;
        }
        if(right == maxSize) {
            right = 0;
        }
    }

    public long removeLeft() {
        left++; // increments the left counter
        if(left == maxSize) {
            left = 0;
        }
        long temp = dequeArray[left]; // creates a temp variable for the deleted element
        if(!isEmpty() || !(left > (maxSize/2) - 1)) { //check to see if list is empty or if the left counter is not on the left
            dequeArray[left] = 0; // delete the element
            nItems--; // decrements the amount of items in the list
        }
        return temp; // return deleted element
    }

    public long removeRight() {
        right--; // decrements the right counter
        if(right == -1) {
            right = maxSize - 1;
        }
        long temp = dequeArray[right]; // creates a temp variable for the deleted element
        if (!isEmpty() || !(right < maxSize/2)) { // check to see if list is empty or if the right counter is not on the right
            dequeArray[right] = 0; // delete element
            nItems--; // decrements item counter
        }
        return temp; // return deleted element
    }

    public boolean isEmpty() {
        return (nItems == 0);
    } // end of isEmpty method

    public boolean isFull() {
        return (nItems == maxSize);
    } // end of isFull method

    public void display() {
        for(int i = 0; i < dequeArray.length; i++) {
            System.out.print(dequeArray[i] + " ");
        } // end of for
        System.out.println();
    }
} // end of Deque class
