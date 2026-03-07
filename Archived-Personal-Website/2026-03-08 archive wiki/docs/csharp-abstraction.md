# C# Abstraction

Abstraction is the process of hiding the internal details and showing only the functionality. It helps in reducing complexity and allows you to focus on what an object does rather than how it does it.

## Abstract Classes
An `abstract` class cannot be instantiated and often contains abstract methods that must be implemented by derived classes.

```csharp
public abstract class Shape
{
    public abstract double CalculateArea(); // No body
}

public class Circle : Shape
{
    public double Radius { get; set; }
    public override double CalculateArea() => Math.PI * Radius * Radius;
}
```

## Interfaces as Abstraction
Interfaces provide a way to achieve abstraction by defining a contract without any implementation.

```csharp
public interface IMessageSender
{
    void Send(string message);
}
```

---
*Back to **[C# Basics](csharp-basics.md)**.*
