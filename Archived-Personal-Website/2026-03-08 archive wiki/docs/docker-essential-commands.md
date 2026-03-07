# Essential Docker Commands You Must Know

## Overview

Docker commands are the primary way to interact with Docker containers, images, networks, and volumes. This comprehensive guide covers all essential commands you need to master Docker effectively.

## Command Structure

### Basic Docker Command Format

```bash
docker [OPTIONS] COMMAND [ARG...]
```

### Getting Help

```bash
# Show Docker version
docker --version
docker version

# Show system information
docker info

# Get help for Docker
docker --help

# Get help for specific command
docker run --help
docker build --help
```

## Image Commands

### Pulling Images

```bash
# Pull latest image
docker pull ubuntu
docker pull nginx

# Pull specific version
docker pull ubuntu:20.04
docker pull node:18-alpine

# Pull from specific registry
docker pull gcr.io/google-containers/nginx
docker pull registry.company.com/app:latest

# Pull all tags of an image
docker pull --all-tags ubuntu
```

### Listing Images

```bash
# List all images
docker images
docker image ls

# List images with specific format
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# List image IDs only
docker images -q

# List dangling images
docker images --filter "dangling=true"

# List images by repository
docker images ubuntu
```

### Removing Images

```bash
# Remove specific image
docker rmi ubuntu:20.04
docker image rm ubuntu:20.04

# Remove image by ID
docker rmi 1a2b3c4d5e6f

# Remove multiple images
docker rmi ubuntu:18.04 ubuntu:20.04 ubuntu:22.04

# Remove all images
docker rmi $(docker images -q)

# Remove dangling images
docker image prune

# Remove all unused images
docker image prune -a

# Force remove image
docker rmi -f ubuntu:20.04
```

### Image Information

```bash
# Inspect image details
docker inspect ubuntu:20.04

# Show image history (layers)
docker history ubuntu:20.04

# Show image size information
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
```

## Container Commands

### Running Containers

```bash
# Basic container run
docker run ubuntu

# Run with interactive terminal
docker run -it ubuntu /bin/bash

# Run in detached mode (background)
docker run -d nginx

# Run with custom name
docker run --name my-nginx -d nginx

# Run with port mapping
docker run -p 8080:80 -d nginx

# Run with environment variables
docker run -e ENV_VAR=value -d myapp

# Run with volume mount
docker run -v /host/path:/container/path -d myapp

# Run with resource limits
docker run --memory=512m --cpus=1.0 -d myapp

# Run with restart policy
docker run --restart=always -d nginx

# Run and remove after exit
docker run --rm ubuntu echo "Hello World"
```

### Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# List container IDs only
docker ps -q

# List containers with custom format
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Start stopped container
docker start container-name
docker start container-id

# Stop running container
docker stop container-name

# Restart container
docker restart container-name

# Pause container
docker pause container-name

# Unpause container
docker unpause container-name

# Kill container (force stop)
docker kill container-name
```

### Container Interaction

```bash
# Execute command in running container
docker exec -it container-name /bin/bash
docker exec -it container-name sh

# Execute single command
docker exec container-name ls -la
docker exec container-name cat /etc/hosts

# Execute as specific user
docker exec -u root -it container-name /bin/bash

# Execute with environment variables
docker exec -e ENV_VAR=value container-name command
```

### Container Information

```bash
# Show container logs
docker logs container-name

# Follow logs in real-time
docker logs -f container-name

# Show last N lines of logs
docker logs --tail 50 container-name

# Show logs with timestamps
docker logs -t container-name

# Inspect container details
docker inspect container-name

# Show container resource usage
docker stats container-name

# Show running processes in container
docker top container-name

# Show container port mappings
docker port container-name
```

### Copying Files

```bash
# Copy file from host to container
docker cp /host/file.txt container-name:/container/path/

# Copy file from container to host
docker cp container-name:/container/file.txt /host/path/

# Copy directory
docker cp /host/directory/ container-name:/container/path/
docker cp container-name:/container/directory/ /host/path/

# Copy with archive mode (preserves permissions)
docker cp -a /host/file.txt container-name:/container/path/
```

### Removing Containers

```bash
# Remove stopped container
docker rm container-name

# Force remove running container
docker rm -f container-name

# Remove multiple containers
docker rm container1 container2 container3

# Remove all stopped containers
docker container prune

# Remove containers older than 24 hours
docker container prune --filter "until=24h"

# Remove all containers (running and stopped)
docker rm -f $(docker ps -aq)
```

## Building Images

### Dockerfile Commands

```bash
# Build image from Dockerfile
docker build -t myapp:latest .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build with build arguments
docker build --build-arg ENV=production -t myapp:prod .

# Build without using cache
docker build --no-cache -t myapp:latest .

# Build with target stage (multi-stage)
docker build --target development -t myapp:dev .

# Build and tag multiple tags
docker build -t myapp:latest -t myapp:1.0 .
```

### Tagging Images

```bash
# Tag existing image
docker tag myapp:latest myapp:v1.0
docker tag myapp:latest registry.company.com/myapp:latest

# Tag with multiple tags
docker tag ubuntu:20.04 my-ubuntu:custom
docker tag ubuntu:20.04 my-ubuntu:latest
```

## Registry Commands

### Pushing and Pulling

```bash
# Push image to registry
docker push myapp:latest
docker push registry.company.com/myapp:latest

# Login to registry
docker login
docker login registry.company.com
docker login -u username -p password registry.company.com

# Logout from registry
docker logout
docker logout registry.company.com

# Search images in Docker Hub
docker search nginx
docker search --limit 10 ubuntu
```

## Volume Commands

### Volume Management

```bash
# Create volume
docker volume create my-volume

# List volumes
docker volume ls

# Inspect volume
docker volume inspect my-volume

# Remove volume
docker volume rm my-volume

# Remove all unused volumes
docker volume prune

# Remove volumes older than 24 hours
docker volume prune --filter "until=24h"
```

### Using Volumes

```bash
# Run container with named volume
docker run -v my-volume:/data -d myapp

# Run container with bind mount
docker run -v /host/path:/container/path -d myapp

# Run container with read-only volume
docker run -v my-volume:/data:ro -d myapp

# Run container with tmpfs mount
docker run --tmpfs /tmp -d myapp
```

## Network Commands

### Network Management

```bash
# List networks
docker network ls

# Create network
docker network create my-network
docker network create --driver bridge my-bridge-network

# Inspect network
docker network inspect my-network

# Connect container to network
docker network connect my-network container-name

# Disconnect container from network
docker network disconnect my-network container-name

# Remove network
docker network rm my-network

# Remove all unused networks
docker network prune
```

### Running Containers with Networks

```bash
# Run container with specific network
docker run --network=my-network -d myapp

# Run container with port publishing
docker run -p 8080:80 --network=my-network -d nginx

# Run container with hostname
docker run --hostname=myapp --network=my-network -d myapp
```

## System Commands

### System Information

```bash
# Show Docker system information
docker system info

# Show disk usage
docker system df

# Show detailed disk usage
docker system df -v

# Monitor Docker events
docker events

# Monitor events for specific container
docker events --filter container=my-container
```

### System Cleanup

```bash
# Remove all unused data
docker system prune

# Remove all unused data including volumes
docker system prune --volumes

# Remove all unused data including images
docker system prune -a

# Force removal without confirmation
docker system prune -f

# Remove data older than specific time
docker system prune --filter "until=72h"
```

## Advanced Commands

### Container Export/Import

```bash
# Export container as tar archive
docker export container-name > container.tar

# Import tar archive as image
docker import container.tar my-image:latest

# Save image as tar archive
docker save myapp:latest > myapp.tar

# Load image from tar archive
docker load < myapp.tar
```

### Container Commit

```bash
# Create image from container changes
docker commit container-name new-image:tag

# Create image with message and author
docker commit -m "Added new feature" -a "Your Name" container-name new-image:tag

# Create image without pausing container
docker commit --pause=false container-name new-image:tag
```

### Multi-platform Commands

```bash
# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .

# Create builder instance
docker buildx create --name mybuilder --use

# Inspect builder
docker buildx inspect mybuilder

# Remove builder
docker buildx rm mybuilder
```

## Docker Compose Commands

### Basic Compose Commands

```bash
# Start services
docker-compose up

# Start services in background
docker-compose up -d

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Build services
docker-compose build

# View service logs
docker-compose logs

# Follow logs
docker-compose logs -f

# Scale services
docker-compose up --scale web=3

# Execute command in service
docker-compose exec web /bin/bash

# Run one-off command
docker-compose run web python manage.py migrate
```

## Command Aliases and Shortcuts

### Useful Aliases

```bash
# Add to your ~/.bashrc or ~/.zshrc
alias dps='docker ps'
alias dpsa='docker ps -a'
alias di='docker images'
alias dlog='docker logs'
alias dexec='docker exec -it'
alias dstop='docker stop $(docker ps -q)'
alias drm='docker rm $(docker ps -aq)'
alias drmi='docker rmi $(docker images -q)'
alias dprune='docker system prune -f'
```

### Common Command Combinations

```bash
# Stop all running containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Remove all dangling images
docker rmi $(docker images -f dangling=true -q)

# Remove all unused containers, networks, and images
docker system prune -a

# Get container IP address
docker inspect container-name | grep IPAddress

# Get container environment variables
docker inspect container-name | grep Env -A 20

# Monitor container resource usage
docker stats --no-stream

# Show container sizes
docker ps -s
```

## Command Cheat Sheet

### Container Lifecycle

| Command | Purpose |
|---------|---------|
| `docker run` | Create and start container |
| `docker start` | Start stopped container |
| `docker stop` | Stop running container |
| `docker restart` | Restart container |
| `docker pause` | Pause container |
| `docker unpause` | Unpause container |
| `docker rm` | Remove container |

### Image Management

| Command | Purpose |
|---------|---------|
| `docker pull` | Download image |
| `docker build` | Build image from Dockerfile |
| `docker push` | Upload image to registry |
| `docker tag` | Tag image |
| `docker rmi` | Remove image |
| `docker save` | Export image to tar |
| `docker load` | Import image from tar |

### Information Commands

| Command | Purpose |
|---------|---------|
| `docker ps` | List containers |
| `docker images` | List images |
| `docker logs` | View container logs |
| `docker inspect` | Detailed object information |
| `docker stats` | Resource usage statistics |
| `docker top` | Running processes |

## Error Handling and Troubleshooting

### Common Issues and Solutions

```bash
# Issue: Permission denied
# Solution: Add user to docker group
sudo usermod -aG docker $USER
# Then logout and login again

# Issue: Port already in use
# Solution: Use different port or stop service using the port
docker run -p 8081:80 nginx  # Use different host port
sudo lsof -i :8080           # Find what's using port 8080

# Issue: No space left on device
# Solution: Clean up Docker data
docker system prune -a
docker volume prune

# Issue: Container exits immediately
# Solution: Check logs and run interactively
docker logs container-name
docker run -it image-name /bin/bash

# Issue: Cannot connect to Docker daemon
# Solution: Start Docker service
sudo systemctl start docker
```

### Debug Commands

```bash
# Run container with debug shell
docker run -it --entrypoint=/bin/bash image-name

# Check container filesystem changes
docker diff container-name

# View Docker daemon logs
journalctl -u docker.service

# Test Docker installation
docker run hello-world

# Check Docker configuration
docker info | grep -i root
```

## Best Practices

### Security Practices

```bash
# Run as non-root user
docker run -u 1000:1000 myapp

# Use read-only filesystem
docker run --read-only myapp

# Drop capabilities
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp

# Set resource limits
docker run --memory=256m --cpus=0.5 myapp

# Use secrets for sensitive data
docker run --env-file secrets.env myapp
```

### Performance Tips

```bash
# Use multi-stage builds
docker build --target production .

# Use .dockerignore file
echo "node_modules" > .dockerignore
echo "*.log" >> .dockerignore

# Clean up regularly
docker system prune --schedule="0 2 * * *"  # Cron job

# Monitor resource usage
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

## Next Steps

After mastering essential Docker commands:

1. **[Create your first container](docker-first-container.md)**
2. **[Learn Dockerfile creation](docker-dockerfile.md)**
3. **[Understand Docker volumes](docker-volumes.md)**
4. **[Explore Docker networking](docker-networking-basics.md)**

Mastering these essential Docker commands is fundamental to working effectively with containers. Start with basic commands and gradually incorporate more advanced features as you become comfortable with Docker's workflow.
