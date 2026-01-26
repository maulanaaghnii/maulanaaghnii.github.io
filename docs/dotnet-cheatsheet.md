# .NET CLI Cheat Sheet

A quick reference for the most common .NET CLI commands.

## Project Management
```bash
# Create a new project
dotnet new webapi -n MyProject
dotnet new console -n MyConsole

# Create a solution
dotnet new sln -n MySolution

# Add project to solution
dotnet sln add MyProject/MyProject.csproj
```

## Dependencies
```bash
# Add a NuGet package
dotnet add package Newtonsoft.Json

# Add a project reference
dotnet add MyProject.csproj reference ../Dependency/Dependency.csproj

# List dependencies
dotnet list package
```

## Build and Run
```bash
# Restore dependencies
dotnet restore

# Build project
dotnet build

# Run project
dotnet run

# Watch for changes and rerun
dotnet watch run
```

## Testing
```bash
# Run tests
dotnet test

# Run tests with filter
dotnet test --filter "FullyQualifiedName~MyNamespace.MyTest"
```

## Publishing
```bash
# Publish for production
dotnet publish -c Release -o ./publish

# Self-contained publish (includes runtime)
dotnet publish -c Release -r win-x64 --self-contained
```
