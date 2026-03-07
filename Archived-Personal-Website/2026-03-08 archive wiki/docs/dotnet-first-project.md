# Creating and Running Your First Project

## Overview

Creating your first .NET project is an exciting milestone in your development journey. This guide walks you through creating various types of projects, understanding project structure, and running your applications successfully.

## Prerequisites

Before starting, ensure you have:

```bash
# Verify .NET installation
dotnet --version

# Should show something like: 8.0.100
# If not installed, follow the installation guide
```

## Your First Console Application

### Step 1: Create the Project

```bash
# Create a new directory for your project
mkdir MyFirstProject
cd MyFirstProject

# Create console application
dotnet new console -n HelloWorld
cd HelloWorld

# Alternative: Create in current directory
dotnet new console
```

### Step 2: Examine Project Structure

```
HelloWorld/
├── HelloWorld.csproj    # Project file
├── Program.cs           # Main program file
└── obj/                 # Build artifacts (auto-generated)
```

### Step 3: Understanding the Project File

```xml
<!-- HelloWorld.csproj -->
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

### Step 4: Examine the Program Code

```csharp
// Program.cs (Traditional approach)
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}

// Program.cs (Modern top-level approach - .NET 6+)
Console.WriteLine("Hello, World!");
```

### Step 5: Run Your Application

```bash
# Run the application
dotnet run

# Expected output:
# Hello, World!
```

## Building a More Interactive Console App

### Enhanced Program Example

```csharp
// Program.cs - Interactive Console Application
using System;

Console.WriteLine("=== Welcome to My First .NET Application ===");
Console.WriteLine();

// Get user input
Console.Write("Please enter your name: ");
string? userName = Console.ReadLine();

Console.Write("Please enter your age: ");
string? ageInput = Console.ReadLine();

// Validate and process input
if (string.IsNullOrEmpty(userName))
{
    userName = "Anonymous";
}

if (int.TryParse(ageInput, out int age))
{
    Console.WriteLine();
    Console.WriteLine($"Hello, {userName}!");
    Console.WriteLine($"You are {age} years old.");
    
    if (age >= 18)
    {
        Console.WriteLine("You are an adult.");
    }
    else
    {
        Console.WriteLine($"You will be an adult in {18 - age} years.");
    }
}
else
{
    Console.WriteLine();
    Console.WriteLine($"Hello, {userName}!");
    Console.WriteLine("Invalid age entered, but nice to meet you!");
}

Console.WriteLine();
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```

### Running the Enhanced Application

```bash
# Build and run
dotnet build
dotnet run

# Or run directly
dotnet run

# Example interaction:
# === Welcome to My First .NET Application ===
# 
# Please enter your name: John Doe
# Please enter your age: 25
# 
# Hello, John Doe!
# You are 25 years old.
# You are an adult.
# 
# Press any key to exit...
```

## Creating a Class Library

### Step 1: Create the Library Project

```bash
# Create class library
dotnet new classlib -n MyLibrary
cd MyLibrary
```

### Step 2: Create a Useful Class

```csharp
// Calculator.cs
namespace MyLibrary
{
    public class Calculator
    {
        public int Add(int a, int b)
        {
            return a + b;
        }

        public int Subtract(int a, int b)
        {
            return a - b;
        }

        public int Multiply(int a, int b)
        {
            return a * b;
        }

        public double Divide(int a, int b)
        {
            if (b == 0)
                throw new ArgumentException("Cannot divide by zero", nameof(b));
            
            return (double)a / b;
        }

        public double GetCircleArea(double radius)
        {
            if (radius < 0)
                throw new ArgumentException("Radius cannot be negative", nameof(radius));
            
            return Math.PI * radius * radius;
        }
    }
}
```

### Step 3: Create a Person Class

```csharp
// Person.cs
namespace MyLibrary
{
    public class Person
    {
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = string.Empty;
        public DateTime BirthDate { get; set; }

        public string FullName => $"{FirstName} {LastName}";

        public int Age
        {
            get
            {
                var today = DateTime.Today;
                var age = today.Year - BirthDate.Year;
                
                if (BirthDate.Date > today.AddYears(-age))
                    age--;
                
                return age;
            }
        }

        public bool IsAdult => Age >= 18;

        public Person(string firstName, string lastName, DateTime birthDate)
        {
            FirstName = firstName;
            LastName = lastName;
            BirthDate = birthDate;
        }

        public override string ToString()
        {
            return $"{FullName} (Age: {Age})";
        }
    }
}
```

## Creating a Console App That Uses the Library

### Step 1: Create Solution Structure

```bash
# Go back to root directory
cd ..

# Create solution
dotnet new sln -n MyFirstSolution

# Add projects to solution
dotnet sln add HelloWorld/HelloWorld.csproj
dotnet sln add MyLibrary/MyLibrary.csproj

# Create new console app that uses the library
dotnet new console -n CalculatorApp
dotnet sln add CalculatorApp/CalculatorApp.csproj

# Add reference from console app to library
dotnet add CalculatorApp/CalculatorApp.csproj reference MyLibrary/MyLibrary.csproj
```

### Step 2: Build the Calculator Console App

```csharp
// CalculatorApp/Program.cs
using MyLibrary;

Console.WriteLine("=== Simple Calculator ===");
Console.WriteLine();

var calculator = new Calculator();
bool continueCalculation = true;

while (continueCalculation)
{
    try
    {
        Console.WriteLine("Choose an operation:");
        Console.WriteLine("1. Addition");
        Console.WriteLine("2. Subtraction");
        Console.WriteLine("3. Multiplication");
        Console.WriteLine("4. Division");
        Console.WriteLine("5. Circle Area");
        Console.WriteLine("6. Exit");
        Console.Write("Enter your choice (1-6): ");

        string? choice = Console.ReadLine();

        switch (choice)
        {
            case "1":
                PerformBasicOperation(calculator.Add, "Addition");
                break;
            case "2":
                PerformBasicOperation(calculator.Subtract, "Subtraction");
                break;
            case "3":
                PerformBasicOperation(calculator.Multiply, "Multiplication");
                break;
            case "4":
                PerformDivision(calculator);
                break;
            case "5":
                CalculateCircleArea(calculator);
                break;
            case "6":
                continueCalculation = false;
                Console.WriteLine("Thank you for using the calculator!");
                break;
            default:
                Console.WriteLine("Invalid choice. Please try again.");
                break;
        }

        if (continueCalculation)
        {
            Console.WriteLine();
            Console.WriteLine("Press any key to continue...");
            Console.ReadKey();
            Console.Clear();
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"An error occurred: {ex.Message}");
        Console.WriteLine();
    }
}

static void PerformBasicOperation(Func<int, int, int> operation, string operationName)
{
    Console.Write("Enter first number: ");
    if (int.TryParse(Console.ReadLine(), out int num1))
    {
        Console.Write("Enter second number: ");
        if (int.TryParse(Console.ReadLine(), out int num2))
        {
            int result = operation(num1, num2);
            Console.WriteLine($"{operationName} result: {result}");
        }
        else
        {
            Console.WriteLine("Invalid second number.");
        }
    }
    else
    {
        Console.WriteLine("Invalid first number.");
    }
}

static void PerformDivision(Calculator calculator)
{
    Console.Write("Enter first number: ");
    if (int.TryParse(Console.ReadLine(), out int num1))
    {
        Console.Write("Enter second number: ");
        if (int.TryParse(Console.ReadLine(), out int num2))
        {
            try
            {
                double result = calculator.Divide(num1, num2);
                Console.WriteLine($"Division result: {result:F2}");
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
        else
        {
            Console.WriteLine("Invalid second number.");
        }
    }
    else
    {
        Console.WriteLine("Invalid first number.");
    }
}

static void CalculateCircleArea(Calculator calculator)
{
    Console.Write("Enter radius: ");
    if (double.TryParse(Console.ReadLine(), out double radius))
    {
        try
        {
            double area = calculator.GetCircleArea(radius);
            Console.WriteLine($"Circle area: {area:F2}");
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
    else
    {
        Console.WriteLine("Invalid radius.");
    }
}
```

### Step 3: Run the Calculator App

```bash
# Navigate to calculator app
cd CalculatorApp

# Run the application
dotnet run

# Or run from solution root
cd ..
dotnet run --project CalculatorApp
```

## Creating Your First Web Application

### Step 1: Create Web API Project

```bash
# Create web API project
dotnet new webapi -n MyFirstWebAPI
cd MyFirstWebAPI

# Add to solution
cd ..
dotnet sln add MyFirstWebAPI/MyFirstWebAPI.csproj
```

### Step 2: Examine Web API Structure

```
MyFirstWebAPI/
├── Controllers/
│   └── WeatherForecastController.cs
├── Properties/
│   └── launchSettings.json
├── appsettings.json
├── appsettings.Development.json
├── MyFirstWebAPI.csproj
└── Program.cs
```

### Step 3: Create a Simple API Controller

```csharp
// Controllers/PersonController.cs
using Microsoft.AspNetCore.Mvc;
using MyLibrary;

namespace MyFirstWebAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PersonController : ControllerBase
    {
        [HttpGet]
        public ActionResult<IEnumerable<Person>> Get()
        {
            var people = new List<Person>
            {
                new Person("John", "Doe", new DateTime(1990, 5, 15)),
                new Person("Jane", "Smith", new DateTime(1985, 8, 22)),
                new Person("Bob", "Johnson", new DateTime(2000, 12, 3))
            };

            return Ok(people);
        }

        [HttpGet("{id}")]
        public ActionResult<Person> Get(int id)
        {
            if (id < 1 || id > 3)
                return NotFound();

            var people = new List<Person>
            {
                new Person("John", "Doe", new DateTime(1990, 5, 15)),
                new Person("Jane", "Smith", new DateTime(1985, 8, 22)),
                new Person("Bob", "Johnson", new DateTime(2000, 12, 3))
            };

            return Ok(people[id - 1]);
        }

        [HttpPost]
        public ActionResult<Person> Create([FromBody] CreatePersonRequest request)
        {
            if (string.IsNullOrEmpty(request.FirstName) || string.IsNullOrEmpty(request.LastName))
                return BadRequest("First name and last name are required.");

            var person = new Person(request.FirstName, request.LastName, request.BirthDate);
            return Ok(person);
        }
    }

    public class CreatePersonRequest
    {
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = string.Empty;
        public DateTime BirthDate { get; set; }
    }
}
```

### Step 4: Add Library Reference to Web API

```bash
# Add reference to library
dotnet add MyFirstWebAPI/MyFirstWebAPI.csproj reference MyLibrary/MyLibrary.csproj
```

### Step 5: Run the Web API

```bash
# Navigate to web API project
cd MyFirstWebAPI

# Run the application
dotnet run

# The application will start and show something like:
# info: Microsoft.Hosting.Lifetime[14]
#       Now listening on: https://localhost:7001
#       Now listening on: http://localhost:5000
```

### Step 6: Test the API

```bash
# Test using curl (in another terminal)
curl https://localhost:7001/api/person

# Or test specific endpoints
curl https://localhost:7001/api/person/1

# Create new person
curl -X POST https://localhost:7001/api/person \
  -H "Content-Type: application/json" \
  -d '{"firstName":"Alice","lastName":"Wonder","birthDate":"1995-03-10T00:00:00"}'
```

## Creating a Unit Test Project

### Step 1: Create Test Project

```bash
# Create xUnit test project
dotnet new xunit -n MyLibrary.Tests

# Add to solution
dotnet sln add MyLibrary.Tests/MyLibrary.Tests.csproj

# Add reference to library being tested
dotnet add MyLibrary.Tests/MyLibrary.Tests.csproj reference MyLibrary/MyLibrary.csproj
```

### Step 2: Write Unit Tests

```csharp
// MyLibrary.Tests/CalculatorTests.cs
using Xunit;
using MyLibrary;

namespace MyLibrary.Tests
{
    public class CalculatorTests
    {
        private readonly Calculator _calculator;

        public CalculatorTests()
        {
            _calculator = new Calculator();
        }

        [Fact]
        public void Add_TwoPositiveNumbers_ReturnsSum()
        {
            // Arrange
            int a = 5;
            int b = 3;
            int expected = 8;

            // Act
            int result = _calculator.Add(a, b);

            // Assert
            Assert.Equal(expected, result);
        }

        [Fact]
        public void Subtract_TwoNumbers_ReturnsDifference()
        {
            // Arrange
            int a = 10;
            int b = 4;
            int expected = 6;

            // Act
            int result = _calculator.Subtract(a, b);

            // Assert
            Assert.Equal(expected, result);
        }

        [Fact]
        public void Multiply_TwoNumbers_ReturnsProduct()
        {
            // Arrange
            int a = 6;
            int b = 7;
            int expected = 42;

            // Act
            int result = _calculator.Multiply(a, b);

            // Assert
            Assert.Equal(expected, result);
        }

        [Fact]
        public void Divide_TwoNumbers_ReturnsQuotient()
        {
            // Arrange
            int a = 15;
            int b = 3;
            double expected = 5.0;

            // Act
            double result = _calculator.Divide(a, b);

            // Assert
            Assert.Equal(expected, result, 2); // 2 decimal places precision
        }

        [Fact]
        public void Divide_ByZero_ThrowsArgumentException()
        {
            // Arrange
            int a = 10;
            int b = 0;

            // Act & Assert
            Assert.Throws<ArgumentException>(() => _calculator.Divide(a, b));
        }

        [Theory]
        [InlineData(1, 3.14159)]
        [InlineData(2, 12.56636)]
        [InlineData(0, 0)]
        public void GetCircleArea_ValidRadius_ReturnsCorrectArea(double radius, double expectedArea)
        {
            // Act
            double result = _calculator.GetCircleArea(radius);

            // Assert
            Assert.Equal(expectedArea, result, 2);
        }

        [Fact]
        public void GetCircleArea_NegativeRadius_ThrowsArgumentException()
        {
            // Arrange
            double radius = -5;

            // Act & Assert
            Assert.Throws<ArgumentException>(() => _calculator.GetCircleArea(radius));
        }
    }
}
```

### Step 3: Write Person Tests

```csharp
// MyLibrary.Tests/PersonTests.cs
using Xunit;
using MyLibrary;

namespace MyLibrary.Tests
{
    public class PersonTests
    {
        [Fact]
        public void Constructor_ValidInput_CreatesPersonCorrectly()
        {
            // Arrange
            string firstName = "John";
            string lastName = "Doe";
            DateTime birthDate = new DateTime(1990, 5, 15);

            // Act
            var person = new Person(firstName, lastName, birthDate);

            // Assert
            Assert.Equal(firstName, person.FirstName);
            Assert.Equal(lastName, person.LastName);
            Assert.Equal(birthDate, person.BirthDate);
            Assert.Equal("John Doe", person.FullName);
        }

        [Fact]
        public void Age_BornInPast_ReturnsCorrectAge()
        {
            // Arrange
            var birthDate = DateTime.Today.AddYears(-25).AddDays(-100); // 25+ years ago
            var person = new Person("John", "Doe", birthDate);

            // Act
            int age = person.Age;

            // Assert
            Assert.True(age >= 25);
        }

        [Fact]
        public void IsAdult_PersonOver18_ReturnsTrue()
        {
            // Arrange
            var birthDate = DateTime.Today.AddYears(-20); // 20 years ago
            var person = new Person("John", "Doe", birthDate);

            // Act
            bool isAdult = person.IsAdult;

            // Assert
            Assert.True(isAdult);
        }

        [Fact]
        public void IsAdult_PersonUnder18_ReturnsFalse()
        {
            // Arrange
            var birthDate = DateTime.Today.AddYears(-16); // 16 years ago
            var person = new Person("Jane", "Doe", birthDate);

            // Act
            bool isAdult = person.IsAdult;

            // Assert
            Assert.False(isAdult);
        }

        [Fact]
        public void ToString_ReturnsFormattedString()
        {
            // Arrange
            var person = new Person("John", "Doe", new DateTime(1990, 5, 15));

            // Act
            string result = person.ToString();

            // Assert
            Assert.Contains("John Doe", result);
            Assert.Contains("Age:", result);
        }
    }
}
```

### Step 4: Run Tests

```bash
# Run all tests
dotnet test

# Run tests with verbose output
dotnet test -v normal

# Run specific test project
dotnet test MyLibrary.Tests

# Run with coverage (requires additional packages)
dotnet test --collect:"XPlat Code Coverage"
```

## Project Structure Best Practices

### Final Solution Structure

```
MyFirstSolution/
├── MyFirstSolution.sln
├── src/
│   ├── MyLibrary/
│   │   ├── Calculator.cs
│   │   ├── Person.cs
│   │   └── MyLibrary.csproj
│   ├── HelloWorld/
│   │   ├── Program.cs
│   │   └── HelloWorld.csproj
│   ├── CalculatorApp/
│   │   ├── Program.cs
│   │   └── CalculatorApp.csproj
│   └── MyFirstWebAPI/
│       ├── Controllers/
│       ├── Program.cs
│       └── MyFirstWebAPI.csproj
└── tests/
    └── MyLibrary.Tests/
        ├── CalculatorTests.cs
        ├── PersonTests.cs
        └── MyLibrary.Tests.csproj
```

### Organizing with Folders

```bash
# Create organized structure
mkdir src tests

# Move projects to appropriate folders
mv MyLibrary src/
mv HelloWorld src/
mv CalculatorApp src/
mv MyFirstWebAPI src/
mv MyLibrary.Tests tests/

# Update solution file references (automatic with newer .NET versions)
dotnet sln list  # Check current projects
```

## Building and Running Everything

### Build Entire Solution

```bash
# Build all projects in solution
dotnet build

# Build in Release mode
dotnet build -c Release

# Clean and rebuild
dotnet clean
dotnet build
```

### Run Different Projects

```bash
# Run console app
dotnet run --project src/HelloWorld

# Run calculator app
dotnet run --project src/CalculatorApp

# Run web API
dotnet run --project src/MyFirstWebAPI

# Run tests
dotnet test tests/MyLibrary.Tests
```

## Common Issues and Solutions

### Issue 1: Project Reference Not Found

```bash
# Problem: Cannot find referenced project
# Solution: Check and fix project references
dotnet list reference
dotnet add reference ../MyLibrary/MyLibrary.csproj
```

### Issue 2: Package Restore Issues

```bash
# Problem: NuGet packages not restored
# Solution: Restore packages
dotnet restore

# Clear cache if needed
dotnet nuget locals all --clear
dotnet restore
```

### Issue 3: Build Errors

```bash
# Problem: Build fails
# Solution: Clean and rebuild
dotnet clean
dotnet build -v normal  # Verbose output for debugging
```

## Next Steps

After creating your first projects:

1. **[Learn NuGet package management](nuget-management.md)**
2. **[Understand dependency injection](dotnet-dependency-injection.md)**
3. **[Explore Entity Framework](entity-framework-core.md)**
4. **[Build REST APIs](aspnetcore-rest-api.md)**

## Summary

You've successfully created:

| Project Type | Purpose | Key Learning |
|--------------|---------|--------------|
| **Console App** | Command-line application | Basic .NET structure |
| **Class Library** | Reusable code components | Code organization |
| **Web API** | REST API service | Web development basics |
| **Unit Tests** | Code quality assurance | Testing fundamentals |

These foundational projects demonstrate core .NET concepts and provide a solid base for more advanced development. Practice building variations of these project types to strengthen your understanding of .NET development patterns.
