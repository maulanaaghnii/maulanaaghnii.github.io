# Ubuntu Isolated Development

Keep your system stable by isolating your development environments.

## 1. Virtual Environments (Python)
```bash
python3 -m venv myenv
source myenv/bin/activate
```

## 2. Docker Containers
The ultimate way to isolate. Run different OS versions or conflicting libraries without touching your host. See **[Docker Isolated Development](docker-isolated-development.md)**.

## 3. Chroot & System Containers (LXD)
Run an entire Ubuntu system inside another Ubuntu system.

## 4. Distrobox
Run any Linux distribution (Arch, Fedora, etc.) inside your Ubuntu terminal using podman/docker.
