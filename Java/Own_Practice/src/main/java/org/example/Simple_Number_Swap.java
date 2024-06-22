package org.example;

import java.util.Scanner;

public class Simple_Number_Swap {

    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);

        System.out.println("a = "); int a = userInput.nextInt();
        System.out.println("b = "); int b = userInput.nextInt();

        int temp = a;
        a = b;
        b = temp;

        System.out.println("\nAfter swapping\na = " + a + "\nb = " + b);

    }
}
