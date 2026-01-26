# Ubuntu Boot and Startup Optimization

Reduce the time it takes for your system to reach the desktop.

## 1. Analyze Boot Performance
```bash
# Get total boot time
systemd-analyze

# Get time spent on each unit
systemd-analyze blame

# Create a graphic visualization
systemd-analyze plot > boot.svg
```

## 2. Disable Unnecessary Services
Look for slow services in the `blame` output and disable them if not needed.
```bash
sudo systemctl disable service-name
```

## 3. GRUB Timeout
Reduce the time the GRUB menu waits for your selection.
Edit `/etc/default/grub`:
```text
GRUB_TIMEOUT=2
```
Apply with `sudo update-grub`.

## 4. Hardware Impact
- **SSD**: The single best upgrade for boot speed.
- **Fast Boot**: Enable "Fast Boot" or "Ultra Fast Boot" in your BIOS/UEFI settings.

---
*For general speed tips, see **[Resource Saving](ubuntu-resource-saving-tips.md)**.*
