/**
 * HashTable
 */

class HashTable {
    private Tree[] hashArray; // array is the hash table
    private int arraySize;

    HashTable(int size) { // constructor
        arraySize = size;
        hashArray = new Tree[arraySize];
        for (int i = 0; i < size; i++) {
            hashArray[i] = new Tree();
        } // end for i
    } // end constuctor

    public void displayTable() {
        for (int i = 0; i < arraySize; i++) {
            if (hashArray[i] != null)
                hashArray[i].displayTree();
            else
                System.out.print("** ");
        } // end for i
        System.out.println("");
    } // end displayTable()

    public int hashFunc(int key) {
        return key % arraySize; // hash function
    } // end hashFunc()

    public void insert(int item) { // insert an item
        int key = item;
        int hashVal = hashFunc(key);
        // checks for duplicates being inserted
        if (hashArray[hashVal].find(key) == 1)
            System.out.println(key + " is already in the HashTable. Try new value.");
        else
            hashArray[hashVal].insert(key);
    } // end insert()

    public int find(int key) { // find item with key
        int hashVal = hashFunc(key);
        int item = hashArray[hashVal].find(key);
        return item;
    } // end find()
} // end class HashTable
