import java.util.Scanner;

// Print sum of two numbers

public class App {
    public static void main(String[] args) throws Exception {
        // Variable declarations
        int n1, n2;
        Scanner sc = new Scanner(System.in);

        // Read the first number
        System.out.println("Please, write the first number: ");
        n1 = sc.nextInt();

        // Read the second number
        System.out.println("Please, write the second number: ");
        n2 = sc.nextInt();

        // Show the result
        System.out.println("You write the numbers: " + n1 + " and " + n2);
        System.out.println("The sum is: " + (n1 + n2));
        sc.close();
    }
}
