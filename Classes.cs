using System;

class Person
{
    // Private fields
    private string name;
    private int age;

    // Constructor
    public Person(string name, int age)
    {
        this.name = name;
        this.age = age;
    }

    // Property for name with get and set (encapsulation)
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    // Property for age with validation in set
    public int Age
    {
        get { return age; }
        set 
        {
            if (value < 0)
                throw new ArgumentException("Age cannot be negative");
            age = value;
        }
    }

    // Method
    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
    }
}

class Program
{
    static void Main()
    {
        Person p = new Person("Alice", 30);

        // Access properties
        p.Display();

        // Change properties with validation
        p.Age = 35;
        p.Name = "Alice Smith";

        p.Display();

        try
        {
            p.Age = -5; // This will throw exception due to validation
        }
        catch(ArgumentException e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
