# Ubuntu Cloud Backup

Automate your backups to cloud storage providers.

## 1. Rclone
The "Swiss Army Knife" for cloud storage. Supports Drive, Dropbox, S3, and more.
```bash
sudo apt install rclone
rclone config
```

## 2. Syncing to the Cloud
```bash
rclone sync /home/user/docs remote:Backup/docs
```

## 3. Automation
Add the sync command to your **[Crontab](ubuntu-cron-automation.md)** to run nightly.

## 4. Backblaze B2 / AWS S3
Highly cost-effective for large data backups. You can use specialized tools like **Duplicati** for an easy web-based GUI.

---
*For local backups, see **[Backup and Restore](ubuntu-backup-restore.md)**.*
