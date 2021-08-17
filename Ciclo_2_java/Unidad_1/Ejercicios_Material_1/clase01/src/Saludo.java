public class Saludo {
    public static void main(String[] args) throws Exception {
        String name = "Carl";
        System.out.println(greeting(name));
    }

    public static String greeting(String name) {
        return "Hola " + name;
    }
}
