import java.util.Scanner;

public class KmMts {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite la velocidad en km: ");
        double velocidad = sc.nextDouble();
        System.out.println(velocidad + "Km/h -> " + velocidad * 1000 / 3600 + " m/s");
        sc.close();
    }
}
