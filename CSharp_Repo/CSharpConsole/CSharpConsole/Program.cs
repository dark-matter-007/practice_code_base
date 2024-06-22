internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Program to calculate the length of a string\n");

        string? mainstr = null;
        Console.WriteLine("Enter a string to find its length : ");
        mainstr = Console.ReadLine();

        int counter = 0;
        if ( mainstr != null ){
            foreach (char character in mainstr ) {
                counter++;
                Console.WriteLine("Current character : " + character);
                Console.WriteLine("Current length : " + counter);
            }
        }

        Console.WriteLine("The length of the given input was  :  " + counter + " using for loop and counter");
        Console.WriteLine("The length of the given input was  :  " + mainstr!.Length + " using length");
    }
}