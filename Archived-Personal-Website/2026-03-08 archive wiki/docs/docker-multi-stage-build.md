# Docker Multi-Stage Builds

Multi-stage builds allow you to optimize your Dockerfiles by using multiple `FROM` statements. This is the best way to keep your production images small.

## How it works
You use one stage to compile/build your app (which requires heavy SDKs) and another stage to run it (using a lightweight runtime).

## Example (.NET)
```dockerfile
# Stage 1: Build
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
WORKDIR /app
COPY . .
RUN dotnet publish -c Release -o out

# Stage 2: Runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build-env /app/out .
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

## Benefits
- **Smaller Images**: No build tools or source code in the final image.
- **Security**: Fewer tools available for an attacker to use if they gain access.
- **Speed**: Layer caching works across stages.

---
*See **[Dockerfile Optimization](docker-dockerfile-optimization.md)** for more tips.*
