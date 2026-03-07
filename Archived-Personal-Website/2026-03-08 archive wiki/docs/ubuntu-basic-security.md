# Basic Ubuntu Security

Crucial steps to protect your Ubuntu installation.

## 1. Enable a Firewall (UFW)
```bash
sudo ufw enable
# Allow only necessary ports
sudo ufw allow ssh
sudo ufw allow http
```

## 2. Strong Passwords & SSH
- Use complex passwords.
- **SSH Key Authentication**: Disable password login for SSH.
Edit `/etc/ssh/sshd_config`:
```text
PasswordAuthentication no
```

## 3. Keep Software Updated
Always run `sudo apt update && sudo apt upgrade`. See **[System Update](ubuntu-system-update.md)**.

## 4. Fail2Ban
Protect against brute-force attacks.
```bash
sudo apt install fail2ban -y
```

## 5. Principle of Least Privilege
Avoid using `root` directly. Use `sudo` only when necessary. See **[Users and Permissions](ubuntu-user-permissions.md)**.

---
*Stay safe!*
