import java.util.Scanner;

public class EvenOddFinder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number to check : ");
        int number = scanner.nextInt();

        if ( number%2 == 0) {
            System.out.println("The number is even...");
        } else {
            System.out.println("The number is odd...");
        }
    }
}
