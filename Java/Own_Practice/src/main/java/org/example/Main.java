package org.example;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        BinaryAdder binaryAdder = new BinaryAdder();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter expr 1 : ");
        binaryAdder.setExpression1(  scanner.nextLine());
        System.out.print("Enter expr 2 : ");
        binaryAdder.setExpression2(scanner.nextLine());

        System.out.println("The sum of " + binaryAdder.getExpression1() + " and " + binaryAdder.getExpression2() + " is : " + binaryAdder.sum());
    }
}