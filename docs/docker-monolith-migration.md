# Migrating Monoliths to Docker

Moving a large, existing application ("monolith") into Docker.

## 1. The Lift-and-Shift Approach
The first step is often to "containerize" the existing app as it is.
- Create a `Dockerfile` for the app.
- Use Docker Compose to add the database it depends on.

## 2. Dealing with Persistence
Monoliths often write files directly to the disk (logs, uploads). You must map these to **[Docker Volumes](docker-volumes.md)** to ensure they aren't lost when the container restarts.

## 3. Configuration Management
Hardcoded connection strings must be moved to **[Environment Variables](docker-environment-variables.md)** so the same image can run in Dev, Test, and Prod.

## 4. Gradual Decomposition
After the monolith is containerized, you can start extracting functionality into separate microservices.

---
*Back to **[Docker Overview](docker-overview.md)**.*
