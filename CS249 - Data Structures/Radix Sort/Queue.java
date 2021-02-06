/**
 * Queue for RadixSort
 */

public class Queue {
    public int size[] = new int[20];
    public int front;
    public int rear;

    public Queue() {
        front = 0;
        rear =- 1;
    }

    public boolean isEmpty() {
        if (rear < front) {
            return true;
        }
        else {
            return false;
        }
    }

    public void add(int element) {
        if (rear < 20) {
            size[++rear] = element;
        }
    }

    public int delete() {
        return size[front++];
    }
}
