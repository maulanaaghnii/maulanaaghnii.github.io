# Essential .NET CLI Commands

## Overview

The .NET CLI (Command Line Interface) is a powerful cross-platform toolchain for developing, building, running, and publishing .NET applications. It provides a consistent experience across all supported platforms and is essential for modern .NET development.

## Getting Started with .NET CLI

### Installation Verification

```bash
# Check .NET version
dotnet --version

# Show detailed information
dotnet --info

# List installed SDKs
dotnet --list-sdks

# List installed runtimes
dotnet --list-runtimes

# Show help
dotnet --help
dotnet -h
```

### CLI Structure

```bash
dotnet [global-options] [command] [command-options] [arguments]
```

## Project Management Commands

### Creating New Projects

```bash
# List available templates
dotnet new list

# Create console application
dotnet new console -n MyConsoleApp

# Create web API
dotnet new webapi -n MyWebAPI

# Create class library
dotnet new classlib -n MyLibrary

# Create unit test project
dotnet new xunit -n MyLibrary.Tests

# Create solution file
dotnet new sln -n MySolution

# Create with specific framework
dotnet new console -n MyApp -f net8.0

# Create in current directory
dotnet new console

# Create with additional options
dotnet new webapi -n MyAPI --use-controllers --auth Individual
```

### Project Templates

| Template | Short Name | Description |
|----------|------------|-------------|
| Console Application | `console` | Command-line application |
| Class Library | `classlib` | Reusable library |
| Web API | `webapi` | REST API service |
| ASP.NET Core Web App | `webapp` | MVC web application |
| Blazor WebAssembly | `blazorwasm` | Client-side Blazor app |
| Blazor Server | `blazorserver` | Server-side Blazor app |
| Worker Service | `worker` | Background service |
| xUnit Test Project | `xunit` | Unit testing project |
| NUnit Test Project | `nunit` | NUnit testing project |
| MSTest Test Project | `mstest` | MSTest testing project |

### Advanced Project Creation

```bash
# Create with custom namespace
dotnet new console -n MyApp --namespace MyCompany.MyApp

# Create in specific directory
dotnet new console -n MyApp -o ./src/MyApp

# Create with language specification
dotnet new console -n MyApp --language C#

# Create with authentication
dotnet new webapp -n MyWebApp --auth Individual

# Create with HTTPS
dotnet new webapi -n MyAPI --use-https

# Force creation (overwrite existing)
dotnet new console -n MyApp --force
```

## Solution Management

### Working with Solutions

```bash
# Create new solution
dotnet new sln -n MySolution

# Add projects to solution
dotnet sln add MyConsoleApp/MyConsoleApp.csproj
dotnet sln add MyLibrary/MyLibrary.csproj
dotnet sln add MyLibrary.Tests/MyLibrary.Tests.csproj

# Add multiple projects at once
dotnet sln add **/*.csproj

# Remove project from solution
dotnet sln remove MyLibrary/MyLibrary.csproj

# List projects in solution
dotnet sln list

# Add project reference
dotnet add MyConsoleApp/MyConsoleApp.csproj reference MyLibrary/MyLibrary.csproj

# Remove project reference
dotnet remove MyConsoleApp/MyConsoleApp.csproj reference MyLibrary/MyLibrary.csproj

# List project references
dotnet list MyConsoleApp/MyConsoleApp.csproj reference
```

## Package Management

### NuGet Package Commands

```bash
# Add package to project
dotnet add package Newtonsoft.Json

# Add specific version
dotnet add package Newtonsoft.Json --version 13.0.3

# Add package to specific project
dotnet add MyProject/MyProject.csproj package Serilog

# Add package from specific source
dotnet add package MyPackage --source https://nuget.company.com/

# Remove package
dotnet remove package Newtonsoft.Json

# List packages in project
dotnet list package

# List outdated packages
dotnet list package --outdated

# List vulnerable packages
dotnet list package --vulnerable

# Update packages
dotnet add package Newtonsoft.Json  # Updates to latest version

# Restore packages
dotnet restore

# Restore with specific source
dotnet restore --source https://api.nuget.org/v3/index.json
```

### Package Sources

```bash
# List package sources
dotnet nuget list source

# Add package source
dotnet nuget add source https://nuget.company.com/ --name CompanyNuGet

# Remove package source
dotnet nuget remove source CompanyNuGet

# Enable/disable source
dotnet nuget enable source CompanyNuGet
dotnet nuget disable source CompanyNuGet

# Update source
dotnet nuget update source CompanyNuGet --source https://new-url.com/
```

## Building and Publishing

### Build Commands

```bash
# Build project
dotnet build

# Build specific project
dotnet build MyProject/MyProject.csproj

# Build in Release mode
dotnet build -c Release

# Build with specific framework
dotnet build -f net8.0

# Build with verbosity
dotnet build -v normal  # quiet, minimal, normal, detailed, diagnostic

# Build without restore
dotnet build --no-restore

# Build specific configuration
dotnet build -c Debug
dotnet build -c Release

# Build for specific runtime
dotnet build -r win-x64
dotnet build -r linux-x64
dotnet build -r osx-x64
```

### Restore and Clean

```bash
# Restore dependencies
dotnet restore

# Restore for specific runtime
dotnet restore -r win-x64

# Restore with lock file
dotnet restore --use-lock-file

# Clean build artifacts
dotnet clean

# Clean specific configuration
dotnet clean -c Release
```

### Publishing Applications

```bash
# Publish application
dotnet publish

# Publish in Release mode
dotnet publish -c Release

# Publish for specific runtime
dotnet publish -r win-x64
dotnet publish -r linux-x64
dotnet publish -r osx-arm64

# Self-contained deployment
dotnet publish -r win-x64 --self-contained true

# Framework-dependent deployment
dotnet publish -r win-x64 --self-contained false

# Single file deployment
dotnet publish -r win-x64 --self-contained true -p:PublishSingleFile=true

# AOT compilation (requires .NET 8+)
dotnet publish -r win-x64 -c Release -p:PublishAot=true

# Trimmed deployment
dotnet publish -r win-x64 --self-contained true -p:PublishTrimmed=true

# Ready to run
dotnet publish -r win-x64 -c Release -p:PublishReadyToRun=true

# Specify output directory
dotnet publish -o ./publish

# Include symbols
dotnet publish --self-contained true -p:IncludeSymbols=true
```

## Running Applications

### Run Commands

```bash
# Run project
dotnet run

# Run specific project
dotnet run --project MyProject/MyProject.csproj

# Run with arguments
dotnet run -- arg1 arg2 arg3

# Run with specific configuration
dotnet run -c Release

# Run with specific framework
dotnet run -f net8.0

# Run with environment variables
ASPNETCORE_ENVIRONMENT=Development dotnet run

# Run and watch for changes
dotnet watch run

# Run with specific launch profile
dotnet run --launch-profile "https"
```

### Executing Published Applications

```bash
# Run published application
dotnet MyApp.dll

# Run with arguments
dotnet MyApp.dll arg1 arg2

# Run self-contained executable
./MyApp  # Linux/macOS
MyApp.exe  # Windows
```

## Testing Commands

### Running Tests

```bash
# Run all tests
dotnet test

# Run tests in specific project
dotnet test MyProject.Tests/

# Run tests with verbose output
dotnet test -v normal

# Run specific test
dotnet test --filter "TestMethodName"

# Run tests by category
dotnet test --filter "Category=Unit"

# Run tests with code coverage
dotnet test --collect:"XPlat Code Coverage"

# Run tests with logger
dotnet test --logger "console;verbosity=detailed"
dotnet test --logger "trx;LogFileName=test-results.trx"

# Run tests in parallel
dotnet test --parallel

# Run tests without building
dotnet test --no-build

# Run tests with specific configuration
dotnet test -c Release
```

### Test Filtering

```bash
# Filter by test name
dotnet test --filter "Name~Calculator"

# Filter by category
dotnet test --filter "Category=Integration"

# Filter by priority
dotnet test --filter "Priority=1"

# Complex filters
dotnet test --filter "(Category=Unit|Category=Integration)&Priority=1"

# Exclude tests
dotnet test --filter "Category!=Slow"
```

## Development Tools

### Tool Management

```bash
# List installed tools
dotnet tool list

# List global tools
dotnet tool list -g

# Install global tool
dotnet tool install -g dotnet-ef
dotnet tool install -g dotnet-aspnet-codegenerator

# Install local tool
dotnet tool install dotnet-ef

# Update tool
dotnet tool update -g dotnet-ef

# Uninstall tool
dotnet tool uninstall -g dotnet-ef

# Restore tools (from .config/dotnet-tools.json)
dotnet tool restore

# Search for tools
dotnet tool search entity
```

### Popular .NET Tools

```bash
# Entity Framework Tools
dotnet tool install -g dotnet-ef

# ASP.NET Code Generator
dotnet tool install -g dotnet-aspnet-codegenerator

# Development certificates
dotnet dev-certs https --trust

# User secrets
dotnet user-secrets init
dotnet user-secrets set "ConnectionStrings:DefaultConnection" "Server=..."
dotnet user-secrets list

# Format code
dotnet tool install -g dotnet-format
dotnet format

# Report generator (code coverage)
dotnet tool install -g dotnet-reportgenerator-globaltool

# Outdated packages checker
dotnet tool install -g dotnet-outdated-tool
```

## Information and Diagnostic Commands

### System Information

```bash
# Show .NET information
dotnet --info

# Show runtime information
dotnet --list-runtimes

# Show SDK information
dotnet --list-sdks

# Show environment information
dotnet --info | grep -A 20 "Host"

# Check for updates
dotnet sdk check
```

### Project Information

```bash
# Show project properties
dotnet msbuild -getProperty:TargetFramework
dotnet msbuild -getProperty:OutputType

# List project files
dotnet msbuild -getItem:Compile

# Show project references
dotnet list reference

# Show package references
dotnet list package

# Show project-to-project references
dotnet list MyProject.csproj reference
```

## Configuration and Environment

### Global Configuration

```bash
# Set global properties
dotnet nuget config -set globalPackagesFolder /path/to/packages

# Show configuration
dotnet nuget config -showAll

# Add package source
dotnet nuget add source https://api.nuget.org/v3/index.json -n nuget.org
```

### Environment Variables

```bash
# Common .NET environment variables
export DOTNET_CLI_TELEMETRY_OPTOUT=1  # Disable telemetry
export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1  # Skip first-time setup
export DOTNET_ROOT=/usr/share/dotnet  # Set .NET installation path
export NUGET_PACKAGES=/path/to/packages  # Set NuGet cache location

# ASP.NET Core specific
export ASPNETCORE_ENVIRONMENT=Development
export ASPNETCORE_URLS="https://localhost:5001;http://localhost:5000"
```

## Advanced Commands

### MSBuild Integration

```bash
# Run MSBuild target
dotnet msbuild -target:Clean
dotnet msbuild -target:Restore
dotnet msbuild -target:Build

# Set MSBuild properties
dotnet build -p:Configuration=Release
dotnet build -p:Platform=x64

# Verbose MSBuild output
dotnet build -v diagnostic

# Show MSBuild version
dotnet msbuild -version
```

### Workload Management

```bash
# List available workloads
dotnet workload search

# Install workload
dotnet workload install maui
dotnet workload install android

# List installed workloads
dotnet workload list

# Update workloads
dotnet workload update

# Uninstall workload
dotnet workload uninstall maui

# Restore workloads
dotnet workload restore
```

## Scripting and Automation

### Batch Operations

```bash
#!/bin/bash
# build-all.sh - Build multiple projects

projects=(
    "src/MyLib"
    "src/MyApp"
    "tests/MyLib.Tests"
)

for project in "${projects[@]}"; do
    echo "Building $project..."
    dotnet build "$project" -c Release
done
```

### CI/CD Commands

```bash
# Restore, build, test, publish pipeline
dotnet restore
dotnet build -c Release --no-restore
dotnet test -c Release --no-build --verbosity normal
dotnet publish -c Release --no-build -o ./publish

# Single command pipeline
dotnet build -c Release && dotnet test -c Release --no-build && dotnet publish -c Release --no-build
```

### Docker Integration

```bash
# Build with Docker
docker build -t myapp .

# Run with .NET CLI in container
docker run -it mcr.microsoft.com/dotnet/sdk:8.0 bash
dotnet --version
```

## Performance and Diagnostics

### Performance Commands

```bash
# AOT publish for better performance
dotnet publish -c Release -r win-x64 -p:PublishAot=true

# Profile application
dotnet-trace collect -p $(pgrep MyApp) --format speedscope

# Memory dump
dotnet-dump collect -p $(pgrep MyApp)

# GC analysis
dotnet-gcdump collect -p $(pgrep MyApp)
```

### Diagnostic Tools

```bash
# Install diagnostic tools
dotnet tool install -g dotnet-trace
dotnet tool install -g dotnet-dump
dotnet tool install -g dotnet-gcdump
dotnet tool install -g dotnet-counters

# Monitor performance counters
dotnet-counters monitor --process-id $(pgrep MyApp)
```

## Troubleshooting

### Common Issues

```bash
# Clear NuGet cache
dotnet nuget locals all --clear

# Restore with force
dotnet restore --force

# Build with detailed logging
dotnet build -v diagnostic

# Check for binding redirects
dotnet list package --include-transitive

# Fix project file issues
dotnet format --include-generated

# Reset to clean state
dotnet clean
rm -rf bin obj
dotnet restore
dotnet build
```

### Debugging Build Issues

```bash
# Show MSBuild evaluation
dotnet build -v diagnostic > build.log 2>&1

# Show target execution order
dotnet msbuild -preprocess:output.xml

# Validate project file
dotnet msbuild -p:ValidateProject=true
```

## Best Practices

### Project Structure Commands

```bash
# Create solution with proper structure
dotnet new sln -n MyProject
mkdir -p src tests tools docs

# Create projects
dotnet new classlib -n MyProject.Core -o src/MyProject.Core
dotnet new webapi -n MyProject.API -o src/MyProject.API
dotnet new xunit -n MyProject.Tests -o tests/MyProject.Tests

# Add to solution
dotnet sln add src/MyProject.Core/MyProject.Core.csproj
dotnet sln add src/MyProject.API/MyProject.API.csproj
dotnet sln add tests/MyProject.Tests/MyProject.Tests.csproj

# Add references
dotnet add src/MyProject.API reference src/MyProject.Core
dotnet add tests/MyProject.Tests reference src/MyProject.Core
```

### Development Workflow

```bash
# Daily development commands
dotnet restore              # Restore packages
dotnet build               # Build solution
dotnet test                # Run tests
dotnet run --project src/MyProject.API  # Run application

# Pre-commit checks
dotnet format              # Format code
dotnet build -c Release    # Build release
dotnet test --no-build     # Test without rebuild
```

## CLI Configuration

### Global Settings

```bash
# Create global.json for SDK version
dotnet new globaljson --sdk-version 8.0.100

# EditorConfig for code style
dotnet new editorconfig

# Directory.Build.props for shared properties
echo '<Project>
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <LangVersion>latest</LangVersion>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>' > Directory.Build.props
```

## Summary

The .NET CLI is essential for modern .NET development. Key command categories:

| Category | Primary Commands | Purpose |
|----------|------------------|---------|
| **Project** | `new`, `add`, `remove` | Project management |
| **Build** | `build`, `publish`, `clean` | Compilation and deployment |
| **Package** | `add package`, `restore` | Dependency management |
| **Test** | `test`, `vstest` | Testing and quality |
| **Tool** | `tool install`, `tool list` | Development tools |
| **Run** | `run`, `watch` | Execution and debugging |

## Next Steps

After mastering .NET CLI:

1. **[Create your first project](dotnet-first-project.md)**
2. **[Learn NuGet package management](nuget-management.md)**
3. **[Explore dependency injection](dotnet-dependency-injection.md)**
4. **[Build REST APIs](aspnetcore-rest-api.md)**

The .NET CLI provides a consistent, powerful interface for all .NET development tasks across platforms. Master these commands to become more productive in your .NET development workflow.
