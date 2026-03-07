# Clean Architecture in .NET

Clean Architecture (or Onion Architecture) focuses on separation of concerns and making the core application logic independent of frameworks, databases, and UI.

## Structure
Typical layers in a Clean Architecture project:

### 1. Domain
The core of the application. Contains:
- Entities
- Value Objects
- Domain Exceptions
- Interfaces for base services

### 2. Application
Contains business logic and use cases.
- **Commands & Queries** (CQRS)
- **Handlers**
- **DTOs** (Request/Response)
- **Mappers** (AutoMapper)
- **Validators** (FluentValidation)
- **Interfaces** for Infrastructure (e.g., `IRepository`)

### 3. Infrastructure
Handles external concerns.
- Data Access (Entity Framework Core)
- Identity Management
- External API Clients
- File System / Storage
- Email Services

### 4. Web API (UI)
The entry point.
- Controllers
- Middleware
- Program.cs / Configuration

## Key Benefits
- **Testable**: Business logic can be tested without a database or web server.
- **Independent of Database**: You can swap SQL Server for PostgreSQL easily.
- **Maintainable**: Clear boundaries make the code easier to navigate.

## Example Flow
`Client -> Controller -> Command -> Handler -> Repository -> Database`

Each layer only knows about the layers "below" or "inside" it.