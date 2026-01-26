# Docker Monitoring and Logging

Keeping an eye on your containers is essential for maintaining a healthy production environment.

## Logging
Docker captures the `stdout` and `stderr` of your containers.
```bash
# View recent logs
docker logs my-container

# Follow logs in real-time
docker logs -f my-container

# View logs since a specific time
docker logs --since 30m my-container
```

## Monitoring
```bash
# View live resource usage (CPU, Memory, Network)
docker stats

# Get detailed info about a container
docker inspect my-container
```

## Advanced Setup (ELK Stack)
For production, you should aggregate logs.
- **Elasticsearch**: Storage and search.
- **Logstash/Fluentd**: Data processing.
- **Kibana**: Visualization.

---
*See **[Docker Overview](docker-overview.md)** for more.*
