# Ubuntu systemd Service Management

`systemd` is the init system and service manager for Ubuntu.

## Common Commands
```bash
# Start a service
sudo systemctl start nginx

# Stop a service
sudo systemctl stop nginx

# Restart a service
sudo systemctl restart nginx

# Enable service to start at boot
sudo systemctl enable nginx

# Disable service at boot
sudo systemctl disable nginx

# Check service status
systemctl status nginx

# List running services
systemctl list-units --type=service
```

## Creating a custom service
Create a file at `/etc/systemd/system/myapp.service`:
```ini
[Unit]
Description=My .NET App

[Service]
ExecStart=/usr/bin/dotnet /path/to/app.dll
Restart=always

[Install]
WantedBy=multi-user.target
```
Then run `sudo systemctl daemon-reload`.
