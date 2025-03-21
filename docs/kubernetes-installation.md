# Kubernetes Installation

## 🪟Windows

```
curl.exe -LO "https://dl.k8s.io/release/v1.32.0/bin/windows/amd64/kubectl.exe"
```
#### Validate installation (optional)
```powershell
curl.exe -LO "https://dl.k8s.io/v1.32.0/bin/windows/amd64/kubectl.exe.sha256"
```
```cmd
CertUtil -hashfile kubectl.exe SHA256
type kubectl.exe.sha256
```
