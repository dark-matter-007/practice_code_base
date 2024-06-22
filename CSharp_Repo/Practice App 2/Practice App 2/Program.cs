using System.ComponentModel.DataAnnotations.Schema;
using System.Data;

class Program {
    public static void Main(string[] args) {
        Console.WriteLine("THIS APP IS INTENDED FOR PRACTICE IN VARIOUS TINY PROBLEMS");

        System.Console.WriteLine(@"
        1 : Find string length
        2 : Simple calculator\n");
        Console.Write("Input your choice : ");
        if (int.TryParse(Console.ReadLine(), out int userInput)) {
            Console.WriteLine("Parse successful");
        } else {
            Console.WriteLine("Parse failed");
        }
        System.Console.WriteLine("Your input is : " + userInput);
    
        if (userInput == 2) {
            Console.WriteLine("Type the expression you want to calculate : ");
            string expression = Console.ReadLine()!; // The exclamation means that the value must not be null when the user gives the input
            DataTable datatable = new();
            int result = (int)datatable.Compute(expression, "");
            Console.WriteLine("The answer is : " + result);
        }
    }
}