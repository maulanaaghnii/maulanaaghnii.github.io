# .Net Web API


## install Entity Framework Core Tools
```
dotnet tool install --global dotnet-ef
```

## Insall Entity .NET Framework
```
dotnet add package MySql.Data
dotnet add package Pomelo.EntityFrameworkCore.MySql
dotnet add package Microsoft.EntityFrameworkCore.Tools

```

## Migration
```
dotnet ef migrations add InitialCreate
dotnet ef database update
```

## Run
```
dotnet run
```

## Build
```
dotnet build
```

## Create .gitignore
```
dotnet new gitignore
```


Read : 
- [Create PingPing API](dotnet-ping-pong-api.md)

