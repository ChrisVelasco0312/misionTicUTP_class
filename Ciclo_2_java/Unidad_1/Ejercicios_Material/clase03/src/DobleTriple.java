import java.util.Scanner;

public class DobleTriple {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Write a number: ");
        int number = sc.nextInt();

        System.out.println("El doble del número: " + number + " es " + squaredNumber(number) + " y el triple es "
                + tripleNumber(number));
    }

    public static int squaredNumber(int num) {
        return num * 2;
    }

    public static int tripleNumber(int num) {
        return num * 3;
    }
}
