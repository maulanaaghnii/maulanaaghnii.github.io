# Go Basics

Learn the fundamental building blocks of Go programs.

## Variables & Constants
Go is statically typed, but provides type inference for brevity.

```go
// Direct declaration
var message string = "Hello"

// Type inference
count := 10

// Constants
const Pi = 3.14
```

## Data Types
- **Numeric**: `int`, `int64`, `float64`, `uint`, etc.
- **String**: UTF-8 encoded sequences.
- **Boolean**: `true` or `false`.

## Control Flow

### If-Else
```go
if x := getVal(); x > 10 {
    fmt.Println("Big")
} else {
    fmt.Println("Small")
}
```

### For (The only loop)
```go
// Standard loop
for i := 0; i < 10; i++ { ... }

// "While" equivalent
for count < 100 { ... }

// Infinite loop
for { ... }
```

### Switch
```go
switch os := runtime.GOOS; os {
case "darwin":
    fmt.Println("OS X")
case "linux":
    fmt.Println("Linux")
default:
    fmt.Println("Other")
}
```
