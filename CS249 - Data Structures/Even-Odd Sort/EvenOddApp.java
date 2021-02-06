/**
 * Even Odd App
 */

class EvenOddApp {
    public static void main(String[] args) {
        EvenOddSort theEvenOddSort = new EvenOddSort(10);

        theEvenOddSort.insert(7); // insert 10 items
        theEvenOddSort.insert(6);
        theEvenOddSort.insert(3);
        theEvenOddSort.insert(22);
        theEvenOddSort.insert(14);
        theEvenOddSort.insert(2);
        theEvenOddSort.insert(8);
        theEvenOddSort.insert(19);
        theEvenOddSort.insert(17);
        theEvenOddSort.insert(16);

        theEvenOddSort.display();
        
        theEvenOddSort.evenOddSort();

        theEvenOddSort.display();
    }
}
