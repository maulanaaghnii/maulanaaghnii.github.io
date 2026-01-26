# NuGet Package Management

NuGet is the package manager for .NET.

## Common CLI Commands
```bash
# Add a package to the current project
dotnet add package Newtonsoft.Json

# Remove a package
dotnet remove package Newtonsoft.Json

# List all packages in a project
dotnet list package

# Restore packages
dotnet restore
```

## Private NuGet Feeds
You can use Azure Artifacts, GitHub Packages, or BaGet for private feeds.
Add a `nuget.config` file to your project:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="MyPrivateFeed" value="https://myserver.com/v3/index.json" />
  </packageSources>
</configuration>
```

## Central Package Management (CPM)
Modern .NET projects use `Directory.Packages.props` to manage versions centrally.

```xml
<Project>
  <PropertyGroup>
    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
  </PropertyGroup>
  <ItemGroup>
    <PackageVersion Include="Newtonsoft.Json" Version="13.0.1" />
  </ItemGroup>
</Project>
```
