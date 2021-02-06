/**
 * Binary Tree
 */

public class BinaryTree {

    public BinaryTree(int num) { // constructor
        makeBranches(num, 1);
    } // end of constructor

    public char makeBranches(int left, int right) {
        if (left == 0) {
            return 'X';
        }
        else {
            int mid = (left / 2);
            for (int i = 0; i < right; i++) {
                for (int j = 0; j < left; j++) {
                    if (j == mid) {
                        System.out.print("X");
                    }
                    else {
                        System.out.print("-");
                    } // end of if/else
                } // end of for
            } // end of for
        System.out.println("");
        return makeBranches(mid, right * 2);
        } // end of if/else
    } // end of makeBranches method

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree(16);
    } // end of main
} // end of BinaryTree class
