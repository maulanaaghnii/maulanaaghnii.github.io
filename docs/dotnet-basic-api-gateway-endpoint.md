# .NET Basic API Gateway Endpoint

An API Gateway provides a single entry point for all clients. In .NET, we often use Ocelot or YARP (Yet Another Reverse Proxy).

## Using YARP (Recommended)
YARP is a high-performance reverse proxy toolkit from Microsoft.

### 1. Install Package
```bash
dotnet add package Microsoft.ReverseProxy
```

### 2. Configure in Program.cs
```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

var app = builder.Build();
app.MapReverseProxy();
app.Run();
```

### 3. AppSettings Configuration
```json
{
  "ReverseProxy": {
    "Routes": {
      "route1" : {
        "ClusterId": "cluster1",
        "Match": {
          "Path": "{**catch-all}"
        }
      }
    },
    "Clusters": {
      "cluster1": {
        "Destinations": {
          "destination1": {
            "Address": "https://localhost:5001/"
          }
        }
      }
    }
  }
}
```

## Why use an API Gateway?
- **Authentication**: Centralize login logic.
- **Rate Limiting**: Protect downstream services.
- **Routing**: Map public URLs to internal service endpoints.
- **SSL Termination**: Handle HTTPS certificates in one place.