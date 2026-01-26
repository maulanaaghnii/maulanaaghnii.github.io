# Dockerfile Optimization

Optimizing your Docker images leads to faster builds, smaller deployments, and better security.

## Best Practices

### 1. Multi-Stage Builds
Build your application in one stage and copy only the necessary artifacts to a smaller final image.
```dockerfile
# Build Stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app

# Final Stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

### 2. Minimize Layers
Combine commands where possible.
```dockerfile
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*
```

### 3. Use `.dockerignore`
Keep unnecessary files (like `.git`, `bin`, `obj`, `node_modules`) out of your build context.

### 4. Order Layers
Put frequently changing layers (like source code) at the bottom and rarely changing layers (like dependencies) at the top.

---
*See **[Dockerfile Guide](docker-dockerfile.md)** for basics.*
