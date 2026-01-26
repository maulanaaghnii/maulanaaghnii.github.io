# Common Ubuntu Issues and Solutions

A quick guide to fixing frequent problems on Ubuntu.

## 1. Locked Package Database
*Error: Could not get lock /var/lib/dpkg/lock-frontend*
- **Solution**: Another program is using `apt`. Wait for it to finish or restart.

## 2. Broken Packages
- **Solution**: Run the following fix commands.
```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
```

## 3. Wi-Fi Not Working
- **Solution**: Check Additional Drivers.
`Software & Updates` -> `Additional Drivers` -> Select proprietary drivers if available.

## 4. Forgotten Sudo Password
- **Solution**: Boot into Recovery Mode (hold Shift during boot) and select `root` to drop to a shell and run `passwd yourusername`.

## 5. GNOME Desktop Frozen
- **Solution**: Restart the Shell (Alt+F2, type `r`, then Enter) or kill the session (Ctrl+Alt+Backspace).

---
*For more, check the **[Ubuntu Overview](ubuntu-overview.md)**.*
