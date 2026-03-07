# .NET Classes and Objects

Understanding the .NET type system is fundamental to building robust applications.

## Value Types vs. Reference Types

### Value Types
Value types hold the actual data. They are usually stored on the stack.
- **Predefined types**: `int`, `long`, `float`, `double`, `decimal`, `bool`, `char`.
- **Structures**: `struct`.
- **Enumerations**: `enum`.

### Reference Types
Reference types hold a reference (memory address) to the actual data. They are stored on the managed heap.
Reference types contain `null` until they are assigned with an instance.
- **Classes**: `class`.
- **Records**: `record` (C# 9+).
- **Interfaces**: `interface`.
- **Delegates**: `delegate`.
- **Arrays**: `[]`.
- **Dynamic**: `dynamic`.

## Classes in .NET
A class is a blueprint for creating objects.

```csharp
public class Person
{
    // Properties
    public string Name { get; set; }
    public int Age { get; set; }

    // Constructor
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // Method
    public void DisplayInfo() => Console.WriteLine($"{Name} is {Age} years old.");
}

// Creating an object
var person = new Person("Alice", 30);
person.DisplayInfo();
```

## Records (C# 9+)
Records provide built-in functionality for encapsulating data with value-based equality.

```csharp
public record User(string Username, string Email);
```

### Source
- [Examine the .NET type system (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/get-started-classes-objects/3-examine-dotnet-type-system)