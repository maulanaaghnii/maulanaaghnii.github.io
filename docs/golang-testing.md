# Testing in Go

Go has a built-in testing framework that is simple but powerful.

## Unit Testing
Files must end in `_test.go`.

```go
func TestAdd(t *testing.T) {
    got := Add(2, 3)
    want := 5
    if got != want {
        t.Errorf("got %d, want %d", got, want)
    }
}
```

## Table-Driven Tests
The idiomatic way to test multiple scenarios.
```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name string
        a, b int
        want int
    }{
        {"positive", 1, 2, 3},
        {"zero", 0, 0, 0},
        {"negative", -1, -2, -3},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.want {
                t.Errorf("Add() = %v, want %v", got, tt.want)
            }
        })
    }
}
```

## Benchmarks
```go
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(1, 2)
    }
}
```

## Running Tests
```bash
# Run all tests in current dir
go test

# Verbose output
go test -v

# Run benchmarks
go test -bench=.
```
