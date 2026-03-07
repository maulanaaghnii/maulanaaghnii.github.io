# .NET Dependency Injection (DI)

Dependency Injection is a design pattern that .NET supports natively. It helps achieve Inversion of Control (IoC) between classes and their dependencies.

## Service Lifetimes
1. **Transient**: Created every time they are requested.
2. **Scoped**: Created once per client request (within a web request).
3. **Singleton**: Created the first time they are requested and then every subsequent request uses the same instance.

## Registration
In `Program.cs`:
```csharp
builder.Services.AddTransient<IMyService, MyService>();
builder.Services.AddScoped<IUserRepository, UserRepository>();
builder.Services.AddSingleton<ICacheService, CacheService>();
```

## Usage
Dependencies are typically injected via the constructor:
```csharp
public class MyController : ControllerBase
{
    private readonly IMyService _myService;

    public MyController(IMyService myService)
    {
        _myService = myService;
    }
}
```
---
*Check **[Clean Architecture](dotnet-clean-architecture.md)** for best practices.*
