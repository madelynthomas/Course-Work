/**
 * Matrix App
 */

import java.util.Scanner;

public class MatrixApp {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x;
        int y;
        int value = 0;
        System.out.println("MATRIX DIMENSIONS (X FOLLOWED BY Y): ");
        while (true) {
            try {
                x = Integer.parseInt(scan.nextLine());
                y = Integer.parseInt(scan.nextLine());
                break;
            }
            catch (NumberFormatException notInt) {
                System.err.println("INPUTS MUST BE INTEGER");
            } // end of try/catch
        } // end of while
        Matrix matrix = new Matrix(x, y);
        matrix.display();
        while (true) {
            System.out.println("");
            System.out.println("1: INSERT VALUE");
            System.out.println("2: FILL VALUE");
            System.out.println("3: SUM");
            System.out.println("4: DISPLAY");
            System.out.println("5: QUIT");
            String input = scan.nextLine();
            if (input.equals("1")) {
                matrix.insert(x, y, value);
            }
            else if (input.equals("2")) {
                matrix.fill(value);
            }
            else if (input.equals("3")) {
                matrix.sum();
            }
            else if (input.equals("4")) {
                matrix.display();
            }
            else if (input.equals("5")) {
                System.out.println("CLOSING MATRIX APP");
                System.exit(1);
            }
            else {
                System.out.println("NOT VALID INPUT");
            } // end of if/else if/else
        } // end of while
    } // end of main method
} // end of MatrixApp class
