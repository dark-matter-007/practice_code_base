// WRITE A PROGRAM TO GET SUM OF ANY INTEGER ENTERED IN LINE COMMAND ARGUMENT IN JAVA

public class Main {
    public static void main(String[] args) {
        Integer sum = 0; // int sum = 0; can also be used. Integer wraps some integral functions with sum.

        for (String argument : args) {
            sum += Integer.parseInt(argument);
        }
        System.out.println("The sum of the numbers is : " + sum);
        // Ashwin
    }
}

