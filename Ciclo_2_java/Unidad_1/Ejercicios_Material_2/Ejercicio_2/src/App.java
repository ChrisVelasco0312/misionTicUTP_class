import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Write the name of the student: ");
        String name = sc.nextLine();

        System.out.println("Write the grade score of the student: ");
        System.out.println("Grade 1: ");
        float grade_1 = sc.nextFloat();
        System.out.println("Grade 2: ");
        float grade_2 = sc.nextFloat();
        System.out.println("Grade 3: ");
        float grade_3 = sc.nextFloat();

        System.out.println(studentScore(name, grade_1, grade_2, grade_3));
        sc.close();
    }

    public static String studentScore(String name, float grade_1, float grade_2, float grade_3) {
        float averageScore = (grade_1 + grade_2 + grade_2) / 3;
        return averageScore >= 3 ? "Student " + name + " PASS with grade: " + averageScore
                : "Student" + name + " does not pass. grade: " + averageScore;
    }
}
