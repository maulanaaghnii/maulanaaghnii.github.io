# C# Encapsulation

Encapsulation is the technique of making the fields in a class private and providing access to them via public properties or methods. It is often called "data hiding."

## Why Encapsulation?
- **Control**: You can make a property read-only or write-only.
- **Validation**: You can add logic to the `set` accessor.
- **Flexibility**: You can change the internal implementation without affecting callers.

## Example
```csharp
public class BankAccount
{
    private decimal _balance; // Hidden field

    public decimal Balance
    {
        get { return _balance; }
    }

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            _balance += amount;
        }
    }
}
```

---
*See **[C# Basics](csharp-basics.md)** for more OOP principles.*
