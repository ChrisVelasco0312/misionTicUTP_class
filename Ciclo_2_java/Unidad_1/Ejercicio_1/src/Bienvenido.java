import java.util.Scanner;

public class Bienvenido {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        System.out.println("Cual es tu nombre?");
        var name = sc.nextLine();

        System.out.println(saludo(name));
        sc.close();

        // While loop
        int counter = 0;
        int times = 10;
        while (counter < times) {
            counter++;
            System.out.println("counter " + counter);
        }

        // for loop
        for (int i = 1; i <= 10; i++) {
            System.out.println("Loop " + i);
        }

        // do while
        int i = 0;
        do {
            i++;
            System.out.println("Contador" + i);
        } while (i <= 10);
    }

    public static String saludo(String name) {
        return "Hola como estas " + name;
    }
}
