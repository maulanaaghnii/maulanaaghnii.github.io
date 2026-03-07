# C# Interfaces

An interface contains only the signatures of methods, properties, events, or indexers.

## Defining an Interface
```csharp
public interface IWorkable
{
    void DoWork();
}
```

## Implementing an Interface
```csharp
public class Employee : IWorkable
{
    public void DoWork()
    {
        Console.WriteLine("Employee is working.");
    }
}
```

---
*Back to **[C# Basics](csharp-basics.md)**.*
