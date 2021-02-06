
/**
 * Even Odd Sort
 */

public class EvenOddSort {
    private int[] array1;
    private int elems;

    public EvenOddSort(int max) { // constructor
        array1 = new int[max];
        elems = 0;
    } // end of EvenOddSort constructor
    
    public void insert(int value) { // put items at rear of array
        array1[elems] = value; // sets array elems to value
        elems++; // increment elems counter
    } // end of insert method
    
    public void display() {
        for(int j=0;j<elems;j++) {
            System.out.println(array1[j] + " ");
        } // end of for
        System.out.println("");
    } // end of display method

    public void swap(int x, int y) {
        int temp = x; // set int temp to x
        x = y; // swap x with y
        y = temp; // return y as temp
    } // end of swap method
    
    public boolean isSorted() {
        int trueCounter = 0; // counter to determine sorted
        for(int i = 1;i<elems;i++){
            if(array1[i-1]<array1[i])
                  trueCounter++;
        }
        if(trueCounter+1 == elems)
            return true;
        else {
            return false;
        }
    } // end of isSorted method
    
    public void evenOddSort() {
        int temp;
        while(!isSorted()) {
            for(int i = 0;i < elems;i=i+2) {
                if(array1[i] > array1[i+1]) {
                    temp = array1[i];
                    array1[i] = array1[i+1];
                    array1[i+1] = temp;
                }
                else {
                    // do nothing
                }
            } // end of for
            for(int j = 1;j < (elems-2);j=j+2){
                if(array1[j] > array1[j+1]){
                    temp = array1[j];
                    array1[j] = array1[j+1];
                    array1[j+1] = temp;
                }
                else {
                    // do nothing
                }
            } // end of for
        } // end of while
    } // end of evenOddSort method
} // end of EvenOddSort class
