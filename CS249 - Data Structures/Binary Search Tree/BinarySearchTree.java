/**
 * Binary Search Tree
 */

import java.lang.Math; // import Math for log

public class BinarySearchTree<E extends Comparable<E>> { // constructor
    public Student root = null;

    public BinarySearchTree(Double[] input) {
        root = new Student(input[0]);
        Student pointer;
        for (int i = 1; i < input.length; i++) {
            pointer = root;
            for (int j = 0; j < (int)(Math.log(input.length)/Math.log(2)); j++) {
                if (pointer.compareTo(new Student(input[i])) == -1) {
                    if (pointer.lChild == null) {
                        pointer.lChild = new Student(input[i]);
                        break;
                    }
                    pointer = pointer.lChild;
                }
                else if (pointer.compareTo(new Student(input[i])) == 0) {
                    if (pointer.rChild == null) {
                        pointer.rChild = new Student(input[i]);
                        break;
                    }
                    pointer = pointer.rChild;
                }
                else if (pointer.compareTo(new Student(input[i])) == 1) {
                    if (pointer.rChild == null) {
                        pointer.rChild = new Student(input[i]);
                        break;
                    }
                    pointer = pointer.rChild;
                } // end if/else if
            } // end for j
        } // end for i
    } // end constructor

    public void insert(Double id) {
        Student newStudent = new Student(id);
        if (root == null)
            root = newStudent;
        else {
            Student pointer = root;
            Student parent;
            while (true) {
                parent = pointer;
                if (pointer.compareTo(newStudent) == -1) {
                    pointer = pointer.lChild;
                    if (pointer == null) {
                        parent.lChild = newStudent;
                        return;
                    } // end if
                } // end if
                else {
                    pointer = pointer.rChild;
                    if (pointer == null) {
                        parent.rChild = newStudent;
                        return;
                    } // end if
                } // end else
            } // end while
        } // end else
    } // end insert

    public Double find(Double key) {
        Student pointer = this.root;
        Student parent;
        if (this.root == null) {
            return null;
        } // end if
        while ((pointer.compareTo(new Student(key)) != 0)) {
            if (pointer.compareTo(new Student(key)) == -1) {
                parent = pointer;
                pointer = pointer.lChild;
            }
            else {
                parent = pointer;
                pointer = pointer.rChild;
            } // end else
            if (pointer == null) {
                if (parent.gpa == key) {
                    pointer = parent;
                    break;
                }
                else {
                    return null;
                } // end else
            } // end if
        } // end while
        return pointer.gpa;
    } // end find

    public boolean delete(Double key) {
        Student pointer = root;
        Student parent = root;
        boolean isLeftChild = true;
        while (pointer.compareTo(new Student(key)) != 0) {
            parent = pointer;
            if (pointer.compareTo(new Student(key)) == -1) {
                isLeftChild = true;
                pointer = pointer.lChild;
            }
            else {
                isLeftChild = false;
                pointer = pointer.rChild;
            } // end else
            if (pointer == null) {
                return false;
            } // end if
        } // end while
        if (pointer.lChild == null && pointer.rChild == null) {
            if (pointer == root) {
                root = null;
            }
            else if (isLeftChild) {
                parent.lChild = null;
            }
            else {
                parent.rChild = null;
            } // end else
        }
        else if (pointer.rChild == null) {
            if (pointer == root) {
                root = pointer.lChild;
            }
            else if (isLeftChild) {
                parent.lChild = pointer.lChild;
            }
            else {
                parent.rChild = pointer.lChild;
            } // end else
        }
        else if (pointer.lChild == null) {
            if (pointer == root) {
                root = pointer.rChild;
            }
            else if (isLeftChild) {
                parent.lChild = pointer.rChild;
            }
            else {
                parent.rChild = pointer.rChild;
            } // end else
        }
        else {
            Student successor = getSuccessor(pointer);
            if (pointer == root) {
                root = successor;
            }
            else if (isLeftChild) {
                parent.lChild = successor;
            }
            else {
                parent.rChild = successor;
            } // end else
            successor.lChild = pointer.lChild;
        } // end else
        return true;
    } // end delete

    private Student getSuccessor(Student student) {
        Student successorParent = student;
        Student successor = student;
        Student pointer = student.rChild;
        while (pointer != null) {
            successorParent = successor;
            successor = pointer;
            pointer = pointer.lChild;
        } // end while
        if (successor != student.rChild) {
            successorParent.lChild = successor.rChild;
            successor.rChild = student.rChild;
        } // end if
        return successor;
    } // end getSuccessor

    public void display(Student first) {
        if (first != null) {
            display(first.lChild);
            System.out.println(first.gpa + " ");
            display(first.rChild);
        } // end if
    } // end display

    public static void main(String[] args){
        BinarySearchTree tree = new BinarySearchTree(new Double[] {2.5, 3.55, 3.45, 3.12, 3.10});
        tree.insert(0.0);
        tree.insert(3.42);
        tree.insert(3.14);
        tree.insert(4.0);
        tree.insert(3.0);
        tree.insert(2.78);
        tree.insert(1.42);
        tree.insert(3.21);
        tree.insert(1.23);
        System.out.println(tree.find(4.0));
        System.out.println(tree.find(3.10));
        tree.delete(3.14);
        tree.delete(1.14);
        tree.display(tree.root);
    }
}
