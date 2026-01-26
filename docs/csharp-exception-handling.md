# C# Exception Handling

Exception handling is used to handle runtime errors in a graceful way.

## Try-Catch-Finally
```csharp
try 
{
    int result = 10 / int.Parse("0");
}
catch (DivideByZeroException ex)
{
    Console.WriteLine("Cannot divide by zero!");
}
catch (Exception ex)
{
    Console.WriteLine($"An error occurred: {ex.Message}");
}
finally
{
    Console.WriteLine("Cleanup code here (always runs).");
}
```

## Throwing Exceptions
```csharp
if (user == null)
{
    throw new ArgumentNullException(nameof(user));
}
```

## Custom Exceptions
```csharp
public class MyBusinessException : Exception
{
    public MyBusinessException(string message) : base(message) { }
}
```
