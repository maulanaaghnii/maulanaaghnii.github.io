# .NET and SQL Server Integration

SQL Server is the most common database used with .NET applications.

## 1. Install Provider
```bash
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
```

## 2. Configuration
In `appsettings.json`:
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;"
  }
}
```

## 3. Register in Program.cs
```csharp
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
builder.Services.AddDbContext<MyDbContext>(options =>
    options.UseSqlServer(connectionString));
```

## LocalDB vs full SQL Server
- **LocalDB**: Lightweight version for development.
- **SQL Server Express**: Free version for small production apps.
- **SQL Server / Azure SQL**: Full-featured versions for enterprise scaling.

---
*For other databases, check **[PostgreSQL](postgresql.md)** or **[MySQL](mysql.md)**.*
