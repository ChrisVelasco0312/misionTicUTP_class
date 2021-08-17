import java.util.Scanner;

public class numCifras {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digita un número para saber cuantas cifras tiene: ");

        var numero = sc.nextInt();

        System.out.println("El numero tiene " + countNumbers(numero) + " cifras");

        sc.close();
    }

    public static int countNumbers(int number) {
        int cifras = 0;
        while (number != 0) {
            number = number / 10;
            cifras = cifras + 1;
        }

        return cifras;
    }
}
