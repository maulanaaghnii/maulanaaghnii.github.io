# C# Generics

Generics allow you to write a class or method that can work with any data type, while maintaining type safety.

## Generic Classes
```csharp
public class Box<T>
{
    private T _content;
    public void Pack(T item) => _content = item;
    public T Unpack() => _content;
}

// Usage
var intBox = new Box<int>();
intBox.Pack(123);

var stringBox = new Box<string>();
stringBox.Pack("Hello");
```

## Generic Methods
```csharp
public void Swap<T>(ref T a, ref T b)
{
    T temp = a;
    a = b;
    b = temp;
}
```

## Benefits
- **Type Safety**: No casting required.
- **Performance**: Avoids boxing/unboxing for value types.
- **Reusability**: One piece of code for many types.
---
*Commonly used in **[LINQ](csharp-linq.md)**.*
