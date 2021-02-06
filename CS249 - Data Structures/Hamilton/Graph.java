/**
 * Graph
 */

import java.util.*;

class Graph {
    public int MAX_VERTS = 10;
    public Vertex vertexList[]; // list of vertices
    public int adjMat[][]; // adjacency matrix
    public int nVerts; // current number of vertices
    public Stack theStack;
    public int startVertex;
    public int length;

    public Graph() { // constructor
        vertexList = new Vertex[MAX_VERTS]; // adjacency matrix
        adjMat = new int[MAX_VERTS][MAX_VERTS];
        nVerts = 0;
        for (int j = 0; j < MAX_VERTS; j++) // set adjacency
            for (int k = 0; k < MAX_VERTS; k++) // matrix to 0
                adjMat[j][k] = 0;
        theStack = new Stack();
    } // end constructor

    public void addVertex(char lab) {
        vertexList[nVerts++] = new Vertex(lab);
    } // end addVertex()

    public void addEdge(int start, int end) {
        adjMat[start][end] = 1;

    } // end addEdge()

    public void warshall() {
        for (int k = 0; k < nVerts; k++) {
            for (int i = 0; i < nVerts; i++) {
                for (int j = 0; j < nVerts; j++) {
                    adjMat[i][j] = (adjMat[i][j] | (adjMat[i][k] & adjMat[k][j]));
                } // end for j
            } // end for i
        } // end for k
    } // end method warshall

    public void adjMatDisplay() {
        for (int i = 0; i < MAX_VERTS; i++) {
            for (int j = 0; j < adjMat[i].length; j++) {
                System.out.print(" " + adjMat[i][j]);
            } // end for j
            System.out.println("");
        } // end for i
    } // end adjMatDisplay()

    public void startV(int v) {
        startVertex = v;
    } // end startV()

    public void findCycle() {
        length = adjMat.length;
        List<Integer> startCircuit = new ArrayList<Integer>();
        startCircuit.add(startVertex);
        findCycleHelper(startCircuit);
    } // end findCycle()

    public void findCycleHelper(List<Integer> sizeSoFar) {
        if (sizeSoFar.size() == 6)
            display(sizeSoFar);
        else if (sizeSoFar.size() == 5) {
            int current = sizeSoFar.get(sizeSoFar.size()-1);
            if (adjMat[current][startVertex] != 0) {
                sizeSoFar.add(startVertex);
                findCycleHelper(sizeSoFar);
                sizeSoFar.remove(sizeSoFar.size()-1);
            } // end if
        }
        else {
            int current = sizeSoFar.get(sizeSoFar.size()-1);
            for (int i = 0; i < length; i++) {
                if (!sizeSoFar.contains(i) && adjMat[current][i] != 0) {
                    sizeSoFar.add(i);
                    findCycleHelper(sizeSoFar);
                    sizeSoFar.remove(sizeSoFar.size()-1);
                } // end if
            } // end for i
        } // end else
    } // end findCycleHelper()

    public void display(List<Integer> sizeSoFar) {
        String vertics;
        for (Integer value : sizeSoFar) {
            switch (value) {
                case 0: vertics = "A";
                    break;
                case 1: vertics = "B";
                    break;
                case 2:  vertics = "C";
                    break;
                case 3: vertics = "D";
                    break;
                case 4: vertics = "E";
                    break;
                default: vertics = "Invalid vertex";
                    break;
            } // end switch (val)
            System.out.print(vertics.toString() + " ");
        }
        System.out.println(" ");
    } // end display()
} // end class Graph()
