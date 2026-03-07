# Docker Naming and Tagging Best Practices

Clear naming and tagging conventions help team collaboration and automation.

## Naming Containers
Don't rely on random names like `focused_newton`.
```bash
docker run --name my-web-api my-image
```
Use kebab-case or snake_case consistently.

## Tagging Images
- **Semantic Versioning**: Use `v1.2.3` for stable releases.
- **Environment**: Use tags like `dev`, `staging`, `prod` (but be careful as these are mutable).
- **Git Commit Hash**: Great for CI/CD traceability (e.g., `my-image:sha-a1b2c3d`).
- **Latest**: Avoid relying on `:latest` in production; it's unpredictable.

## Registries
Prefix your images with the repository name:
`my-company/my-project/web-worker:v1.0.0`

---
*For more, see **[Image Management](docker-image-management.md)**.*
