import java.util.Scanner;

// Auhor: Christian velasco
// Based on the exercise lesson by Luis Guillermo Molero | MisionTic2022 course

// Given the user's birth date (day, month, year), 
// calculates the lucky number.

// Lucky number is calculated, summing the day, month, and year of the birth date
// and then summing the total of digits of the resulting number

public class App {
    public static void main(String[] args) throws Exception {

        // Instantiate the Scanner util class, to read user input
        Scanner sc = new Scanner(System.in);
        // Variable declarations
        int day, month, year;

        System.out.println("Write your birth date: ");

        // Read the day, month, and year from the user's input
        System.out.println("Day: ");
        day = sc.nextInt();

        System.out.println("Month: ");
        month = sc.nextInt();

        System.out.println("Year: ");
        year = sc.nextInt();

        // Print a message and calling the method that calculates the lucky number
        System.out.println("Your lucky number is : " + calcLuckyNumber(day, month, year));
        sc.close();
    }

    /**
     * 
     * @param day
     * @param month
     * @param year
     * @return
     */
    public static int calcLuckyNumber(int day, int month, int year) {
        // Initialize the variable result.
        int result = 0;
        // Sum the digits of the day, month, and year
        int dateSum = day + month + year;
        // Start a while loop, running until the dateSum is 0
        while (dateSum != 0) {
            // The result is the dateSum modul 10,
            // this way we can abstract the last digit of dateSum
            result = result + (dateSum % 10);
            // dateSum divides by ten, and rounded to the nearest integer
            // in order to break the number down into all its digits
            dateSum = (int) (dateSum / 10);
            // Alternatively we could use Math.random()
            // dateSum = Math.round(dateSum / 10);
        }
        return result;
    }
}
