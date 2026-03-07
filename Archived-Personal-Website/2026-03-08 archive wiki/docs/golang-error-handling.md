# Go Error Handling

Go uses explicit value checking for errors instead of exceptions.

## Basic Pattern
```go
res, err := doSomething()
if err != nil {
    // Handle error
    return err
}
fmt.Println(res)
```

## Creating Errors
```go
// Simple string error
err := errors.New("something went wrong")

// Formatted error
err := fmt.Errorf("user %d not found", id)
```

## Custom Error Types
```go
type MyError struct {
    Code int
    Msg  string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("[%d] %s", e.Code, e.Msg)
}
```

## Error Wrapping (Go 1.13+)
```go
// Wrap
err := fmt.Errorf("database failed: %w", originalErr)

// Check
if errors.Is(err, sql.ErrNoRows) { ... }

// Unwrap
var myErr *MyError
if errors.As(err, &myErr) { ... }
```

## Panic and Recover
Use only for unrecoverable errors.
```go
func main() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from", r)
        }
    }()
    panic("BOOM!")
}
```
---
*See **[Best Practices](golang-best-practices.md)** for how to handle errors effectively.*
