# Ubuntu Task Automation with Cron

Cron is a time-based job scheduler in Unix-like operating systems.

## The Crontab
Each user has their own crontab file where jobs are defined.

```bash
# Edit your crontab
crontab -e

# List your crontab jobs
crontab -l
```

## Syntax
`* * * * * command_to_execute`
- Minute (0-59)
- Hour (0-23)
- Day of Month (1-31)
- Month (1-12)
- Day of Week (0-6, Sunday=0)

## Examples
```bash
# Run a backup script every day at 2 AM
0 2 * * * /home/user/scripts/backup.sh

# Run every 15 minutes
*/15 * * * * /home/user/scripts/check_health.sh
```

---
*For system-level jobs, see also **[systemd timers](ubuntu-systemd-management.md)**.*
