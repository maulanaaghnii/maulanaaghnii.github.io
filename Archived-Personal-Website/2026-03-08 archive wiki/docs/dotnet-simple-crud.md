# Simple CRUD in .NET

CRUD stands for **C**reate, **R**ead, **U**pdate, and **D**elete. These are the four basic operations of persistent storage.

## Create
```csharp
var user = new User { Name = "John" };
context.Users.Add(user);
await context.SaveChangesAsync();
```

## Read
```csharp
// Get all
var allUsers = await context.Users.ToListAsync();
// Get by ID
var user = await context.Users.FindAsync(id);
```

## Update
```csharp
var user = await context.Users.FindAsync(id);
user.Name = "Updated Name";
await context.SaveChangesAsync();
```

## Delete
```csharp
var user = await context.Users.FindAsync(id);
context.Users.Remove(user);
await context.SaveChangesAsync();
```

---
*Powered by **[Entity Framework Core](entity-framework-core.md)**.*
