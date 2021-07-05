import java.util.Scanner;

// Read two integer values in N and removes the M last values.
// Example: If N = 123456 and M = 2 the new value of N will be 1234

public class App {
    public static void main(String[] args) throws Exception {
        // Instantiate the Scanner util class and ask the user for a number
        Scanner sc = new Scanner(System.in);
        System.out.println("Write a number: ");
        // Save the number in N variable
        var N = sc.nextInt();

        // Ask the number of digits to be deleted and saves in M variable
        System.out.println("How many digits you want to delete?: ");
        var M = sc.nextInt();

        // Print the message with the resulting new number, calling the delete digits
        // method
        System.out.println("Your number is: " + (int) (deleteDigits(N, M)));
    }

    /**
     * 
     * @param numN
     * @param numM
     * @return
     */
    public static double deleteDigits(int numN, int numM) {
        // the function takes as argument the number given by
        // the user and the number of digits to be removed from this number
        // then take the number from which you want to remove the digits
        // and divide it by the result of 10 raised to the number of digits you want to
        // remove.
        return (int) (numN / Math.pow(10, numM));
    }
}
