/**
 * Game
 */

public class Game {
    public int playerCount;
    public int correctPos;
    public int startPos;
    public Node removeLoc;
    public int playerID;

    public Game(int pc, int cp, int sp) {
        CircularLinkList circle = new CircularLinkList();
        playerCount = pc;
        correctPos = cp;
        startPos = sp;
        for (int i = 0; i < playerCount; i++) {
            circle.insert(i);
        } // end of for
        while (circle.getSize() > 1) {
            for(int i = sp; i < correctPos; i++){
                removeLoc = circle.delete();
            } // end of for
            removeLoc = circle.delete();
            System.out.println(removeLoc + " is killed!");
        } // end of while 
        System.out.println(circle + "is the survior!");
    } // end of Game
} // end of Game
