import java.util.Scanner;

public class Array {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of array: ");
        int[] array = new int[scanner.nextInt()];

        for ( int index = 0; index < array.length; index++){
            System.out.print("Enter element at index " + index + ": " );
            array[index] = scanner.nextInt();
        }
        System.out.println("THe formed array of length " + array.length + " is : ");
        for ( int element : array ) {
            System.out.printf(element + "  ");
        }
    }
}
