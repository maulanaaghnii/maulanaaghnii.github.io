# Virtualization on Ubuntu

Run multiple operating systems on a single Ubuntu host.

## VirtualBox
The most popular GUI-based virtualization tool.
```bash
sudo apt update
sudo apt install virtualbox -y
```

## KVM (Kernel-based Virtual Machine)
Native Linux virtualization, highly performant.

### Installation
```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager -y
```

### Management
Users must be in the `libvirt` and `kvm` groups:
```bash
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
```
Use `virt-manager` for a graphical interface.

## LXD / LXC
System containers (like a full OS) rather than application containers (like Docker).
```bash
sudo snap install lxd
lxd init
```

---
*For smaller application-focused containers, use **[Docker](ubuntu.md#useful-tools)**.*
