import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        System.out.println("Write 2 numbers");
        System.out.println("Number 1: ");

        float number_1 = sc.nextFloat();

        System.out.println("Number 2: ");

        float number_2 = sc.nextFloat();

        System.out.println(
                "The multiplication of " + number_1 + " and " + number_2 + " is: " + multiply(number_1, number_2));

        System.out.println("The sum of " + number_1 + " and " + number_2 + " is: " + sum(number_1, number_2));

        System.out.println(
                "The difference of " + number_1 + " and " + number_2 + " is: " + difference(number_1, number_2));

        sc.close();
    }

    public static float sum(float num_1, float num_2) {
        return num_1 + num_2;
    }

    public static float difference(float num_1, float num_2) {
        return num_1 / num_2;
    }

    public static float multiply(float num_1, float num_2) {
        return num_1 * num_2;
    }
}