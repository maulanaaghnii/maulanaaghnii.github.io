# Ubuntu Data Backup and Restore

Protecting your data against system failure or accidental deletion is a critical task.

## Simple File Backup
Using `tar` to archive a directory:
```bash
# Create a compressed backup
tar -cvzf backup_date.tar.gz /home/user/documents

# Extract a backup
tar -xvzf backup_date.tar.gz -C /path/to/restore
```

## Using rsync
`rsync` is a powerful tool for syncing directories:
```bash
# Sync local directory to an external drive
rsync -av --delete /home/user/ /media/user/backup_drive/
```

## System Snapshots (Timeshift)
Timeshift is the "System Restore" equivalent for Linux. It protects system files and configurations.
```bash
sudo apt install timeshift
```

## Database Backups
```bash
# PostgreSQL
pg_dump dbname > backup.sql

# MySQL
mysqldump -u user -p dbname > backup.sql
```
