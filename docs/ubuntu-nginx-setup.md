# Ubuntu Nginx Web Server Setup

Nginx is a highly performant web server and reverse proxy.

## Installation
```bash
sudo apt update
sudo apt install nginx -y
```

## Basic Configuration
Configuration files are located in `/etc/nginx/sites-available/`.

### Example Server Block
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection keep-alive;
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## Commands
- `sudo nginx -t`: Test configuration for errors.
- `sudo systemctl reload nginx`: Apply changes without downtime.
- `sudo systemctl restart nginx`: Full restart.

---
*See **[systemd management](ubuntu-systemd-management.md)** for controlling the service.*
