using System;

class MultiplicationTable
{
    static void Main()
    {
        Console.Write("Enter the number for the multiplication table: ");
        int number = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter the range (till which number you want the table): ");
        int range = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine($"\nMultiplication Table of {number} till {range}:\n");

        int i = 1;
        while (i <= range)
        {
            Console.WriteLine($"{number} x {i} = {number * i}");
            i++;
        }

        Console.WriteLine("\nTable Generated Successfully!");
    }
}
