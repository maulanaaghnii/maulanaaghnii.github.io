# C# Serialization

Serialization is the process of converting an object into a format that can be stored or transmitted (like JSON or XML).

## JSON Serialization (System.Text.Json)
The modern, high-performance default for .NET.

```csharp
using System.Text.Json;

var user = new User { Name = "Mek", Age = 25 };

// Serialize
string json = JsonSerializer.Serialize(user);

// Deserialize
var newUser = JsonSerializer.Deserialize<User>(json);
```

## JSON Serialization (Newtonsoft.Json)
The classical "gold standard" with many features not yet in `System.Text.Json`.

```csharp
using Newtonsoft.Json;

string json = JsonConvert.SerializeObject(user);
var newUser = JsonConvert.DeserializeObject<User>(json);
```

## Binary Serialization
Rarely used nowadays for security reasons, but available for extreme performance in trusted environments (e.g., Protobuf).

## XML Serialization
```csharp
var serializer = new XmlSerializer(typeof(User));
using var writer = new StreamWriter("user.xml");
serializer.Serialize(writer, user);
```

---
*Used heavily in **[REST APIs](aspnetcore-rest-api.md)**.*
