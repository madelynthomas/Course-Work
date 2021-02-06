/**
 * Tree
 */

import java.util.Stack;

class Tree {
    public Node root;

    public Tree() {
        root = null;
    }

    public int find(int key) {
        Node current = root;
        while (current != null && current.aDataItem != key) {
            if (key < current.aDataItem) {
                current = current.leftChild;
            else {
                current = current.rightChild;
            }

        }
        if (current == null) {
            return -1; // return null
        }
        return 1; // return current
    }

    public void insert(int adi) {
        Node newNode = new Node(); // make new node
        newNode.aDataItem = adi; // insert data
        if (root == null) // no node in root
            root = newNode;
        else { // root occupied
            Node current = root; // start at root
            Node parent;
            while (true) { // (exits internally)
                parent = current;
                if (adi < current.aDataItem) { // go left?
                    current = current.leftChild;
                    if (current == null) { // if end of the line,
                        // insert on left
                        parent.leftChild = newNode;
                        return;
                    }
                } // end if go left
                else { // or go right?
                    current = current.rightChild;
                    if (current == null) { // if end of the line
                        // insert on right
                        parent.rightChild = newNode;
                        return;
                    }
                } // end else go right
            } // end while
        } // end else not root
    } // end insert()

    public void displayTree() {
        Stack globalStack = new Stack();
        globalStack.push(root);
        int nBlanks = 32;
        boolean isRowEmpty = false;
        while (isRowEmpty == false) {
            Stack localStack = new Stack();
            isRowEmpty = true;
            for(int j=0; j < nBlanks; j++)
                System.out.print(" ");
            while (globalStack.isEmpty() == false) {
                Node temp = (Node)globalStack.pop();
                if (temp != null) {
                    System.out.print(temp.aDataItem);
                    localStack.push(temp.leftChild);
                    localStack.push(temp.rightChild);
                    if(temp.leftChild != null ||
                            temp.rightChild != null)
                        isRowEmpty = false;
                }
                else {
                    System.out.print("--");
                    localStack.push(null);
                    localStack.push(null);
                }
                for (int j = 0; j < nBlanks * 2 - 2; j++)
                    System.out.print(" ");
            } // end while globalStack not empty
            System.out.println();
            nBlanks /= 2;
            while (localStack.isEmpty() == false)
                globalStack.push(localStack.pop());
        } // end while isRowEmpty is false
        System.out.println("......................................................");
    } // end displayTree()
}
