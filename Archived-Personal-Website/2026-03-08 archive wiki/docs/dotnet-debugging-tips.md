# .NET Debugging Tips

Mastering the debugger can save you hours of frustration.

## 1. Breakpoints and Beyond
- **Conditional Breakpoints**: Right-click a breakpoint to set a condition.
- **Tracepoints**: Print messages to output without stopping execution.
- **Logpoints**: Similar to tracepoints but specifically integrated with logging.

## 2. Inspecting Data
- **Watch Windows**: Monitor specific variables or expressions.
- **Immediate Window**: Execute C# code during a debug session.
- **Visualizers**: Use the magnifying glass icon to view complex objects (like JSON or XML) in a readable format.

## 3. Exceptions
- **Exception Settings**: Configure the debugger to break when an exception is *thrown*, not just when it is unhandled.
- **Inner Exception**: Always check the `InnerException` property for the root cause of failures.

## 4. Debugging Tools
- **dotnet-dump**: Capture and analyze system dumps.
- **dotnet-trace**: Profile performance and collect traces.

---
*For common errors, see **[Common Issues](dotnet-common-issues.md)**.*
