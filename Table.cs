using System;

class MultiplicationTable
{
    static void Main()
    {
        Console.Write("Enter a number for the multiplication table: ");
        int number = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine($"\nMultiplication Table of {number}:\n");

        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{number} x {i} = {number * i}");
        }

        Console.WriteLine("\nDone!");
    }
}
