
```
dotnet new web -n PingPongAPI --framework net8.0
```

code : 
```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/ping", () => Results.Ok("pong"));

app.Run();
```
