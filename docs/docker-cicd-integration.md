# Docker CI/CD Integration

Automating your build, test, and deployment pipeline using Docker.

## 1. Why Docker for CI/CD?
- **Consistency**: The same environment is used in development, testing, and production.
- **Isolation**: Each build runs in its own clean container.
- **Speed**: Take advantage of layer caching.

## 2. Typical Workflow
1. **Developer pushes code** to GitHub/GitLab.
2. **CI Server** (GitHub Actions, Jenkins) is triggered.
3. **Build Image**: Docker builds the image using the `Dockerfile`.
4. **Run Tests**: Tasks like `dotnet test` or `npm test` are run inside containers.
5. **Push to Registry**: If tests pass, the image is pushed to a **[Private Registry](docker-private-registry.md)**.
6. **CD Pipeline**: The image is pulled and deployed to production.

## 3. GitHub Actions Example
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build and Push
        run: |
          docker build -t my-image:latest .
          docker login -u ${{ secrets.USER }} -p ${{ secrets.PASS }}
          docker push my-image:latest
```

---
*See **[Docker Overview](docker-overview.md)** for more.*
