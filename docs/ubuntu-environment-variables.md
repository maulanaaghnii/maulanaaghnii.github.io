# Ubuntu Environment Variables

Managing system and user variables in Ubuntu.

## Viewing Variables
```bash
# Show all variables
printenv

# Show a specific variable
echo $PATH
```

## Setting Variables
### 1. Temporary (Current session)
```bash
export MY_VAR="hello"
```

### 2. User-Specific (Permanent)
Add the export command to your `~/.bashrc` or `~/.zshrc` file.
```bash
echo 'export MY_VAR="hello"' >> ~/.bashrc
source ~/.bashrc
```

### 3. System-Wide
Edit the `/etc/environment` file (requires sudo).

## Common Variables
- `PATH`: List of directories where the system looks for executable files.
- `HOME`: Current user's home directory.
- `USER`: Current logged-in user.
- `EDITOR`: Default text editor (e.g., nano, vim).

---
*For development, see **[.NET Env Vars](dotnet-environment-variables.md)**.*
