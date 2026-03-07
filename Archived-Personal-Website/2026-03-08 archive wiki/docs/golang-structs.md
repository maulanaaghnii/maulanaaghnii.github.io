# Go Structs & Methods

Go is not a traditional object-oriented language, but it provides structs and methods for data encapsulation.

## Structs
```go
type User struct {
    ID    int
    Name  string
    Email string
}

// Initializing
u := User{ID: 1, Name: "Mek", Email: "mek@example.com"}
```

## Methods
Methods are functions attached to a specific type.

```go
// Value Receiver (Copies the struct)
func (u User) Greet() string {
    return "Hello, I am " + u.Name
}

// Pointer Receiver (Modifies the original struct)
func (u *User) Rename(newName string) {
    u.Name = newName
}
```

## Embedding (Composition)
Go uses embedding instead of traditional inheritance.

```go
type Admin struct {
    User  // Embedded field
    Level int
}

a := Admin{User: User{Name: "SuperMek"}, Level: 10}
fmt.Println(a.Name) // Access fields directly
```

## Tags
Used for metadata, especially for JSON serialization.
```go
type User struct {
    Name string `json:"user_name"`
    Age  int    `json:"age,omitempty"`
}
```
---
*See **[Interfaces](golang-interfaces.md)** for how to use these structs polymorphically.*
