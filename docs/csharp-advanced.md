# Advanced C# Concepts

A look into more complex features of the C# language.

## 1. Reflection
The ability of code to inspect its own metadata and types at runtime.
```csharp
Type type = typeof(MyClass);
var methods = type.GetMethods();
```

## 2. Dynamic Programming
Using the `dynamic` keyword to bypass compile-time type checking.
```csharp
dynamic obj = GetUnknownObject();
obj.DoSomething(); // Checked at runtime
```

## 3. Extension Methods
Adding methods to existing types without creating a new derived type.
```csharp
public static class StringExtensions
{
    public static bool IsNumeric(this string s) => int.TryParse(s, out _);
}
```

## 4. Attributes
Adding decorative metadata to code elements.
```csharp
[Serializable]
public class UserData { ... }
```

## 5. Unsafe Code
Working directly with memory addresses using pointers (requires the `unsafe` keyword and project configuration).

---
*Back to **[C# Basics](csharp-basics.md)**.*
