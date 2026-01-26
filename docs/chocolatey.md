# Chocolatey Package Manager

Chocolatey is a software management solution that allows you to manage Windows software (install, update, uninstall) from the command line.

## Installation
Run the following command in an **elevated (Administrator) PowerShell**:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

## Basic Commands
```bash
# Search for a package
choco search nodejs

# Install a package
choco install nodejs -y

# Upgrade a package
choco upgrade nodejs -y

# Upgrade all packages
choco upgrade all -y

# Uninstall a package
choco uninstall nodejs
```

## Popular Packages for Developers
- `vscode`: Visual Studio Code
- `git`: Git for Windows
- `docker-desktop`: Docker Desktop
- `nvm`: Node Version Manager
- `postman`: API testing tool
- `dbeaver`: Database manager

## Why Use Chocolatey?
- **Speed**: No more clicking through installers.
- **Automation**: Easily scriptable environments.
- **Maintenance**: Update all your software with a single command.