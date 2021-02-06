/**
 * Hamilton App
 */

class HamiltonApp {
    public static void main(String[] args) {
        Graph theGraph = new Graph();
        theGraph.addVertex('A');  // 0  (start)
        theGraph.addVertex('B');  // 1
        theGraph.addVertex('C');  // 2
        theGraph.addVertex('D');  // 3
        theGraph.addVertex('E');  // 4

        theGraph.addEdge(0, 1);   // AB
        theGraph.addEdge(0, 2);   // AC
        theGraph.addEdge(0, 3);   // AD
        theGraph.addEdge(1, 2);   // BC
        theGraph.addEdge(1, 4);   // BE
        theGraph.addEdge(2, 3);   // CD
        theGraph.addEdge(2, 4);   // CE
        theGraph.addEdge(3, 4);   // DE
        theGraph.addEdge(4, 0);   // EA
        theGraph.addEdge(3, 1);   // DB

        for (int i = 0; i < 5; i++){
            theGraph.startV(i);          // set starting vertex
            theGraph.findCycle();        // find Hamiltonian cycle
        }
    }  // end main()
}  // end class HamiltonApp
