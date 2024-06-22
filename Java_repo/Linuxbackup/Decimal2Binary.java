// Write a program to convert decimal number to binary number

import java.util.Scanner;

public class Decimal2Binary {
    private static Scanner sc;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.print("Enter the decimal number : ");
        int decimal = sc.nextInt();
        String binaryString = Integer.toBinaryString(decimal);
        System.out.println("Binary equivalent of " + decimal + " = " + binaryString);
    }
}
