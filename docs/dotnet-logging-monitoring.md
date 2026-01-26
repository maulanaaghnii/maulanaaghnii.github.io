# .NET Logging and Monitoring

Beyond simple logs: tracking health, metrics, and distributed traces.

## 1. Advanced Logging (Serilog Enrichers)
Adding more context to your logs automatically.
```csharp
Log.Logger = new LoggerConfiguration()
    .Enrich.FromLogContext()
    .Enrich.WithMachineName()
    .Enrich.WithThreadId()
    .CreateLogger();
```

## 2. Health Checks
Allow external systems (like Kubernetes or Load Balancers) to monitor if your app is ready.
```csharp
builder.Services.AddHealthChecks();
app.MapHealthChecks("/health");
```

## 3. Metrics (OpenTelemetry)
Collecting counts, rates, and durations.
```csharp
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics => metrics.AddAspNetCoreInstrumentation().AddPrometheusExporter());
```

## 4. Distributed Tracing
Tracking a single request as it passes through multiple services.
- **Tools**: Jaeger, Zipkin, Azure Application Insights.

---
*Check out the **[Logging Tutorial](dotnet-logging-tutorial.md)** for basics.*
