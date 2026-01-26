# Go Functions & Packages

Go uses a clean, consistent syntax for functions and organizational structure.

## Function Syntax
```go
func Add(a int, b int) int {
    return a + b
}

// Multiple return values (Standard Go pattern)
func Divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / b, nil
}
```

## Named Return Values
```go
func Split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return // Naked return
}
```

## Packages & Visibility
- **Exported**: Variables/Functions starting with an **Uppercase** letter are public.
- **Internal**: Starting with a **lowercase** letter are private to the package.

```go
package calculator

var GlobalConfig = "v1.0" // Public
var secretKey = "xyz"    // Private
```

## The `init` Function
Runs automatically when the package is initialized.
```go
func init() {
    // Setup logic
}
```
