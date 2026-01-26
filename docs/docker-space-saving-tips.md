# Docker Space Saving Tips

Docker can quickly consume a lot of disk space. Here's how to keep it lean.

## 1. Prune Regularly
```bash
# Remove stopped containers, unused networks, and dangling images
docker system prune

# Remove everything (including unused volumes)
docker system prune -a --volumes
```

## 2. Use Lightweight Base Images
Choose Alpine Linux or "distroless" images when possible.
```dockerfile
# Instead of node:20 (900MB+)
FROM node:20-alpine
# Instead of aspnet:8.0 (200MB+)
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine
```

## 3. Clean Up Build Cache
If you're using `apt` or `npm`, clean up after yourself in the same layer.
```dockerfile
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*
```

## 4. Multi-Stage Builds
The ultimate way to save space. See **[Multi-Stage Builds](docker-multi-stage-build.md)** for details.

---
*Back to **[Docker Overview](docker-overview.md)**.*
