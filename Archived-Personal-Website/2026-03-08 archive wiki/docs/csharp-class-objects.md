# C# Classes and Objects

Classes and objects are the fundamental building blocks of object-oriented programming in C#.

## Defining a Class
```csharp
public class Car
{
    // Properties
    public string Model { get; set; }
    public string Color { get; set; }

    // Constructor
    public Car(string model, string color)
    {
        Model = model;
        Color = color;
    }

    // Method
    public void Drive()
    {
        Console.WriteLine($"The {Color} {Model} is driving.");
    }
}
```

## Creating an Object
```csharp
Car myCar = new Car("Tesla Model 3", "Red");
myCar.Drive();
```

---
*For more basics, see **[C# Basics](csharp-basics.md)**.*
