# Entity Framework Core (EF Core)

EF Core is a modern object-database mapper (ORM) for .NET. It lets you work with data using .NET objects.

## Core Concepts
- **DbContext**: The bridge between your code and the database.
- **DbSet**: Represents a table in the database.
- **Migrations**: Tracks changes to your model and applies them to the database schema.

## Basic Setup
```csharp
public class MyDbContext : DbContext
{
    public DbSet<User> Users { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer("Your_Connection_String");
    }
}
```

## Common Commands
```bash
# Add a migration
dotnet ef migrations add InitialCreate

# Update database
dotnet ef database update

# Remove last migration
dotnet ef migrations remove
```

## Querying Data (LINQ)
```csharp
var users = context.Users
    .Where(u => u.IsActive)
    .OrderBy(u => u.Name)
    .ToList();
```

---
*See **[Entity Framework Minimal](dotnet-entity-framework-minimal.md)** for a quick start.*
