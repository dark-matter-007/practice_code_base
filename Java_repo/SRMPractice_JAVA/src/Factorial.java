import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int result, multiplier, userInput = 0;

        System.out.println("Enter the number to find factorial of : ");
        result = userInput = scanner.nextByte();

        for ( multiplier = userInput-1; multiplier >= 1; multiplier--  ) {
            result = result*multiplier;
        }

        System.out.println("The factorial of " + userInput + " is " + result); // int will be type-casted implicitly
    }
}
