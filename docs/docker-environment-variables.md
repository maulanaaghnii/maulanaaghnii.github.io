# Docker Environment Variables

Environment variables are the standard way to configure containerized applications.

## Passing Variables
### 1. Command Line (`-e`)
```bash
docker run -e DB_HOST=localhost -e DB_PORT=5432 my-app
```

### 2. Env File (`--env-file`)
Create a `.env` file:
```text
DB_HOST=production-db
API_KEY=secret_key_123
```
Run with:
```bash
docker run --env-file .env my-app
```

### 3. Docker Compose
```yaml
services:
  web:
    image: my-web-app
    environment:
      - NODE_ENV=production
      - DEBUG=true
```

## Accessing in Apps
- **C#**: `Environment.GetEnvironmentVariable("DB_HOST")`
- **Node.js**: `process.env.DB_HOST`
- **Python**: `os.environ.get("DB_HOST")`

---
*Back to **[Docker Overview](docker-overview.md)**.*
