# C# Lambda Expressions

Lambda expressions are anonymous functions that you can use to create delegates or expression tree types.

## Basic Syntax
`(input-parameters) => expression-or-statement-block`

```csharp
// Simple expression
Func<int, int> square = x => x * x;
Console.WriteLine(square(5)); // 25

// Statement block
Action<string> greet = name => {
    string message = $"Hello {name}!";
    Console.WriteLine(message);
};
```

## Usage with LINQ
Lambdas are most commonly used with LINQ methods.
```csharp
var scores = new[] { 90, 71, 82, 93, 75 };
var passingScores = scores.Where(s => s >= 80);
```

## Closures
Lambdas can "capture" variables from the outer scope.
```csharp
int factor = 2;
Func<int, int> multiplier = n => n * factor;
```

---
*Learn more in **[LINQ](csharp-linq.md)**.*
