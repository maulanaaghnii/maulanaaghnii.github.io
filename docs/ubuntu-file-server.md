# Making Ubuntu a File Server

Ubuntu can easily serve files to other computers using Samba (Windows-compatible) or FTP.

## 1. Using Samba (SMB)
Best for sharing files with Windows and Mac.
```bash
sudo apt update
sudo apt install samba -y

# Configuration
# Edit /etc/samba/smb.conf to add your share
```

## 2. Using FTP (vsftpd)
Standard for transferring files over a network.
```bash
sudo apt install vsftpd -y
# Start the service
sudo systemctl enable --now vsftpd
```

## 3. Using SSH (SFTP)
If you have SSH installed, you already have a secure file server.
```bash
# Connect from another machine
sftp user@ubuntu-ip
```

---
*See **[System Management](ubuntu-systemd-management.md)** for controlling these services.*
