# Ubuntu System Monitoring

Tools and commands to keep an eye on your Ubuntu system's health.

## 1. Top & Htop
The classic way to see running processes and CPU/RAM usage.
```bash
# Basic (Built-in)
top

# Interactive (Recommended)
sudo apt install htop
htop
```

## 2. Disk Usage
```bash
# Show free disk space
df -h

# Show size of a specific directory
du -sh /path/to/dir
```

## 3. Network Monitoring
```bash
# Show active network connections
ss -tuln

# Show live network bandwidth
sudo apt install nload
nload
```

## 4. Hardware Info
```bash
# CPU Details
lscpu

# Memory Details
free -h
```
