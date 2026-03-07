# Testing in .NET

Writing tests ensures your application behaves as expected and prevents regressions.

## Types of Tests
1. **Unit Tests**: Test individual classes or methods in isolation.
2. **Integration Tests**: Test how different parts of the system work together (e.g., API + Database).
3. **End-to-End (E2E) Tests**: Test the entire application flow from the user's perspective.

## Common Frameworks
- **xUnit**: The most modern and popular choice for .NET.
- **NUnit**: Feature-rich and well-established.
- **MSTest**: Microsoft's official testing framework.

## Sample xUnit Test
```csharp
public class CalculatorTests
{
    [Fact]
    public void Add_ShouldReturnSum()
    {
        // Arrange
        var calc = new Calculator();

        // Act
        var result = calc.Add(2, 2);

        // Assert
        Assert.Equal(4, result);
    }
}
```

## Useful Testing Libraries
- **Moq**: For creating mock objects in unit tests.
- **FluentAssertions**: For writing more readable assertions.
- **AutoFixture**: For generating test data automatically.

## Running Tests
```bash
dotnet test
```
---
*Check **[GitHub Guide](github.md)** for running tests in CI/CD.*
