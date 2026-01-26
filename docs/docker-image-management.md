# Docker Image Management

Effectively managing your Docker images prevents clutter and ensures you're always using the right versions.

## Common Operations
```bash
# List all images
docker images

# Remove a specific image
docker rmi my-image:1.0

# Remove all dangling (unused) images
docker image prune
```

## Tagging
Tags are used to version your images.
```bash
# Tag an image for a private registry
docker tag my-local-image:latest my-registry.com/my-project:v2.1
```

## Inspecting
```bash
# See detailed metadata about an image
docker image inspect my-image:latest

# See the layers of an image
docker history my-image:latest
```

---
*Back to **[Docker Overview](docker-overview.md)**.*
