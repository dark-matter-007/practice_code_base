import java.util.Scanner;

public class BinaryManual {
    public static void main(String[] args) {

        System.out.print("Enter a number : ");
        Integer myDecimalNumber = (new Scanner(System.in)).nextInt();
        System.out.printf("The binary for %d is %s".formatted(myDecimalNumber, getBinaryStringForThisNumber(myDecimalNumber)));
    }

    static String getBinaryStringForThisNumber(Integer number) {
        String answerString = new String();
        while (number > 1) {
            int tempAnswer = number %2;
            System.out.println("Current state = " + number);
            answerString = answerString.concat(Integer.toString(tempAnswer));
            number = Math.floorDiv(number, 2);
        }
        answerString = answerString.concat(Integer.toString(number));

        while (answerString.length() < 3){
            answerString = answerString.concat("0"); // as the string is not yet reversed we don't "0".concat(string)
        }

        return String.valueOf((new StringBuilder(answerString)).reverse());
    }
}
