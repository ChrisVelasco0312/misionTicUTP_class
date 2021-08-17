import java.util.Scanner;

public class ParImpar {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Write a number: ");
        int number = sc.nextInt();

        System.out.println(checkOddEven(number));
        sc.close();
    }

    public static String checkOddEven(int number) {
        // Con condicionales
        // if (number % 2 == 0) {
        // return number + " is Even";
        // } else {
        // return number + " is Odd";
        // }

        // Con operador ternario
        return number + (number % 2 == 0 ? " is Even" : " is Odd");
    }
}
