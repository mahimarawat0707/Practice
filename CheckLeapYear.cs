using System;

class Program
{
    static void Main()
    {
        int year = 2024;

        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
            Console.WriteLine(year + " is a Leap Year");
        else
            Console.WriteLine(year + " is Not a Leap Year");
    }
}
