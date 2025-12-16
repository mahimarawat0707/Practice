using System;

class Program
{
    static void Main()
    {
        int num = 49;
        int sqrt = (int)Math.Sqrt(num);

        if (sqrt * sqrt == num)
            Console.WriteLine(num + " is a Perfect Square");
        else
            Console.WriteLine(num + " is Not a Perfect Square");
    }
}
