# Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications.

## Why use Compose?
Instead of running multiple `docker run` commands, you define your entire application stack in a single YAML file.

## Example `docker-compose.yml`
```yaml
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
  db:
    image: postgres:latest
    environment:
      POSTGRES_PASSWORD: example_password
```

## Common Commands
```bash
# Start all services in background
docker-compose up -d

# Stop and remove containers
docker-compose down

# View logs
docker-compose logs -f

# List running services
docker-compose ps
```

---
*See **[Docker Overview](docker-overview.md)** for more.*
