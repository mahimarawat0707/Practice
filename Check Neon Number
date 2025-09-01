using System;

class Program
{
    static void Main()
    {
        int num = 9, square = num * num, sum = 0;

        while (square > 0)
        {
            sum += square % 10;
            square /= 10;
        }

        if (sum == num)
            Console.WriteLine(num + " is a Neon Number");
        else
            Console.WriteLine(num + " is Not a Neon Number");
    }
}
