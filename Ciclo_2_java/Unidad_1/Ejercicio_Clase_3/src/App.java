import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // Instanciar clase scanner
        Scanner sc = new Scanner(System.in);
        System.out.println("Write your first name: ");
        var firstName = sc.nextLine();
        System.out.println("Write your last name: ");
        var lastName = sc.nextLine();

        System.out.println(name(firstName, lastName));
    }

    public static String name(String firstName, String lastName) {
        return "Your name is " + firstName + " " + lastName;
    }
}
