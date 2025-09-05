# Dockerfile: Creating Custom Images

## Overview

A Dockerfile is a text file that contains instructions for building Docker images. It defines the environment, dependencies, and configuration needed to run your application in a container.

## Dockerfile Basics

### What is a Dockerfile?

A Dockerfile is a **recipe** for creating Docker images. It contains step-by-step instructions that Docker follows to build an image automatically.

### Basic Structure

```dockerfile
# Comment
INSTRUCTION arguments
```

### Simple Example

```dockerfile
# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "app.py"]
```

## Dockerfile Instructions

### FROM - Base Image

```dockerfile
# Official image
FROM ubuntu:20.04

# Specific version
FROM node:18.16.0

# Multi-stage build
FROM node:18 AS builder
FROM nginx:alpine AS runtime

# Scratch (empty base)
FROM scratch
```

### RUN - Execute Commands

```dockerfile
# Single command
RUN apt-get update

# Multiple commands (recommended)
RUN apt-get update && \
    apt-get install -y \
        curl \
        wget \
        vim && \
    rm -rf /var/lib/apt/lists/*

# Using arrays (shell form vs exec form)
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "curl"]
```

### COPY vs ADD

```dockerfile
# COPY (recommended for simple file copying)
COPY source destination
COPY app.py /app/
COPY requirements.txt /app/
COPY . /app/

# ADD (has additional features)
ADD source destination
ADD https://example.com/file.tar.gz /app/  # Downloads from URL
ADD archive.tar.gz /app/                   # Auto-extracts archives

# Best practice: Use COPY unless you need ADD's features
```

### WORKDIR - Set Working Directory

```dockerfile
# Set working directory
WORKDIR /app

# All subsequent commands run from this directory
COPY . .
RUN ls -la  # Lists contents of /app

# Create directory if it doesn't exist
WORKDIR /app/data/logs
```

### ENV - Environment Variables

```dockerfile
# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000
ENV DATABASE_URL=postgresql://localhost/mydb

# Multiple variables
ENV NODE_ENV=production \
    PORT=3000 \
    DEBUG=false

# Use variables
ENV APP_HOME=/app
WORKDIR $APP_HOME
```

### ARG - Build Arguments

```dockerfile
# Define build arguments
ARG NODE_VERSION=18
ARG APP_ENV=production

# Use in FROM instruction
FROM node:${NODE_VERSION}

# Use in other instructions
ENV ENVIRONMENT=${APP_ENV}

# Build with arguments
# docker build --build-arg NODE_VERSION=16 .
```

### EXPOSE - Document Ports

```dockerfile
# Document which ports the container listens on
EXPOSE 80
EXPOSE 443
EXPOSE 8000/tcp
EXPOSE 53/udp

# Multiple ports
EXPOSE 80 443 8080
```

### USER - Set User

```dockerfile
# Create user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Switch to user
USER appuser

# Switch back to root if needed
USER root

# Use numeric IDs
USER 1000:1000
```

### CMD vs ENTRYPOINT

```dockerfile
# CMD - Default command (can be overridden)
CMD ["python", "app.py"]
CMD python app.py

# ENTRYPOINT - Fixed command (cannot be overridden)
ENTRYPOINT ["python", "app.py"]

# Combination (ENTRYPOINT + CMD)
ENTRYPOINT ["python"]
CMD ["app.py"]

# This allows: docker run myimage script.py
```

### VOLUME - Mount Points

```dockerfile
# Create mount points
VOLUME ["/data"]
VOLUME ["/var/log", "/var/db"]

# Or
VOLUME /data
VOLUME /var/log /var/db
```

### LABEL - Metadata

```dockerfile
# Add metadata
LABEL version="1.0"
LABEL description="My web application"
LABEL maintainer="yourname@example.com"

# Multiple labels
LABEL version="1.0" \
      description="My web application" \
      maintainer="yourname@example.com"
```

## Real-World Examples

### Node.js Application

```dockerfile
# Use official Node.js runtime
FROM node:18-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Copy application code
COPY --chown=nextjs:nodejs . .

# Switch to non-root user
USER nextjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Start application
CMD ["npm", "start"]
```

### Python Web Application

```dockerfile
# Multi-stage build
FROM python:3.11-slim as builder

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Production stage
FROM python:3.11-slim

# Create app user
RUN groupadd -r app && useradd -r -g app app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl && \
    rm -rf /var/lib/apt/lists/*

# Copy wheels from builder stage
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache /wheels/*

# Set working directory
WORKDIR /app

# Copy application code
COPY --chown=app:app . .

# Switch to app user
USER app

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1

# Start application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
```

### Java Spring Boot Application

```dockerfile
# Multi-stage build
FROM maven:3.8-openjdk-17 as builder

# Set working directory
WORKDIR /app

# Copy POM file
COPY pom.xml .

# Download dependencies (cached layer)
RUN mvn dependency:go-offline -B

# Copy source code
COPY src ./src

# Build application
RUN mvn clean package -DskipTests

# Runtime stage
FROM openjdk:17-jre-slim

# Install curl for health checks
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Create app user
RUN groupadd -r spring && useradd -r -g spring spring

# Set working directory
WORKDIR /app

# Copy jar from builder stage
COPY --from=builder /app/target/*.jar app.jar

# Change ownership
RUN chown spring:spring app.jar

# Switch to app user
USER spring

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# JVM options
ENV JAVA_OPTS="-Xmx512m -Xms256m"

# Start application
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

### .NET Application

```dockerfile
# Multi-stage build
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copy project files
COPY *.csproj ./
RUN dotnet restore

# Copy source code
COPY . ./
RUN dotnet publish -c Release -o /app/publish

# Runtime stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime

# Install curl for health checks
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Create app user
RUN groupadd -r app && useradd -r -g app app

WORKDIR /app

# Copy published app
COPY --from=build /app/publish .

# Change ownership
RUN chown -R app:app /app

# Switch to app user
USER app

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost/health || exit 1

# Start application
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

## Multi-Stage Builds

### Benefits of Multi-Stage Builds

- **Smaller final images**
- **Separation of build and runtime dependencies**
- **Better security** (no build tools in final image)
- **Faster deployments**

### Advanced Multi-Stage Example

```dockerfile
# Build stage
FROM node:18-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Development dependencies
FROM node:18-alpine AS dev-dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Build stage
FROM dev-dependencies AS build
COPY . .
RUN npm run build && npm run test

# Runtime stage
FROM node:18-alpine AS runtime
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

WORKDIR /app

# Copy dependencies
COPY --from=dependencies --chown=nextjs:nodejs /app/node_modules ./node_modules

# Copy built application
COPY --from=build --chown=nextjs:nodejs /app/dist ./dist
COPY --from=build --chown=nextjs:nodejs /app/package.json ./package.json

USER nextjs

EXPOSE 3000

CMD ["npm", "start"]
```

## Best Practices

### 1. Use Official Base Images

```dockerfile
# Good
FROM node:18-alpine
FROM python:3.11-slim
FROM openjdk:17-jre-slim

# Avoid
FROM ubuntu:latest  # Too generic, large size
```

### 2. Minimize Layers

```dockerfile
# Bad (multiple layers)
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN rm -rf /var/lib/apt/lists/*

# Good (single layer)
RUN apt-get update && \
    apt-get install -y \
        curl \
        wget && \
    rm -rf /var/lib/apt/lists/*
```

### 3. Use .dockerignore

```dockerignore
# .dockerignore file
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
.nyc_output
coverage
.coverage
.pytest_cache
.DS_Store
*.pyc
*.pyo
*.pyd
__pycache__
.vscode
.idea
```

### 4. Leverage Build Cache

```dockerfile
# Copy dependency files first (cached layer)
COPY package*.json ./
RUN npm install

# Copy source code last (changes frequently)
COPY . ./
```

### 5. Run as Non-Root User

```dockerfile
# Create user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set ownership
COPY --chown=appuser:appuser . /app

# Switch to user
USER appuser
```

### 6. Use Specific Tags

```dockerfile
# Good
FROM node:18.16.0-alpine

# Bad
FROM node:latest
FROM node
```

### 7. Add Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

## Common Patterns

### Configuration Management

```dockerfile
# Environment-specific configuration
ARG ENV=production
COPY config/config.${ENV}.json /app/config.json

# Template-based configuration
COPY config/app.conf.template /app/
RUN envsubst < /app/app.conf.template > /app/app.conf
```

### Secret Management

```dockerfile
# Use build secrets (BuildKit)
# syntax=docker/dockerfile:1
FROM alpine
RUN --mount=type=secret,id=mypassword \
  cat /run/secrets/mypassword

# Build with: docker build --secret id=mypassword,src=./password.txt .
```

### Caching Strategies

```dockerfile
# Cache package installations
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Use build cache mounts
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

## Building and Optimization

### Build Commands

```bash
# Basic build
docker build -t myapp .

# Build with arguments
docker build --build-arg ENV=production -t myapp .

# Build specific stage
docker build --target runtime -t myapp .

# Build with custom Dockerfile
docker build -f Dockerfile.prod -t myapp .

# Build without cache
docker build --no-cache -t myapp .
```

### Image Optimization

```dockerfile
# Use alpine variants
FROM node:18-alpine

# Remove package manager caches
RUN apt-get update && \
    apt-get install -y package && \
    rm -rf /var/lib/apt/lists/*

# Use multi-stage builds
FROM builder AS runtime

# Remove unnecessary files
RUN rm -rf /tmp/* /var/tmp/*
```

## Dockerfile Linting

### Using hadolint

```bash
# Install hadolint
brew install hadolint

# Lint Dockerfile
hadolint Dockerfile

# Ignore specific rules
hadolint --ignore DL3008 Dockerfile
```

### Common Issues

```dockerfile
# DL3008: Pin versions in apt-get install
RUN apt-get install -y curl=7.68.0-1ubuntu2

# DL3009: Delete apt-get lists
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# DL3006: Always tag the version of an image explicitly
FROM ubuntu:20.04
```

## Debugging Dockerfiles

### Debug Techniques

```bash
# Build up to specific stage
docker build --target debug -t myapp-debug .

# Run intermediate stage
docker run -it myapp-debug /bin/bash

# Check build history
docker history myapp

# Inspect final image
docker inspect myapp
```

### Debug Dockerfile

```dockerfile
FROM ubuntu:20.04 AS debug

# Install debugging tools
RUN apt-get update && \
    apt-get install -y \
        curl \
        wget \
        vim \
        htop \
        strace && \
    rm -rf /var/lib/apt/lists/*

# Your application setup
FROM debug AS app
COPY . /app
WORKDIR /app

# Production stage
FROM ubuntu:20.04 AS production
COPY --from=app /app /app
WORKDIR /app
CMD ["./start.sh"]
```

## Testing Dockerfiles

### Test Structure

```bash
# Test script
#!/bin/bash
set -e

# Build image
docker build -t test-app .

# Test 1: Image builds successfully
echo "✓ Image builds successfully"

# Test 2: Application starts
docker run -d --name test-container test-app
sleep 5

# Test 3: Health check passes
docker exec test-container curl -f http://localhost:3000/health

# Test 4: Cleanup
docker stop test-container
docker rm test-container

echo "✓ All tests passed"
```

## Next Steps

After mastering Dockerfile creation:

1. **[Learn Docker volumes](docker-volumes.md)**
2. **[Understand Docker networking](docker-networking-basics.md)**
3. **[Explore Docker Compose](docker-compose.md)**
4. **[Study image optimization](docker-dockerfile-optimization.md)**

Creating effective Dockerfiles is essential for building efficient, secure, and maintainable container images. Start with simple examples and gradually incorporate advanced patterns as your applications become more complex.
