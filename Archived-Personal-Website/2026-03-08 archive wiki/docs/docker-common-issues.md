# Common Docker Issues and Solutions

A survival guide for common problems when working with Docker.

## 1. "Permission Denied" (Linux)
You need to run docker with `sudo` or add your user to the `docker` group.
```bash
sudo usermod -aG docker $USER
# Log out and log back in
```

## 2. "Conflict: Name already in use"
A container with that name exists, even if it's stopped.
```bash
docker rm -f <container_name>
```

## 3. "No space left on device"
Docker accumulate old images, containers, and volumes.
```bash
# Clean up everything unused
docker system prune -a --volumes
```

## 4. "Cannot connect to Docker daemon"
The docker engine is not running.
- **Windows/Mac**: Start Docker Desktop.
- **Linux**: `sudo systemctl start docker`

## 5. "Localhost" inside a container
Inside a container, `localhost` refers to the container itself, not your computer.
- Use `host.docker.internal` (Windows/Mac) to reach services on your host.
- Use the service name defined in **[Docker Compose](docker-compose.md)**.
