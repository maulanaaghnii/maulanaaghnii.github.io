# .NET Naming Best Practices

Consistency is key to maintainable code. Follow these Microsoft-standard conventions.

## 1. PascalCase
Used for almost everything public.
- **Classes**: `UserController`
- **Interfaces**: `IUserRepository` (Always starts with `I`)
- **Methods**: `GetUserInfo`
- **Properties**: `CreatedAt`
- **Namespaces**: `MyCompany.MyProject.Services`

## 2. camelCase
Used for local items.
- **Method parameters**: `firstName`
- **Local variables**: `resultCount`

## 3. Private Fields (`_camelCase`)
Private fields should use camelCase prefixed with an underscore.
```csharp
private readonly ILogger _logger;
```

## 4. File Naming
- File names should match the name of the main class they contain.
- Use `.cs` extension.

---
*Back to **[Clean Architecture](dotnet-clean-architecture.md)**.*
