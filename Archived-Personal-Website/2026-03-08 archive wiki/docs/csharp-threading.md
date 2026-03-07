# C# Threading & Concurrency

Threading allows your C# programs to perform multiple tasks simultaneously. This is essential for keeping UI responsive and improving performance on multi-core systems.

## Basic Threading
Using the `System.Threading` namespace.

```csharp
using System;
using System.Threading;

class Program
{
    static void Main()
    {
        Thread t = new Thread(WriteY);
        t.Start();                          // Run WriteY on a new thread

        // Simultaneously, do something on the main thread.
        for (int i = 0; i < 1000; i++) Console.Write("x");
    }

    static void WriteY()
    {
        for (int i = 0; i < 1000; i++) Console.Write("y");
    }
}
```

## Task Parallel Library (TPL)
Modern C# development uses `Task` instead of raw `Thread`.

```csharp
using System.Threading.Tasks;

Task task = Task.Run(() => {
    // Some background work
    Console.WriteLine("Task running on thread pool");
});

await task; // Wait for completion
```

## Async and Await
The preferred way to handle asynchronous operations.

```csharp
public async Task<string> DownloadContentAsync(string url)
{
    using var client = new HttpClient();
    // Non-blocking wait
    string result = await client.GetStringAsync(url);
    return result;
}
```

## Synchronization
Preventing race conditions using `lock`.

```csharp
private readonly object _locker = new object();
private int _counter = 0;

void Increment()
{
    lock (_locker)
    {
        _counter++;
    }
}
```

## Advanced Concepts
- **SemaphoreSlim**: Restrict the number of threads accessing a resource.
- **Concurrent Collections**: `ConcurrentDictionary`, `ConcurrentQueue`.
- **CancellationToken**: Gracefully cancelling tasks.
