# Docker Security Best Practices

Securing your containers is as important as securing your host system.

## 1. Use Non-Root Users
By default, Docker containers run as `root`. This is a security risk.
```dockerfile
# Create a user
RUN useradd -m myuser
USER myuser
```

## 2. Use Trusted Images
Always pull images from official or verified sources (e.g., Docker Hub Official Images). Use specific tags instead of `:latest`.

## 3. Scan for Vulnerabilities
Use tools like `docker scout` or `Snyk` to find known vulnerabilities in your layers.
```bash
docker scout quickview my-image:tag
```

## 4. Limit Resources
Prevent DoS attacks by limiting CPU and RAM.
```bash
docker run --memory="512m" --cpus="1.0" my-image
```

## 5. Keep Secrets Secret
Never hardcode passwords or API keys in your `Dockerfile`. Use Environment Variables or Docker Secrets.

---
*Back to **[Docker Overview](docker-overview.md)**.*
