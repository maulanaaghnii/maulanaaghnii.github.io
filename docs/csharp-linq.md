# C# LINQ (Language Integrated Query)

LINQ provides a consistent way to query various data sources like collections, databases, and XML.

## Basic Example
```csharp
int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

// Query syntax
var evenNumbers = from n in numbers
                  where n % 2 == 0
                  select n;

// Method syntax
var evenNumbersMethod = numbers.Where(n => n % 2 == 0);
```

## Common Operators
- `Where`: Filter
- `Select`: Project
- `OrderBy`: Sort
- `First` / `FirstOrDefault`: Get first element
- `ToList` / `ToArray`: Convert to collection
