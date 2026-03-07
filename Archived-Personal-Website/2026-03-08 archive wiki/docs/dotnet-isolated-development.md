# .NET Isolated Development

Using containers and virtual environments to isolate your .NET dev workflow.

## 1. Using Docker
Run your .NET SDK and runtime inside a container. See **[Docker Isolated Development](docker-isolated-development.md)** for details.

## 2. Global JSON
Use a `global.json` file in your project root to force a specific SDK version for that directory.
```json
{
  "sdk": {
    "version": "8.0.100"
  }
}
```

## 3. Tool Isolation
Install .NET tools locally to your project instead of globally using a tool manifest.
```bash
dotnet new tool-manifest
dotnet tool install dotnet-ef
```
