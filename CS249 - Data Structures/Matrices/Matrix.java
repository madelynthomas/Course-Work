/**
 * Matrix
 */

public class Matrix { // class variables
    Node left;
    Node start;
    Node current;
    Node above;
    int width;
    int height;
    // end of class variables

    public Matrix(int width, int height) { // constuctor
        this.width = width;
        this.height = height;
        start = new Node(0);
        above = start;
        current = start;
        left = start;
        for (int i = 1; i < height; i++) { // iterate over all columns
            for (int j = 1; j < width; j++) { // iterate over all rows
                above.right = new Node(j);
                above = above.right;
                current = above;
            } // end of for j
            left.down = new Node(i);
            current = left.down;
            left = current;
        } // end of for i
    } // end of constructor

    public void insert(int x, int y, int value) {
        current = start;
        left = start;
        above = start;
        for (int i = 0; i <= y; i++) {
            current = left.down;
            for (int j = 0; j <= x; j++) {
            current = above.right;
            } // end of for j
        } // end of for i
        current.data = value;
    } // end of insert

    public void fill(int value) {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
            } // end of for j
            System.out.println(value);
        } // end of for i
    } // end of fill method

    public void sum() {
        int sumCol = 0;
        int sumRow = 0;
        for (int i = 0; i < height; i++) {
            sumCol += height;
            for (int j = 0; j < width; j++) {
                sumRow += width;
            } // end of for j
        } // end of for j
        System.out.println("SUM OF COLUMNS: " + sumCol);
        System.out.println("SUM OF ROWS: " + sumRow);
    } // end of sum method

    public void display() {
        current = start;
        left = start;
        above = start;
        for (int i = 0; i < height; i++) {
            String matrix = "";
            for (int j = 0; j < width; j++) {
                matrix += String.valueOf(left.data) + String.valueOf(current.data) + " ";
                current = current.right;
            } // end of for j
            System.out.println(matrix);
            current = above;
            left = left.down;
        } // end of for i
    } // end of display method
} // end of Matrix class
