/**
 * Knapsack
 */

public class Knapsack { // constructor
    int[] sack = {2, 2, 2, 2, 5};
    int[] sackContents = new int[5];
    int count = 0;
    boolean packItem;
    // end of constructor

    public boolean itemsToPack(int total, int item) { // itemsToPack method
        if (item == sack.length)
            return false;
        else if (sack[item] > total) // if the item in the sack is greater than the total
            return itemsToPack(total, item + 1); // recursively return the total and move to the next item
        else if (sack[item] < total) { // if the item in the sack is less than the total
            packItem = itemsToPack(total - sack[item], item + 1); // place the item in the sack and move item pointer
            if (!packItem) { // if the item not packed
                return itemsToPack(total, item + 1); // recursively return the total and move the item pointer
            }
            else {
                sackContents[count++] = sack[item]; // increment count and move item pointer
                return true;
            } // end of nested if/else
        }
        else { // otherwise
            sackContents[count++] = sack[item]; // increment the count and move item pointer
            return true;
        } // end of if/else if/else if/else
    } // end of itemsToPack method

    public static void main(String[] args) { // main method
        Knapsack myKnapsack = new Knapsack(); // create new Knapsack named myKnapsack
        if (myKnapsack.itemsToPack(5, 0)) { // if itemsToPack is equal to total, print pass and knapsack contents
            System.out.println("PASS");
            System.out.println("KNAPSACK CONTENTS");
            for (int i = 0; i < myKnapsack.sackContents.length; i++) {
                System.out.print(myKnapsack.sackContents[i] + " ");
            } // end of for
        }
        else { // if no combinations were possible
            System.out.println("FAIL");
            System.out.println("NO VALID COMBINATIONS");
        } // end of if/else
    } // end of main method
} // end of Knapsack class
