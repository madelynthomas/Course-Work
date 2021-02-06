/**
 * Odd-Even Protocol
 */

import java.lang.*;

public class OddEvenProtocol {
    private static final int WAITING = 0;
    private static final int RESPONSE = 1;
    private static final int ANOTHER = 2;

    private int state = WAITING;

    private String talking;

    public String processInput(String theInput) {
        int theOutput = Integer.parseInt(theInput);

        if (state == WAITING) {
            talking = "Gimme a number: ";
            state = RESPONSE;
        } else if (state == RESPONSE) {
            if ((theOutput & 1) == 0) {
                talking = "The number is EVEN!";
            }
            else {
                talking = "The number is ODD!";
            }
            state = RESPONSE;
        }
        else if (state == ANOTHER) {
            if (theInput.equalsIgnoreCase("y")) {
                talking = "Gimme another number: ";
                state = RESPONSE;
            } else {
                talking = "Bye.";
                state = WAITING;
            }
        }
        return talking;
    }
}