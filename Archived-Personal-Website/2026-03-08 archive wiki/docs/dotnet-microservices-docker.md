# Running .NET Microservices with Docker

Combining .NET's modular architecture with Docker's portability.

## 1. Organizing the Solution
In a microservices repo, each service typically has its own directory and its own `Dockerfile`.

## 2. Shared Library Pitfall
If your services share a local library project, your `COPY` commands in the `Dockerfile` must be able to reach that project (often by building from the solution root).

## 3. Communication
- **Service Discovery**: Within a docker network, use service names as hostnames.
- **Environment Variables**: Configure connection strings for each service differently.

## 4. Docker Compose for Local Dev
```yaml
services:
  identity-api:
    build: ./src/Identity.API
  catalog-api:
    build: ./src/Catalog.API
    environment:
      - DatabaseSettings__ConnectionString=mongodb://db
```

---
*See **[.NET Microservices Architecture](dotnet-microservices.md)** for design patterns.*
