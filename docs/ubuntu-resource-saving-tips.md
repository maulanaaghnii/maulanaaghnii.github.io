# Ubuntu Resource Saving Tips

Optimize your Ubuntu installation for performance, especially on older hardware.

## 1. Disable Startup Applications
`Activities` -> Search for `Startup Applications`. Uncheck what you don't need.

## 2. Reduce "Swappiness"
By default, Ubuntu swaps data from RAM to disk very early.
```bash
# Check current value (usually 60)
cat /proc/sys/vm/swappiness

# Set to a lower value (e.g., 10) temporarily
sudo sysctl vm.swappiness=10
```

## 3. Install Lightweight Desktop Environment
If GNOME is too heavy, try:
- **XFCE**: `sudo apt install xfce4`
- **LXQt**: `sudo apt install lxqt`

## 4. Clear Cache and Logs
```bash
# Clean apt cache
sudo apt clean

# Limit journal log size
sudo journalctl --vacuum-time=1w
```

## 5. Use Stacer
`Stacer` is a great all-in-one system optimizer GUI.
```bash
sudo apt install stacer
```

---
*For system monitoring, see **[Monitoring Tools](ubuntu-system-monitoring.md)**.*
