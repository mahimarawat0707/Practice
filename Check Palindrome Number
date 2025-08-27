using System;

class Program
{
    static void Main()
    {
        int num = 121, temp = num, reverse = 0;

        while (num != 0)
        {
            reverse = reverse * 10 + (num % 10);
            num /= 10;
        }

        if (temp == reverse)
            Console.WriteLine(temp + " is Palindrome");
        else
            Console.WriteLine(temp + " is Not Palindrome");
    }
}
