# .NET Authentication and Authorization

Authentication (Who are you?) and Authorization (What can you do?) are core to secure .NET applications.

## Authentication Schemes
- **JWT (JSON Web Tokens)**: Standard for modern APIs and Microservices.
- **Cookies**: Traditional for server-side rendered apps (MVC/Razor Pages).
- **Identity Server / OpenID Connect**: For complex SSO requirements.
- **Windows Authentication**: For internal corporate apps.

## Identity Framework
ASP.NET Core Identity is a complete membership system that includes:
- Login/Logout
- Password hashing
- Roles and Claims
- Two-factor authentication (2FA)

## Basic Configuration
In `Program.cs`:
```csharp
builder.Services.AddAuthentication(options => { ... });
builder.Services.AddAuthorization(options => {
    options.AddPolicy("AdminOnly", policy => policy.RequireRole("Admin"));
});
```

## Usage
Add `[Authorize]` to controllers or specific actions.

---
*Deep dive: **[JWT Authentication](dotnet-jwt-authentication.md)**.*
