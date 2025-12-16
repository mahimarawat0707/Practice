using System;

class Program
{
    static void Main()
    {
        string num = "3210";

        if (num.StartsWith("0"))
            Console.WriteLine(num + " is Not a Duck Number");
        else if (num.Contains("0"))
            Console.WriteLine(num + " is a Duck Number");
        else
            Console.WriteLine(num + " is Not a Duck Number");
    }
}
