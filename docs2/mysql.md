# Uninstall MySQL

```
sudo systemctl stop mysql

sudo apt-get remove --purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-* -y

sudo rm -rf /etc/mysql /var/lib/mysql

sudo rm -rf /var/log/mysql

sudo apt-get autoremove

sudo apt-get autoclean
```


# Install Mysql

``` {.yaml .copy}
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password123';

GRANT ALL PRIVILEGES ON *.* TO 'new_user'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

EXIT;

```

# Create New User With GRANT
```
CREATE USER 'new_user'@'%' IDENTIFIED BY 'new_user_password';

GRANT ALL PRIVILEGES ON *.* TO 'new_user'@'%';

FLUSH PRIVILEGES;

```

