using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== DIVISION PROGRAM ===");

        Console.Write("Enter the numerator: ");
        bool isValid1 = double.TryParse(Console.ReadLine(), out double numerator);

        Console.Write("Enter the denominator: ");
        bool isValid2 = double.TryParse(Console.ReadLine(), out double denominator);

        if (!isValid1 || !isValid2)
        {
            Console.WriteLine("❌ Invalid input! Please enter valid numbers.");
        }
        else if (denominator == 0)
        {
            Console.WriteLine("⚠️ Error: Cannot divide by zero!");
        }
        else
        {
            double result = numerator / denominator;
            Console.WriteLine($"✅ Result: {numerator} ÷ {denominator} = {result}");
        }

        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }
}
