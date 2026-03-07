# Go Generics

Introduced in Go 1.18, generics allow you to write functions and types that work with various data types without sacrificing type safety.

## Type Parameters
```go
func PrintSlice[T any](s []T) {
    for _, v := range s {
        fmt.Println(v)
    }
}
```

## Type Constraints
You can limit which types can be used.
```go
// Using comparable (for keys in maps)
func Index[T comparable](s []T, x T) int { ... }

// Using interfaces as constraints
type Number interface {
    int | int64 | float64
}

func Sum[T Number](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}
```

## Generic Types
```go
type List[T any] struct {
    head, tail *Element[T]
}

type Element[T any] struct {
    next *Element[T]
    val  T
}
```

## When to use?
- Collections (LInked List, Stack, Queue).
- Math operations on different numeric types.
- General purpose tools.
---
*Avoid overusing generics; simple code is often better Go code.*
