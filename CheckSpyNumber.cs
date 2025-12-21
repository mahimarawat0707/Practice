using System;

class Program
{
    static void Main()
    {
        int num = 1124, sum = 0, product = 1, temp = num;

        while (num > 0)
        {
            int digit = num % 10;
            sum += digit;
            product *= digit;
            num /= 10;
        }

        if (sum == product)
            Console.WriteLine(temp + " is a Spy Number");
        else
            Console.WriteLine(temp + " is Not a Spy Number");
    }
}
