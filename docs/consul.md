# HashiCorp Consul

Consul is a multi-cloud service networking platform to connect and secure services across any runtime platform and public or private cloud.

## Key Features
- **Service Discovery**: Automatically register and discover services.
- **Health Checking**: Monitor the health of services and nodes.
- **KV Store**: A hierarchical key/value store for configuration.
- **Service Mesh**: Secure service-to-service communication with mTLS.

## Getting Started
For a quick start using Docker, see the **[Consul Docker Guide](consule-docker.md)**.

## Basic CLI Commands
```bash
# Check consul members
consul members

# Put a value in KV store
consul kv put my-key my-value

# Get a value
consul kv get my-key
```

## Architecture
Consul usually runs in a cluster of **Servers** and **Agents**. Servers maintain the state, while Agents run on every node and handle health checks and service registration.
