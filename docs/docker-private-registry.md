# Docker Private Registry

Running your own registry for secure, local image storage.

## 1. Quick Start (Local Registry)
```bash
docker run -d -p 5000:5000 --name registry registry:2
```

## 2. Pushing to your Registry
```bash
# Tag the image
docker tag my-image:latest localhost:5000/my-image:latest

# Push it
docker push localhost:5000/my-image:latest
```

## 3. Remote Registry Settings
To access the registry from other machines, you usually need to:
- Set up HTTPS (recommended).
- Or add it to `/etc/docker/daemon.json` under `insecure-registries`.

## 4. Alternatives
- **Cloud Providers**: Azure Container Registry (ACR), Google Container Registry (GCR), Amazon ECR.
- **Self-Hosted**: Harbor (highly recommended for production).

---
*Back to **[Docker Overview](docker-overview.md)**.*
