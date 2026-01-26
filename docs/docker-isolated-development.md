# Isolated Development with Docker

Keep your host machine clean by running everything in containers.

## 1. No More "It Works on My Machine"
When your compiler, runtime, and database are all inside a container, the environment is 100% reproducible for every team member.

## 2. Dev Containers (VS Code)
VS Code can use a container as your full-featured development environment.
- Install the **Dev Containers** extension.
- Add a `.devcontainer` folder with a `devcontainer.json` file.
- Your source code is mounted inside the container where your tools are installed.

## 3. Simultaneous Projects
Need Java 17 for one project and Java 11 for another? With Docker isolation, you don't have to manage multiple versions on your main OS.

---
*See **[Docker Overview](docker-overview.md)** for more.*
