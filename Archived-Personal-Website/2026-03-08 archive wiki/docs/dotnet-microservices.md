# .NET Microservices

Microservices architecture involves breaking down a large application into smaller, independent services that communicate over a network.

## Key Concepts
- **Independence**: Each service can be developed, deployed, and scaled independently.
- **Communication**: Services talk via HTTP/REST, gRPC, or Message Brokers (RabbitMQ, Kafka).
- **Database per Service**: Each service owns its own data.

## Essential Technologies
- **API Gateway**: Ocelot, YARP.
- **Service Discovery**: Consul, Eureka.
- **Messaging**: MassTransit, Rebus.
- **Containerization**: Docker, Kubernetes.

## Communication Patterns
### Synchronous
- **HTTP/REST**: Simple and widely used.
- **gRPC**: High-performance, binary protocol.

### Asynchronous
- **Publish/Subscribe**: One service publishes an event, many subscribe.
- **Command/Queue**: One service sends a command to another via a queue.

## Sample Architecture
1. **Identity Service**: Handles Authentication (JWT).
2. **Catalog Service**: Manages products.
3. **Ordering Service**: Handles orders and payments.
4. **API Gateway**: The entry point for clients.

## Implementation with .NET
.NET simplifies microservices with:
- `HttpClientFactory` for resilient requests.
- `System.Text.Json` for serialization.
- Built-in Dependency Injection.
