/**
 * Deque App
 */

class DequeApp {
    public static void main(String[] args) {
        Deque theDeque = new Deque(4);
        theDeque.insertRight(28);
        theDeque.insertRight(7);
        theDeque.insertRight(97);
        theDeque.insertRight(73);
        theDeque.removeLeft();
        theDeque.removeLeft();
        theDeque.insertLeft(42);

        theDeque.display();
    }
}
