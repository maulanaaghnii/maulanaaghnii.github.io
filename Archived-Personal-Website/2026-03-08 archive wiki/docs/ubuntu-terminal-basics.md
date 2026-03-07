# Basic Ubuntu Terminal Commands

## What is the Terminal?

The terminal (also called command line, shell, or console) is a text-based interface for interacting with your Ubuntu system. While Ubuntu has a graphical interface, the terminal provides powerful tools for system administration, development, and automation.

## Opening the Terminal

### Methods to Access Terminal

1. **Keyboard Shortcut**: `Ctrl + Alt + T`
2. **Activities Search**: Press `Super` key, type "terminal"
3. **Applications Menu**: Show Applications → Utilities → Terminal
4. **Right-click**: Right-click on desktop → "Open in Terminal"

### Terminal Interface Components

```
username@hostname:~/current/directory$ command
    │        │              │           │
    │        │              │           └── Command to execute
    │        │              └── Current working directory
    │        └── Computer name
    └── Current user
```

Example:
```bash
john@ubuntu-desktop:~/Documents$ ls
```

## Navigation Commands

### Understanding the File System

```bash
# Print current directory
pwd

# List directory contents
ls

# List with detailed information
ls -l

# List including hidden files
ls -la

# List with human-readable file sizes
ls -lh

# Change directory
cd /path/to/directory

# Go to home directory
cd ~
# or simply
cd

# Go up one directory
cd ..

# Go to previous directory
cd -

# Go to root directory
cd /
```

### Navigation Examples

```bash
# Navigate to your home directory
cd ~

# Navigate to Documents folder
cd Documents

# Go back to previous directory
cd ..

# Navigate using absolute path
cd /usr/local/bin

# Navigate using relative path
cd ../Downloads

# Quick navigation to common directories
cd ~/Desktop     # Desktop folder
cd ~/Downloads   # Downloads folder
cd ~/Pictures    # Pictures folder
```

## File and Directory Operations

### Creating Files and Directories

```bash
# Create an empty file
touch filename.txt

# Create multiple files
touch file1.txt file2.txt file3.txt

# Create a directory
mkdir directory_name

# Create multiple directories
mkdir dir1 dir2 dir3

# Create nested directories
mkdir -p parent/child/grandchild

# Create directory with specific permissions
mkdir -m 755 secure_directory
```

### Copying Files and Directories

```bash
# Copy a file
cp source_file.txt destination_file.txt

# Copy file to another directory
cp file.txt ~/Documents/

# Copy multiple files
cp file1.txt file2.txt ~/Documents/

# Copy directory and its contents
cp -r source_directory destination_directory

# Copy with verbose output
cp -v file.txt ~/Documents/

# Copy preserving attributes
cp -p file.txt backup_file.txt
```

### Moving and Renaming

```bash
# Move/rename a file
mv old_name.txt new_name.txt

# Move file to another directory
mv file.txt ~/Documents/

# Move multiple files
mv file1.txt file2.txt ~/Documents/

# Move directory
mv old_directory new_directory

# Move with confirmation
mv -i file.txt ~/Documents/
```

### Deleting Files and Directories

```bash
# Remove a file
rm filename.txt

# Remove multiple files
rm file1.txt file2.txt file3.txt

# Remove with confirmation
rm -i filename.txt

# Remove directory and contents
rm -r directory_name

# Force remove (be careful!)
rm -f filename.txt

# Force remove directory and contents (DANGEROUS!)
rm -rf directory_name

# Remove empty directory
rmdir empty_directory
```

## File Content Operations

### Viewing File Contents

```bash
# Display entire file
cat filename.txt

# Display file with line numbers
cat -n filename.txt

# View file page by page
less filename.txt
# Navigation in less: Space (next page), b (previous page), q (quit)

# Alternative pager
more filename.txt

# Display first 10 lines
head filename.txt

# Display first N lines
head -n 20 filename.txt

# Display last 10 lines
tail filename.txt

# Display last N lines
tail -n 15 filename.txt

# Follow file changes (useful for logs)
tail -f /var/log/syslog
```

### Creating and Editing Files

```bash
# Create file with content using echo
echo "Hello, World!" > hello.txt

# Append content to file
echo "Second line" >> hello.txt

# Create file using cat (Ctrl+D to save)
cat > newfile.txt
This is the content
Press Ctrl+D to save

# Edit file with nano (beginner-friendly)
nano filename.txt

# Edit file with vim (advanced)
vim filename.txt

# Edit file with gedit (GUI editor)
gedit filename.txt
```

### Searching in Files

```bash
# Search for pattern in file
grep "pattern" filename.txt

# Search case-insensitively
grep -i "pattern" filename.txt

# Search recursively in directories
grep -r "pattern" /path/to/directory

# Search and show line numbers
grep -n "pattern" filename.txt

# Search for whole words only
grep -w "word" filename.txt

# Search for multiple patterns
grep -E "pattern1|pattern2" filename.txt

# Count matching lines
grep -c "pattern" filename.txt
```

## File Permissions and Ownership

### Understanding Permissions

```
-rwxrwxrwx
│││││││││
│││└┬┘└┬┘
│││ │  └── Others permissions (read, write, execute)
│││ └──── Group permissions (read, write, execute)
│└┬────── Owner permissions (read, write, execute)
└─────── File type (- for file, d for directory)
```

### Permission Values

| Permission | Symbol | Numeric |
|------------|--------|---------|
| Read | r | 4 |
| Write | w | 2 |
| Execute | x | 1 |

Common combinations:
- `755` = rwxr-xr-x (Owner: read+write+execute, Group: read+execute, Others: read+execute)
- `644` = rw-r--r-- (Owner: read+write, Group: read, Others: read)
- `600` = rw------- (Owner: read+write, Group: none, Others: none)

### Changing Permissions

```bash
# Change permissions using symbolic notation
chmod u+x filename.txt    # Add execute for owner
chmod g-w filename.txt    # Remove write for group
chmod o+r filename.txt    # Add read for others
chmod a+x filename.txt    # Add execute for all

# Change permissions using numeric notation
chmod 755 filename.txt    # rwxr-xr-x
chmod 644 filename.txt    # rw-r--r--
chmod 600 filename.txt    # rw-------

# Change permissions recursively
chmod -R 755 directory/
```

### Changing Ownership

```bash
# Change file owner
sudo chown username filename.txt

# Change file owner and group
sudo chown username:groupname filename.txt

# Change ownership recursively
sudo chown -R username:groupname directory/

# Change only group
sudo chgrp groupname filename.txt
```

## System Information Commands

### System Status

```bash
# Display system information
uname -a

# Display operating system information
lsb_release -a

# Show current user
whoami

# Show current user ID
id

# Display system uptime
uptime

# Show system date and time
date

# Show calendar
cal

# Show users currently logged in
who

# Show what users are doing
w
```

### Resource Monitoring

```bash
# Display running processes
ps aux

# Interactive process viewer
top

# Better process viewer (if installed)
htop

# Display memory usage
free -h

# Display disk usage
df -h

# Display directory size
du -h directory/

# Display directory size summary
du -sh directory/

# Monitor system resources
iostat
vmstat
```

### Hardware Information

```bash
# List PCI devices
lspci

# List USB devices
lsusb

# List block devices (storage)
lsblk

# CPU information
lscpu

# Memory information
cat /proc/meminfo

# Hardware information
sudo lshw

# Hardware summary
sudo lshw -short
```

## Package Management

### APT Commands

```bash
# Update package lists
sudo apt update

# Upgrade installed packages
sudo apt upgrade

# Full system upgrade
sudo apt full-upgrade

# Install package
sudo apt install package-name

# Install multiple packages
sudo apt install package1 package2 package3

# Remove package
sudo apt remove package-name

# Remove package and configuration files
sudo apt purge package-name

# Remove orphaned packages
sudo apt autoremove

# Search for packages
apt search keyword

# Show package information
apt show package-name

# List installed packages
apt list --installed

# List upgradable packages
apt list --upgradable
```

### Package Information

```bash
# Check if package is installed
dpkg -l | grep package-name

# List files installed by package
dpkg -L package-name

# Find which package provides a file
dpkg -S /path/to/file

# Show package dependencies
apt depends package-name

# Show reverse dependencies
apt rdepends package-name
```

## Network Commands

### Network Information

```bash
# Display network interfaces
ip addr show
# or
ifconfig

# Display routing table
ip route show
# or
route -n

# Test network connectivity
ping google.com

# Test specific port connectivity
telnet hostname port

# Download files from internet
wget http://example.com/file.zip

# Alternative download tool
curl -O http://example.com/file.zip

# Display network connections
netstat -tuln

# Show listening ports
ss -tuln
```

### Network Configuration

```bash
# Bring interface up
sudo ip link set interface_name up

# Bring interface down
sudo ip link set interface_name down

# Restart network service
sudo systemctl restart networking

# Flush DNS cache
sudo systemd-resolve --flush-caches

# Show DNS configuration
systemd-resolve --status
```

## Process Management

### Process Control

```bash
# Start process in background
command &

# List background jobs
jobs

# Bring background job to foreground
fg %1

# Send job to background
bg %1

# Kill process by PID
kill PID

# Kill process forcefully
kill -9 PID

# Kill process by name
killall process-name

# Kill all processes matching pattern
pkill pattern
```

### Service Management

```bash
# Check service status
sudo systemctl status service-name

# Start service
sudo systemctl start service-name

# Stop service
sudo systemctl stop service-name

# Restart service
sudo systemctl restart service-name

# Enable service at boot
sudo systemctl enable service-name

# Disable service at boot
sudo systemctl disable service-name

# List all services
systemctl list-units --type=service

# List failed services
systemctl --failed
```

## Archive and Compression

### Creating Archives

```bash
# Create tar archive
tar -cvf archive.tar files/

# Create compressed tar archive (gzip)
tar -czvf archive.tar.gz files/

# Create compressed tar archive (bzip2)
tar -cjvf archive.tar.bz2 files/

# Create zip archive
zip -r archive.zip files/
```

### Extracting Archives

```bash
# Extract tar archive
tar -xvf archive.tar

# Extract compressed tar archive (gzip)
tar -xzvf archive.tar.gz

# Extract compressed tar archive (bzip2)
tar -xjvf archive.tar.bz2

# Extract to specific directory
tar -xzvf archive.tar.gz -C /path/to/directory

# Extract zip archive
unzip archive.zip

# List archive contents without extracting
tar -tzvf archive.tar.gz
zip -l archive.zip
```

## Text Processing

### Text Manipulation

```bash
# Sort lines in file
sort filename.txt

# Sort and remove duplicates
sort -u filename.txt

# Remove duplicate lines
uniq filename.txt

# Count lines, words, characters
wc filename.txt

# Count only lines
wc -l filename.txt

# Cut specific columns
cut -d',' -f1,3 file.csv

# Find and replace text
sed 's/old/new/g' filename.txt

# Replace text in-place
sed -i 's/old/new/g' filename.txt
```

### Advanced Text Processing

```bash
# Process text with awk
awk '{print $1}' filename.txt

# Print specific columns
awk '{print $1, $3}' filename.txt

# Filter and process
awk '$3 > 100 {print $1, $3}' data.txt

# Compare files
diff file1.txt file2.txt

# Compare directories
diff -r dir1/ dir2/
```

## Input/Output Redirection

### Redirection Operators

```bash
# Redirect output to file
command > output.txt

# Append output to file
command >> output.txt

# Redirect error to file
command 2> error.txt

# Redirect both output and error
command > output.txt 2>&1

# Redirect to null (discard)
command > /dev/null

# Pipe output to another command
command1 | command2

# Pipe with tee (output to file and screen)
command | tee output.txt
```

### Practical Examples

```bash
# Save directory listing to file
ls -la > directory_listing.txt

# Search and save results
grep "error" /var/log/syslog > errors.txt

# Count files in directory
ls | wc -l

# Find largest files
ls -la | sort -k5 -nr | head -10

# Monitor log file with filter
tail -f /var/log/syslog | grep "error"
```

## Environment Variables

### Working with Environment Variables

```bash
# Display all environment variables
env

# Display specific variable
echo $HOME
echo $PATH
echo $USER

# Set temporary variable
export MY_VAR="value"

# Add to PATH
export PATH=$PATH:/new/path

# Make permanent (add to ~/.bashrc)
echo 'export MY_VAR="value"' >> ~/.bashrc
source ~/.bashrc
```

### Common Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `$HOME` | User's home directory | `/home/username` |
| `$PATH` | Executable search path | `/usr/bin:/bin:/usr/local/bin` |
| `$USER` | Current username | `username` |
| `$PWD` | Current working directory | `/home/username/Documents` |
| `$SHELL` | Current shell | `/bin/bash` |

## Command History and Shortcuts

### Command History

```bash
# Show command history
history

# Show last N commands
history 10

# Search command history
history | grep "command"

# Execute command from history
!123        # Execute command number 123
!!          # Execute last command
!string     # Execute last command starting with 'string'
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + C` | Cancel current command |
| `Ctrl + D` | Exit shell/logout |
| `Ctrl + Z` | Suspend current process |
| `Ctrl + L` | Clear screen |
| `Ctrl + A` | Move to beginning of line |
| `Ctrl + E` | Move to end of line |
| `Ctrl + U` | Delete from cursor to beginning |
| `Ctrl + K` | Delete from cursor to end |
| `Ctrl + R` | Search command history |
| `Tab` | Auto-complete |
| `Tab Tab` | Show all possibilities |

## Getting Help

### Help Commands

```bash
# Show command manual
man command

# Show command help
command --help

# Show brief description
whatis command

# Search manual pages
apropos keyword

# Show command location
which command

# Show command type
type command

# Get info about command
info command
```

## Common Command Combinations

### Useful One-liners

```bash
# Find and delete files older than 30 days
find /path -type f -mtime +30 -delete

# Show disk usage of current directory, sorted
du -h | sort -hr

# Find largest directories
du -h --max-depth=1 | sort -hr

# Monitor system load
watch -n 1 'uptime'

# Show network connections with process names
sudo netstat -tulpn

# Find processes using most memory
ps aux --sort=-%mem | head

# Find files containing text
find /path -type f -exec grep -l "text" {} \;

# Count files by extension
find . -type f | sed 's/.*\.//' | sort | uniq -c | sort -nr
```

## Terminal Best Practices

### Safety Tips

1. **Always double-check destructive commands**
   ```bash
   # Use -i flag for confirmation
   rm -i important_file.txt
   cp -i source dest
   ```

2. **Use tab completion to avoid typos**
   ```bash
   # Type partial command and press Tab
   cd Doc<Tab>  # Expands to Documents/
   ```

3. **Test commands on sample data first**
   ```bash
   # Test regex on small file before applying to large dataset
   grep "pattern" small_file.txt
   ```

4. **Keep backups of important files**
   ```bash
   cp important_file.txt important_file.txt.backup
   ```

### Productivity Tips

1. **Use aliases for frequent commands**
   ```bash
   alias ll='ls -la'
   alias la='ls -A'
   alias l='ls -CF'
   ```

2. **Use command substitution**
   ```bash
   # Use output of one command in another
   echo "Today is $(date)"
   cd $(dirname $(which python))
   ```

3. **Chain commands efficiently**
   ```bash
   # Execute second command only if first succeeds
   make && make install
   
   # Execute second command only if first fails
   test -f file.txt || touch file.txt
   ```

## Next Steps

After mastering basic terminal commands:

1. **[Learn file and folder management](ubuntu-file-folder-management.md)**
2. **[Understand user and permissions](ubuntu-user-permissions.md)**
3. **[Explore software installation](ubuntu-software-installation.md)**
4. **[Set up development environment](ubuntu-software-development.md)**

## Summary

The terminal is a powerful tool that becomes more valuable as you learn to use it effectively. Start with basic commands and gradually build your skills:

| Skill Level | Focus Areas |
|-------------|-------------|
| **Beginner** | Navigation, file operations, basic text viewing |
| **Intermediate** | Permissions, process management, text processing |
| **Advanced** | Scripting, automation, system administration |

Remember: The terminal might seem intimidating at first, but with practice, it becomes an indispensable tool for efficient system management and development work.
