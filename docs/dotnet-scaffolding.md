# .NET Scaffolding (Existing Databases)


## 1. Packages Requirements

### Install EF (if doesn't exist)

```
dotnet tool install --global dotnet-ef
```

### Add project package

```
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
dotnet tool install --global dotnet-aspnet-codegenerator
```

## 2. Start Scaffolding DbContext & Models From Databases

### Without SQL Auth

```
dotnet ef dbcontext scaffold "Server=localhost;Database=meknetic_db;Trusted_Connection=True;TrustServerCertificate=True;" Microsoft.EntityFrameworkCore.SqlServer --output-dir Models --context-dir Data --context AppDbContext --force

```

### SQL Auth

```

dotnet ef dbcontext scaffold "Server=localhost;Database=meknetic_db;User ID=sa;Password=YourPassword;TrustServerCertificate=True;" Microsoft.EntityFrameworkCore.SqlServer --output-dir Models --context-dir Data --context AppDbContext --force```
```

## 3. Start Scaffolding Controllers for CRUD (ex. WebApi Template)

```
dotnet aspnet-codegenerator controller -name YourControllerName -api -m MekneticBlog.Models.YourModelName -dc MekneticBlog.Data.AppDbContext --relativeFolderPath Controllers
```


## 4. Update Programs.cs

```
using Microsoft.EntityFrameworkCore;
using MekneticBlog.Data;

var builder = WebApplication.CreateBuilder(args);

// Tambahkan service untuk controller dan Swagger
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Ambil koneksi dari appsettings.json
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

// Registrasi DbContext
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(connectionString));

var app = builder.Build();

// Aktifkan Swagger di mode development
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();
app.MapControllers();

app.Run();

```
