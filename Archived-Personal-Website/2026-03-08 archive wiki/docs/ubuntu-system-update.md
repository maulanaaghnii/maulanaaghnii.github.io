# Ubuntu System Update & Upgrade

Keeping your system updated is essential for security and stability.

## Standard Update Workflow
```bash
# Update the package index
sudo apt update

# Upgrade installed packages
sudo apt upgrade -y

# Perform a full upgrade (handles dependency changes)
sudo apt full-upgrade -y
```

## Cleaning up
```bash
# Remove unnecessary packages (unused dependencies)
sudo apt autoremove -y

# Clean up local repository of retrieved package files
sudo apt clean
```

## PPA (Personal Package Archives)
To get newer versions of certain software:
```bash
sudo add-apt-repository ppa:some-author/ppa
sudo apt update
```

---
*For managing software sources, see **[Repositories and PPA](ubuntu-repository-ppa.md)**.*
