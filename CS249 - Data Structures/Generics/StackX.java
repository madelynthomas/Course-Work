/**
 * Generic Stack
 */

public class StackX<E> {
    GenericNode<E> first, last;

    public StackX() { // constructor
        first = null;
        last = null;
    } // end of constructor

    public void push(E data) {
        if (last == null) { // if last is null
            first = new GenericNode<E>(data); // add first pointer
            first.next = first; // move first pointer to next
            last = first; // set last pointer to first
        }
        else if (first == last) { // check to see if first equals last
            last = new GenericNode<E>(data);
            first.next = last; // move first pointer to last
            last.next = first; // and last pointer to first
        }
        else {
            last.next = new GenericNode<E>(data); // insert new node at last
            last = last.next; // movel last pointer to next node
            last.next = first; // and move last pointer to to first for wrap-around
        } // end of if/else if/else
    }

    public E pop() {
        GenericNode<E> retVal = first; // set retVal to first
        if (retVal != null) { // as long as retVal is not null
            while (retVal.next != last) { // iterate over the list
                retVal = retVal.next; // 
            } // end of while
            GenericNode<E> temp = retVal; // set temp to retVal
            retVal = retVal.next; // advance retVal pointer
            temp.next = first; // set temp back to first
            last = temp; // set last to temp
        } // end of if
        return retVal.data;
    } // end of pop

    public boolean isEmpty() {
        return (first == null);
    } // end of isEmpty

    public void display() {
        GenericNode<E> printLoc = first; // printLoc of first item
        while (printLoc != last) { // iterate over list
            System.out.print(printLoc.data + " ");
            printLoc = printLoc.next; // advance printLoc and print item
        } // end of while
        printLoc = last;
        System.out.println(printLoc.data); // print data
    } // end of display
} // end of StackX
