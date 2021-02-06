/**
 * Radix Sort
 */

import java.util.*; // import utilities library

public class RadixSort {

    public static void RadixSort(int array[], int lsdDigit) {
        int division;
        int queueIndex;
        int digit;

        Queue myQueue[] = new Queue[10];
        for (int i = 0; i < 10; i++) {
            myQueue[i] = new Queue();
        } // end for i
        division = 1;
        for (digit = 1; digit <= lsdDigit; digit++) {
            for (int i = 0; i < array.length; i++) {
                queueIndex = (array[i] / division) % 10;
                myQueue[queueIndex].add(array[i]);
            } // end for i
            int j = 0;
            for (int i = 0; i < 10; i++) {
                while (!myQueue[i].isEmpty()) {
                    array[j] = myQueue[i].delete();
                    j++;
                } // end while
            } // end for i
            division *= 10;
        } // end for digit
    } // end RadixSort

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("NUMBER OF ELEMENTS IN ARRAY: ");
        int num = scanner.nextInt();
        int array[] = new int[num];
        System.out.println("LEAST SIGNIFICANT DIGIT: ");
        int lsdDigit = scanner.nextInt();
        System.out.println("ENTER ELEMENTS OF ARRAY: ");
        for (int i = 0; i < num; i++) {
            array[i] = scanner.nextInt();
        } // end for i
        RadixSort(array, lsdDigit);
        System.out.println("RADIXSORT COMPLETED");
        System.out.println("SORTED ARRAY");
        for (int j = 0; j < num; j++) {
            System.out.print(array[j] + " ");
        } // end for j
    } // end main
} // end RadixSort class
