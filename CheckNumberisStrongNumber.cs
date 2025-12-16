using System;

class Program
{
    static void Main()
    {
        int num = 145, temp = num, sum = 0;

        while (num > 0)
        {
            int digit = num % 10;
            int fact = 1;

            for (int i = 1; i <= digit; i++)
                fact *= i;

            sum += fact;
            num /= 10;
        }

        if (sum == temp)
            Console.WriteLine(temp + " is a Strong Number");
        else
            Console.WriteLine(temp + " is Not a Strong Number");
    }
}
