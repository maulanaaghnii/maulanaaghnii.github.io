# Go Concurrency

Go's concurrency model (CSP) is one of its most powerful features.

## Goroutines
Lightweight threads managed by the Go runtime.

```go
func main() {
    go sayHello() // Runs in background
    fmt.Println("Main thread")
}
```

## Channels
Typed conduits through which you can send and receive values.
```go
ch := make(chan int)

go func() {
    ch <- 42 // Send
}()

val := <-ch // Receive (Blocks until data arrives)
```

## Select Statement
Allows a goroutine to wait on multiple communication operations.
```go
select {
case msg1 := <-ch1:
    fmt.Println(msg1)
case ch2 <- "Hello":
    fmt.Println("Sent")
case <-time.After(time.Second):
    fmt.Println("Timeout")
}
```

## Buffered Channels
```go
ch := make(chan string, 2) // Can hold 2 items without blocking
ch <- "One"
ch <- "Two"
```

## Sync Package
For low-level synchronization (Mutexes, WaitGroups).
```go
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    // Work
}()
wg.Wait()
```
---
*Advanced patterns can be found in **[Golang Microservices](golang-microservices.md)**.*
