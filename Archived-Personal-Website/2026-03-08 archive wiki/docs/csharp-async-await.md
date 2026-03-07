# C# Async and Await

The `async` and `await` keywords are the heart of asynchronous programming in modern .NET.

## Basic Pattern
```csharp
public async Task<string> GetWebDataAsync(string url)
{
    using var client = new HttpClient();
    // The execution of this method is suspended until GetStringAsync completes
    string result = await client.GetStringAsync(url);
    return result;
}
```

## Key Rules
- **Async all the way**: If you use `await`, the calling method should also be `async`.
- **ReturnType**: Use `Task` (no return), `Task<T>` (returns T), or `ValueTask` (performance).
- **Avoid `.Result` or `.Wait()`**: These can cause deadlocks.

## Waiting for Multiple Tasks
```csharp
var task1 = DoWork1Async();
var task2 = DoWork2Async();

await Task.WhenAll(task1, task2);
```

---
*For low-level details, see **[C# Threading](csharp-threading.md)**.*
