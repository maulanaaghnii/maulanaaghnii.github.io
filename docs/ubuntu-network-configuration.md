# Ubuntu Network Configuration

Managing networks in Ubuntu can be done through the GUI or the command line using `Netplan` or `nmcli`.

## Command Line Tools
### 1. Simple IP info
```bash
ip addr show
```

### 2. nmcli (Network Manager CLI)
```bash
# List all connections
nmcli connection show

# Connect to a WiFi network
nmcli device wifi connect "SSID_NAME" password "PASSWORD"
```

## Static IP with Netplan
Ubuntu uses Netplan for network configuration (usually stored in `/etc/netplan/`).

Example config:
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```
Apply with: `sudo netplan apply`

## Troubleshooting
```bash
# Check connectivity
ping google.com

# Trace network path
traceroute google.com

# Show open ports
ss -tuln
```
