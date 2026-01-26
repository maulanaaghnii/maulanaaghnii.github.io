# Docker Swarm

Docker Swarm is a container orchestration tool, built-in to the Docker Engine. It allows you to manage a cluster of Docker engines as a single virtual system.

## Key Concepts
- **Node**: An instance of the Docker engine participating in the swarm.
- **Manager Node**: Handles cluster management and orchestration.
- **Worker Node**: Receives and executes tasks from manager nodes.
- **Service**: The definition of the tasks to execute on worker nodes.

## Basic Commands
```bash
# Initialize a swarm
docker swarm init

# Create a service
docker service create --name my-web --replicas 3 -p 8080:80 nginx

# List services
docker service ls

# Scale a service
docker service scale my-web=5
```

## Swarm vs Kubernetes
- **Swarm**: Easier to set up, integrated with Docker CLI, better for simple clusters.
- **Kubernetes**: More powerful, complex features, industry standard for large scale orchestration.

---
*See **[Docker Overview](docker-overview.md)** for more container topics.*
