# Connecting Frontend to .NET Web API

Best practices for communication between your client-side app (React, Angular, Vue) and your .NET backend.

## 1. CORS (Cross-Origin Resource Sharing)
By default, browsers block requests to a different domain.
```csharp
// Program.cs
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll",
        builder => builder.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod());
});

app.UseCors("AllowAll");
```

## 2. Shared Data Models
Consider using a tool to generate TypeScript interfaces from your C# DTOs to keep them in sync.

## 3. Global Exception Handling
Ensure your API returns standard error objects so the frontend can display helpful messages instead of raw stack traces.

## 4. Environment Switching
Use different base URLs for the API depending on whether the frontend is in development or production.

---
*Check **[REST API Guide](aspnetcore-rest-api.md)** for backend patterns.*
