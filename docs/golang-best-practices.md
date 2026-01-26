# Go Best Practices & Patterns

Write code that is idiomatic, clean, and "Go-like".

## 1. Keep it Simple
Go values readability over Cleverness. Avoid complex abstractions and deeply nested structures.

## 2. Naming Conventions
- Keep it short: `idx` instead of `indexVariable`.
- Use **MixedCaps** (PascalCase for Exported, camelCase for internal).
- Acronyms should be all caps: `serveHTTP`, `ID`, `URL`.

## 3. Interfaces
- Define interfaces where they are **used**, not where they are implemented.
- Keep them small (1-3 methods).

## 4. Error Handling
- Never ignore errors (`_ = ...`).
- Wrap errors with context: `fmt.Errorf("failed to save: %w", err)`.

## 5. Concurrency
- "Don't communicate by sharing memory, share memory by communicating."
- Always ensure goroutines have a way to exit (Avoid leaks).

## 6. Project Layout (Standard)
```text
/cmd/app-name/main.go
/internal/      (private app code)
/pkg/           (public libraries)
/api/           (proto/openapi specs)
```

---
*Reference: [Effective Go](https://go.dev/doc/effective_go)*
