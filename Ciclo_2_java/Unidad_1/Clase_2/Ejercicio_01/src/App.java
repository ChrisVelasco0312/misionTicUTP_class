import java.util.Scanner;

// Evaluar si un número es divisible entre 10
public class App {
    public static void main(String[] args) throws Exception {
        // Instancio la clase util Scanner para pedir el número
        Scanner sc = new Scanner(System.in);
        System.out.println("Write a number: ");
        int number = sc.nextInt();
        // Imprimo el numero y llamo la funcion que se
        // encarga de evaluar si es divisible por 10
        System.out.println(number + checkIfDivisibleBy10(number));
        sc.close();
    }

    public static String checkIfDivisibleBy10(int number) {
        // Con operador ternario, evaluo si el numero
        // es divisible por 10, usando el operador mod
        // que devuelve 0 en caso de que no halla resto
        // es decir que es divisible por 10
        return number % 10 == 0 ? " number is divisible by 10" : " number is not divisible by 10";
    }
}
