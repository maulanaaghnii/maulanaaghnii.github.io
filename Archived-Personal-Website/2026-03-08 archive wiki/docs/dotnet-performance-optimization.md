# .NET Performance Optimization

Making your .NET apps faster and more efficient.

## EF Core Optimizations
- **NoTracking**: Use `AsNoTracking()` for read-only queries to save memory.
- **Filtering**: Always filter data on the database side (`Where`) before bringing it to memory (`ToList`).
- **Paging**: Use `Skip` and `Take` to return only small chunks of data.

## Code-Level Tips
- **StringBuilder**: Use `StringBuilder` instead of string concatenation in loops.
- **Span<T>**: Use `Span` for memory-efficient buffer manipulation.
- **Structs**: Use `struct` for small, short-lived data to avoid heap allocation.

## Asynchronous Code
Use `async/await` throughout to avoid blocking threads on I/O operations. This increases the throughput of your application.

## Caching
Use `IMemoryCache` or a distributed cache like **Redis** to store frequently accessed data.

---
*See **[Async/Await](csharp-async-await.md)** for best practices.*
