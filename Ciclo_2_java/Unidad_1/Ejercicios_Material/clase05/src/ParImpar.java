import java.util.Scanner;

public class ParImpar {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Write a number: ");
        int number = sc.nextInt();

        System.out.println(checkOddEven(number));
    }

    public static String checkOddEven(int number) {
        if (number % 2 == 0) {
            return number + " is Even";
        } else {
            return number + " is Odd";
        }
    }
}
