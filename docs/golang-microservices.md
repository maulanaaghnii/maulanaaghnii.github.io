# Golang Microservices

Go (Golang) is one of the most popular languages for building microservices due to its performance, concurrency model, and small binary size.

## Why Go for Microservices?
- **Concurrency**: Goroutines and Channels make it easy to handle thousands of concurrent requests.
- **Fast Startup**: Compiled binaries start almost instantly.
- **Simple Deployment**: Single static binary with no external dependencies.
- **Efficient**: Low memory footprint.

## Common Frameworks
- **Gin / Echo**: High-performance HTTP frameworks.
- **Go-Kit**: A toolkit for microservices (highly opinionated).
- **Fiber**: Fast, Express-like framework.
- **gRPC-go**: Official Go implementation of gRPC.

## Communication
### gRPC in Go
Go has excellent support for gRPC, which is often preferred for internal service-to-service communication.

```go
// Example Protobuf definition
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}
```

### Message Brokers
- **Go-RabbitMQ**: Simple RabbitMQ wrapper.
- **Confluent-Kafka-Go**: Kafka client.

## Standard Project Structure
```text
/cmd/service-name/main.go
/internal/app/...        (private code)
/pkg/utils/...           (public code)
/api/proto/...           (gRPC definitions)
```

## Resilience Patterns
- **Retries**: Using libraries like `go-resiliency`.
- **Circuit Breaker**: `gobreaker`.
- **Rate Limiting**: `golang.org/x/time/rate`.
