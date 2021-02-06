/**
 * Driver for Store
 */

import java.util.Scanner;

public class Driver {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numClerks = 0;
        int variable = 0;

        System.out.print("NUMBER OF CLERKS?: ");

        while (true) {
            try {
                int totalClerks = Integer.parseInt(scan.nextLine());
                break;
            }
            catch (NumberFormatException notInt) {
                System.err.println("INPUT MUST BE INTEGER");
            }
        }

        System.out.print("NUMBER OF CUSTOMERS: ");

        while (true) {
            try {
                int totalCustomers = Integer.parseInt(scan.nextLine());
                break;
            }
            catch (NumberFormatException notInt) {
                System.err.println("INPUT MUST BE INTEGER");
            }
        }
    Store store = new Store(numClerks, variable);
        while (true) {
            System.out.println("T: TIME ELAPSED");
            System.out.println("C: ADD CUSTOMER");
            System.out.println("S: STORE");
            System.out.println("Q: QUIT");
            String input = scan.nextLine();
            if (input.equals("T")) {
                store.tick();
            }
            else if (input.equals("C")) {
                store.addCustomer();
            }
            else if (input.equals("S")) {
                store.display();
            }
            else if (input.equals("Q")) {
                System.out.println("STORE IS NOW CLOSED! COME AGAIN!");
                System.exit(1);
            }
            else {
                System.out.println("NOT VALID INPUT");
            }
        }
    } // end of main method
} // end class QueueApp
