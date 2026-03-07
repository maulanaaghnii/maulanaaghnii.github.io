# Common .NET Issues and Solutions

A troubleshooting guide for common .NET development problems.

## 1. "CS0246: The type or namespace name could not be found"
- **Cause**: Missing `using` directive or missing project/package reference.
- **Fix**: Check `dotnet list package` or ensure the project is in the same solution.

## 2. Ports already in use
*Error: Failed to bind to address http://localhost:5000*
- **Fix**: Change `applicationUrl` in `Properties/launchSettings.json` or kill the process using the port.
```powershell
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

## 3. "The EF Core tools version is older than the runtime"
- **Fix**: Update your global tools.
```bash
dotnet tool update --global dotnet-ef
```

## 4. HTTPS Certificate Issues (Local Dev)
- **Fix**: Trust the dev certificate.
```bash
dotnet dev-certs https --trust
```

## 5. Startup failure after moving project
- **Fix**: Clean your `bin` and `obj` folders and rebuild.
```bash
dotnet clean
dotnet build
```
---
*See **[Debugging Tips](dotnet-debugging-tips.md)** for more.*
