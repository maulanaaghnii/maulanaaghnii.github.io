# .NET Logging Tutorial

Logging is a critical part of monitoring and debugging .NET applications.

## Built-in Logging
.NET provides a built-in logging abstraction via `ILogger`.

### Setup in ASP.NET Core
By default, ASP.NET Core configures logging in `Program.cs`.

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", (ILogger<Program> logger) => {
    logger.LogInformation("Handling request at {Time}", DateTime.UtcNow);
    return "Hello World";
});

app.Run();
```

### Logging Levels
- **Trace**: Very detailed messages.
- **Debug**: Information useful during development.
- **Information**: General flow of the application.
- **Warning**: Unexpected events that don't stop the app.
- **Error**: Failures that require investigation.
- **Critical**: Severe failures requiring immediate attention.

## Structured Logging
Instead of just strings, log objects to make them searchable.

```csharp
logger.LogInformation("User {UserId} logged in from {IpAddress}", userId, ip);
```

## Popular Logging Providers
- **Serilog**: Highly recommended for structured logging.
- **NLog**: Powerful and flexible.
- **Application Insights**: Great for Azure-hosted apps.

### Example: Serilog Setup
```bash
dotnet add package Serilog.AspNetCore
```

```csharp
Log.Logger = new LoggerConfiguration()
    .WriteTo.Console()
    .WriteTo.File("logs/log.txt", rollingInterval: RollingInterval.Day)
    .CreateLogger();

builder.Host.UseSerilog();
```
