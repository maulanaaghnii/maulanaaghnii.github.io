# Ubuntu for Software Development

Ubuntu is the preferred OS for many developers due to its native support for tools, stability, and similarity to production environments.

## Setting Up Your Environment

### Essential Build Tools
```bash
sudo apt update
sudo apt install -y build-essential git curl wget
```

### IDEs and Editors
- **VS Code**: Install via `snap install code --classic` or as a `.deb` package.
- **Rider / IntelliJ**: Use JetBrains Toolbox or `snap`.
- **Neovim**: Highly customizable terminal editor.

### SDKs and Runtimes
- **.NET**: Use Microsoft's official repository for the latest SDKs.
- **Node.js**: Recommended to use `nvm` (Node Version Manager) for flexibility.
- **Python**: Ubuntu comes with Python 3; use `venv` for isolated environments.
- **Docker**: The native platform for containers.

## Best Practices
- **Use SSH Keys**: For secure GitHub/GitLab interactions.
- **Dotfiles**: Version control your shell configuration (`.bashrc`, `.zshrc`).
- **Terminal Emulator**: Use **Alacritty**, **Terminator**, or the default with **Oh My Zsh**.

---
*See **[Software Installation](ubuntu-software-installation.md)** for more details.*
