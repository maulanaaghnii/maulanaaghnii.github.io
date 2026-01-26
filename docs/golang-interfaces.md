# Go Interfaces & Abstraction

Interfaces in Go provide a way to specify the behavior of an object. If a type implements all methods in an interface, it implicitly satisfies the interface.

## Defining an Interface
```go
type Logger interface {
    Log(message string)
}
```

## Implementing
Implicitly implemented. No `implements` keyword.
```go
type ConsoleLogger struct{}

func (c ConsoleLogger) Log(message string) {
    fmt.Println(message)
}
```

## The Empty Interface `interface{}`
Can hold values of any type. In modern Go, this is often written as `any`.
```go
func PrintAnything(v any) {
    fmt.Println(v)
}
```

## Type Assertion & Switches
```go
// Assertion
s, ok := val.(string)

// Switch
switch v := val.(type) {
case int:
    fmt.Println("Integer", v)
case string:
    fmt.Println("String", v)
}
```

## Interface Values
Technically, an interface is a tuple of (Value, Type). An interface is only `nil` if both the value and type are `nil`.
