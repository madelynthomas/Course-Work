/**
 * Generic Node
 */

public class GenericNode<E> {
    public E data;
    public GenericNode<E> next;

    public GenericNode(E data) { // constructor
        this.data = data;
        next = null;
    } // end of constructor

    public E displayNode() {
        return data;
    } // end of displayNode
} // end of GenericNode