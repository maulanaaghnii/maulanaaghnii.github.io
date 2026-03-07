# .NET Environment Variables

Configuring behavior in .NET applications using environment variables, often used in conjunction with `appsettings.json`.

## Configuration Provider
By default, .NET loads environment variables via the `EnvironmentVariablesConfigurationProvider`.

```csharp
// Program.cs
var builder = WebApplication.CreateBuilder(args);
// Builder automatically calls AddEnvironmentVariables()
```

## Naming Conventions
To map nested JSON configuration to environment variables, use double underscores (`__`).
`ConnectionStrings:DefaultConnection` becomes `ConnectionStrings__DefaultConnection`.

## Accessing Variables
```csharp
// Via IConfiguration (Preferred)
string dbHost = configuration["DB_HOST"];

// Directly from the system
string path = Environment.GetEnvironmentVariable("PATH");
```

## ASPNETCORE_ENVIRONMENT
Used to determine which `appsettings.{Environment}.json` to load.
- `Development`
- `Staging`
- `Production`

---
*For container usage, see **[Docker Environment Variables](docker-environment-variables.md)**.*
