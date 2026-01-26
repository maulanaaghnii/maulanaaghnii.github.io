# .NET JWT Authentication

JSON Web Tokens (JWT) are an open standard for securely transmitting information between parties as a JSON object.

## Setup in .NET
1. **Install Package**: `Microsoft.AspNetCore.Authentication.JwtBearer`
2. **Configure in Program.cs**:
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => {
        options.TokenValidationParameters = new TokenValidationParameters {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            // ... keys and other settings
        };
    });
```
3. **Use Middleware**:
```csharp
app.UseAuthentication();
app.UseAuthorization();
```

## Protecting Endpoints
Use the `[Authorize]` attribute.
```csharp
[Authorize]
[HttpGet]
public IActionResult GetSecretData() => Ok("Secure data");
```
---
*See **[Microservices](dotnet-microservices.md)** for distributed auth patterns.*
