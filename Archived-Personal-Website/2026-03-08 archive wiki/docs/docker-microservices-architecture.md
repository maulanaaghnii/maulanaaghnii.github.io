# Docker for Microservices Architecture

Docker is the backbone of modern microservices development.

## 1. Modularity
Each microservice is an independent container. It has its own operating system dependencies, isolated from other services.

## 2. Shared Infrastructure
Services like **Redis**, **RabbitMQ**, and your **Databases** should also run in containers during development.

## 3. Orchestration
A simple `docker run` is not enough for production microservices. You will need:
- **Docker Compose**: For local dev.
- **Docker Swarm**: For small production clusters.
- **Kubernetes**: For large, complex deployments.

## 4. API Gateway
Use a containerized reverse proxy (like **Nginx** or **YARP**) to route traffic to your microservices.

---
*See **[Microservices with .NET](dotnet-microservices.md)** for more.*
