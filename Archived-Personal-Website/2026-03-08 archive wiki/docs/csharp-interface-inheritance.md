# C# Interface Inheritance

Interfaces in C# can inherit from one or more other interfaces.

## Basic Syntax
```csharp
public interface IBase
{
    void BaseMethod();
}

public interface IDerived : IBase
{
    void DerivedMethod();
}
```

## Implementation
When a class implements `IDerived`, it must provide implementation for *all* methods in the hierarchy.
```csharp
public class MyClass : IDerived
{
    public void BaseMethod() { ... }
    public void DerivedMethod() { ... }
}
```

## Multiple Interface Inheritance
A single interface can inherit from multiple parent interfaces.
```csharp
public interface ICombined : IBase, IOther { ... }
```

---
*For more, see **[C# Interfaces](csharp-interface.md)**.*
