public class App {
    public static void main(String[] args) throws Exception {
        int count = 0;
        for (;;) {
            count++;
            System.out.println(count);
            if (count == 25) {
                break;
            }
        }
    }
}
