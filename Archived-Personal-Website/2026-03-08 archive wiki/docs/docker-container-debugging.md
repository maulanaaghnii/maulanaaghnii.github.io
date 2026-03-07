# Docker Container Debugging

How to find out why your container isn't working.

## 1. Inspecting Logs
The first step is always checking the output.
```bash
docker logs <container_id>
```

## 2. Interactive Shell
Go inside the container to explore the environment.
```bash
docker exec -it <container_id> /bin/bash
# or for alpine
docker exec -it <container_id> /bin/sh
```

## 3. Investigating Exit Codes
```bash
docker ps -a
# Check the STATUS column (e.g., Exited (137) means Out of Memory)
```

## 4. Resource Usage
```bash
docker stats
```

## 5. Network Troubleshooting
```bash
# Check if a port is listening
docker exec <container_id> netstat -tuln
```

---
*For general issues, see **[Docker Common Issues](docker-common-issues.md)**.*
