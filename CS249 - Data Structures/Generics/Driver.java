/**
 * Driver for StackX
 */

public class Driver {
    public static void main(String[] args) {
        StackX<Integer> theStackX = new StackX<Integer>(); // create new stack

        System.out.println("EMPTY STACK: " + theStackX.isEmpty());

        theStackX.push(1); // push 6 items
        theStackX.push(5);
        theStackX.push(4);
        theStackX.push(2);
        theStackX.push(7);
        theStackX.push(5);

        theStackX.pop(); // pop off top item

        theStackX.display(); // display stack

        theStackX.push(42); // push 42

        theStackX.display(); /// display stack
    } // end of main
} // end of Driver
