# .NET CI/CD Automation

Automation techniques specifically for .NET projects.

## 1. Fast Build Feedback
Use the `dotnet` CLI in your pipeline for fast execution.
```bash
dotnet restore
dotnet build --no-restore
dotnet test --no-build
```

## 2. Artifact Management
- **NuGet Packages**: Push libraries to GitHub Packages or Azure Artifacts.
- **Publishing**: Use `dotnet publish` to create ready-to-deploy binaries.

## 3. Deployment Targets
- **Azure App Service**: Native integration with .NET.
- **Docker/K8s**: Containerize your published output.

## 4. Environment-Specific Config
Use **[Environment Variables](dotnet-environment-variables.md)** in your CI/CD tool to override settings in `appsettings.json` during deployment.

---
*Back to **[.NET Overview](dotnet-overview.md)**.*
