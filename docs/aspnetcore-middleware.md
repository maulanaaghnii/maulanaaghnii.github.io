# ASP.NET Core Middleware

Middleware is software that is assembled into an app pipeline to handle requests and responses. Each component chooses whether to pass the request to the next component in the pipeline.

## The Pipeline
```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Middleware examples
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.UseAuthentication();
app.UseAuthorization();

app.MapControllers();

app.Run();
```

## Custom Middleware
You can create your own middleware to handle cross-cutting concerns like logging or custom headers.
```csharp
app.Use(async (context, next) =>
{
    // Do something before the next middleware
    await next.Invoke();
    // Do something after the next middleware
});
```

---
*See **[Dependency Injection](dotnet-dependency-injection.md)** for more.*
