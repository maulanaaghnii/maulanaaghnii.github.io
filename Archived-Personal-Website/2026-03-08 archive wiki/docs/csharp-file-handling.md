# C# File Handling

Working with the file system using the `System.IO` namespace.

## Reading Files
```csharp
string path = "data.txt";

// Read all text
string content = File.ReadAllText(path);

// Read all lines into an array
string[] lines = File.ReadAllLines(path);
```

## Writing Files
```csharp
// Write string to file (overwrites)
File.WriteAllText(path, "Hello World");

// Append text
File.AppendAllText(path, "\nNew Line");
```

## Directory Operations
```csharp
// Create a directory
Directory.CreateDirectory("logs");

// Get all files in a folder
string[] files = Directory.GetFiles("C:\\docs");
```

## Streams (For large files)
```csharp
using (StreamWriter writer = new StreamWriter("large.txt"))
{
    writer.WriteLine("Efficient writing");
}
```

---
*See **[Async/Await](csharp-async-await.md)** for non-blocking file operations.*
