# Docker for Database Development

Using Docker to manage databases during development ensures every developer has the same version and configuration.

## 1. Quick Start
```bash
# PostgreSQL
docker run --name my-db -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

# MySQL
docker run --name my-sql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql
```

## 2. Best Practices
### Use Persistent Volumes
Never store data only inside the container.
```bash
-v my-postgres-data:/var/lib/postgresql/data
```

### Use Docker Compose
Perfect for managing an app and its database together.
```yaml
services:
  db:
    image: postgres:15-alpine
    volumes:
      - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

### Custom Initialization
You can mount scripts to `/docker-entrypoint-initdb.d/` to run them on first startup.

---
*See **[PostgreSQL](postgresql.md)** or **[MySQL](mysql.md)** for DB-specific commands.*
