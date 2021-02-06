/**
 * Generic Circ List
 */

public class GenericCircList <E> {
    private GenericNode<E> current; // ref to current Node
    private int count; // # of nodes on list
    private GenericNode<E> next;

    public GenericCircList() { // constructor
        count = 0; // no nodes on list yet
        current = null;
    } // end of constructor

    public boolean isEmpty() {
        return count == 0;
    } // end of isEmpty

    public int getSize() {
        return count;
    } // end of getSize

    public void insert(E data) { // insert before current Node
        GenericNode<E> newNode = new GenericNode<E>(data); // make new Node
        if (count == 0) { // if first one
            current = newNode; // current points to it
            newNode.next = newNode; // next one is ourself
        }
        else if (count == 1) {
            current.next = newNode;
            newNode.next = current;
        }
        else { // already at least one Node
            newNode.next = current; // set newNode to point to last thing added
            current = newNode;
            GenericNode<E> pointer = current;
            for (int i = 0; i < count; i++) { // find the first node added
                pointer = pointer.next; // because it needs to point back to newNode
            }
            pointer.next = current; // this if the first node added it points to newNode
            current = newNode; // update current so it points to most recently added item
        }
        count++; // one more Node
    } // end of insert

    public GenericNode<E> delete() {
        GenericNode<E> temp = current; // create temp and set to current
        if (isEmpty()) { // check to see if data is empty
            System.out.println("EMPTY LIST");
            return new GenericNode<E>(null); 
        }
        else if (count == 1) {
            current = null; // set current to null
            count--; // decrement counter
            return temp;
        } 
        else {
            for (int i = 0; i < count-1; i++) { // iterate over data
                temp = temp.next; // advance temp pointer
            } // end of for
            temp.next = current.next; // move temp.next and current.next pointers
            current = current.next; // set current pointer to next node
            count--; // decrement counter
            return temp;
        } // end of if/else if/else
    } // end of delete

    public void display() { // display the list
        for (int j = 0; j < count; j++) {
            System.out.println(current.displayNode()); // always display next link
            current = current.next;     // move to next link
        }
        System.out.println("");     // return null or deleted link
    } // end of display
} // end class GenericCircList
