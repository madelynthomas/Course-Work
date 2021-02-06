/**
 * Circular Link List
 */

public class CircularLinkList {
    public Node current;
    public int count;
    public int data;

    public CircularLinkList() { // constructor
        count = 0;
        current = null;
    } // end of constructor

    public boolean isEmpty() {
        return count == 0;
    } // end of isEmpty

    public int getData() {
        return data;
    } // end of getData

    public int getSize() {
        return count;
    } // end of getSize

    public void insert(int id) {
        Node newNode = new Node(id);
        if (count == 0) {
            current = newNode;
            newNode.next = current;
        }
        else {
            newNode.next = current;
            for (int i = 1; i < count; i++){
                current = current.next;
            }
            current.next = newNode;
            current = newNode;
        } // end of if/else
        count++; // increment coun
        this.data = data;
    } // end of insert

    public Node delete() {
        Node tempNode = null;
        if (isEmpty()) { //empty list, return null
            return tempNode;
        }
        else if (count == 1) {
            tempNode = current; // copy node data to temp
            current = null; // set node equal to null
            count--; // decrement count to 0
        }
        else {
            tempNode = current; // temp to copy node data
            for (int i = 1; i < count; i++) { // iterate to second to last node
                current = current.next; // iterate through link list
            } // end of for
            current.next = tempNode.next; // move pointer away from last node a.k.a. remove node
            current = current.next; // set current to front of list
            count--; // decrement count
        } // end of else
        return tempNode; // return removed node
    } // end of delete

    public void displayList(){
        for (int i = 0; i < count; i++){
            current.display();
            current= current.next;
        } // end of for
    } // end of displayList
} // end CircularLinkList
