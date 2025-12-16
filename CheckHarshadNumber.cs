using System;

class Program
{
    static void Main()
    {
        int num = 18, sum = 0, temp = num;

        while (num > 0)
        {
            sum += num % 10;
            num /= 10;
        }

        if (temp % sum == 0)
            Console.WriteLine(temp + " is a Harshad Number");
        else
            Console.WriteLine(temp + " is Not a Harshad Number");
    }
}
