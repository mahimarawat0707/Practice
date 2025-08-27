using System;

class Program
{
    static void Main()
    {
        int num = 7;
        bool isPrime = true;

        if (num < 2) isPrime = false;

        for (int i = 2; i <= num / 2; i++)
        {
            if (num % i == 0)
            {
                isPrime = false;
                break;
            }
        }

        if (isPrime)
            Console.WriteLine(num + " is Prime");
        else
            Console.WriteLine(num + " is Not Prime");
    }
}
