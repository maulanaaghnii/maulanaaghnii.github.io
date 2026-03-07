# Docker Networking Basics

Docker networking allows containers to communicate with each other and the outside world.

## Default Networks
1. **bridge**: The default network for containers.
2. **host**: The container shares the host's networking namespace.
3. **none**: No networking for the container.

## User-Defined Bridge Networks (Recommended)
User-defined bridges provide automatic DNS resolution between containers.
```bash
# Create a network
docker network create my-app-net

# Run containers on the network
docker run -d --name db --network my-app-net postgres
docker run -d --name web --network my-app-net my-web-app
```
Inside the `web` container, you can reach the database using the hostname `db`.

## Exposing Ports
```bash
# Map host port 8080 to container port 80
docker run -p 8080:80 nginx
```

## Inspecting Networks
```bash
docker network ls
docker network inspect my-app-net
```
