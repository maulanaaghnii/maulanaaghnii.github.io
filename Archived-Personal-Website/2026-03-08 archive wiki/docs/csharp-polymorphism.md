# C# Polymorphism

Polymorphism means "many shapes." In C#, it allows objects of different types to be treated as objects of a common base type.

## Types of Polymorphism

### 1. Static Polymorphism (Method Overloading)
Defining multiple methods with the same name but different parameters.
```csharp
public int Add(int a, int b) => a + b;
public double Add(double a, double b) => a + b;
```

### 2. Dynamic Polymorphism (Method Overriding)
Allowing a derived class to provide a specific implementation of a method that is already defined in its base class using `virtual` and `override`.

```csharp
public class Printer
{
    public virtual void Print() => Console.WriteLine("General printing...");
}

public class LaserPrinter : Printer
{
    public override void Print() => Console.WriteLine("Laser printing...");
}
```

---
*For more, check **[Inheritance](csharp-inheritance.md)**.*
