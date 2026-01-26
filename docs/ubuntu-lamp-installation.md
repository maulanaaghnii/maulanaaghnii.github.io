# Installing LAMP Stack on Ubuntu

LAMP stands for **L**inux, **A**pache, **M**ySQL, and **P**HP. It is a classic stack for web development.

## 1. Apache
Install the web server:
```bash
sudo apt update
sudo apt install apache2 -y
```

## 2. MySQL
Install the database:
```bash
sudo apt install mysql-server -y
# Secure it
sudo mysql_secure_installation
```

## 3. PHP
Install PHP and the Apache module:
```bash
sudo apt install php libapache2-mod-php php-mysql -y
```

## 4. Verification
Create a test file at `/var/www/html/info.php`:
```php
<?php
phpinfo();
?>
```
Visit `http://localhost/info.php` in your browser.

## Managing Services
```bash
sudo systemctl restart apache2
sudo systemctl status mysql
```

---
*For a modern alternative, see **[Nginx Setup](ubuntu-nginx-setup.md)**.*
