# Ubuntu Repositories and PPA

Repositories are servers that host software packages for Ubuntu. PPAs (Personal Package Archives) allow developers to distribute software directly to users.

## Standard Repositories
Ubuntu uses four main repositories:
- **Main**: Canonical-supported free and open-source software.
- **Universe**: Community-maintained free and open-source software.
- **Restricted**: Proprietary drivers for devices.
- **Multiverse**: Software restricted by copyright or legal issues.

## Managing PPAs
```bash
# Add a PPA
sudo add-apt-repository ppa:author/ppa-name

# Remove a PPA
sudo add-apt-repository --remove ppa:author/ppa-name

# List all sources
ls /etc/apt/sources.list.d/
```

## Updating after changes
Whenever you add a repository, you must update the package index:
```bash
sudo apt update
```
---
*See **[System Update](ubuntu-system-update.md)** for how to upgrade packages.*
