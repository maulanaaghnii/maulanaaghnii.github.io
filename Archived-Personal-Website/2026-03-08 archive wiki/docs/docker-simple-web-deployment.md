# Simple Web Deployment with Docker

A quick guide to getting a web app up and running.

## 1. Prepare your App
Ensure your app (React, static HTML, or an API) has a `Dockerfile`.

## 2. Build the Image
```bash
docker build -t my-web-app .
```

## 3. Run with Nginx Reverse Proxy
Instead of exposing your app directly, use Nginx to handle HTTPS and multiple domains.
```yaml
# docker-compose.yml
services:
  web:
    image: my-web-app
  proxy:
    image: nginx
    ports:
      - "80:80"
```

## 4. One-Click Options
- **CapRover**: A simple PaaS you can run on your own VPS that uses Docker under the hood.
- **Coolify**: An open-source, self-hosted alternative to Heroku/Netlify.

---
*Back to **[Docker Overview](docker-overview.md)**.*
