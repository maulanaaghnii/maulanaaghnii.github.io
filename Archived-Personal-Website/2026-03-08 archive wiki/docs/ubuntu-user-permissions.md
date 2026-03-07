# Ubuntu Users and Permissions

Understanding who can access what is crucial for system security.

## User Types
- **Root**: The superuser with full control.
- **Regular Users**: Standard accounts with limited access.
- **Sudoers**: Regular users with administrative privileges.

## Permissions (rwx)
Every file and directory has three types of permissions:
- **Read (r)**: View content.
- **Write (w)**: Modify content.
- **Execute (x)**: Run a file as a program.

## Changing Permissions (chmod)
```bash
# Give execute permission to owner
chmod u+x filename

# Set specific permissions (755)
chmod 755 filename
```

## Changing Ownership (chown)
```bash
# Change owner of a file
sudo chown username filename

# Change owner and group
sudo chown username:groupname filename
```

## Sudo
Use `sudo` to run commands with root privileges.
```bash
sudo apt update
```
