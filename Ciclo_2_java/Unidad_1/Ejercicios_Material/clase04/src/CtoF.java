import java.util.Scanner;

public class CtoF {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        System.out.println("Write the temperature in celsius: ");

        int celsius = sc.nextInt();

        System.out.println(celsius + "°C(celsius) are " + celsiusToFarenheit(celsius) + "°F(farenheit)");
    }

    public static int celsiusToFarenheit(int celsius) {
        return 32 + (9 * celsius / 5);
    }
}
