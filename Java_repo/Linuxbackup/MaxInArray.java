import java.util.Arrays;

public class MaxInArray {
    public static void main(String[] args) {
        int[] myArray = {1,2,5,10,30,2,3,4};
        System.out.println(Arrays.stream(myArray).max());
    }
}
