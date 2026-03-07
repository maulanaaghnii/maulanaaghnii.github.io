# C# Inheritance

Inheritance allows a class to inherit members from another class.

## Base and Derived Classes
```csharp
// Base class (Parent)
public class Animal
{
    public void Eat() => Console.WriteLine("Eating...");
}

// Derived class (Child)
public class Dog : Animal
{
    public void Bark() => Console.WriteLine("Barking...");
}
```

## Usage
```csharp
Dog myDog = new Dog();
myDog.Eat();  // Inherited method
myDog.Bark(); // Own method
```

---
*Back to **[C# Basics](csharp-basics.md)**.*
